# PEPEPOW Hand-Drawn Visual Assets

This directory stores accepted hand-drawn visual assets for pepepow.net.

Current production inventory (2026-09-20):

- 5 concept direction images
- 4 hero/scenic images
- 1 reusable signpost
- 8 hand-drawn icons
- 2 doodle packs
- 6 page-header illustrations
- 4 lettering/note assets
- 4 miner-frog mascot assets
- 4 editorial spot illustrations
- 2 texture/background packs

Total: 40 generated visual assets.

Upload categories:

- heroes/
- concepts/
- signs/
- icons/
- doodles/
- headers/
- mascot/
- lettering/
- textures/
- spots/

## Current implementation status

Homepage visual slice is implemented on GitHub `main`:

- scenic hero: `heroes/homepage-hero-valley-right-space-v1.webp`
- foreground signpost: `signs/signpost-mine-build-share-belong-v1.webp`
- hero lettering: `lettering/lettering-small-chain-big-community-v1.webp`
- Start Here cards use the Wallet, Mining, Masternode, Share/Market, and Guides icons

The homepage rollout uses a scoped light `handdrawn` theme so the visual refresh can be reviewed before applying it site-wide.

The six page-header illustrations are the next implementation set after homepage visual acceptance.

Mascot assets are intentionally not yet wired into production pages. They remain available for small secondary accents after manual visual/provenance review.

Generation and review rules are defined in:

- docs/HAND_DRAWN_VISUAL_REFRESH_PLAN.md
- docs/HAND_DRAWN_ASSET_PROMPTS.md

Use optimized WebP for generated raster illustrations unless another format is clearly better. Keep semantic website text in HTML/CSS rather than baking critical copy into images.
