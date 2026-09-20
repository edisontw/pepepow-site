---
title: "Masternode"
description: "Current PEPEPOW masternode requirements, collateral tiers, Windows and Linux setup guidance, status checks, backups, and security reminders."
date: "2020-04-13 11:18:50"
updated: "2026-09-19 20:25:51"
slug: "masternode"
categories: []
tags: []
legacy_url: "https://pepepow.org/masternode/"
source_url: "https://pepepow.org/masternode/"
status: "draft"
featured: false
migration_review: true
---

## PEPEPOW Masternodes

A PEPEPOW masternode is a continuously available network node configured with a qualifying PEPEW collateral output. Masternodes participate in PEPEPOW network services and reward selection, and they form part of the project's governance and infrastructure model.

Operators should treat the collateral transaction, masternode key, wallet backup, server access, and software version as security-sensitive operational data.

## Current requirements

You can run a masternode on your own machine or use a third-party hosting service. Self-hosting gives you direct control of the node and its configuration; third-party services introduce additional custody and operational risk.

- Supported collateral tiers: **10,000,000 / 25,000,000 / 50,000,000 / 100,000,000 PEPEW**
- Higher collateral tiers receive proportionally higher reward-selection frequency
- The current **PEPEPOW Core wallet**
- A computer or VPS/server that can remain online continuously
- A stable public IP address for the masternode
- Access to the wallet and masternode configuration files
- A separate safe backup of `wallet.dat`

Wallet download:
<https://github.com/MattF42/PePe-core/releases>

Current Core release reviewed on 19 Sep 2026: **v2.9.0.5**.

## Windows Masternode Setup

### 1. Install and Sync the Wallet

- Download and install the **PEPEPOW QT Wallet**.
- Launch the wallet and allow it to fully sync.
- Initial sync may take several hours.
- If syncing is slow or stuck, check the PEPEPOW website or Discord for help.

### 2. Create a Receiving Address

- Open **File → Receiving Addresses**.
- Create a new address if you do not already have one.

This address will be used for your Masternode collateral.

### 3. Create the Collateral Output

Choose one supported tier and create the matching collateral output:

- **10,000,000 PEPEW**
- **25,000,000 PEPEW**
- **50,000,000 PEPEW**
- **100,000,000 PEPEW**

Use the exact amount for the selected tier and keep the collateral as a dedicated output. Do not split one masternode tier across several smaller outputs.

### 4. Enable the Masternode Tab

- Go to **Settings → Options → Wallet**.
- Enable the **Masternode** tab.
- Restart the wallet.

### 5. Generate the Masternode Output and Key

Open **Tools → Debug Console** and run:

```
masternode outputs
masternode genkey
```

Record the collateral transaction output and the generated masternode key in a secure place. Do not post the masternode key in public support channels.

### 6. Edit `PEPEPOW.conf`

Open **Tools → Open Wallet Configuration File** and add:

```
masternode=1
masternodeprivkey=<Your_Private_Key>
externalip=<Your_Static_IP>
```

### 7. Edit `masternode.conf`

Open **Tools → Open Masternode Configuration File** and add one line:

```
<Node_Name> <Static_IP>:8833 <Private_Key> <Transaction_Output>
```

### 8. Verify Your Configuration

Open the **Masternode** tab and check **My Masternodes** to confirm your entry appears correctly.

### 9. Start the Masternode

- Click **Start All**.
- Confirm the action.

When successful, the status should show **ENABLED**.

### 10. Check the Status

In **Debug Console**, run:

```
masternode status
```

A successful setup should show **Successfully STARTED**.

You can also verify it on the explorer:
<https://explorer.pepepow.org/network>

### 11. Rewards

Masternode reward timing is not fixed. It depends on the number of active masternodes, collateral tier, queue position, and current network conditions. Use the current Explorer/network page to verify masternode state rather than relying on a fixed first-payment estimate.

## Ubuntu / Linux Masternode Setup

### 1. Connect to Your Server

```
ssh -i <Your_Private_Key>.key user@<Your_IP_Address>
```

### 2. Download the Wallet

**AARCH64**

```
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.9.0.5/PEPEPOW-v2.9.0.5-5a9debc-release-aarch64-linux-gnu.tgz -O - | tar -xz
```

**x86\_64**

```
wget -c https://github.com/MattF42/PePe-core/releases/download/v2.9.0.5/PEPEPOW-v2.9.0.5-5a9debc-release-x86_64-linux-gnu.tgz -O - | tar -xz
```

### 3. Start the Daemon

```
./PEPEPOWd -daemon
```

### 4. Check Sync Progress

```
./PEPEPOW-cli getblockcount
```

### 5. Check Address and Balance

```
./PEPEPOW-cli getaccountaddress ""
./PEPEPOW-cli getbalance
```

### 6. Generate the Masternode Output and Key

```
./PEPEPOW-cli masternode outputs
./PEPEPOW-cli masternode genkey
```

### 7. Edit the Configuration Files

If needed, install Nano first:

```
sudo apt update -y
sudo apt install nano
```

Then edit the wallet files:

```
cd ~/.PEPEPOWcore
nano PEPEPOW.conf
nano masternode.conf
```

### 8. Restart the Wallet and Start the Masternode

```
./PEPEPOW-cli stop
./PEPEPOWd -daemon
./PEPEPOW-cli masternode start-all
```

### 9. Check Masternode Status

```
./PEPEPOW-cli masternode status
./PEPEPOW-cli masternodelist info "<Your_IP>"
```

### 10. Back Up Your Wallet

Always keep a separate copy of `wallet.dat` before and after configuration changes. Run the copy command from your local computer, not from the masternode server.

Example:

```bash
scp -i <Your_Private_Key>.key ubuntu@<Your_IP>:/home/ubuntu/.PEPEPOWcore/wallet.dat ./wallet.dat
```

Store the backup somewhere separate from the VPS and protect it as sensitive wallet data.

## Third-Party Masternode Services

Third-party services change independently of PEPEPOW. Never infer that a service is endorsed, non-custodial, or currently accepting PEPEPOW solely because it appeared on the old website.

- [NodeHub](https://nodehub.io/dashboard/view_coin?coin=pepepow) — its public explorer still indexes PEPEPOW. Confirm current hosting terms and PEPEPOW support before paying or entering configuration data.
- [Pecunia Platform](https://www.pecuniaplatform.io/coin-stats/PEPEPOW) — retained as a legacy service reference, but the PEPEPOW product page could not be independently verified during this migration audit. Confirm availability directly before use.

Do not send masternode collateral or private keys to a third-party service until you understand its custody model, withdrawal process, fees, and security requirements.

## Final checks

Before starting or restarting a masternode, confirm:

- the selected collateral tier is represented by the correct dedicated output;
- the node is fully synchronized;
- the public IP and masternode key are configured correctly;
- `wallet.dat` has a separate backup;
- the current Core release notes do not require an additional protocol or restart step;
- the masternode key has not been exposed in public support channels.

Reward timing is not fixed. Verify current masternode state through the [Network page](/network/) or the [PEPEPOW Explorer](https://explorer.pepepow.org/network).

For community support, use the current links on the [Community page](/community/).
