---
title: "Development Roadmap"
description: "The current PEPEPOW development roadmap, showing completed, in-progress, and planned ecosystem projects."
date: "2026-09-21 21:33:00"
updated: "2026-09-21 21:33:00"
slug: "roadmap"
categories: ["Development"]
tags: ["Roadmap", "Development"]
status: "published"
featured: false
migration_review: false
---

## Status

This roadmap restores the earlier PEPEPOW development plan in a clearer current format. It is a **working development map, not a delivery promise**: priorities can change with contributor availability, technical feasibility, security review, funding, and community needs.

“Completed” means a usable implementation has shipped or is in active use. It does not mean maintenance has ended.

<section class="roadmap-summary" aria-label="Roadmap status summary"><div><strong>6</strong><span>Completed</span></div><div><strong>1</strong><span>In progress</span></div><div><strong>7</strong><span>Planned</span></div></section>

<p class="roadmap-updated">Status reviewed: 21 September 2026</p>

## Projects

<div class="roadmap-grid"><article class="roadmap-card roadmap-card--done"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--done">Completed</span><span class="roadmap-number">01</span></div><h3>API Server</h3><p>REST backend for wallets, explorers, and external apps, providing fast balance, transaction, and service queries without exposing node RPC to browsers.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium</p></article><article class="roadmap-card roadmap-card--done"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--done">Completed</span><span class="roadmap-number">02</span></div><h3>ElectrumX Server</h3><p>Lightweight backend for SPV and light-wallet workflows, including fast address balance and transaction-history queries without full-node synchronization.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium–High</p></article><article class="roadmap-card roadmap-card--done"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--done">Completed</span><span class="roadmap-number">03</span></div><h3>Web Wallet (Non-custodial)</h3><p>Browser-based self-custodial wallet for key generation, balance viewing, transaction creation, and sending PEPEW without a custodian.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium</p></article><article class="roadmap-card roadmap-card--done"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--done">Completed</span><span class="roadmap-number">04</span></div><h3>PepewPay — Payment Link / POS PWA</h3><p>Merchant payment flow with payment links, QR codes, and live confirmation for simple in-store and online PEPEW payments.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium</p></article><article class="roadmap-card roadmap-card--planned"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--planned">Planned</span><span class="roadmap-number">05</span></div><h3>JS/TS SDK (pepew-js)</h3><p>A unified JavaScript and TypeScript toolkit for key derivation, transaction building and signing, plus REST/WebSocket integration for application developers.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium</p></article><article class="roadmap-card roadmap-card--done"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--done">Completed</span><span class="roadmap-number">06</span></div><h3>Mobile Wallet</h3><p>The mobile-wallet milestone is fulfilled by the non-custodial Android wallet. Future iOS support, if resumed, should be treated as a separate maintenance target rather than implying current iOS availability.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium–High</p></article><article class="roadmap-card roadmap-card--done"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--done">Completed</span><span class="roadmap-number">07</span></div><h3>Telegram Mini Wallet Bot</h3><p>Social wallet tooling inside Telegram for tipping, small payments, and easier onboarding into the PEPEW ecosystem.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium–High</p></article><article class="roadmap-card roadmap-card--planned"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--planned">Planned</span><span class="roadmap-number">08</span></div><h3>PEPEW Inscriptions & Viewer</h3><p>An optional on-chain creative layer with an explorer-style viewer for inscription content and related metadata.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium</p></article><article class="roadmap-card roadmap-card--planned"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--planned">Planned</span><span class="roadmap-number">09</span></div><h3>Unity Game Kit v1</h3><p>A reference integration kit showing how Unity games can interact with PEPEPOW so game projects can experiment with PEPEW-based rewards and spending.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium</p></article><article class="roadmap-card roadmap-card--progress"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--progress">In progress</span><span class="roadmap-number">10</span></div><h3>Masternode Tools & Monitoring</h3><p>Operational tools and dashboards for masternode setup, reward tracking, status monitoring, alerts, and easier maintenance.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium–High</p></article><article class="roadmap-card roadmap-card--planned"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--planned">Planned</span><span class="roadmap-number">11</span></div><h3>Multi-signature Vault Wallet</h3><p>A secure multi-signature treasury workflow for teams or DAOs, with multiple approvals and optional time-lock controls.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> Medium–High</p></article><article class="roadmap-card roadmap-card--planned"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--planned">Planned</span><span class="roadmap-number">12</span></div><h3>Minimal Oracle Gateway</h3><p>A narrowly scoped gateway for signed and verifiable price or event feeds needed by future bridges and on-chain applications.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> High</p></article><article class="roadmap-card roadmap-card--planned"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--planned">Planned</span><span class="roadmap-number">13</span></div><h3>Liquidity Pool (wPEPEW)</h3><p>Explore wrapped PEPEW on an EVM-compatible or other suitable chain and a PEPEW liquidity pool where security, custody, and maintenance requirements are acceptable.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> High</p></article><article class="roadmap-card roadmap-card--planned"><div class="roadmap-card-topline"><span class="roadmap-status roadmap-status--planned">Planned</span><span class="roadmap-number">14</span></div><h3>DEX Aggregator Integration</h3><p>Integrate a future wrapped PEPEW liquidity path with major DEX aggregators where technically and operationally practical.</p><p class="roadmap-difficulty"><strong>Difficulty:</strong> High</p></article></div>

