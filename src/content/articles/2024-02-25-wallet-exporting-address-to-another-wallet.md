---
title: "[Wallet] Exporting Address to Another Wallet"
description: ""
date: "2024-02-25 17:38:18"
updated: "2024-02-27 15:44:21"
slug: "wallet-exporting-address-to-another-wallet"
categories: ["Articles", "Wallet"]
tags: ["BlockChain", "CLI", "DebugConsole", "PrivateKey", "Wallet"]
legacy_url: "https://pepepow.org/wallet-exporting-address-to-another-wallet/"
source_url: "https://pepepow.org/wallet-exporting-address-to-another-wallet/"
status: "draft"
featured: false
migration_review: true
---

1. Use the CLI or debug console to execute the command:
- `dumpprivkey "PEPEPOWaddress"`
2. In a new wallet, import the private key:
- `importprivkey "PEPEPOWprivkey" ("label" rescan)`
Repeat these steps for each address you wish to transfer between wallets.
