---
title: "[Wallet] Recovering Android Mobile Wallet on PC"
description: ""
date: "2024-02-26 05:15:09"
updated: "2024-02-26 05:16:14"
slug: "wallet-recovering-android-mobile-wallet-on-pc"
categories: ["Articles", "Wallet"]
tags: ["Android", "Backup", "BlockChain", "Recovery", "Wallet"]
legacy_url: "https://pepepow.org/wallet-recovering-android-mobile-wallet-on-pc/"
source_url: "https://pepepow.org/wallet-recovering-android-mobile-wallet-on-pc/"
status: "draft"
featured: false
migration_review: true
---

> **Legacy safety warning:** This archived procedure targets the software and network state at its publication date. Do not run these commands verbatim on a current wallet or node. Verify the current PEPEPOW Core release and network state first. Stop the wallet cleanly and keep a separate backup of `wallet.dat` before file or blockchain changes. Never share private keys or recovery phrases. Treat hard-coded peers, block heights, download URLs, and services as historical, and inspect any remote script before executing it.

Follow these steps to recover your Android mobile wallet on a PC wallet using a 12-word recovery phrase:
1. Stop the wallet program. If there is an existing PC wallet, backup or rename the original PC wallet file `wallet.dat`. Skip this step if there is no previous PC wallet.
2. Edit or create a file named `PEPEPOW.conf` in the wallet folder and add the following lines:
```
usehd=1
mnemonic= [12-word recovery phrase]
```
3. Save the file and restart the wallet to synchronize.
A new `wallet.dat` file will be generated, representing the mobile wallet. If the balance shows as 0, execute `./PEPEPOWd -rescan` to rescan the blockchain. Your old wallet should then be restored.
(Note: If you want to use another PC wallet, remember to remove the added content in `PEPEPOW.conf`.)
