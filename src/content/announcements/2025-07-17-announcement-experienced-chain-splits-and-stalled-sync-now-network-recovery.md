---
title: "[Announcement] Experienced chain splits and stalled sync, now network recovery !"
description: ""
date: "2025-07-17 12:26:16"
updated: "2025-07-17 16:08:51"
slug: "announcement-experienced-chain-splits-and-stalled-sync-now-network-recovery"
categories: ["Announcements", "Masternode", "Mining", "Update"]
tags: []
legacy_url: "https://pepepow.org/announcement-experienced-chain-splits-and-stalled-sync-now-network-recovery/"
source_url: "https://pepepow.org/announcement-experienced-chain-splits-and-stalled-sync-now-network-recovery/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

Dear PEPEPOW Community,
Over the past 24 hours, our blockchain experienced a major network disruption caused by a combination of outdated masternode payment data, stalled masternode sync, and issues related to SPORK21’s blacklist mechanism during initial block download (IBD). This resulted in chain splits, stalled sync, and some nodes ending up on different forks.
How We Fixed It:

- Rolled back to the correct chain, coordinated a resync across key nodes, and shared updated data to help the network recover smoothly.

Node Sync Tips:

- If your node is stuck, please stop it, remove `blocks` and `chainstate` folders, and resync using the official seed nodes.
- Only connect to trusted peers (official seeds/pools) until full consensus is restored.

**New Release – v2.8.1.3:**
A new release [v2.8.1.3](https://github.com/MattF42/PePe-core/releases/tag/v2.8.1.3) is now available.
**Upgrading is not strictly mandatory, but if you experience any sync issues, upgrading should be the first thing you try.**
This update includes fixes for SPORK21 and IBD to make future network recovery and sync more robust.
**Special Thanks**
Huge thanks to Foztor and everyone who supported recovery efforts, including all node operators who coordinated quickly to get the chain back on track.
**If you have any questions or need support, please join PEPEPOW community and post it. Let’s continue to keep PEPEPOW strong and resilient!**
