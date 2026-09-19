---
title: "[Masernode] Installation Guide for Masternode"
description: ""
date: "2024-12-14 12:28:51"
updated: "2024-12-14 13:04:20"
slug: "masernode-installation-guide-for-masternode"
categories: ["Articles", "Masternode"]
tags: ["Masternode"]
legacy_url: "https://pepepow.org/masernode-installation-guide-for-masternode/"
source_url: "https://pepepow.org/masernode-installation-guide-for-masternode/"
status: "draft"
featured: false
migration_review: true
---

> **Legacy safety warning:** This archived procedure targets the software and network state at its publication date. Do not run these commands verbatim on a current wallet or node. Verify the current PEPEPOW Core release and network state first. Stop the wallet cleanly and keep a separate backup of `wallet.dat` before file or blockchain changes. Never share private keys or recovery phrases. Treat hard-coded peers, block heights, download URLs, and services as historical, and inspect any remote script before executing it.

### **Installation Guide for Masternode on Windows**

---

#### **Introduction**

PEPEPOW is a decentralized blockchain project that combines innovation, transparency, and community engagement. Below is a comprehensive guide to setting up a Masternode on Windows.

---

### **Requirements**

- 10 million PEPEW coins.
- Wallet program (downloadable from the [PEPEPOW GitHub](https://github.com/MattF42/PePe-core/releases)).
- A computer that is always online.
- A static IP address.

---

### **Step-by-Step Installation**

1. **Install the Wallet Program**
   - Download and install the **QT Wallet** from the official GitHub page.
   - Allow the wallet to fully synchronize (this may take several hours).
   - If synchronization issues arise, refer to resources on the PEPEPOW website or Discord.
2. **Find Your Wallet Address**
   - Open the wallet, navigate to **File > Receiving Addresses**.
   - If no address exists, create a new one.
3. **Transfer PEPEW Coins**
   - Send exactly **10 million PEPEW coins** to your address in a **single transaction**.
   - Ensure the receiving wallet address has a zero balance before transferring.
4. **Enable the Masternode Tab**
   - Open the wallet, go to **Settings > Options > Wallet**.
   - Enable the Masternode tab and restart the wallet.
5. **Find Masternode Output and Private Key**
   - Open **Tools > Debug Console** and enter the following commands:
     - `masternode outputs` (to get the transaction output).
     - `masternode genkey` (to generate the private key).
6. **Edit `PEPEPOW.conf`**
   - Navigate to **Tools > Open Wallet Configuration File** and add the following lines:

     ```
     masternode=1
     masternodeprivkey=<Your_Private_Key>
     externalip=<Your_Static_IP>
     ```
7. **Edit `masternode.conf`**
   - Navigate to **Tools > Open Masternode Configuration File** and input:

     ```
     <Node_Name> <Static_IP>:8833 <Private_Key> <Transaction_Output>
     ```
8. **View Configured Masternodes**
   - Go to the **Masternode screen > My Masternodes** to verify your configuration.
9. **Start the Masternode**
   - Click the **Start All** button and confirm the action.
   - Check if your node is listed with the status **ENABLED**.
10. **Verify Status**
    - Open **Debug Console** and input:

      ```
      masternode status
      ```
    - Ensure the response shows **Successfully STARTED**.
    - Verify on the [PEPEPOW Explorer](https://explorer.pepepow.org/masternodes).
11. **Receive Rewards**
    - The first reward will be credited approximately 24 hours after your Masternode is in **ENABLED** status.

---

### **Masternode Setup Guide (Ubuntu/Linux)**

---

#### **Requirements**

- Virtual machine with a static IP address  (SSH access optional).
- 10 million PEPEW coins.
- Latest PEPEPOW wallet from GitHub.

---

### **Step-by-Step Installation**

1. **Establish SSH Connection**

   ```
   ssh -i <Your_Private_Key>.key user@<Your_IP_Address>
   ```
2. **Download and Extract Wallet Files**
   For ARM64:

   ```
   wget -c https://github.com/MattF42/PePe-core/releases/download/v2.6.2.12/PEPEPOW-v2.6.2.12-b837f88-release-aarch64-linux-gnu.tgz -O - | tar -xz
   ```

   For X64 (QT-gui):

   ```
   wget -c https://github.com/MattF42/PePe-core/releases/download/v2.6.2.12/PEPEPOW-v2.6.2.12-b837f88-release-x86_64-linux-gnu.tgz -O - | tar -xz
   ```
3. **Synchronize the Wallet**

   ```
   ./PEPEPOWd -daemon
   ```
4. **Check Synchronization Status**

   ```
   ./PEPEPOW-cli getblockcount
   ```
5. **Obtain Wallet Address and Transfer Coins**

   ```
   ./PEPEPOW-cli getaccountaddress ""
   ./PEPEPOW-cli getbalance
   ```
6. **Generate Masternode Output and Private Key**

   ```
   ./PEPEPOW-cli masternode outputs
   ./PEPEPOW-cli masternode genkey
   ```
7. **Edit Configuration Files**
   - Install Nano if not available:

     ```
     sudo apt update -y
     sudo apt install nano
     cd .PEPEPOWcore
     nano PEPEPOW.conf
     nano masternode.conf
     ```
   - Add the necessary details to `PEPEPOW.conf` and `masternode.conf`.
8. **Restart the Wallet and Run Masternode**

   ```
   ./PEPEPOW-cli stop
   ./PEPEPOWd -daemon
   ./PEPEPOW-cli masternode start-all
   ```
9. **Verify Masternode Status**

   ```
   ./PEPEPOW-cli masternode status
   ./PEPEPOW-cli masternodelist info "<Your_IP>"
   ```
10. **Download Wallet Backup**

    ```
    scp -i <Your_Private_Key>.key ubuntu@<Your_IP_Address>:/home/ubuntu/.PEPEPOWcore/wallet.dat C:\Users\<Your_User>\Downloads\wallet.dat
    ```

---

This guide provides the complete steps for setting up a PEPEPOW Masternode on both **Windows** and **Linux** platforms. Follow these instructions to securely configure and operate your node while earning rewards!
