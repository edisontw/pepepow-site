---
title: "[Announcement]  Mine PEPEW on your Android phones !"
description: ""
date: "2025-05-26 15:26:39"
updated: "2025-05-26 15:53:39"
slug: "announcement-mine-pepew-on-your-android-phones"
categories: ["Announcements", "Mining"]
tags: ["Miner", "Mining"]
legacy_url: "https://pepepow.org/announcement-mine-pepew-on-your-android-phones/"
source_url: "https://pepepow.org/announcement-mine-pepew-on-your-android-phones/"
status: "draft"
featured: false
migration_review: true
---

(Posted by Foztor on Discord)
Mining on ARM takes a big step forward today!
I have made some significant performance improvements with NEON/SIMD.
For the moment I'm not publishing the source, but optimised variants are available at:
https://github.com/MattF42/pepew-cpu-miner/releases/tag/v3.2.1
Yes, this means you can now mine PEPEW on your Android phones through Termux or similar ?
TL;DR
curl -s -L https://github.com/MattF42/pepew-cpu-miner/releases/download/v3.2.1/install.sh | sh
Expect further optimizations to this in the near future, I'm now going to take a look at what I can do on X64.
This release includes a 1.5% DevFee in the miner.
These are "oven-ready" miners, which will just run on supported hardware without any dependancy issues or complex tool chains to build!
Happy mining !
