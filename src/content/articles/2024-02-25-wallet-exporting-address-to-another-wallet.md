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

> **Legacy safety warning:** This archived procedure targets the software and network state at its publication date. Do not run these commands verbatim on a current wallet or node. Verify the current PEPEPOW Core release and network state first. Stop the wallet cleanly and keep a separate backup of `wallet.dat` before file or blockchain changes. Never share private keys or recovery phrases. Treat hard-coded peers, block heights, download URLs, and services as historical, and inspect any remote script before executing it.

1. Use the CLI or debug console to execute the command:
- `dumpprivkey "PEPEPOWaddress"`
2. In a new wallet, import the private key:
- `importprivkey "PEPEPOWprivkey" ("label" rescan)`
Repeat these steps for each address you wish to transfer between wallets.
