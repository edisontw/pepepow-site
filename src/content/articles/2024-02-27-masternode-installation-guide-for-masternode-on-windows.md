---
title: "[Masternode] Installation Guide for Masternode on Windows"
description: ""
date: "2024-02-27 15:41:31"
updated: "2024-02-27 15:42:30"
slug: "masternode-installation-guide-for-masternode-on-windows"
categories: ["Articles", "Masternode"]
tags: ["Masternode", "QTWallet", "Windows"]
legacy_url: "https://pepepow.org/masternode-installation-guide-for-masternode-on-windows/"
source_url: "https://pepepow.org/masternode-installation-guide-for-masternode-on-windows/"
status: "draft"
featured: false
migration_review: true
---

> **Legacy safety warning:** This archived procedure targets the software and network state at its publication date. Do not run these commands verbatim on a current wallet or node. Verify the current PEPEPOW Core release and network state first. Stop the wallet cleanly and keep a separate backup of `wallet.dat` before file or blockchain changes. Never share private keys or recovery phrases. Treat hard-coded peers, block heights, download URLs, and services as historical, and inspect any remote script before executing it.

1. Obtain 10 million PEPEW coins.
2. Install a new QT wallet and wait for synchronization. Find the wallet address under: File >> Receiving Addresses. Transfer exactly 10 million PEPEW coins in one transaction.
3. Open Masternode setup: Settings >> Options >> Wallet >> Enable Masternode tab. Configure and restart the wallet.
4. Find Masternode Output and Private Key: Tools >> Debug Console, input:
- `masternode outputs` to get Output
- `masternode genkey` to get Private Key
5. Edit PEPEPOW.conf: Tools >> Open Wallet Configuration File, input:
- `masternode=1`
- `masternodeprivkey=Private Key`
- `externalip=Static IP`
6. Edit masterstone.conf: Tools >> Open Masternode Configuration File, input:
- `Node Name Static IP:8833 Private Key Output`
7. View configured Masternodes in Masternode screen >> My Masternodes.
8. Start Masternode: Click "Start All" button, confirm with "yes." Check for your node in the list. Status should change to "ENABLED."
9. Verification: In Debug Console, input "masternode status." It should display "Successfully STARTED." Check also on https://explorer.pepepow.org/masternodes.
10. Receive first reward after 24 hours of "ENABLE" status.
