---
title: "About"
description: "An overview of PEPEPOW: its Proof-of-Work network, masternodes, governance history, current infrastructure, and community-built direction."
date: "2024-12-14 07:50:58"
updated: "2026-09-20 16:35:00"
slug: "about"
categories: []
tags: []
legacy_url: "https://pepepow.org/about/"
source_url: "https://pepepow.org/about/"
status: "draft"
featured: false
migration_review: true
---

## A Community-Built Proof-of-Work Network

PEPEPOW is a community-built cryptocurrency network centered on Proof of Work, masternodes, open-source development, and continued adaptation. Its Genesis Block launched on **12 May 2023**, and the project has since moved through several mining, governance, and infrastructure eras.

### Network at a glance

- **Genesis Block:** 12 May 2023
- **Current Proof-of-Work era:** HooHash V110
- **Target average block time:** 20 seconds
- **Coinbase outputs:** Miner · Masternode · Foundation
- **Long-term supply target:** 90B PEPEW before tail Super Blocks

## How the network works

### Proof-of-Work mining

Miners secure PEPEPOW with HooHash V110. Earlier versions of the network used Memehash and later XelisV2-pepew before the current HooHash era.

Under the current Core coinbase logic, the miner receives the remainder after the foundation payment and masternode payment are calculated. The miner share therefore varies with the block reward rather than remaining a permanent fixed percentage.

For current miner software and pool entry points, use the [Mining page](/mining/).

### Masternodes

Masternodes contribute to PEPEPOW network services and governance. Current Core code calculates the masternode payment as **35% of the block reward remaining after the foundation payment is subtracted**.

PEPEPOW currently uses tiered masternode collateral levels of **10M, 25M, 50M, and 100M PEPEW**. Higher tiers receive proportionally higher reward-selection frequency.

For current setup and maintenance guidance, use the [Masternode page](/masternode/).

### Development funding

Older PEPEPOW material often uses the term **DevFee**. Current Core consensus code describes the corresponding coinbase output as a **foundation payment**.

For current mainnet blocks, `GetFoundationPayment()` returns **250 PEPEW** after the 2024 activation height. The amount follows PEPEPOW's special-block pattern and can become 2× or 5× on the corresponding higher-reward blocks.

This current code-based description supersedes the older simplified 65% miner / 35% masternode wording for present operation.

### Governance and community development

PEPEPOW has used DAO-oriented governance structures including adminDAO, miningDAO, nodeDAO, marketDAO, and devDAO. Governance practice has changed over time, so older DAO documents are best read as historical policy references rather than descriptions of every current procedure.

Community discussion, public repositories, dated announcements, and verifiable network data remain important parts of the project's operating model.

## How the project evolved

PEPEPOW began as a small blockchain experiment shaped by meme culture and decentralized currency. Over time it also faced chain instability, changes in developer maintenance, service disruptions, and security incidents affecting community communication.

Community contributors continued maintaining wallets, mining infrastructure, documentation, pools, explorers, monitoring services, and node support. That history pushed the project toward practical maintenance, public verification, and distributed contribution.

Selected milestones:

- **2023-05-12:** Genesis Block launched.
- **2023-08-10:** First hard fork; the community agreed to remove founder fees and update Core.
- **2023-09-25:** CoinGecko listing improved external market visibility.
- **2023-10:** DAO nominations and appointments marked a new stage of community governance.
- **2024-01-14:** Community vote approved a 5% developer fee for development and integration needs.
- **2024-02-24:** A new Discord server was launched following community communication changes.
- **2024-08-29:** Mining moved to XelisV2-pepew.
- **2026-04:** The mandatory HooHash V110 hard fork opened the current mining era.

For dated details, use the [announcement archive](/announcements/) and [site search](/search/).

## Current direction

PEPEPOW development focuses on practical infrastructure rather than a fixed roadmap of promised features. Priorities can change with contributor availability, technical feasibility, funding, and community consensus.

Current areas of work include:

- **Core infrastructure:** API services, ElectrumX, explorers, monitoring, and masternode tools.
- **Wallet access:** non-custodial web and mobile access, safer onboarding, backup, and recovery guidance.
- **Developer tools:** SDKs, payment experiments, game integrations, and community-built utilities.
- **Liquidity and interoperability:** exchange access, liquidity paths, swaps, and bridge-related experiments where practical.

## AI-assisted development

As a small community project, PEPEPOW uses AI-assisted workflows where they can extend development capacity—for example in code review, debugging, log analysis, monitoring scripts, documentation, FAQs, translation, and user support.

AI assistance does not replace human responsibility. Security-sensitive changes, wallet releases, protocol upgrades, treasury operations, payout handling, and public announcements still require human review and judgment.

## Visual identity

The current visual direction emphasizes effort, persistence, construction, open participation, and forward movement. Website artwork uses a bright hand-drawn editorial system with natural scenery, practical objects, and restrained community motifs.

Character artwork remains secondary to content, network data, tools, and technical guidance.

## Reference documents

- [PEPEPOW White Paper v1.0 — 18 Sep 2023, Minus](/docs/legacy/2023/09/whitepaper-v1.0.1.pdf)
- [PEPEPOW DAO Reference — 25 Oct 2023, Minus](/docs/legacy/2023/10/pepepow-dao-op-policy-v1.0.0.pdf)
- [PEPEPOW White Paper v2.0 — 26 Jan 2025, Edison](https://docs.google.com/document/d/1FIs7lQo_7tjNhJ9n95_YrvuIGmLlSjmkKqEWIktlU5Q/edit?tab=t.0)
- [PEPEPOW Visual Reference Guideline v1.0 — 1 Jan 2026, Edison](/docs/legacy/2026/01/PEPEPOW-Visual-Reference-Guideline-v1.0.pdf)
- [PEPEPOW White Paper v2.1 — 31 May 2026, Edison](/docs/legacy/2026/05/PEPEPOW-Whitepaper-v2.1.pdf)

## Risk and verification

PEPEPOW is a small community cryptocurrency. Exchange availability, liquidity, trading volume, mining participation, infrastructure reliability, and development activity can all change over time.

This page is a project and technical reference, not financial, investment, or legal advice. Verify current sources before mining, trading, operating nodes, moving funds, or building services around PEPEPOW.

Useful current entry points:

- [Network Pulse](/network/)
- [Wallets](/wallet/)
- [Mining](/mining/)
- [Masternode](/masternode/)
- [Market](/market/)
- [Community](/community/)
- [PEPEPOW Core source](https://github.com/MattF42/PePe-core)
