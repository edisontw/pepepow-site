---
title: "Mining"
description: ""
date: "2020-04-13 11:18:48"
updated: "2026-06-21 15:30:28"
slug: "mining"
categories: []
tags: []
legacy_url: "https://pepepow.org/mining/"
source_url: "https://pepepow.org/mining/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

# PEPEPOW Mining

## Earn and participate in the network through mining

Join the Mining Community

Mining is the process by which new PEPEPOW Crypocions are created and transactions are validated and added to the blockchain. As a decentralized network, PEPEPOW Crypocions relies on miners to secure and maintain its blockchain.

Become a part of the PEPEPOW Crypocions mining community and contribute to the decentralized network's security and stability. Whether you're a novice miner or an experienced enthusiast, mining PEPEPOW Crypocions offers opportunities for participation and potential rewards.

## Start Mining

![](/media/legacy/2024/02/Pepepow1a.png)

### How Mining Works

Mining involves solving complex mathematical puzzles to validate transactions and create new blocks. Miners compete to find the solution to these puzzles, and the first miner to solve it is rewarded with a block reward in PEPEPOW Crypocions.

![](/media/legacy/2024/02/P-coin4-1.png)

### Mining Pools

Due to the competitive nature of mining, many miners join mining pools to combine their resources and increase their chances of successfully mining blocks. Mining pools distribute rewards among participants based on their contribution to the pool's computational power..

![](/media/legacy/2024/02/7594bf0b-5b3a-4c0e-83b3-c6a3087eaa97.jpg)

### Mining Equipment

To participate in mining PEPEPOW Crypocions, miners typically use specialized hardware called mining rigs. These rigs are equipped with powerful centeral processor units (CPUs) or graphics cards (GPUs) specifically high performance for mining cryptocurrencies.

![](/media/legacy/2024/02/a27d4a8f-2cfb-4f6f-899b-5c601ebb696a-1.jpg)

### Rewards

Miners receive rewards in the form of newly minted PEPEPOW Crypocions and transaction fees for successfully mining blocks. These rewards serve as an incentive for miners to contribute their computational power to secure the network.

## PEPEPOW Mining Quick Guide

Follow these steps to start mining PEPEPOW using HTN Miner. CPU and GPU examples are included below, along with ready-to-run pool commands.

Algorithm: **Hoohash-pepew**
Miner: **HTN Miner (CPU / GPU)**
Required flag: **--pepepow**

### Download Mining Software

