---
title: "[Announcement] PEPEPOW Mandatory Upgrade – Hoohash Hard Fork"
description: ""
date: "2026-03-16 11:39:27"
updated: "2026-03-16 11:39:27"
slug: "announcement-pepepow-mandatory-upgrade-hoohash-hard-fork"
categories: ["Announcements", "Masternode", "Mining", "Update", "Wallet"]
tags: ["Masternode", "Miner", "Pool", "Update", "Upgrade", "Wallet"]
legacy_url: "https://pepepow.org/announcement-pepepow-mandatory-upgrade-hoohash-hard-fork/"
source_url: "https://pepepow.org/announcement-pepepow-mandatory-upgrade-hoohash-hard-fork/"
status: "draft"
featured: false
migration_review: true
---

The PEPEPOW network will perform a mandatory protocol upgrade introducing the new Proof-of-Work algorithm hoohash-pepew.
**Hard Fork Schedule**
Block Height: 4354200
Estimated Date: April 10, 2026
UTC Time: 18:00 – 19:00
Nodes running earlier versions will no longer synchronize with the network after this block height.
Required Software Version
All operators must upgrade to: PePe-core v2.9.0.2
**Release page:**
<https://github.com/MattF42/PePe-core/releases/tag/v2.9.0.2>
**Masternode Operators**
After upgrading and synchronizing your node, restart masternodes using:
./PEPEPOW-cli masternode start-all
Failure to restart may cause the masternode to expire and stop receiving rewards.
**Miners**
Mining will transition to the Hoohash algorithm. New mining software is available:
hoo\_cpu
hoo\_gpu
hoo\_gpu\_amd
hoo\_cpu\_arm
Download:
<https://htn.foztor.net/>
Miners should switch to the new miner only after the fork activates.
**Pool Operators**
Mining pools must support the algorithm hoohash-pepew.
Reference implementations are available at:
<https://github.com/MattF42/PePePow_multi-hashing>
<https://github.com/HoosatNetwork/hoohash>
Testing on testnet before the mainnet activation is recommended.
