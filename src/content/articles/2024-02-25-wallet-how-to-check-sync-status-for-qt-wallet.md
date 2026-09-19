---
title: "[Wallet] How to Check Sync Status for QT Wallet"
description: ""
date: "2024-02-25 17:28:32"
updated: "2024-02-27 15:43:43"
slug: "wallet-how-to-check-sync-status-for-qt-wallet"
categories: ["Articles", "Wallet"]
tags: ["Explorer", "QTWallet", "SyncIssues", "Troubleshooting", "Wallet"]
legacy_url: "https://pepepow.org/wallet-how-to-check-sync-status-for-qt-wallet/"
source_url: "https://pepepow.org/wallet-how-to-check-sync-status-for-qt-wallet/"
status: "draft"
featured: false
migration_review: true
---

1. Open your QT wallet and navigate to Tool >> Debug Console.
2. Type the command: `getblockcount`.
3. Ensure that the returned block count matches or is very close to the block height displayed on one of the following explorers: <https://pepew.ccore.online/>, <https://explorer.pepepow.org/>, or <https://explorer2.pepepow.org/>.
\*\*Troubleshooting Sync Issues:\*\*
- If your local sync stops at a significantly lower height for an extended period (approximately 10 minutes), take the following steps:
- Delete all files in the wallet directory except for "wallet.dat".
- Re-sync the wallet.
\*\*Checking Address and Balance:\*\*
To check your address and balance, use the command: `listaddressgroupings`.
