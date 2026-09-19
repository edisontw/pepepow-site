---
title: "[Masternode] Wallet Update Process"
description: ""
date: "2024-02-27 15:21:51"
updated: "2024-03-02 16:49:56"
slug: "masternode-wallet-update-process"
categories: ["Articles", "Masternode"]
tags: ["Masternode", "SyncIssue", "Ubuntu", "Wallet"]
legacy_url: "https://pepepow.org/masternode-wallet-update-process/"
source_url: "https://pepepow.org/masternode-wallet-update-process/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

1. Stop the wallet program on Ubuntu:
./PEPEPOW-cli stop
2. Download and extract the wallet, ensuring the correct working path:
For ARM64:
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.4.7.1/PEPEPOW-v2.4.7.1--release-aarch64-linux-gnu.tgz -O - | tar -xz
For X64 (QT-gui):
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.4.7.1/PEPEPOW-v2.4.7.1--release-x86\_64-linux-gnu.tgz -O - | tar -xz
X64 (non-QT-gui, smaller download):
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.4.7.1/PEPEPOW-v2.4.7.1--release-cli-x86\_64-linux-gnu.tgz -O - | tar -xz
3. Restart the wallet program:
./PEPEPOWd -daemon
4. Check the wallet version:
./PEPEPOW-cli --version
5. Restart the node (only if experiencing issues with masternode status):
./PEPEPOW-cli masternode start-all
If masternode status remains incorrect, try running start-all multiple times. Check for any synchronization problems. Some users have reported success by using a local wallet to start the node.
