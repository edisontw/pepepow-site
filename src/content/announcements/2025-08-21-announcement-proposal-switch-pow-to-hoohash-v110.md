---
title: "[Announcement] Proposal: Switch PoW to HooHash V110"
description: ""
date: "2025-08-21 12:56:36"
updated: "2025-08-21 12:56:36"
slug: "announcement-proposal-switch-pow-to-hoohash-v110"
categories: ["Announcements", "Campaigns", "Masternode", "Mining"]
tags: []
legacy_url: "https://pepepow.org/announcement-proposal-switch-pow-to-hoohash-v110/"
source_url: "https://pepepow.org/announcement-proposal-switch-pow-to-hoohash-v110/"
status: "draft"
featured: false
migration_review: true
---

Foztor has spoken with Tonto (owner of HTN & HooHash). If PEPEPOW adopts HooHash V110, we would gain:
CUDA miner (NVIDIA)
OpenCL miner (AMD/Intel, to be extended by Tonto)
CPU miner (already available)
This would finally bring full GPU mining support while keeping CPUs competitive.
**Pros**
-  High energy efficiency — lower wattage on both GPUs and CPUs
- CPU remains competitive (not fully displaced by GPUs)
-  Resistant to ASIC/FPGA by design
- Attracts more miners — GPU miners can join easily
**Cons**
- Not a mature PoW — shorter history, less proven than older algos
- Consensus change required — risk in switching to a new algorithm
- Public miner support uncertain — may lose support from existing devs (e.g., SRBMiner may not adopt HooHash)
**Vote Question**
Should PEPEPOW switch its Proof of Work algorithm from XelisV2-pepew to HooHash V110?
**Options**
Yes — Switch to HooHash V110
No — Stay on XelisV2-pepew
Abstain
Voting Period: Aug 21 ? Sep 4, 2025 (UTC+8)
https://discord.com/channels/1206789719825055754/1208677848353865728/1408063314105471166
**FAQ**
Q1: Will I lose my coins or need to swap?
No. This is only a PoW change. Balances and masternodes remain the same.
Q2: Do masternodes change?
No economic change. Just upgrade binaries to stay on consensus.
Q3: What about exchanges?
Exchanges will need a short maintenance window, we will coordinate.
Q4: Can I still mine with the old XelisV2 miner?
After activation, XelisV2 blocks will be invalid. Please switch to HooHash miners (CPU, CUDA, OpenCL).
