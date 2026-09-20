# PEPEPOW Hand-Drawn Visual Refresh Specification

Status: Production review fixes implemented / Batch 05 asset gaps queued
Target: https://pepepow.net
Repository authority: edisontw/pepepow-site main
Last aligned: 2026-09-20

---

## 1. Purpose

This document defines the visual direction for gradually refreshing pepepow.net from the current production design into a hand-drawn illustration system with restrained handwritten accents.

This is a visual-system evolution, not a site architecture rewrite. The existing Astro site, content structure, routes, Network Pulse, search, deployment model, and production safety rules remain authoritative.

The design goal is to make the site feel more human, memorable, community-built, and approachable while preserving the clarity and trust required for wallet, mining, masternode, network, and technical information.

---

## 2. Core visual direction

The target style combines:

- clean modern website UI
- hand-drawn editorial illustration
- light sketchbook / travel-journal character
- soft watercolor or gouache-like color fills
- generous white space
- handwritten accent notes used sparingly
- simple doodle arrows, underlines, hearts, sunbursts, and dividers
- natural scenery such as mountains, valleys, rivers, paths, trees, rocks, villages, and wooden signs

The visual reference is a bright white landing page with a scenic illustrated landscape, restrained green accents, simple hand-drawn feature icons, and occasional handwritten notes around the edges.

The site must not become a rasterized poster, a meme landing page, or a cartoon-heavy character site.

---

## 3. Brand mood

The visual system should communicate:

- community-built
- proof of work
- open participation
- self-custody
- practical contribution
- long-term building
- calm optimism
- transparency
- decentralization

A working visual slogan may use:

Small Chain, Big Community

Supporting phrases may include:

- Mine · Build · Share · Belong
- People Power Progress
- Together We Build a Brighter Tomorrow
- A More Open, Fairer Future
- Built by the community, for the people

Marketing copy remains editable HTML text unless an item is intentionally created as a decorative handwritten asset.

---

## 4. Design principles

### 4.1 Content and usability remain primary

The visual refresh must not reduce:

- content completeness
- route preservation
- accessibility
- readability
- responsive behavior
- SEO
- performance
- operational clarity
- maintainability

Network status, wallet instructions, mining instructions, masternode operations, release information, and technical guides must remain easy to scan and read.

### 4.2 Illustration is a layer, not the layout engine

Do not render the entire page as one generated image.

Use HTML/CSS for:

- navigation
- headings that carry semantic meaning
- body text
- buttons
- cards
- tables
- status components
- live data
- forms or tools
- accessibility labels

Use image assets for:

- scenic illustrations
- decorative handwritten notes
- doodles
- signposts
- mascot appearances
- non-semantic illustration
- page-header art

### 4.3 Handwriting is an accent

Target approximately 85–90% conventional readable typography and 10–15% handwritten or hand-drawn accent treatment.

Handwritten treatment is appropriate for:

- short hero phrases
- marginal notes
- arrows and underlines
- small callouts
- wooden sign labels
- decorative dividers

Do not use handwriting for long paragraphs, tables, status data, wallet safety instructions, or dense technical text.

---

## 5. Mascot direction and intellectual-property guardrails

The preferred long-term direction is an original PEPEPOW miner-frog mascot rather than making the site dependent on a third-party Pepe character. However, visual quality takes priority over forcing artificial differences that make the mascot unattractive or inconsistent.

Required direction:

- the yellow miner helmet is the primary recurring PEPEPOW character cue
- small secondary presence
- appears only occasionally
- normally placed near a corner, edge, path, sign, or scenic foreground
- optional miner lamp, backpack, work jacket, gloves, boots, map, or pickaxe
- simple friendly expression
- prefer original clothing, gear, pose language, proportions, and facial treatment
- do not deliberately distort the character merely to make it look different
- avoid making the frog mascot the site logo or dominant hero subject unless separately reviewed

Preferred generation path:

1. first attempt an original PEPEPOW miner-frog design with the yellow miner helmet
2. keep the best-looking design if it is visually coherent and clearly works with the hand-drawn site
3. if repeated original-design attempts produce an unattractive or awkward mascot, a more familiar Pepe-like frog form may be used temporarily as a visual fallback
4. any fallback that closely resembles recognizable third-party Pepe artwork should remain small, secondary, and explicitly marked for provenance/licensing review before production release

