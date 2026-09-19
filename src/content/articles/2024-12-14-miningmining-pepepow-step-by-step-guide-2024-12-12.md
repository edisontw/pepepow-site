---
title: "[Mining]Mining PEPEPOW: Step-by-Step Guide (2024.12.12)"
description: ""
date: "2024-12-14 12:10:17"
updated: "2024-12-14 13:03:07"
slug: "miningmining-pepepow-step-by-step-guide-2024-12-12"
categories: ["Articles", "Mining"]
tags: ["Mining"]
legacy_url: "https://pepepow.org/miningmining-pepepow-step-by-step-guide-2024-12-12/"
source_url: "https://pepepow.org/miningmining-pepepow-step-by-step-guide-2024-12-12/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

### 

### Algorithm Details

- **Algorithm**: Xelish2-pepew (modified from Xelis)
- **Repository**: [Xelis Hash GitHub](https://github.com/xelis-project/xelis-hash/blob/master/README.md)

---

### Steps to Start Mining

**Step 1: Download/Create a Wallet**

- **Options**: Core wallet or web wallet
- **Purpose**: To store your PEPEPOW earnings

**Step 2: Get Your Wallet Address**

- This address will be used to receive mined PEPEPOW.

**Step 3: Choose a Mining Pool**

- Example Pool: `stratum-eu.pepepow.foztor.net:3232`

**Step 4: Download and Set Up Mining Software**

- **Recommended Mining Software**: SRBMiner or HiveOS
- **Algorithm**: `xelishashv2_pepew`
- **Simplest Option**: Use SRBMiner with guided setup

**Sample SRBMiner Command**:

```
SRBMiner-MULTI.exe --algorithm xelishashv2_pepew --pool stratum+tcp://stratum-eu.pepepow.foztor.net:3232 --wallet YOUR_WALLET.WORKER_NAME --password x  
pause
```

**Step 5: Start Mining and HODL**

- Launch the miner and watch as you accumulate PEPEPOW.

---

### Mining Pools

**Community Pool**

```
SRBMiner-MULTI.exe --algorithm xelishashv2_pepew --pool stratum+tcp://stratum-eu.pepepow.foztor.net:3232 --wallet YOUR_WALLET_ADDRESS --password x --cpu-threads 0 --disable-gpu
```

**Mining4people Pool**

- **Pool Address**: `na2.mining4people.com:4176`

```
SRBMiner-MULTI.exe --algorithm xelishashv2_pepew --pool stratum+tcp://na2.mining4people.com:4176 --wallet YOUR_WALLET_ADDRESS --password x --cpu-threads 0 --disable-gpu
```

**Zpool**

```
SRBMiner-MULTI.exe --algorithm xelishashv2_pepew -o stratum+tcp://xelisv2-pepew.na.mine.zpool.ca:4833 -u YOUR_WALLET_ADDRESS --password c=PEPEW
```

**Mining with HiveOS**

- **Select Miner**: SRBMiner
- **Algorithm**: `xelishashv2_pepew`

### Mining Software

**CPU Mining**

1. **SRBMiner**: Download it [here](https://github.com/doktor83/SRBMiner-Multi/releases).
2. **CPUMiner (Foztor's Version)**: Get it [here](https://github.com/MattF42/pepew-cpu-miner/releases).

**GPU Mining**

- **Status**: Currently not available.

---

### Supported Pools

1. **Community Pool**: Visit [community-pool.pepepow.org](https://community-pool.pepepow.org/).
2. **Zpool**: Access it at [zpool.ca](http://zpool.ca/).
3. **Mining4people PPLNS**: 95% PPLNS pool is available [here](https://mining4people.com/pool/pepecoin-pplns/).
4. **Mining4people Solo**: 70% Solo pool is available [here](https://mining4people.com/pool/pepecoin-solo/).
