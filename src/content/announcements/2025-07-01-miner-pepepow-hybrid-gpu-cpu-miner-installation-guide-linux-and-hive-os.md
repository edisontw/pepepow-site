---
title: "[Miner] PEPEPOW Hybrid GPU + CPU Miner Installation Guide (Linux and Hive OS)"
description: ""
date: "2025-07-01 15:44:51"
updated: "2025-07-01 16:07:27"
slug: "miner-pepepow-hybrid-gpu-cpu-miner-installation-guide-linux-and-hive-os"
categories: ["Mining"]
tags: ["Miner", "Mining"]
legacy_url: "https://pepepow.org/miner-pepepow-hybrid-gpu-cpu-miner-installation-guide-linux-and-hive-os/"
source_url: "https://pepepow.org/miner-pepepow-hybrid-gpu-cpu-miner-installation-guide-linux-and-hive-os/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

## Linux - Native Installation

### 1.1 Prepare Your System

```
sudo apt -y install nvidia-driver-535
sudo reboot
```

**Verify setup:**

```
nvidia-smi
ldconfig -p | grep libcudart
```

If missing: install `nvidia-utils-535` or similar for your distro.

---

### 1.2 Download & Verify Miner

```
mkdir -p ~/pepepow && cd ~/pepepow
wget https://pepepow.foztor.net/beta/pepepow-miner
echo "ca1196319dfd9495c4bd46687d5e22aafbaaf2156a72d8e0055882c2b4393bca pepepow-miner" | sha256sum -c -
chmod +x pepepow-miner
```

---

### 1.3 Run the Miner

**CPU-only:**

```
./pepepow-miner -o stratum+tcp://POOL:PORT --no-longpoll -u WALLET.CPUTEST
```

**Hybrid (GPU + CPU):**

```
./pepepow-miner -o stratum+tcp://POOL:PORT --no-longpoll -u WALLET.GPUTEST --blake3gpu --gpu-id 0
```

**Useful Flags:**

| Flag | Description |
| --- | --- |
| `-t N` | Set number of CPU threads |
| `--list-gpus` | List available GPUs |
| `--gpu-id X` | Choose specific NVIDIA GPU |
| `--batch-size` | Experiment with 128–4096 (default = auto) |
| `--no-longpoll` | Recommended for some pools |

> **Note:** GPU telemetry is not built-in – use `nvidia-smi` to monitor temps.
> Start with conservative clocks (e.g., mem = 810 MHz).

---

# Hive OS  - Create Custom Miner

1. Go to Hive Dashboard > `Flight Sheets > Custom Miner > Add Miner`
2. Fill in fields:

| Field | Value |
| --- | --- |
| Name | `pepepow-hybrid` |
| Installation URL | `https://pepepow.foztor.net/beta/pepepow-miner` |
| Hash algorithm | `xelishashv2` |
| Miner executable | `pepepow-miner` |
| Launch parameters | *(see below)* |

**Launch Parameters Example:**

```
-o stratum+tcp://%URL%:%PORT% --no-longpoll -u %WAL%.%WORKER_NAME% --blake3gpu --gpu-id 0
```

1. Save and install.

---

## Create a Flight Sheet

- **Wallet:** select your PEPEPOW address
- **Coin:** `PEPEPOW` (custom)
- **Pool:** choose or enter URL
- **Miner:** select `pepepow-hybrid`
- Click **Create Flight Sheet**

---

## Apply to Rig

- Go to **Workers**   select a rig
- Click **Rocket** icon   apply Flight Sheet
- Check logs: `/var/log/miner/pepepow-hybrid` or web console

---

## Troubleshooting

| Issue | Fix |
| --- | --- |
| `libcudart.so.12` missing | Update Hive (`hive-replace -y --upgrade`) |
| No GPU detected | Use `nvidia-smi`; upgrade to NVIDIA driver 525+ |
| Low hashrate | Ensure `--blake3gpu` is added |
| Crashes on riser | Try x16 slot, reduce `--batch-size`, lock mem = 810 MHz |
