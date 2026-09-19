---
title: "[Announcement] Transition to XelisV2 Algorithm"
description: ""
date: "2024-08-07 03:32:47"
updated: "2024-09-01 05:05:22"
slug: "announcement-transition-to-xelisv2-algorithm"
categories: ["Announcements", "Update"]
tags: ["Disocrd", "Update", "Vote"]
legacy_url: "https://pepepow.org/announcement-transition-to-xelisv2-algorithm/"
source_url: "https://pepepow.org/announcement-transition-to-xelisv2-algorithm/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

**Dear PEPEPOW Community,**
We are excited to announce a proposed change to our Proof of Work (PoW) algorithm from memehash to XelisV2. This new algorithm offers enhanced security and aligns with the latest standards in PoW technology.
**Development Overview**:
- XelisV2 Implementation: A new Proof of Work (PoW) hash algorithm, XelisV2, has been developed by the XELIS (XEL) blockchain, and implemented in PepePOW by Foztor.
- Node and Miner Compatibility: Initial testing showed successful block mining using a forked version of cpuminer. The current focus is on debugging and refining the implementation.
- Regtest Network: A regtest network is used for testing, with nodes and miners able to connect and sync using provided configurations.
- Stratum Support: Development of stratum support is now availavle for pool mining.
**Pros of XelisV2:**
1. Enhanced Security: XelisV2 offers improved security features compared to memehash.
2. Compatibility: Miner developers who have implemented Xelis for other coins can easily adapt their miners for PEPEPOW.
3. Encourages Decentralisation: XelisV2 brings an egalitarian level of mining performance between CPUs and GPUs.
4. Support Solo Mining: Solo mining directly to a node is now supported.
5. Reduced energy consumption\*\*: Introducing CPU mining on an similar footing to GPUs introduces reduced energy opportunities
**Cons of XelisV2:**
1. Transition Complexity: Switching from memehash to XelisV2 requires updates to all existing mining software and infrastructure.
2. Initial Incompatibility: Existing XelisV2 miners are not directly compatible with PEPEPOW, requiring adjustments by developers.
3. Learning Curve: Miners and node operators need to familiarize themselves with the new algorithm and its implementation.
The poll fot this decision on adoption of XelisV2 is now live on discord and will close in one week. Please join us and share any thought !
(By Foztor)
[Discord Vote](https://discord.com/channels/1206789719825055754/1208677848353865728/1270330496877985825)