The site should not sacrifice the overall visual quality merely to create forced facial or body differences. At the same time, scenery, objects, typography, icons, signs, and network/mining metaphors should carry most of the site's identity so the design does not become character-dependent.

Before public release of any character-heavy or close-derivative asset, perform a manual provenance/IP review.

---

## 6. Color direction

The palette should remain light and natural.

Primary direction:

- off-white / warm white page background
- PEPEPOW green for actions and accents
- leaf and meadow greens
- warm wood and earth tones
- pale sky blue
- muted mountain blue-grey
- dark ink / charcoal for text and line art
- limited warm yellow for the miner-helmet cue and small highlights

Avoid:

- neon overload
- casino gold
- heavy glow
- large black backgrounds
- aggressive red
- exchange-like trading visual language

Dark sections may remain where functionally justified, especially data/status areas, but the default visual refresh should move toward a bright editorial surface.

---

## 7. Illustration language

Preferred illustration traits:

- hand-drawn ink outlines
- subtle line variation
- watercolor, gouache, or colored-pencil feeling
- slightly imperfect organic edges
- simplified perspective
- restrained detail
- clean white-space integration
- calm scenic depth

Avoid:

- photorealism
- glossy 3D mascot rendering
- cinematic VFX
- hyper-detailed concept art
- clip-art inconsistency
- anime character treatment
- retro pixel art as the primary site style
- crowded full-screen illustrations

---

## 8. Typography strategy

### Interface typography

Use the site's normal accessible web font stack for:

- navigation
- headings
- body text
- buttons
- cards
- data
- documentation

### Handwritten accents

Use one of these methods:

1. generated transparent handwritten image assets for short decorative phrases
2. a carefully selected licensed handwritten web font
3. manually drawn vector lettering for final high-value phrases

Generated lettering should be treated as decorative and should not be the only source of critical information.

Where a generated handwritten phrase contains meaningful text, provide equivalent accessible HTML text when practical.

---

## 9. Homepage direction

The homepage remains concise and operationally useful.

### Hero

Recommended composition:

- large clean text area on one side
- scenic mountain / valley / river illustration on the other
- optional small wooden sign cluster
- optional small PEPEPOW miner-frog mascot near a corner
- one or two handwritten accent notes only
- current CTAs remain real HTML buttons

Illustration concepts can visually suggest:

- a path into a valley
- people building together
- proof of work as real effort
- an open network
- small chain / large community

### Network Pulse

Keep the operational data UI clean and conventional.

Allowed hand-drawn treatment:

- very small page-section illustration
- subtle divider
- tiny doodle pulse/signal motif
- light paper or brush background accent

Do not render live values, charts, or statuses as handwritten graphics.

### Start Here

The existing role/action cards can gradually use a consistent hand-drawn icon family:

- Wallet
- Mining
- Masternode
- Market
- Learn

### Latest PEPEPOW / News

Keep editorial cards simple. Illustration should not compete with title/date/source.

---

## 10. Page-level visual mapping

### Mining

Visual metaphors:

- pickaxe
- trail
- rocks
- mine entrance
- workbench
- mining rig simplified as line art
- wooden wayfinding signs

Mood: work, security, fairness, participation.

### Wallets

Visual metaphors:

- wallet
- key
- lock
- backup notebook
- envelope
- safe path
- personal control

Mood: calm, safe, understandable, self-custody.

### Masternode

Visual metaphors:

- connected cabins or stations
- signal posts
- network nodes
- route map
- stable infrastructure
- flag or beacon

Mood: reliability, participation, infrastructure.

### Community

Visual metaphors:

- people
- shared table
- signposts
- paths meeting
- notes
- open landscape
- contribution symbols

Mood: welcoming, collaborative, open.

### Learn / Guides

Visual metaphors:

- open book
- map
- numbered path
- arrows
- notes
- simple diagrams

Mood: approachable, instructional, low-friction.

### Network / Tools

Visual metaphors:

- nodes
- pulses
- signal lines
- small charts
- map-like connections

Mood: factual, transparent, technical but friendly.

Keep the actual data UI conventional.

---

## 11. Asset production model

Generated imagery should be produced as reusable assets rather than full-page screenshots.

Preferred categories:

