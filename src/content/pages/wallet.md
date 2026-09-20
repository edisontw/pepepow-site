---
title: "Wallet"
description: "Choose a PEPEW wallet, verify official sources, and follow current guidance for backups, updates, synchronization, and recovery."
date: "2020-04-13 11:18:52"
updated: "2026-09-20 16:35:00"
slug: "wallet"
categories: []
tags: []
legacy_url: "https://pepepow.org/wallet/"
source_url: "https://pepepow.org/wallet/"
status: "draft"
featured: false
migration_review: true
---

Choose the wallet that fits how you use PEPEW. Before entering a recovery phrase, importing keys, or moving funds, verify that you are using the official project URL or release source.

## Wallet options

### PEPEW Light Web Wallet

[Open PEPEW Light Wallet](https://light.pepepow.net/wallet/)

PEPEW Light is the recommended browser-based starting point for most users. It is client-side and non-custodial: mnemonic and private-key handling stays in the browser, while the public PEPEW Light API supplies address, history, and UTXO data and broadcasts transactions that have already been signed locally.

The wallet remains a **public beta**. Start with small amounts, keep your recovery phrase private, and confirm that the address bar shows the official `light.pepepow.net` domain before entering recovery words.

![](/media/legacy/2026/01/web-wallet1.png)

### Android Wallet

The PEPEW Android wallet is available as a public **v1.0.0** release.

[PEPEW Android Wallet releases](https://github.com/edisontw/pepepow-android-wallet-v2/releases)

The Android wallet is non-custodial and uses PEPEW Light services for balance, history, and UTXO queries, plus broadcast of locally signed transactions.

![](/media/legacy/2025/12/android-wallet-release.png)

### Desktop Core Wallet

PEPEPOW Core remains the full desktop wallet and node option for Windows and Linux.

- [PEPEPOW Core releases](https://github.com/MattF42/PePe-core/releases)
- Latest release reviewed on 19 Sep 2026: **v2.9.0.5**
- v2.9.0.5 is an optional update that raises the minimum peer protocol so the node connects only to peers that understand the HooHash hard fork.

![PEPEPOW Desktop Wallet](/media/legacy/2024/09/PEPEPOW-desktop1.webp)

#### Windows x86_64

[Download PEPEPOW Core v2.9.0.5 for Windows x86_64](https://github.com/MattF42/PePe-core/releases/download/v2.9.0.5/PEPEPOW-v2.9.0.5-5a9debc-release-x86_64-w64-mingw32.zip)

#### Linux x86_64

```bash
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.9.0.5/PEPEPOW-v2.9.0.5-5a9debc-release-x86_64-linux-gnu.tgz -O - | tar -xz
```

#### Linux ARM64 / AARCH64

```bash
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.9.0.5/PEPEPOW-v2.9.0.5-5a9debc-release-aarch64-linux-gnu.tgz -O - | tar -xz
```

## Installing or updating PEPEPOW Core

1. Download the current release from the official PEPEPOW Core GitHub releases page.
2. Confirm that the downloaded filename matches your platform and CPU architecture.
3. Stop the existing Core wallet cleanly before replacing binaries.
4. Keep a separate backup of `wallet.dat` before wallet maintenance or recovery work.
5. Start the updated wallet and allow it to synchronize fully.
6. If you operate masternodes, check the current release notes for any protocol-bump or restart requirement.

### Linux Update Example

Check the current daemon first:

```bash
./PEPEPOW-cli getblockcount
./PEPEPOW-cli mnsync status
```

Stop it cleanly:

```bash
./PEPEPOW-cli stop
```

Download the correct current build for your architecture, extract it, then restart:

```bash
./PEPEPOWd -daemon
```

For masternode-specific startup/status commands, use the current [Masternode guide](/masternode/).

## Sync and Recovery Safety

Do **not** delete the PEPEPOW data directory as a first troubleshooting step.

Before any destructive recovery step:

- shut down the wallet cleanly
- back up `wallet.dat` to a separate safe location
- verify the PEPEPOW Core version
- check the current Explorer/network status to distinguish a local sync problem from a network incident
- use a current recovery guide or ask in the PEPEPOW community if the correct recovery path is unclear

Dated blockchain bootstrap archives can still help in specific recovery cases, but they are not the default download path because they become stale quickly.

## Verify before you download

- [PEPEPOW Explorer](https://explorer.pepepow.org/)
- [PEPEW Light status/API](https://light.pepepow.net/)
- [PEPEPOW Core releases](https://github.com/MattF42/PePe-core/releases)
- [Android wallet releases](https://github.com/edisontw/pepepow-android-wallet-v2/releases)

