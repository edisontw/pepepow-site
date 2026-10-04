---
title: "PEPEW Payment Bot is now live!"
description: "You can now create a PEPEW payment request directly from Telegram or Discord."
date: "2026-10-04T02:53:00Z"
slug: "pepew-payment-bot-is-now-live"
categories: ["Announcements", "Wallet", "Community"]
tags: ["wallet", "pay", "paymentbot"]
status: "published"
featured: false
migration_review: false
---

**PEPEW Payment Bot is now live!** 🐸⚡

You can now create a PEPEW payment request directly from Telegram or Discord.

**Telegram**
Bot: @pepepow_paymentbot

```text
/pay <PEPEW-address> <amount>
```

Example:
```text
/pay PRfbEeHAKKbz6Voz85WJudrJwTA3ZbHunb 1000
```

**Discord**
Invite the bot:
https://discord.com/oauth2/authorize?client_id=1554856855467982908

Command:
```text
/pepew-pay address:<PEPEW-address> amount:<amount>
```

Example:
```text
/pepew-pay address:PRfbEeHAKKbz6Voz85WJudrJwTA3ZbHunb amount:1000
```

### How it works

```text
Telegram / Discord command
        ↓
PEPEW Payment API
        ↓
PepewPay payment link
        ↓
User pays and signs locally in the wallet
        ↓
PEPEW network confirmation
        ↓
Signed Payment Platform webhook
        ↓
Bot updates the payment status
```

The receiving address is supplied for each request and validated by the Payment Platform. The bot never receives or stores mnemonics, private keys, or wallet signing material. 🔐

Current production settings use a **15-minute payment window** and **1 confirmation** for payment confirmation.

This payment bot also provides part of the infrastructure for **PepewPay**([https://pay.pepepow.net/](https://pay.pepepow.net/)), which is currently being expanded from payment-link functionality toward a more complete merchant payment / POS PWA experience.

Technical documentation:
[https://github.com/edisontw/pepepow-electrumx-service/blob/main/docs/PAYMENT_API_V1.md](https://github.com/edisontw/pepepow-electrumx-service/blob/main/docs/PAYMENT_API_V1.md)
[https://github.com/edisontw/pepepow-devkit/blob/main/docs/BOT_OPERATIONS.md](https://github.com/edisontw/pepepow-devkit/blob/main/docs/BOT_OPERATIONS.md)
