(() => {
  'use strict';

  const P = BigInt('0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F');
  const N = BigInt('0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141');
  const G = {
    x: BigInt('0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798'),
    y: BigInt('0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8'),
  };
  const P2PKH_VERSION = 0x37;
  const WIF_VERSION = 0xCC;
  const LIGHT_API = 'https://light.pepepow.net';
  const BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';
  const textEncoder = new TextEncoder();

  const mod = (a, m = P) => {
    const r = a % m;
    return r >= 0n ? r : r + m;
  };

  const modPow = (base, exp, m) => {
    let result = 1n;
    let b = mod(base, m);
    let e = exp;
    while (e > 0n) {
      if (e & 1n) result = (result * b) % m;
      b = (b * b) % m;
      e >>= 1n;
    }
    return result;
  };

  const inv = (a) => modPow(a, P - 2n, P);

  const jacobianDouble = (p) => {
    if (!p || p.z === 0n || p.y === 0n) return { x: 0n, y: 1n, z: 0n };
    const xx = mod(p.x * p.x);
    const yy = mod(p.y * p.y);
    const yyyy = mod(yy * yy);
    const s = mod(4n * p.x * yy);
    const m = mod(3n * xx);
    const x3 = mod(m * m - 2n * s);
    const y3 = mod(m * (s - x3) - 8n * yyyy);
    const z3 = mod(2n * p.y * p.z);
    return { x: x3, y: y3, z: z3 };
  };

  const jacobianAddAffine = (p, q) => {
    if (!p || p.z === 0n) return { x: q.x, y: q.y, z: 1n };
    const z1z1 = mod(p.z * p.z);
    const u2 = mod(q.x * z1z1);
    const s2 = mod(q.y * p.z * z1z1);
    const h = mod(u2 - p.x);
    const r0 = mod(s2 - p.y);
    if (h === 0n) {
      if (r0 === 0n) return jacobianDouble(p);
      return { x: 0n, y: 1n, z: 0n };
    }
    const hh = mod(h * h);
    const i = mod(4n * hh);
    const j = mod(h * i);
    const r = mod(2n * r0);
    const v = mod(p.x * i);
    const x3 = mod(r * r - j - 2n * v);
    const y3 = mod(r * (v - x3) - 2n * p.y * j);
    const z3 = mod((p.z + h) * (p.z + h) - z1z1 - hh);
    return { x: x3, y: y3, z: z3 };
  };

  const scalarMultG = (k) => {
    const scalar = mod(k, N);
    if (scalar === 0n) throw new Error('Invalid secp256k1 scalar');
    let r = { x: 0n, y: 1n, z: 0n };
    for (const bit of scalar.toString(2)) {
      r = jacobianDouble(r);
      if (bit === '1') r = jacobianAddAffine(r, G);
    }
    const zInv = inv(r.z);
    const z2 = mod(zInv * zInv);
    return {
      x: mod(r.x * z2),
      y: mod(r.y * z2 * zInv),
    };
  };

  const bigIntToBytes = (value, length) => {
    let hex = value.toString(16);
    if (hex.length > length * 2) throw new Error('Integer too large');
    hex = hex.padStart(length * 2, '0');
    const out = new Uint8Array(length);
    for (let i = 0; i < length; i += 1) out[i] = parseInt(hex.slice(i * 2, i * 2 + 2), 16);
    return out;
  };

  const bytesToBigInt = (bytes) => {
    let hex = '';
    for (const b of bytes) hex += b.toString(16).padStart(2, '0');
    return BigInt(`0x${hex || '0'}`);
  };

  const concatBytes = (...parts) => {
    const out = new Uint8Array(parts.reduce((n, p) => n + p.length, 0));
    let offset = 0;
    for (const p of parts) {
      out.set(p, offset);
      offset += p.length;
    }
    return out;
  };

  const u32be = (n) => new Uint8Array([(n >>> 24) & 255, (n >>> 16) & 255, (n >>> 8) & 255, n & 255]);

  const compressedPubkey = (privateKey) => {
    const point = scalarMultG(bytesToBigInt(privateKey));
    return concatBytes(new Uint8Array([point.y & 1n ? 0x03 : 0x02]), bigIntToBytes(point.x, 32));
  };

  const sha256 = async (data) => new Uint8Array(await crypto.subtle.digest('SHA-256', data));

  const hmacSha512 = async (keyBytes, dataBytes) => {
    const key = await crypto.subtle.importKey(
      'raw',
      keyBytes,
      { name: 'HMAC', hash: 'SHA-512' },
      false,
      ['sign'],
    );
    return new Uint8Array(await crypto.subtle.sign('HMAC', key, dataBytes));
  };

  const rol = (x, n) => ((x << n) | (x >>> (32 - n))) >>> 0;

  const ripemd160 = (message) => {
    const r1 = [
      0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
      7,4,13,1,10,6,15,3,12,0,9,5,2,14,11,8,
      3,10,14,4,9,15,8,1,2,7,0,6,13,11,5,12,
      1,9,11,10,0,8,12,4,13,3,7,15,14,5,6,2,
      4,0,5,9,7,12,2,10,14,1,3,8,11,6,15,13,
    ];
    const r2 = [
      5,14,7,0,9,2,11,4,13,6,15,8,1,10,3,12,
      6,11,3,7,0,13,5,10,14,15,8,12,4,9,1,2,
      15,5,1,3,7,14,6,9,11,8,12,2,10,0,4,13,
      8,6,4,1,3,11,15,0,5,12,2,13,9,7,10,14,
      12,15,10,4,1,5,8,7,6,2,13,14,0,3,9,11,
    ];
    const s1 = [
      11,14,15,12,5,8,7,9,11,13,14,15,6,7,9,8,
      7,6,8,13,11,9,7,15,7,12,15,9,11,7,13,12,
      11,13,6,7,14,9,13,15,14,8,13,6,5,12,7,5,
      11,12,14,15,14,15,9,8,9,14,5,6,8,6,5,12,
      9,15,5,11,6,8,13,12,5,12,13,14,11,8,5,6,
    ];
    const s2 = [
      8,9,9,11,13,15,15,5,7,7,8,11,14,14,12,6,
      9,13,15,7,12,8,9,11,7,7,12,7,6,15,13,11,
      9,7,15,11,8,6,6,14,12,13,5,14,13,13,7,5,
      15,5,8,11,14,14,6,14,6,9,12,9,12,5,15,8,
      8,5,12,9,12,5,14,6,8,13,6,5,15,13,11,11,
    ];
    const k1 = [0x00000000,0x5a827999,0x6ed9eba1,0x8f1bbcdc,0xa953fd4e];
    const k2 = [0x50a28be6,0x5c4dd124,0x6d703ef3,0x7a6d76e9,0x00000000];
    const f = (j, x, y, z) => {
      if (j <= 15) return (x ^ y ^ z) >>> 0;
      if (j <= 31) return ((x & y) | (~x & z)) >>> 0;
      if (j <= 47) return ((x | ~y) ^ z) >>> 0;
      if (j <= 63) return ((x & z) | (y & ~z)) >>> 0;
      return (x ^ (y | ~z)) >>> 0;
    };

    const bitLen = BigInt(message.length) * 8n;
    const totalLen = Math.ceil((message.length + 9) / 64) * 64;
    const padded = new Uint8Array(totalLen);
    padded.set(message);
    padded[message.length] = 0x80;
    for (let i = 0; i < 8; i += 1) padded[totalLen - 8 + i] = Number((bitLen >> BigInt(8 * i)) & 0xffn);

    let h0 = 0x67452301;
    let h1 = 0xefcdab89;
    let h2 = 0x98badcfe;
    let h3 = 0x10325476;
    let h4 = 0xc3d2e1f0;

    for (let offset = 0; offset < padded.length; offset += 64) {
      const x = new Uint32Array(16);
      for (let i = 0; i < 16; i += 1) {
        const j = offset + i * 4;
        x[i] = (padded[j] | (padded[j + 1] << 8) | (padded[j + 2] << 16) | (padded[j + 3] << 24)) >>> 0;
      }
      let al = h0, bl = h1, cl = h2, dl = h3, el = h4;
      let ar = h0, br = h1, cr = h2, dr = h3, er = h4;
      for (let j = 0; j < 80; j += 1) {
        const tl = (rol((al + f(j, bl, cl, dl) + x[r1[j]] + k1[Math.floor(j / 16)]) >>> 0, s1[j]) + el) >>> 0;
        al = el; el = dl; dl = rol(cl, 10); cl = bl; bl = tl;
        const tr = (rol((ar + f(79 - j, br, cr, dr) + x[r2[j]] + k2[Math.floor(j / 16)]) >>> 0, s2[j]) + er) >>> 0;
        ar = er; er = dr; dr = rol(cr, 10); cr = br; br = tr;
      }
      const t = (h1 + cl + dr) >>> 0;
      h1 = (h2 + dl + er) >>> 0;
      h2 = (h3 + el + ar) >>> 0;
      h3 = (h4 + al + br) >>> 0;
      h4 = (h0 + bl + cr) >>> 0;
      h0 = t;
    }

    const out = new Uint8Array(20);
    [h0,h1,h2,h3,h4].forEach((h, i) => {
      out[i * 4] = h & 255;
      out[i * 4 + 1] = (h >>> 8) & 255;
      out[i * 4 + 2] = (h >>> 16) & 255;
      out[i * 4 + 3] = (h >>> 24) & 255;
    });
    return out;
  };

  const base58Encode = (bytes) => {
    let x = bytesToBigInt(bytes);
    let out = '';
    while (x > 0n) {
      out = BASE58[Number(x % 58n)] + out;
      x /= 58n;
    }
    for (let i = 0; i < bytes.length && bytes[i] === 0; i += 1) out = '1' + out;
    return out || '1';
  };

  const base58Check = async (payload) => {
    const first = await sha256(payload);
    const second = await sha256(first);
    return base58Encode(concatBytes(payload, second.slice(0, 4)));
  };

  const publicKeyToAddress = async (pubkey) => {
    const digest = await sha256(pubkey);
    const h160 = ripemd160(digest);
    return base58Check(concatBytes(new Uint8Array([P2PKH_VERSION]), h160));
  };

  const privateKeyToWif = async (privateKey) => base58Check(
    concatBytes(new Uint8Array([WIF_VERSION]), privateKey, new Uint8Array([0x01])),
  );

  const mnemonicToSeed = async (mnemonic) => {
    const normalized = mnemonic.normalize('NFKD').trim().toLowerCase().replace(/\s+/g, ' ');
    const material = await crypto.subtle.importKey('raw', textEncoder.encode(normalized), 'PBKDF2', false, ['deriveBits']);
    return new Uint8Array(await crypto.subtle.deriveBits({
      name: 'PBKDF2',
      hash: 'SHA-512',
      salt: textEncoder.encode('mnemonic'),
      iterations: 2048,
    }, material, 512));
  };

  const masterFromSeed = async (seed) => {
    const i = await hmacSha512(textEncoder.encode('Bitcoin seed'), seed);
    const key = i.slice(0, 32);
    const scalar = bytesToBigInt(key);
    if (scalar === 0n || scalar >= N) throw new Error('Invalid BIP32 master key');
    return { key, chainCode: i.slice(32), pubkey: null };
  };

  const deriveChild = async (node, index, hardened = false) => {
    const childIndex = hardened ? (index + 0x80000000) >>> 0 : index >>> 0;
    const data = hardened
      ? concatBytes(new Uint8Array([0]), node.key, u32be(childIndex))
      : concatBytes(node.pubkey || (node.pubkey = compressedPubkey(node.key)), u32be(childIndex));
    const i = await hmacSha512(node.chainCode, data);
    const il = bytesToBigInt(i.slice(0, 32));
    if (il >= N) throw new Error('Invalid BIP32 child key');
    const child = mod(il + bytesToBigInt(node.key), N);
    if (child === 0n) throw new Error('Invalid BIP32 child key');
    return { key: bigIntToBytes(child, 32), chainCode: i.slice(32), pubkey: null };
  };

  const derivePath = async (root, path) => {
    let node = root;
    const parts = path.replace(/^m\/?/, '').split('/').filter(Boolean);
    for (const part of parts) {
      const hardened = part.endsWith("'");
      const value = Number(hardened ? part.slice(0, -1) : part);
      if (!Number.isInteger(value) || value < 0 || value >= 0x80000000) throw new Error(`Invalid path segment: ${part}`);
      node = await deriveChild(node, value, hardened);
    }
    return node;
  };

  const deriveIndexed = async (branchNode, index) => {
    const node = await deriveChild(branchNode, index, false);
    const pubkey = compressedPubkey(node.key);
    const address = await publicKeyToAddress(pubkey);
    return { index, node, address };
  };

  const parseBalanceAtoms = (data) => {
    const confirmed = Number(data?.balance?.confirmed ?? 0);
    const unconfirmed = Number(data?.balance?.unconfirmed ?? 0);
    return Number.isFinite(confirmed) && Number.isFinite(unconfirmed) ? confirmed + unconfirmed : 0;
  };

  const formatPepew = (atoms) => new Intl.NumberFormat('en-US', {
    maximumFractionDigits: 8,
  }).format(Number(atoms) / 1e8);

  const fetchBalance = async (address) => {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 9000);
    try {
      const res = await fetch(`${LIGHT_API}/api/wallet/address/${encodeURIComponent(address)}`, {
        headers: { Accept: 'application/json' },
        signal: controller.signal,
      });
      if (!res.ok) throw new Error(`Light API HTTP ${res.status}`);
      const data = await res.json();
      return { atoms: parseBalanceAtoms(data), data };
    } finally {
      clearTimeout(timer);
    }
  };

  const selfTest = async () => {
    const emptyRipemd = Array.from(ripemd160(new Uint8Array())).map((b) => b.toString(16).padStart(2, '0')).join('');
    if (emptyRipemd !== '9c1185a5c5e9fc54612808977ee8f548b2258d31') throw new Error('RIPEMD-160 self-test failed');
    const pub1 = compressedPubkey(bigIntToBytes(1n, 32));
    const pub1Hex = Array.from(pub1).map((b) => b.toString(16).padStart(2, '0')).join('');
    if (pub1Hex !== '0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798') {
      throw new Error('secp256k1 self-test failed');
    }
    const seed = Uint8Array.from([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]);
    const master = await masterFromSeed(seed);
    const keyHex = Array.from(master.key).map((b) => b.toString(16).padStart(2, '0')).join('');
    const chainHex = Array.from(master.chainCode).map((b) => b.toString(16).padStart(2, '0')).join('');
    if (keyHex !== 'e8f32e723decf4051aefac8e2c93c9c5b214313817cdb01a1494b917c8436b35'
      || chainHex !== '873dff81c02f525623fd1fe5167eac3a55a049de3d314bb42ee227ffed37d508') {
      throw new Error('BIP32 self-test failed');
    }
    const child = await derivePath(master, "m/0'");
    const childHex = Array.from(child.key).map((b) => b.toString(16).padStart(2, '0')).join('');
    if (childHex !== 'edb2e14f9ee77d26dd93b4ecede8d16ed408ce149b6cd80b0715a2d911a0afea') {
      throw new Error('BIP32 child derivation self-test failed');
    }
  };

  const initPage = () => {
    const mnemonicEl = document.querySelector('#recovery-mnemonic');
    const oldAddressEl = document.querySelector('#known-address');
    const depthEl = document.querySelector('#scan-depth');
    const scanBtn = document.querySelector('#scan-wallet');
    const clearBtn = document.querySelector('#clear-recovery');
    const statusEl = document.querySelector('#recovery-status');
    const resultsEl = document.querySelector('#recovery-results');
    const summaryEl = document.querySelector('#recovery-summary');
    const testEl = document.querySelector('#crypto-self-test');
    if (!mnemonicEl || !scanBtn || !resultsEl || !statusEl) return;

    let generation = 0;
    const secrets = new Map();

    const setStatus = (message, kind = '') => {
      statusEl.textContent = message;
      statusEl.dataset.kind = kind;
    };

    const clearAll = () => {
      generation += 1;
      mnemonicEl.value = '';
      if (oldAddressEl) oldAddressEl.value = '';
      resultsEl.replaceChildren();
      secrets.clear();
      if (summaryEl) summaryEl.textContent = '';
      setStatus('Sensitive fields cleared. Close or refresh this tab when finished.');
      mnemonicEl.focus();
    };

    const addResult = ({ label, path, address, atoms, node, matched }) => {
      const card = document.createElement('article');
      card.className = 'recovery-result-card';
      const id = `result-${crypto.randomUUID ? crypto.randomUUID() : Math.random().toString(36).slice(2)}`;
      secrets.set(id, node);
      const balanceText = atoms === null ? 'Not queried' : `${formatPepew(atoms)} PEPEW`;
      card.innerHTML = `
        <div class="recovery-result-head">
          <div>
            <p class="eyebrow">${matched ? 'Matched address' : 'Funds found'}</p>
            <h3>${label}</h3>
          </div>
          <strong>${balanceText}</strong>
        </div>
        <dl class="recovery-result-data">
          <div><dt>Address</dt><dd><code>${address}</code></dd></div>
          <div><dt>Derivation path</dt><dd><code>${path}</code></dd></div>
        </dl>
        <div class="recovery-result-actions">
          <a class="button secondary" href="https://explorer.pepepow.net/address/${encodeURIComponent(address)}" target="_blank" rel="noopener noreferrer">Open in Explorer</a>
          <button class="button danger" type="button" data-reveal="${id}">Reveal recovery private key</button>
        </div>
        <div class="recovery-secret" data-secret="${id}" hidden>
          <p><strong>Private key (WIF)</strong> — anyone with this key can spend these coins.</p>
          <code data-wif="${id}"></code>
          <button class="button secondary" type="button" data-copy="${id}">Copy WIF</button>
          <p class="small-note">After recovery, move the full balance to a new wallet address and do not continue using this exposed private key.</p>
        </div>
      `;
      resultsEl.append(card);
    };

    resultsEl.addEventListener('click', async (event) => {
      const target = event.target;
      if (!(target instanceof HTMLElement)) return;
      const revealId = target.dataset.reveal;
      const copyId = target.dataset.copy;
      if (revealId) {
        const node = secrets.get(revealId);
        const box = resultsEl.querySelector(`[data-secret="${CSS.escape(revealId)}"]`);
        const code = resultsEl.querySelector(`[data-wif="${CSS.escape(revealId)}"]`);
        if (!node || !box || !code) return;
        if (!window.confirm('Reveal the private key on this screen? Anyone who sees or copies it can spend the funds.')) return;
        code.textContent = await privateKeyToWif(node.key);
        box.hidden = false;
        target.textContent = 'Private key revealed';
        target.setAttribute('disabled', 'disabled');
      }
      if (copyId) {
        const code = resultsEl.querySelector(`[data-wif="${CSS.escape(copyId)}"]`);
        if (!code?.textContent) return;
        await navigator.clipboard.writeText(code.textContent);
        target.textContent = 'Copied';
        setTimeout(() => { target.textContent = 'Copy WIF'; }, 1400);
      }
    });

    scanBtn.addEventListener('click', async () => {
      const run = ++generation;
      resultsEl.replaceChildren();
      secrets.clear();
      if (summaryEl) summaryEl.textContent = '';
      const mnemonic = mnemonicEl.value.normalize('NFKD').trim().toLowerCase().replace(/\s+/g, ' ');
      const words = mnemonic ? mnemonic.split(' ') : [];
      const knownAddress = oldAddressEl?.value.trim() || '';
      const depth = Math.max(1, Math.min(100, Number(depthEl?.value || 20)));
      if (words.length !== 12) {
        setStatus('The old Android wallet recovery phrase must contain exactly 12 words.', 'error');
        return;
      }

      scanBtn.setAttribute('disabled', 'disabled');
      clearBtn?.setAttribute('disabled', 'disabled');
      try {
        setStatus('Preparing the wallet locally…');
        const seed = await mnemonicToSeed(mnemonic);
        const root = await masterFromSeed(seed);
        const branchDefs = [
          { label: 'BIP44 receive', base: "m/44'/5'/0'/0" },
          { label: 'BIP44 change', base: "m/44'/5'/0'/1" },
          { label: 'Legacy receive', base: "m/0'/0" },
          { label: 'Legacy change', base: "m/0'/1" },
        ];
        const branches = [];
        for (const def of branchDefs) branches.push({ ...def, node: await derivePath(root, def.base) });

        let checked = 0;
        let found = 0;
        const total = branchDefs.length * depth;
        for (const branch of branches) {
          for (let index = 0; index < depth; index += 1) {
            if (run !== generation) return;
            const item = await deriveIndexed(branch.node, index);
            const path = `${branch.base}/${index}`;
            checked += 1;
            setStatus(`Checking ${checked} of ${total}: ${branch.label} #${index}…`);

            if (knownAddress) {
              if (item.address === knownAddress) {
                let atoms = null;
                try { atoms = (await fetchBalance(item.address)).atoms; } catch {}
                addResult({ label: branch.label, path, address: item.address, atoms, node: item.node, matched: true });
                found += 1;
                if (summaryEl) summaryEl.textContent = `Found the supplied old address at ${path}.`;
                setStatus('Old address found. Verify it in Explorer, then reveal its recovery private key only if needed.', 'success');
                return;
              }
            } else {
              let balance = null;
              try {
                balance = await fetchBalance(item.address);
              } catch (error) {
                if (String(error?.message || error).includes('429')) {
                  await new Promise((resolve) => setTimeout(resolve, 1200));
                  try { balance = await fetchBalance(item.address); } catch {}
                }
              }
              if (balance && balance.atoms > 0) {
                addResult({ label: branch.label, path, address: item.address, atoms: balance.atoms, node: item.node, matched: false });
                found += 1;
              }
              await new Promise((resolve) => setTimeout(resolve, 75));
            }
          }
        }

        if (knownAddress) {
          setStatus(`The supplied address was not found in the first ${depth} addresses of the four old Android wallet branches. Increase scan depth and try again.`, 'error');
          if (summaryEl) summaryEl.textContent = 'No matching derivation path found yet.';
        } else if (found > 0) {
          setStatus(`Scan complete. Found ${found} address${found === 1 ? '' : 'es'} with a current balance.`, 'success');
          if (summaryEl) summaryEl.textContent = `Checked ${total} old-wallet addresses locally; only public addresses were sent to PEPEW Light API for balance lookup.`;
        } else {
          setStatus(`No current balance found in the first ${depth} addresses of each old-wallet branch. Increase scan depth or enter a known old public address.`, 'error');
          if (summaryEl) summaryEl.textContent = `Checked ${total} derived addresses.`;
        }
      } catch (error) {
        console.error(error);
        setStatus(`Recovery scan failed: ${error?.message || error}`, 'error');
      } finally {
        scanBtn.removeAttribute('disabled');
        clearBtn?.removeAttribute('disabled');
      }
    });

    clearBtn?.addEventListener('click', clearAll);

    selfTest().then(() => {
      if (testEl) testEl.textContent = 'Local cryptography self-test: PASS';
    }).catch((error) => {
      console.error(error);
      if (testEl) testEl.textContent = 'Local cryptography self-test: FAILED — do not use this page.';
      scanBtn.setAttribute('disabled', 'disabled');
      setStatus('Local cryptography self-test failed. Do not enter a recovery phrase.', 'error');
    });
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initPage, { once: true });
  else initPage();
})();