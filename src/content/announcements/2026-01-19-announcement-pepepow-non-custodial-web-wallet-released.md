---
title: "[Announcement] PEPEPOW Non-Custodial Web Wallet Released"
description: ""
date: "2026-01-19 14:52:50"
updated: "2026-01-19 14:52:50"
slug: "announcement-pepepow-non-custodial-web-wallet-released"
categories: ["Announcements", "Wallet"]
tags: ["Telegram", "Tip", "Wallet", "WebWallet"]
legacy_url: "https://pepepow.org/announcement-pepepow-non-custodial-web-wallet-released/"
source_url: "https://pepepow.org/announcement-pepepow-non-custodial-web-wallet-released/"
status: "draft"
featured: false
migration_review: true
---

We are pleased to announce that the new **PEPEPOW Non-Custodial Web Wallet** has been completed and is now available for public testing.

This wallet is designed with a security-first philosophy. Mnemonic phrases and private keys are generated and stored exclusively on the user side. All transaction signing is performed locally, ensuring that sensitive key material is never exposed to the server.

The backend service is strictly limited to blockchain data retrieval, transaction fee estimation, and raw transaction broadcasting. It does not store private keys, mnemonics, or signed data.

The same wallet core is shared between the Web Wallet and the upcoming Telegram Mini App, providing a consistent and extensible foundation for future PEPEPOW wallet services.

For developers and advanced users, detailed documentation and architectural notes are available on GitHub:  
<https://github.com/edisontw/pepepow-wallet-suite/tree/main/docs>

Feedback and bug reports during the testing phase are highly appreciated.

<https://wallet.pepepow.net/>
