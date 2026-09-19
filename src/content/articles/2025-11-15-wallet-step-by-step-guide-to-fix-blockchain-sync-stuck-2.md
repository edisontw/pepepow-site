---
title: "[Wallet] Step-by-Step Guide to Fix Blockchain Sync Stuck"
description: ""
date: "2025-11-15 11:53:28"
updated: "2025-11-15 11:55:36"
slug: "wallet-step-by-step-guide-to-fix-blockchain-sync-stuck-2"
categories: ["Articles", "Masternode", "Wallet"]
tags: ["PePeCore", "Wallet"]
legacy_url: "https://pepepow.org/wallet-step-by-step-guide-to-fix-blockchain-sync-stuck-2/"
source_url: "https://pepepow.org/wallet-step-by-step-guide-to-fix-blockchain-sync-stuck-2/"
status: "draft"
featured: false
migration_review: true
---

If your **PEPEPOW wallet** stops syncing at a specific block and won’t move forward, follow these steps to safely recover full synchronization.

### **Step 1: Check Debug Log for Errors**

Inspect the last part of your log to identify what’s causing the stall:

```
tail -n 50 ~/.PEPEPOWcore/debug.log
```

Look for messages such as:

- Checkpoint not reached
- block is marked invalid
- Failed to connect to peers
- AcceptBlockHeader: invalid header received

Take note of any repeated errors — they’ll help identify where sync is stuck.

### **Step 2: Verify the Current Block Height**

Check your node’s current height:

```
./PEPEPOW-cli getblockcount
```

Compare it with the latest block number shown on the **official explorer**.  
If your block height is lower and not increasing, continue below.

### **Step 3: Reset Masternode Sync (if showing -0.25 progress)**

If `mnsync` seems frozen or keeps showing negative progress:

```
./PEPEPOW-cli mnsync status
./PEPEPOW-cli mnsync reset
sleep 30
./PEPEPOW-cli mnsync status
```

This refreshes internal masternode sync state without touching the blockchain.

### **Step 4: Restart Node and Clear Network Cache**

Bad peers or banned nodes often block progress.  
Restart the node and clear peer/ban lists:

```
./PEPEPOW-cli stop
rm -f ~/.PEPEPOWcore/peers.dat
rm -f ~/.PEPEPOWcore/banlist.dat
./PEPEPOWd -daemon
```

Then check:

```
./PEPEPOW-cli getblockcount
```

### **Step 5: Invalidate and Reconsider the Stuck Block**

Force the node to roll back and rebuild from the previous valid block.  
Example (replace the block number with your stuck height):

```
./PEPEPOW-cli invalidateblock $(./PEPEPOW-cli getblockhash 3703297)
./PEPEPOW-cli reconsiderblock $(./PEPEPOW-cli getblockhash 3703296)
```

This tells the wallet to reject the problematic block and continue from the last verified one.

### **Step 6: Restart Node Again**

Apply changes by restarting:

```
./PEPEPOW-cli stop
./PEPEPOWd -daemon
```

Wait 1–2 minutes, then verify if syncing resumes:

```
./PEPEPOW-cli getblockcount
```

If the number starts increasing, the issue is resolved ?

### **Step 7: Add Reliable Peers (Optional)**

If you still can’t connect to working nodes, add known healthy peers manually:

```
./PEPEPOW-cli addnode 37.60.251.140:8833 add
./PEPEPOW-cli addnode 84.247.171.81:8833 add
./PEPEPOW-cli addnode 164.68.112.140:8833 add
./PEPEPOW-cli addnode 167.86.71.165:8833 add
```

Or edit `pepepow.conf` and restart the daemon.

### **Step 8: Reindex or Rebuild (If Still Stuck)**

**Option A — Quick repair (keeps block files):**

```
./PEPEPOW-cli stop
./PEPEPOWd -reindex-chainstate -daemon
```

**Option B — Full reindex (slower):**

```
./PEPEPOW-cli stop
PEPEPOWd -reindex -daemon
```

**Option C — Start from scratch (only if data corruption suspected):**

```
./PEPEPOW-cli stop
rm -rf ~/.PEPEPOWcore/blocks ~/.PEPEPOWcore/chainstate
./PEPEPOWd -daemon
```

### **Summary of Useful Commands**

```
tail -n 50 ~/.PEPEPOWcore/debug.log
./PEPEPOW-cli getblockcount
./PEPEPOW-cli mnsync reset
./PEPEPOW-cli invalidateblock <hash>
./PEPEPOW-cli reconsiderblock <hash>
rm -f ~/.PEPEPOWcore/peers.dat ~/.PEPEPOWcore/banlist.dat
./PEPEPOWd -reindex-chainstate -daemon
```
