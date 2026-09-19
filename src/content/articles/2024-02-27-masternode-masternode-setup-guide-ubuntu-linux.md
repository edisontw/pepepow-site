---
title: "[Masternode] Masternode Setup Guide (Ubuntu/Linux)"
description: ""
date: "2024-02-27 14:36:04"
updated: "2024-12-10 18:15:27"
slug: "masternode-masternode-setup-guide-ubuntu-linux"
categories: ["Articles", "Masternode"]
tags: ["Block", "Cloud", "Linux", "Masternode", "SSH", "SyncIssue", "Ubuntu", "Wallet"]
legacy_url: "https://pepepow.org/masternode-masternode-setup-guide-ubuntu-linux/"
source_url: "https://pepepow.org/masternode-masternode-setup-guide-ubuntu-linux/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

1. Establish SSH connection to the virtual machine using the private key obtained during creation:
ssh -i XXXXX.key user@ip
2. Download and extract the latest wallet files (v2.6.2.12):
For X64:
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.6.2.12/PEPEPOW-v2.6.2.12-b837f88-release-x86\_64-linux-gnu.tgz -O - | tar -xz
For ARM64:
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.6.2.12/PEPEPOW-v2.6.2.12-b837f88-release-aarch64-linux-gnu.tgz -O - | tar -xz
3. Synchronize the wallet:
./PEPEPOWd -daemon
4. Check block synchronization:
./PEPEPOW-cli getblockcount
5. Obtain the wallet address and transfer 10M PEPEPW:
./PEPEPOW-cli getaccountaddress ""
6. Check account balance:
./PEPEPOW-cli getbalance
7. Find masternode output and key:
./PEPEPOW-cli masternode outputs
./PEPEPOW-cli masternode genkey
8. Use Nano to edit configuration files:
if nano is not installed:
sudo apt update -y
sudo apt install nano
cd .PEPEPOWcore
nano PEPEPOW.conf
nano masternode.conf
9. Restart the wallet and run masternode (remember to open port 8833):
./PEPEPOW-cli stop
./PEPEPOWd -daemon
./PEPEPOW-cli masternode start-all
./PEPEPOW-cli masternode status
10. Check masternode status and online presence:
./PEPEPOW-cli masternodelist info "your IP"
11. Download wallet.dat for backup (path for Windows):
scp -i XXXX.key ubuntu@IP:/home/ubuntu/.PEPEPOWcore/wallet.dat C:\Users\XXXX\Downloads\wallet.dat
