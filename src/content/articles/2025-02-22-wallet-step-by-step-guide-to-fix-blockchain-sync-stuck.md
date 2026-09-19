---
title: "[Wallet] Step-by-Step Guide to Fix Blockchain Sync Stuck"
description: ""
date: "2025-02-22 15:04:49"
updated: "2025-02-22 15:04:49"
slug: "wallet-step-by-step-guide-to-fix-blockchain-sync-stuck"
categories: ["Articles", "Wallet"]
tags: ["SyncIssue", "Wallet"]
legacy_url: "https://pepepow.org/wallet-step-by-step-guide-to-fix-blockchain-sync-stuck/"
source_url: "https://pepepow.org/wallet-step-by-step-guide-to-fix-blockchain-sync-stuck/"
status: "draft"
featured: false
migration_review: true
---

### **Step-by-Step Guide to Fix Blockchain Sync Stuck**

If your PEPEPOW wallet is stuck at a certain block and not syncing further, follow these steps to troubleshoot and resolve the issue.

### **Step 1: Check Debug Log for Errors**

First, check the last 50 lines of the debug log to identify any potential errors or issues:

```
tail -n 50 ~/.PEPEPOWcore/debug.log
```

Look for errors such as:

- Checkpoint not reached
- Invalid block detected
- Failed to connect to peers

If there are any error messages, take note of them as they might indicate the issue.

### **Step 2: Check the Current Block Height**

Verify if your wallet is stuck at a specific block:

```
./PEPEPOW-cli getblockcount
```

Compare the output with the latest block height on an official explorer.
If your node is behind and not progressing, continue to the next steps.

### **Step 3: Restart Node and Clear Peers**

If the node is stuck due to bad peers, restart it and remove the `peers.dat` file:

```
./PEPEPOW-cli stop
rm ~/.PEPEPOWcore/peers.dat
./PEPEPOWd -daemon
```

The `peers.dat` file stores known network peers. Deleting it forces the wallet to reconnect to fresh peers.
Check if the block count starts increasing after the restart:

```
./PEPEPOW-cli getblockcount
```

If the sync is still stuck, proceed to the next step.

### **Step 4: Invalidate the Stuck Block**

If your wallet is stuck at block 2633306, force it to roll back and reconsider previous blocks:

```
./PEPEPOW-cli invalidateblock $(./PEPEPOW-cli getblockhash 2633306)
```

This command tells the wallet to reject the problematic block and attempt to resync from an earlier valid block.

### **Step 5: Restart the Node**

After invalidating the block, restart the node to apply the changes:

```
./PEPEPOW-cli stop
./PEPEPOWd -daemon
```

Wait a few minutes and then check the sync progress again:

```
./PEPEPOW-cli getblockcount
```

If the block count is increasing, the issue is resolved.

### **Additional Steps (If Still Not Syncing)**

If the sync is still stuck, consider:

1. **Manually adding nodes (if cannot connect to nodes)**
   Find active nodes and add them manually:

   ```
   ./PEPEPOW-cli addnode "IP_ADDRESS":8833 add
   ```
2. **Reindexing the blockchain (longer process)**

   ```
   ./PEPEPOW-cli stop
   ./PEPEPOWd -daemon -reindex
   ```
3. **Deleting corrupted blockchain data and resyncing from scratch**

   ```
   ./PEPEPOW-cli stop
   rm -rf ~/.PEPEPOWcore/blocks ~/.PEPEPOWcore/chainstate
   ./PEPEPOWd -daemon
   ```
