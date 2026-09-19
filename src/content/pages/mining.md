---
title: "Mining"
description: ""
date: "2020-04-13 11:18:48"
updated: "2026-09-19 20:25:51"
slug: "mining"
categories: []
tags: []
legacy_url: "https://pepepow.org/mining/"
source_url: "https://pepepow.org/mining/"
status: "draft"
featured: false
migration_review: true
---

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

Current operational details below were reviewed against the HooHash/HTN miner documentation on **19 Sep 2026**.

- **Algorithm:** HooHash V110 (PEPEPOW variant)
- **Recommended miner source:** [HTN Miner downloads](https://htn.foztor.net/)
- **Current HTN release shown by the download site:** v1.4.22
- **Current PEPEPOW detection:** HTN Miner v1.4.19 and later can automatically detect PEPEPOW from a valid PEPEPOW wallet address. The older `--pepepow` flag is no longer required for current releases.

### Miner Options

HTN currently provides several builds:

- `hoo_cpu` — x86_64 CPU miner; AVX2 is required
- `hoo_gpu` — NVIDIA CUDA GPU miner
- `hoo_gpu_amd` — AMD GPU miner
- `hoo_cpu_arm` — ARM64 CPU miner, including supported Linux/Termux environments

Always use the current download page rather than copying an old versioned binary from a historical announcement.

### Download Mining Software

#### HTN CPU Miner

```bash
wget -c https://htn.foztor.net/hoo_cpu.tar.gz -O - | tar -xz
cd hoo_cpu
```

#### HTN NVIDIA GPU Miner

```bash
wget -c https://htn.foztor.net/hoo_gpu.tar.gz -O - | tar -xz
cd hoo_gpu
```

For AMD or ARM64, use the matching current package from the [HTN Miner download page](https://htn.foztor.net/).

### Basic Mining Flow

1. Create or choose a PEPEPOW wallet.
2. Copy your own PEPEW receiving address.
3. Choose a currently operating PEPEPOW pool and confirm its current Stratum endpoint.
4. Download the current HTN Miner build for your hardware.
5. Start the miner with your pool URL and wallet address.
6. Confirm accepted shares on the pool dashboard before leaving the miner unattended.

Example CPU command:

```bash
./hoo_cpu -o stratum+tcp://YOUR_POOL_HOST:PORT \
  -u YOUR_WALLET_ADDRESS -p x
```

Example NVIDIA GPU command:

```bash
./hoo_gpu -o stratum+tcp://YOUR_POOL_HOST:PORT \
  -u YOUR_WALLET_ADDRESS -p x --gpu-id 0
```

List available NVIDIA GPUs:

```bash
./hoo_gpu --list-gpu
```

### Pool Status

#### Foztor Community Pool

[Open PEPEPOW Community Pool](https://community-pool.pepepow.org/)

The community pool currently exposes a HooHash V110 PEPEW pool and active miner statistics. Use its **Connect** page for the current Stratum configuration instead of relying on an old copied port.

#### PEPEPOW Lab Pool

[Open PEPEPOW Lab Pool](https://pool.pepepow.net/)

The Lab Pool is a community development/testing pool. Confirm its current status and connection instructions on the pool itself before mining.

#### Mining4People

[Mining4People — PEPEW / HooHash pool](https://mining4people.com/pool/pepew)

A current PEPEW HooHash pool page is available. Its displayed command examples may lag behind the latest HTN Miner behavior, so use the pool's current Stratum endpoint while following the current HTN release documentation for miner flags.

#### Other Pools

[MiningPoolStats — PEPEPOW](https://miningpoolstats.stream/pepepow)

Other third-party endpoints can change over time. They should not be treated as current merely because they appear in an older PEPEPOW guide. Verify the pool page, algorithm, wallet format, fee, payout policy, and Stratum endpoint before connecting.

### HiveOS

Use **Custom Miner** with the current HTN Miner package rather than an old Xelis/SRBMiner preset.

Suggested baseline:

| Setting | Value |
| --- | --- |
| Miner package | current `hoo_cpu`, `hoo_gpu`, or other matching HTN build |
| Installation source | `https://htn.foztor.net/` |
| Pool URL | current PEPEPOW Stratum URL from the selected pool |
| Wallet | your PEPEW receiving address |
| Password | pool-specific; often `x` |
| `--pepepow` | not required on current HTN releases with address auto-detection |

If HiveOS shows an old Xelis algorithm, unsupported-algorithm message, or rewrites the connection to a legacy WebSocket/Xelis preset, the worker is using the wrong miner configuration.

### Safety Reminder

- Use your own wallet address.
- Verify accepted shares on the pool dashboard.
- Download miners only from the current trusted project source.
- Re-check pool status before reusing an old flight sheet or command.
- Historical PEPEPOW mining posts may describe Memehash or XelisV2 and must not be used as current HooHash setup instructions.

![](/media/legacy/2024/11/PEPEPOW-triumphant.webp)
