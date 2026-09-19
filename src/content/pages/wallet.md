---
title: "Wallet"
description: ""
date: "2020-04-13 11:18:52"
updated: "2026-08-05 16:10:58"
slug: "wallet"
categories: []
tags: []
legacy_url: "https://pepepow.org/wallet/"
source_url: "https://pepepow.org/wallet/"
status: "draft"
featured: false
migration_review: true
---

> Migration candidate generated from the legacy WordPress export. Review facts, links, software versions, commands, and media before publishing.

# PEPEPOW Wallets

## Wallets are essential tools

Please download the lastest version on Github

Wallets are essential tools for securely storing, sending, and receiving PEPEPOW Crypocions. Whether you're a trader, investor, or enthusiast, having a reliable wallet is crucial for managing your cryptocurrency holdings. Please use the lastest version on Github.

PEPEPOW Wallets

Choose the wallet that fits your needs: full-featured desktop wallet, lightweight web wallet (non-custodial), or mobile wallet under development.

### Desktop Wallet

Official desktop wallet for Windows and Linux, with optional block file bootstrap.

Main wallet
![PEPEPOW Desktop Wallet](https://pepepow.org/wp-content/uploads/2024/09/PEPEPOW-desktop1.webp)
[PePecore Releases](https://github.com/MattF42/PePe-core/releases)
[Download Block Files](https://pepepow.foztor.net/chain/pepepow-23Dec-24.zip)
Windows

- [Download ZIP](https://github.com/MattF42/PePe-core/releases/download/v2.9.0.5/PEPEPOW-v2.9.0.5-5a9debc-release-x86_64-w64-mingw32.zip)

Ubuntu / Linux (x86\_64)
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.9.0.5/PEPEPOW-v2.9.0.5-5a9debc-release-x86\_64-linux-gnu.tgz
-O - | tar -xz
Linux (AARCH64)
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.9.0.5/PEPEPOW-v2.9.0.5-5a9debc-release-aarch64-linux-gnu.tgz
-O - | tar -xz

### Web Wallet

Lightweight access for quick use. Includes a fully non-custodial option.

Non-custodial
![](https://pepepow.org/wp-content/uploads/2026/01/web-wallet1.png)
[Open Non-Custodial Web Wallet](https://light.pepepow.net/wallet/)

This is a fully non-custodial web wallet. Your mnemonic and private keys are generated
and stored only on your device.

---

### Mobile Wallet

The mobile wallet is for quick transfers and storing assets .

New release
![](https://pepepow.org/wp-content/uploads/2025/12/android-wallet-release.png)
Download
<https://github.com/edisontw/pepepow-android-wallet-v2/releases>
3rd-Party Platforms

- nonKYC:
  [iOS](https://ios.nonkyc.io/) /
  [Android](https://nonkyc.io/download/latestAPK)

## PEPEPOW Wallet Installation Guide (2025.5.6)

core wallet installation

1. **Download the Wallet**
   - Visit the official release on GitHub and download the Windows wallet file: **[Download PEPEPOW Wallet for Windows](https://github.com/MattF42/PePe-core/releases/download/v2.9.0.4/PEPEPOW-v2.9.0.4-c1394e6-release-x86_64-w64-mingw32.zip)**
2. **Install the Wallet**
   - Unzip the downloaded file.
   - Run the `PEPEPOW-qt.exe` file to launch the wallet.
3. **Sync the Blockchain**
   - The wallet will take some time to synchronize with the blockchain. Make sure your internet connection is stable.
4. **Troubleshooting Sync Issues**
   - If you encounter sync problems:
     - Use the **rescan** option within the wallet.
     - Alternatively, delete all files in the PEPEPOW folder except for `wallet.dat`, then restart the wallet to re-sync.
     - Download the latest block files for faster synchronization: **[Download Block Files](https://pepepow.foztor.net/chain/pepepow-12-April-2026.zip)**

---

**Ubuntu Wallet Installation & Update**

1. **Check Masternode Sync Status**
   - Run the following commands in the terminal:

     ```
     ./PEPEPOW-cli mnsync status
     ./PEPEPOW-cli masternode status
     ```
2. **Stop the Existing Wallet**
   - Use the following command:

     ```
     ./PEPEPOW-cli stop
     ```
3. **Download and Extract the Latest Wallet Files**
   - For **Ubuntu (x86\_64)**:

     ```
     wget -c https://github.com/MattF42/PePe-core/releases/download/v2.9.0.4/PEPEPOW-v2.9.0.4-c1394e6-release-aarch64-linux-gnu.tgz -O - | tar -xz
     ```
   - For **AARCH64**:

     ```
     wget -c https://github.com/MattF42/PePe-core/releases/download/v2.9.0.4/PEPEPOW-v2.9.0.4-c1394e6-release-x86_64-linux-gnu.tgz -O - | tar -xz
     ```
4. **Start the Wallet Daemon**
   - After extracting the files, start the wallet daemon:

     ```
     ./PEPEPOWd -daemon
     ```
5. **Start Masternodes**
   - Ensure your masternodes are correctly configured and start them:

     ```
     ./PEPEPOW-cli masternode start-all
     ```
6. **Check Masternode Status**
   - Verify the status of your masternodes:

     ```
     ./PEPEPOW-cli masternodelist info
     ```

---
