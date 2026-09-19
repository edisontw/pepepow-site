---
title: "[Announcement] PEPEPOW Web Wallet Update: UTXO Consolidation Feature"
description: ""
date: "2026-01-21 14:23:20"
updated: "2026-01-21 14:23:20"
slug: "announcement-pepepow-web-wallet-update-utxo-consolidation-feature"
categories: ["Announcements", "Wallet"]
tags: ["UTXO", "WebWallet"]
legacy_url: "https://pepepow.org/announcement-pepepow-web-wallet-update-utxo-consolidation-feature/"
source_url: "https://pepepow.org/announcement-pepepow-web-wallet-update-utxo-consolidation-feature/"
status: "draft"
featured: false
migration_review: true
---

The PEPEPOW Web Wallet has been updated with a new **UTXO Consolidation feature**.
This feature allows users to combine multiple small unspent outputs into a single output, reducing transaction size and preventing failures caused by the “TRANSACTION TOO LARGE” error.
Such errors typically occur when a wallet accumulates a large number of small UTXOs over time, for example from mining rewards or frequent small transactions. Consolidation improves transaction reliability and overall wallet usability.
Please note that \*\*legacy PEPEPOW addresses created without a mnemonic phrase are not supported\*\* in the Web Wallet. Due to the wallet’s strict non-custodial design, private keys cannot be reconstructed for these addresses.
To use consolidation and future Web Wallet features, users are advised to generate a **new mnemonic-backed address** within the Web Wallet. These addresses are designed for permanent, long-term use.
