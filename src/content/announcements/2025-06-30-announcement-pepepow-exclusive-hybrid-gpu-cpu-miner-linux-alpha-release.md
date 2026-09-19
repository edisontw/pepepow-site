---
title: "[Announcement] PEPEPOW Exclusive Hybrid GPU/CPU Miner (Linux)– Alpha Release!"
description: ""
date: "2025-06-30 12:00:16"
updated: "2025-07-01 15:34:05"
slug: "announcement-pepepow-exclusive-hybrid-gpu-cpu-miner-linux-alpha-release"
categories: ["Announcements", "Mining"]
tags: ["Miner", "Mining"]
legacy_url: "https://pepepow.org/announcement-pepepow-exclusive-hybrid-gpu-cpu-miner-linux-alpha-release/"
source_url: "https://pepepow.org/announcement-pepepow-exclusive-hybrid-gpu-cpu-miner-linux-alpha-release/"
status: "draft"
featured: false
migration_review: true
---

**PEPEPOW Exclusive Hybrid GPU/CPU Miner (Linux)– Alpha Release!**
After much development by Foztor and enthusiastic developers, the first hybrid GPU/CPU miner specifically for PEPEPOW is now in public alpha testing! All miners are welcome to test and share your performance results!
**Key Notes & Testing Guidelines**
1. **NVIDIA GPUs only** (CUDA required) and **Linux only** (HiveOS should work)
2. No GPU monitoring or overclocking features included yet—please use external tools (e.g. nvidia-smi, Afterburner) to watch your GPU temps and clocks!
3. The miner defaults to GPU0. Use `--list-gpus` to check GPU IDs or `--gpu-id X` to select another card.
4. The GPU currently only handles part of the workload. At present, the hybrid mode is about 10–20% faster than pure CPU mining (example: Xeon 40 threads + 3070M gives about 2KH/s more than CPU alone), but performance will improve as the pipeline is optimized!
5. Stability on risers is not guaranteed—using a direct x16 slot is recommended for testing.
6. Both CPU and GPU modes support multithreading. Default is all logical cores; use `-t N` to set the number of threads.
7. Download link: [[https://pepepow.foztor.net/beta/pepepow-miner](https://pepepow.foztor.net/beta/pepepow-miner "https://pepepow.foztor.net/beta/pepepow-miner")]
SHA256 for verification:

```
ca1196319dfd9495c4bd46687d5e22aafbaaf2156a72d8e0055882c2b4393bca  pepepow-miner
```

8. Example commands:

**CPU mode:**

```
./pepepow-miner -o stratum+tcp://POOL:PORT --no-longpoll -u WALLET.CPUTEST
```

**GPU mode:**

```
./pepepow-miner -o stratum+tcp://POOL:PORT --no-longpoll -u WALLET.GPUTEST --blake3gpu
```

?Please share your performance results, issues, or suggestions
Please share your results, issues, and suggestions! We will continue optimizing so PEPEPOW can be a truly community-friendly, energy-efficient blockchain!