<p class="roadmap-footnote"><strong>Maintenance continues after completion.</strong> API, ElectrumX, wallets, payment tooling, and Telegram services still require monitoring, security updates, compatibility work, and documentation as their dependencies evolve.</p>

<style>
.roadmap-summary {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: .75rem;
  margin: 1.4rem 0 .75rem;
}
.roadmap-summary > div {
  display: grid;
  gap: .15rem;
  padding: 1rem 1.1rem;
  border: 1px solid #d7ddcf;
  border-radius: .85rem;
  background: rgba(255, 255, 255, .72);
}
.roadmap-summary strong {
  color: #243128;
  font-size: 1.8rem;
  line-height: 1.1;
}
.roadmap-summary span,
.roadmap-updated,
.roadmap-difficulty,
.roadmap-footnote {
  color: #667168;
}
.roadmap-updated {
  margin-top: 0;
  font-size: .9rem;
}
.roadmap-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: .9rem;
  margin-top: 1.25rem;
}
.roadmap-card {
  min-width: 0;
  display: flex;
  flex-direction: column;
  padding: 1.05rem;
  border: 1px solid #d7ddcf;
  border-radius: .9rem;
  background: rgba(255, 255, 255, .74);
  box-shadow: 0 .4rem 1.2rem rgba(65, 85, 63, .04);
}
.roadmap-card--done {
  border-color: #b9d1bd;
}
.roadmap-card--progress {
  border-color: #ddc98f;
}
.roadmap-card-topline {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
}
.roadmap-status {
  display: inline-flex;
  align-items: center;
  min-height: 1.7rem;
  padding: .18rem .55rem;
  border: 1px solid #d2d9cf;
  border-radius: 999px;
  font-size: .72rem;
  font-weight: 800;
  letter-spacing: .03em;
}
.roadmap-status--done {
  border-color: #9bc3a4;
  background: #edf6ec;
  color: #2d7444;
}
.roadmap-status--progress {
  border-color: #d9bd70;
  background: #fff7df;
  color: #7f5918;
}
.roadmap-status--planned {
  background: #f3f5f0;
  color: #667168;
}
.roadmap-number {
  color: #8a958c;
  font-size: .8rem;
  font-weight: 800;
  letter-spacing: .08em;
}
.roadmap-card h3 {
  margin: 1rem 0 .55rem;
  color: #243128;
  font-size: 1.18rem;
  line-height: 1.3;
}
.roadmap-card p {
  margin: 0;
  color: #5d6a60;
  line-height: 1.6;
}
.roadmap-card .roadmap-difficulty {
  margin-top: auto;
  padding-top: 1rem;
  font-size: .86rem;
}
.roadmap-card .roadmap-difficulty strong {
  color: #445149;
}
.roadmap-footnote {
  margin-top: 1.5rem;
  padding: 1rem 1.1rem;
  border-left: .2rem solid #4d9360;
  background: rgba(242, 246, 235, .82);
}
@media (max-width: 38rem) {
  .roadmap-summary {
    grid-template-columns: 1fr;
  }
  .roadmap-grid {
    grid-template-columns: 1fr;
  }
}
</style>
