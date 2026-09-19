---
title: "[Annoucement] PEPEPOW Network Update: Chain Stable After Hoohash Upgrade"
description: ""
date: "2026-04-16 16:41:32"
updated: "2026-04-16 16:42:35"
slug: "annoucement-pepepow-network-update-chain-stable-after-hoohash-upgrade"
categories: ["Announcements", "Masternode", "Mining", "Update", "Wallet"]
tags: ["Masternode", "Miner", "Update", "Wallet"]
legacy_url: "https://pepepow.org/annoucement-pepepow-network-update-chain-stable-after-hoohash-upgrade/"
source_url: "https://pepepow.org/annoucement-pepepow-network-update-chain-stable-after-hoohash-upgrade/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

## PEPEPOW Network Update: Chain Stable After Hoohash Upgrade

PEPEPOW has completed its Hoohash upgrade, and the chain is now stable and operating normally.

Following the hard fork, the network experienced a small temporary stall. Since then, the community has continued to identify issues, release miner fixes, and improve node consistency across different platforms. The result is a network that is now stable while ongoing debugging and optimization continue.

### Miner Updates

Community miner releases have progressed quickly:

- **v1.4.7** fixed a bug that prevented miners from finding solutions meeting network difficulty.
- **v1.4.8** corrected `--cpu-affinity` behavior in `hoo_cpu` and added a 65536 difficulty multiplier.
- **v1.4.9** added proper `xtranonce2` support, improved DevFee stratum selection to reduce stall risk, and removed duplicate solution issues.

Miner downloads are available at:

[`https://htn.foztor.net/`](https://htn.foztor.net/)

### Community Pool

Mining is currently available through the PEPEPOW community pool:

[`https://community-pool.pepepow.org/`](https://community-pool.pepepow.org/)  
`stratum+tcp://stratum-eu.pepepow.foztor.net:13232`  
`stratum+tcps://stratum-eu.pepepow.foztor.net:13432`

### Supported Miner Builds

- `hoo_cpu` for x64 CPUs with AVX2
- `hoo_gpu` for Nvidia GPUs (Maxwell or newer)
- `hoo_cpu_arm` for ARM64 CPUs, including mobile environments such as Termux

### Core Update

A new Pepe-Core release is now available:

**Pepe-Core v2.9.0.4**  
[`https://github.com/MattF42/PePe-core/releases/tag/v2.9.0.4`](https://github.com/MattF42/PePe-core/releases/tag/v2.9.0.4)

This version is required for correct operation on Windows x64 and is also strongly recommended for Linux nodes.  
It includes:

- switch to `openlibm` for improved FP64 determinism across platforms
- a blockchain checkpoint at block height `4362478`
- stricter FP64 compilation flags

### Current Status

The PEPEPOW chain is stable, but the work is not finished. The network is now entering a continued phase of refinement, testing, and optimization. Community contributors are actively monitoring miner behavior, node consistency, and pool compatibility to make the ecosystem more reliable over time.

Thank you to everyone who upgraded quickly, tested new releases, reported bugs, and helped move PEPEPOW through this transition.
