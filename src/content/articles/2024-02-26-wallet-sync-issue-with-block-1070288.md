---
title: "[Wallet] Sync issue with block 1070288"
description: ""
date: "2024-02-26 05:09:31"
updated: "2024-03-02 16:50:48"
slug: "wallet-sync-issue-with-block-1070288"
categories: ["Articles", "Wallet"]
tags: ["Block", "DebugConsole", "Masternode", "SyncIssues", "Update", "Wallet"]
legacy_url: "https://pepepow.org/wallet-sync-issue-with-block-1070288/"
source_url: "https://pepepow.org/wallet-sync-issue-with-block-1070288/"
status: "draft"
featured: false
migration_review: true
---

If you're experiencing sync problems with block 1070288, please follow these steps:
1. Ensure you're using the latest wallet version (v2.4.7.1) for Windows. Download it from: [PEPEPOW-v2.4.7.1-release-x86\_64-w64-mingw32.zip](https://github.com/MattF42/PePe-core/releases/download/v2.4.7.1/PEPEPOW-v2.4.7.1--release-x86\_64-w64-mingw32.zip)
2. Open the wallet and navigate to `Tools` >> `Debug Console`.
3. Input the following commands:
```
addnode 193.122.107.175:8833 add
addnode 132.145.54.241:8833 add
addnode 13.40.57.124:8833 add
addnode 23.239.15.91:8833 add
addnode 2.98.13.50:8833 add
addnode 186.12.200.15:8833 add
invalidateblock 00000000007fd335476c87e3ed71d33faf6aeb2e577e877943599894541937e7
reconsiderblock 00000000012c695bd9543cfd11fa1bd22a647f517fb4980662c5be956a1b69be
```
This should resolve the sync issue with the specified block.
