---
title: "[Masternode] 2024.2.1 EMERGENCY RELEASE (1070288 block issue)"
description: ""
date: "2024-02-27 15:26:25"
updated: "2024-02-27 15:42:24"
slug: "masternode-2024-2-1-emergency-release-1070288-block-issue"
categories: ["Articles", "Masternode"]
tags: ["Block", "Masternode", "SyncIssues", "Update"]
legacy_url: "https://pepepow.org/masternode-2024-2-1-emergency-release-1070288-block-issue/"
source_url: "https://pepepow.org/masternode-2024-2-1-emergency-release-1070288-block-issue/"
status: "draft"
featured: false
migration_review: true
---

**Don't need to do this if there's no sysnc problem**
In case of sync issues with block 1070288, follow these steps:
1. Update to the new wallet version
2. Add additional nodes for synchronization:
- ./PEPEPOW-cli addnode 186.12.200.15:8833 add
- ./PEPEPOW-cli addnode 173.249.22.16:8833 add
- ./PEPEPOW-cli addnode 167.86.80.36:8833 add
- ./PEPEPOW-cli addnode 164.68.112.227:8833 add
- ./PEPEPOW-cli addnode 207.180.218.133:8833 add
- ./PEPEPOW-cli addnode 34.162.17.167:8833 add
3. Remove invalidated blocks:
- ./PEPEPOW-cli invalidateblock 00000000007fd335476c87e3ed71d33faf6aeb2e577e877943599894541937e7
- ./PEPEPOW-cli reconsiderblock 00000000012c695bd9543cfd11fa1bd22a647f517fb4980662c5be956a1b69be
4. Check status:
- ./PEPEPOW-cli --version
- ./PEPEPOW-cli getblockcount
- ./PEPEPOW-cli mnsync status
- ./PEPEPOW-cli masternode status
- ./PEPEPOW-cli masternodelist info IP
If the masternode status shows WATCHDOG\_EXPIRED and rewards are not received, execute:
- ./PEPEPOW-cli masternode start-all