1. scenic hero backgrounds
2. page-header illustrations
3. original mascot corner accents
4. wooden signposts
5. hand-drawn icon family
6. handwritten phrase assets
7. doodle accent packs
8. watercolor / brush background shapes
9. divider art
10. small editorial spot illustrations

---

## 12. Asset inventory

### 12.1 Hero and scenic assets

| ID | Asset | Purpose | Target size | Background | Priority |
| --- | --- | --- | --- | --- | --- |
| H-01 | Homepage scenic hero | Main homepage hero | 1800×1000 or larger | opaque / white-integrated | High |
| H-02 | Homepage scenic hero alternate | Layout fallback | 1800×1000 or larger | opaque / white-integrated | High |
| H-03 | Wide valley background | Flexible crop source | 2000×1100 or larger | opaque | Medium |
| H-04 | Scenic path / village spot | Section transition | 1400×700 | opaque / white-integrated | Medium |
| H-05 | Wooden sign cluster | Reusable foreground | 1200×1200 | transparent | High |

### 12.2 Handwritten text assets

| ID | Text | Purpose | Background | Priority |
| --- | --- | --- | --- | --- |
| T-01 | Small Chain, Big Community | Hero accent option | transparent | High |
| T-02 | Mine · Build · Share · Belong | Divider / section accent | transparent | High |
| T-03 | People Power Progress | Marginal note | transparent | Medium |
| T-04 | Together We Build a Brighter Tomorrow | Marginal note | transparent | Medium |
| T-05 | Good People Build Great Things | Small note | transparent | Low |
| T-06 | A More Open, Fairer Future | CTA accent | transparent | Medium |

### 12.3 Hand-drawn icons

| ID | Icon | Usage | Priority |
| --- | --- | --- | --- |
| I-01 | Mine / pickaxe | homepage, Mining | High |
| I-02 | Build | homepage | High |
| I-03 | Share | homepage | High |
| I-04 | Belong / heart-community | homepage | High |
| I-05 | Wallet | Wallets | High |
| I-06 | Masternode | Masternode | High |
| I-07 | Community | Community | High |
| I-08 | Guides / book | Learn / Guides | High |
| I-09 | Open network | Network | Medium |
| I-10 | Security / shield | Wallet / network | Medium |

### 12.4 Doodle assets

| ID | Asset | Usage | Priority |
| --- | --- | --- | --- |
| D-01 | Arrow pack | callouts | High |
| D-02 | Underline / brush stroke pack | headings | High |
| D-03 | Heart / sun / sparkle pack | light decoration | Medium |
| D-04 | Scribble note frames | editorial callouts | Medium |
| D-05 | Divider line pack | sections | Medium |
| D-06 | Pale green brush blobs | background accents | Medium |

### 12.5 Mascot assets

| ID | Asset | Usage | Priority |
| --- | --- | --- | --- |
| C-01 | seated miner-frog corner pose | homepage | Medium |
| C-02 | standing miner-frog with pickaxe | Mining | Low |
| C-03 | miner-frog with backpack / map | Guides / Community | Low |
| C-04 | miner-frog pointing toward sign | CTA / navigation accent | Low |

Mascot assets are intentionally lower priority than scenery, icons, signs, and typographic/doodle assets.

### 12.6 Page-header illustrations

| ID | Page | Target size | Priority |
| --- | --- | --- | --- |
| P-01 | Mining | 1600×600 | High |
| P-02 | Wallets | 1600×600 | High |
| P-03 | Masternode | 1600×600 | High |
| P-04 | Community | 1600×600 | High |
| P-05 | Guides / Learn | 1600×600 | Medium |
| P-06 | Network Pulse | 1600×600 | Medium |

### 12.7 Texture assets

| ID | Asset | Usage | Priority |
| --- | --- | --- | --- |
| B-01 | subtle paper grain | optional site background | Low |
| B-02 | light watercolor wash | section background | Low |
| B-03 | pale green brush shapes | heading accents | Medium |

---

## 13. File naming and repository placement

Recommended production paths:

public/media/visual/handdrawn/heroes/
public/media/visual/handdrawn/headers/
public/media/visual/handdrawn/icons/
public/media/visual/handdrawn/doodles/
public/media/visual/handdrawn/signs/
public/media/visual/handdrawn/mascot/
public/media/visual/handdrawn/textures/

Use lowercase kebab-case filenames.

Examples:

