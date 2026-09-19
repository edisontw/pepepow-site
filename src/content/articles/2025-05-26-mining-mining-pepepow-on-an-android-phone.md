---
title: "[Mining] Mining PEPEPOW on an Android Phone"
description: ""
date: "2025-05-26 16:03:12"
updated: "2025-05-28 13:32:58"
slug: "mining-mining-pepepow-on-an-android-phone"
categories: ["Articles", "Mining"]
tags: ["Miner", "Mining"]
legacy_url: "https://pepepow.org/mining-mining-pepepow-on-an-android-phone/"
source_url: "https://pepepow.org/mining-mining-pepepow-on-an-android-phone/"
status: "draft"
featured: false
migration_review: true
---

> **Legacy safety warning:** This archived procedure targets the software and network state at its publication date. Do not run these commands verbatim on a current wallet or node. Verify the current PEPEPOW Core release and network state first. Stop the wallet cleanly and keep a separate backup of `wallet.dat` before file or blockchain changes. Never share private keys or recovery phrases. Treat hard-coded peers, block heights, download URLs, and services as historical, and inspect any remote script before executing it.

Quick & Complete Guide – Mining PEPEPOW on Android

## Quick & Complete Guide – Mining **PEPEPOW** on an Android Phone

**Goal:** Run the new ARM-optimized *cpuminer v3.2.2* in Termux.  
**Total setup time:** ≈ 5 minutes.

---

### 1 · Install Termux

1. Visit **F-Droid** → <https://f-droid.org/packages/com.termux/>
2. Download **Termux APK** → install → open it.

---

### 2 · Prep Termux (first launch)

```
pkg update && pkg upgrade -y      # refresh system
pkg install curl -y               # curl is required for download
```

---

### 3 · Auto-install the Optimised Miner

Paste the single line below; it fetches the right binary for your CPU (A53, A72, etc.) and sets permissions automatically.

```
curl -s -L https://github.com/MattF42/pepew-cpu-miner/releases/download/v3.2.2/install.sh | sh
```

*Includes a built-in **1.5% dev-fee**.*

---

### 4 · Start Mining

```
./cpuminer -a xelisv2-pepew \
-o stratum+tcp://eu.pepepow.foztor.net:3232 \
-u YOUR_DGB_OR_PEPEPOW_ADDRESS \
-p c=DGB,zap=PEPEW \
-t 4
```

- Replace **YOUR\_DGB\_OR\_PEPEPOW\_ADDRESS** with your wallet address.
- `-t 4` = number of CPU threads (adjust up/down for heat & speed).

---

### 5 · Monitor & Optimize

- Watch accepted shares scrolling in the terminal; higher **KH/s** is better.
- If phone overheats, lower thread count (`-t 2`) or use a cooling pad.
- Optional: `pkg install htop` → run `htop` in another Termux tab to see CPU load.

---

### Done! ? Your Android device is now mining PEPEPOW.