Official HTN
[Download HTN CPU Miner](https://htn.foztor.net/hoo_cpu.tar.gz)
[Download HTN GPU Miner](https://htn.foztor.net/hoo_gpu.tar.gz)

#### HTN CPU Miner

wget -c https://htn.foztor.net/hoo\_cpu.tar.gz -O - | tar -xz
cd hoo\_cpu

#### HTN GPU Miner

wget -c https://htn.foztor.net/hoo\_gpu.tar.gz -O - | tar -xz
cd hoo\_gpu
?? SRBMiner and Xelis-based miners are no longer supported after the Hoohash upgrade. Please use HTN Miner with `--pepepow`.

### Steps to Start Mining

Beginner friendly
1 Download or Create a Wallet

**Options:** Core wallet or web wallet

**Purpose:** Store your mined PEPEPOW earnings

2 Get Your Wallet Address

This address will be used to receive mining rewards.

3 Choose a Mining Pool

**Example:** `stratum-eu.pepepow.foztor.net:13232`

See pool list: [miningpoolstats.stream/pepepow](https://miningpoolstats.stream/pepepow)

4 Run HTN Miner

- **Required miner:** HTN Miner
- **Algorithm:** Hoohash-pepew
- **Important:** Must include `--pepepow`

CPU Mining Example
./hoo\_cpu -o stratum+tcp://stratum-eu.pepepow.foztor.net:13232
-u YOUR\_WALLET\_ADDRESS -t 1 -p x --pepepow
GPU Mining Example
export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:~/hoo\_gpu/libs
./hoo\_gpu -o stratum+tcp://stratum-eu.pepepow.foztor.net:13232
-u YOUR\_WALLET\_ADDRESS -gpu-id 0 -p x --pepepow
List Available GPUs
./hoo\_gpu --list-gpu
5 Start Mining

Run the miner and begin earning PEPEPOW rewards.

Tip: Replace **YOUR\_WALLET\_ADDRESS** before running commands.

### Supported Mining Pools

Copy & run

#### Community Pool

**Pool:** `stratum-eu.pepepow.foztor.net:13232`

[Visit Community Pool](https://community-pool.pepepow.org/)

./hoo\_cpu -o stratum+tcp://stratum-eu.pepepow.foztor.net:13232
-u YOUR\_WALLET\_ADDRESS -t 1 -p x --pepepow

#### Mining4people PPLNS

**Pool:** `na2.mining4people.com:4176`

[Open PPLNS Pool](https://mining4people.com/pool/pepecoin-pplns/)

./hoo\_cpu -o stratum+tcp://na2.mining4people.com:4176
-u pepew:YOUR\_WALLET\_ADDRESS -p x --pepepow

#### Mining4people Solo

**Pool:** `See pool page`

[Open Solo Pool](https://mining4people.com/pool/pepecoin-solo/)

Check the latest solo pool connection details on the Mining4people solo page before mining.

#### Zpool

**Pool:** `xelisv2-pepew.na.mine.zpool.ca:4833`

[Open Zpool](http://zpool.ca/)

./hoo\_cpu -o stratum+tcp://xelisv2-pepew.na.mine.zpool.ca:4833
-u YOUR\_WALLET\_ADDRESS -p c=PEPEW --pepepow

#### GPU Selection

Use this command to view all available GPUs before starting GPU mining.

./hoo\_gpu --list-gpu

#### Important Reminder

Use your own wallet address, or you will mine for someone else.

Required flag: --pepepow

### HiveOS Custom Miner Setup

HTN Miner / Hoohash-pepew

PEPEPOW on HiveOS should be configured with **Custom Miner** using **HTN Miner**.
Do not use old SRBMiner or Xelis-based presets. The miner must connect with the
**stratum+tcp** pool URL and include the required `--pepepow` flag.

Important: leave **Hash algorithm** empty or set to **empty**. Do not select old Xelis or preset algo templates.

|  |  |
| --- | --- |
| Miner name | `hoo_cpu` |
| Installation URL | `https://htn.foztor.net/hoo_cpu.tar.gz` |
| Hash algorithm | leave empty |
| Wallet and worker template | `%WAL%.%WORKER_NAME%` |
| Pool URL | `stratum+tcp://stratum-eu.pepepow.foztor.net:13232` |
| Pass | `x` |
| Extra config arguments | `--pepepow` |

#### Flight Sheet

**Coin:** PEPEW

**Wallet:** your PEPEPOW wallet

**Pool:** Configure in miner

**Miner:** Custom

**Name:** choose any name for this flight sheet

#### What Each Setting Means

**Miner name** is the executable package HiveOS installs and runs.

**Pool URL** must include `stratum+tcp://`.

**Extra config arguments** passes the required PEPEPOW flag to HTN Miner.

**Wallet and worker template** automatically inserts your wallet and worker name.

The resulting connection will be equivalent to running HTN Miner with your wallet, worker name, pool URL, password, and the `--pepepow` flag.

#### Setup Steps

1. Create or select your PEPEPOW wallet in HiveOS.
2. Create a new Flight Sheet and choose **Custom** as miner.
3. Open **Setup Miner Config**.
4. Fill in the fields exactly as shown above.
5. Keep **Hash algorithm** empty.
6. Save the config and update the Flight Sheet.
7. Apply the Flight Sheet to your worker and check miner logs.

If you see messages such as `UNSUPPORTED ALGO`, `XELIS WebSocket`, or automatic conversion to a websocket URL, the rig is still using an old preset or an incorrect wrapper path.
Example values
Miner name: hoo\_cpu
Installation URL: https://htn.foztor.net/hoo\_cpu.tar.gz
Hash algorithm:
Wallet and worker template: %WAL%.%WORKER\_NAME%
Pool URL: stratum+tcp://stratum-eu.pepepow.foztor.net:13232
Pass: x
Extra config arguments: --pepepow
If a new HTN Miner version is released, the safest way in HiveOS is to create a new custom miner name for the updated version, such as `hoo_cpu_v147` or `hoo_gpu_v147`. This avoids old cached files being reused.

![](/media/legacy/2024/11/PEPEPOW-triumphant.webp)