homepage-hero-valley-v1.webp
homepage-signpost-mine-build-share-belong.webp
icon-wallet-v1.svg
doodle-arrow-curved-v1.svg
mascot-miner-frog-seated-v1.webp

Do not commit raw generation contact sheets or large temporary source files unless they are intentionally retained as production provenance material.

---

## 14. Output format guidance

For production assets:

- prefer WebP or AVIF for scenic raster illustrations
- keep PNG/WebP with alpha for transparent cutouts
- prefer SVG for manually cleaned icons, doodles, and lettering when practical
- retain high-resolution source only when useful for future crops
- generate responsive image sizes during implementation where practical
- avoid shipping multi-megabyte hero files directly to users

---

## 15. Generation workflow

Generation is intentionally batched to reduce tool instability and style drift.

Rule:

Generate no more than 10 images in one production batch.

Workflow:

1. choose the next 10 prompt IDs from docs/HAND_DRAWN_ASSET_PROMPTS.md
2. generate the batch
3. visually review all 10 together
4. reject off-style, malformed, text-corrupted, or IP-risky outputs
5. regenerate only failed items
6. crop / remove background / clean edges as required
7. convert to production format
8. place accepted assets in the correct public/media/visual/handdrawn directory
9. update an asset manifest or this document when production status changes
10. implement only after a coherent asset set is approved

Do not generate multiple unrelated visual styles in the same batch.

---

## 16. Acceptance criteria

An asset passes when:

- it matches the bright hand-drawn editorial direction
- it works with a mostly white page
- colors are restrained and consistent
- linework feels hand-drawn rather than clip-art
- composition leaves usable whitespace where required
- it does not contain malformed or unintended text
- any mascot is visibly secondary
- any mascot follows the approved character direction; close Pepe-like fallback art is explicitly flagged for provenance/licensing review
- it can be cropped or positioned responsively
- it does not require the full page to become a raster image
- it is technically suitable for optimization and web delivery

A homepage implementation passes when:

- the first screen remains clear on desktop and mobile
- CTA text stays HTML
- critical information stays accessible without the illustration
- Network Pulse remains easy to read
- illustration does not materially worsen load performance
- the page feels community-oriented without becoming meme-heavy

---

## 17. Non-goals

This visual refresh does not authorize:

- rebuilding the Astro architecture
- replacing current content with generated marketing copy
- changing Network Pulse data architecture
- adding a database or image-generation backend
- introducing a full-screen animated background
- turning the site into a character-first meme portal
- publishing close third-party character derivatives without provenance/licensing review
- changing production deployment or Apache configuration solely for visual work

---

## 18. Implementation sequence

Recommended order:

1. lock the shared illustration palette and line style
2. produce Batch 01 concept/heroes
3. produce Batch 02 icons/signs/doodles
4. implement homepage visual shell with real HTML text
5. validate responsive and performance behavior
6. produce page-header assets
7. migrate visual treatment page by page
8. add only a small number of mascot accents after the non-character system is stable
9. perform final accessibility, provenance, and performance review

The hand-drawn system should grow gradually around the existing site rather than replace working UX all at once.


---

## 19. Current rollout status

As of 2026-09-20:

- all 40 generated hand-drawn assets are present in `public/media/visual/handdrawn/`
- the homepage is the first production implementation slice
- the homepage uses a scoped bright editorial theme rather than changing every existing page at once
- semantic text, navigation, CTAs, and Network Pulse remain HTML/live UI
- the first homepage slice uses the scenic hero, signpost, lettering, and selected Start Here icons
- six page-header illustrations are now wired into Mining, Wallets, Masternode, Community, Learn, and Network
- those six pages use the same scoped bright editorial theme while their semantic content and operational controls remain HTML
- the homepage hero was corrected after production review so the title cannot overlap the scenic illustration at intermediate desktop widths
- current pages without a table of contents now collapse to a true single-column content layout instead of leaving a narrow empty grid column
- About and Market now use the bright editorial theme even before their dedicated header artwork is available
- three unattractive legacy Mining illustrations were removed while retaining the requested second introductory image
- Batch 05 prompts are queued for About and Market headers, a dedicated Market icon, About/Market editorial spots, and a current-mining setup spot
- after those assets are generated and uploaded, wire the About and Market headers, replace the temporary homepage Market icon, and review whether the remaining legacy Mining inline art should be replaced
- mascot assets remain unreferenced in production until a manual visual/provenance review
