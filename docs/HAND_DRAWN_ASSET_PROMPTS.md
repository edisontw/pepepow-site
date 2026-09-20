# PEPEPOW Hand-Drawn Asset Generation Prompts

Status: Batches 01–05 generated and uploaded / Batch 05 integrated into About, Market, Mining, and homepage navigation
Related specification: docs/HAND_DRAWN_VISUAL_REFRESH_PLAN.md
Batch rule: maximum 10 generated images per production batch

---

## 1. How to use this file

Generate assets in the listed batch order unless a later design review changes priorities.

For each batch:

1. generate no more than 10 images
2. review the full batch together
3. regenerate failed items only
4. do not move to the next batch until the previous batch has a coherent visual style
5. store only accepted production assets in the repository

The prompts below are intentionally written in English because current image-generation systems generally follow visual instructions more consistently in English.

Do not treat generated text inside concept images as final website copy. Final semantic text should normally remain HTML/CSS.

---

## 2. Shared style prefix

Use this direction for all assets unless a prompt explicitly overrides it:

Create artwork for the PEPEPOW website in a clean hand-drawn editorial illustration style with restrained handwritten accents. Use a warm white background, fresh natural greens, warm wood tones, pale sky blue, muted mountain blue-grey, and dark ink outlines. The mood is friendly, open, community-built, optimistic, practical, and trustworthy. Use slightly imperfect organic linework with watercolor, gouache, or colored-pencil-like fills. Keep compositions airy and suitable for a real modern website.

If a mascot appears, first try an original small green PEPEPOW miner-frog mascot with a yellow miner helmet. The yellow miner helmet is mandatory for the recurring character cue; optional details include a miner lamp, backpack, work jacket, gloves, boots, map, or pickaxe. Prefer original clothing, gear, pose language, proportions, and facial treatment, but do not deliberately distort the character into an unattractive design merely to make it different. Keep the mascot secondary, small in scale, and usually near a corner or edge. If the original redesign repeatedly looks awkward, a more familiar Pepe-like frog form may be used as a temporary fallback reference, still with the yellow miner helmet and still secondary; such fallback assets require manual provenance/licensing review before production use.

Avoid dark cyberpunk, casino styling, neon overload, glossy 3D mascot rendering, photorealism, aggressive meme expressions, dense fake UI, excessive text, clutter, or full-screen poster composition.

---

## 3. Batch 01 — Homepage direction and hero source art

Goal: establish the primary scenic style before producing the full asset system.

### 01 — H-01 Homepage scenic hero, left text space

Suggested ratio: 16:9
Suggested output: heroes/homepage-hero-valley-left-space-v1

Prompt:

Create a wide scenic hero illustration for the PEPEPOW website. Show a peaceful mountain valley with a river, a small welcoming village, meadows, trees, distant snowy peaks, and a walking path. Keep the left 45 percent mostly open and light for real HTML headline and CTA content. Put most scenic detail toward the right and lower-right. Include a small rustic signpost near the landscape edge with visual cues for Mine, Build, Share, and Belong, but avoid relying on generated text. Optionally place a very small original PEPEPOW miner-frog mascot with a yellow miner helmet sitting on a rock in the far lower-right corner, facing the valley. The mascot must be subtle and not the focal point.

### 02 — H-02 Homepage scenic hero, right text space

Suggested ratio: 16:9
Suggested output: heroes/homepage-hero-valley-right-space-v1

Prompt:

Create an alternate wide PEPEPOW homepage hero in the same hand-drawn editorial style. Place the scenic mountain valley, river, path, village, trees, and wooden signs mainly on the left and lower-left. Keep the right 45 percent calm, bright, and open for real website text and CTA buttons. If a mascot appears, make it a tiny original miner-frog with a yellow miner helmet near the far left foreground, secondary to the landscape.

### 03 — H-03 Wide valley background without mascot

Suggested ratio: 16:9
Suggested output: heroes/homepage-valley-background-v1

Prompt:

Create a clean hand-drawn panoramic mountain valley background for the PEPEPOW website with no mascot and no visible words. Include a river, a small town, footpaths, trees, rocks, meadows, and distant mountains. Use soft watercolor/gouache color and dark ink linework. Keep large areas of pale sky and white integration so the image can blend into a white webpage and be cropped responsively.

### 04 — H-04 Scenic path toward community

Suggested ratio: 16:9
Suggested output: heroes/community-path-landscape-v1

Prompt:

Create a hand-drawn scenic website illustration showing a winding path leading from a quiet foreground into a small open community in a green valley. Include subtle visual metaphors of participation and building together: a bridge, shared workshop, small signposts, and people-sized activity in the distance. Do not make it busy. No mascot. No words. Keep a clean white-integrated editorial feel.

### 05 — H-05 Wooden sign cluster

Suggested ratio: 1:1
Transparent background preferred
Suggested output: signs/signpost-mine-build-share-belong-v1

Prompt:

Create a standalone hand-drawn rustic wooden signpost cluster for the PEPEPOW website. Four separate arrow boards should visually represent the concepts Mine, Build, Share, and Belong. Keep the lettering area simple and easy to replace or overlay in HTML/CSS if necessary. Use warm wood, ink outlines, slightly weathered but friendly surfaces, and small green accents. Isolated object, transparent background, no scenery.

### 06 — Concept A: landscape-led homepage mood board

Suggested ratio: 16:9
Concept only, not production UI
Suggested output: concepts/homepage-direction-landscape-led-v1

Prompt:

Create a PEPEPOW homepage visual-direction concept showing how a bright hand-drawn landscape could coexist with a clean modern website. Use a large white text area, scenic valley art, subtle wooden signs, small doodle accents, and restrained green buttons. Use minimal fake interface copy. The landscape should carry more visual weight than any character. If a mascot appears, keep it tiny in a corner with a yellow miner helmet.

### 07 — Concept B: sketchbook editorial homepage

Suggested ratio: 16:9
Concept only
Suggested output: concepts/homepage-direction-sketchbook-v1

Prompt:

Create a PEPEPOW homepage concept in a refined sketchbook editorial style. Use white space, thin ink lines, pale watercolor washes, hand-drawn section separators, small icon sketches, and a scenic mountain vignette. Keep the layout professional and modern rather than childish. No large mascot. Use only tiny handwritten marginal notes.

### 08 — Concept C: trail-map community homepage

Suggested ratio: 16:9
Concept only
Suggested output: concepts/homepage-direction-trail-map-v1

Prompt:

Create a PEPEPOW homepage visual concept inspired by an illustrated hiking map and community trail. Use a clean white layout, hand-drawn paths connecting small visual landmarks for Wallet, Mining, Masternode, Learn, and Community. Include mountain and valley scenery as a soft backdrop. Keep the UI readable and modern. No mascot required.

### 09 — Concept D: village-building homepage

Suggested ratio: 16:9
Concept only
Suggested output: concepts/homepage-direction-village-building-v1

Prompt:

Create a bright PEPEPOW homepage concept where a small illustrated valley village symbolizes an open-source community building together. Use workshops, bridge paths, signposts, greenery, and small human-scale activity. Keep large whitespace for real website content. Use a friendly editorial illustration style, not a fantasy game and not a cartoon poster. No mascot required.

### 10 — Concept E: proof-of-work landscape

Suggested ratio: 16:9
Concept only
Suggested output: concepts/homepage-direction-pow-landscape-v1

Prompt:

Create a PEPEPOW homepage concept that visually communicates Proof of Work through honest physical work metaphors: a trail, tools, a small bridge under construction, stone markers, and a mountain path. Keep the mood calm, constructive, and community-oriented. Use hand-drawn ink and watercolor on a white modern layout. If included, the original yellow-helmet miner-frog mascot should be tiny and peripheral.

---

## 4. Batch 02 — Core icons, doodles, and signs

Goal: establish a reusable non-character asset system.

### 11 — I-01 Mine icon

Suggested ratio: 1:1
Transparent background
Suggested output: icons/icon-mine-pickaxe-v1

Prompt:

Create a standalone hand-drawn website icon for Mine. Show a simple pickaxe and two or three small rocks. Use dark ink outlines, restrained green and warm-earth fills, slightly imperfect organic lines, and a clear silhouette at small size. Transparent background. No text.

### 12 — I-02 Build icon

Suggested ratio: 1:1
Transparent background
Suggested output: icons/icon-build-v1

Prompt:

Create a standalone hand-drawn website icon for Build. Use a simple constructive metaphor such as two hands assembling a small structure, blocks, or a small workbench. Keep it friendly, minimal, and readable at small size. Dark ink outlines with restrained green and warm accents. Transparent background. No text.

### 13 — I-03 Share icon

Suggested ratio: 1:1
Transparent background
Suggested output: icons/icon-share-v1

Prompt:

Create a standalone hand-drawn website icon for Share. Use a simple open-hand, branching path, or seed-sharing metaphor. Keep it minimal, warm, community-oriented, and easy to read at small size. Transparent background. No text.

### 14 — I-04 Belong icon

Suggested ratio: 1:1
Transparent background
Suggested output: icons/icon-belong-v1

Prompt:

Create a standalone hand-drawn website icon for Belong. Show a small heart integrated with a simple group or welcoming-circle motif. Keep the linework organic and the palette restrained. Transparent background. No text.

### 15 — I-05 Wallet icon

Suggested ratio: 1:1
Transparent background
Suggested output: icons/icon-wallet-v1

Prompt:

Create a standalone hand-drawn website icon for Wallet. Show a simple closed wallet with a small key or coin accent that implies personal control and self-custody. Avoid exchange/trading imagery. Use dark ink outlines and soft green/warm fills. Transparent background. No text.

### 16 — I-06 Masternode icon

Suggested ratio: 1:1
Transparent background
Suggested output: icons/icon-masternode-v1

Prompt:

Create a standalone hand-drawn website icon for Masternode. Show a small stable node station, beacon, or compact server connected to two or three network points. Friendly and understandable rather than highly technical. Transparent background. No text.

### 17 — I-07 Community icon

Suggested ratio: 1:1
Transparent background
Suggested output: icons/icon-community-v1

Prompt:

Create a standalone hand-drawn website icon for Community. Show three to five simplified people in a welcoming circular arrangement. Use a soft green accent and warm human-centered style. Transparent background. No text.

### 18 — I-08 Guides icon

Suggested ratio: 1:1
Transparent background
Suggested output: icons/icon-guides-book-v1

Prompt:

Create a standalone hand-drawn website icon for Guides. Show an open book with a small path arrow or bookmark. Keep the design minimal, friendly, and clear at small size. Transparent background. No text.

### 19 — D-01 Arrow and underline doodle sheet

Suggested ratio: 4:3
Transparent background
Suggested output: doodles/doodle-arrows-underlines-v1

Prompt:

Create a clean asset sheet of hand-drawn website doodles on a transparent background. Include curved arrows, straight arrows, loose underlines, circle highlights, one or two green brush strokes, and small directional marks. Use dark ink with limited PEPEPOW green accents. Keep each item separated with generous spacing. No words.

### 20 — D-02 Heart, sun, sparkle, pulse doodle sheet

Suggested ratio: 4:3
Transparent background
Suggested output: doodles/doodle-small-accents-v1

Prompt:

Create a transparent asset sheet containing small hand-drawn decorative accents for the PEPEPOW website: simple hearts, sunburst rays, tiny sparkles, a network pulse line, a leaf, and a small star. Use dark ink with restrained green and warm-yellow accents. Keep each doodle separate and simple. No words.

---

## 5. Batch 03 — Page headers and editorial spot illustrations

Goal: extend the style to core functional pages without compromising technical clarity.

### 21 — P-01 Mining header

Suggested ratio: 8:3
Suggested output: headers/header-mining-v1

Prompt:

Create a wide PEPEPOW Mining page header illustration. Show a mountain trail, a modest mine/workshop entrance, a pickaxe, rocks, and subtle network/security motifs. Keep the center or one side open for real HTML page title and intro. Use bright hand-drawn editorial styling, not dark mining-cave drama. No mascot required. No words.

### 22 — P-02 Wallets header

Suggested ratio: 8:3
Suggested output: headers/header-wallets-v1

Prompt:

Create a wide PEPEPOW Wallets page header illustration in a clean hand-drawn style. Use visual metaphors of self-custody and safety: a wallet, key, backup notebook, lock, and a calm path leading home. Keep large clean whitespace for HTML text. Avoid trading charts, exchange screens, and fake app UI. No mascot. No words.

### 23 — P-03 Masternode header

Suggested ratio: 8:3
Suggested output: headers/header-masternode-v1

Prompt:

Create a wide PEPEPOW Masternode page header illustration. Show a stable small network station or beacon connected to several simple nodes across a landscape, suggesting infrastructure and participation. Use a bright white-integrated hand-drawn editorial style with clean open space for HTML text. No words.

### 24 — P-04 Community header

Suggested ratio: 8:3
Suggested output: headers/header-community-v1

Prompt:

Create a wide PEPEPOW Community page header illustration. Show several paths meeting at an open village square or shared workshop in a green valley, with subtle people-scale activity, contribution, and collaboration. Keep the scene welcoming and uncluttered with whitespace for HTML content. No mascot. No words.

### 25 — P-05 Guides / Learn header

Suggested ratio: 8:3
Suggested output: headers/header-guides-v1

Prompt:

Create a wide PEPEPOW Guides and Learn page header illustration. Show an open book, a hand-drawn map, simple route signs, arrows, and a path into a clear landscape. The mood should be beginner-friendly, practical, and calm. Leave generous whitespace for HTML title and description. No words.

### 26 — P-06 Network Pulse header

Suggested ratio: 8:3
Suggested output: headers/header-network-pulse-v1

Prompt:

Create a wide PEPEPOW Network Pulse page header illustration. Combine a calm landscape with subtle connected nodes, signal lines, pulse marks, and a small observation-beacon metaphor. Keep the visual language hand-drawn and human-friendly. Do not draw fake data dashboards or numbers. Leave clean whitespace for real data UI and HTML text. No words.

### 27 — Editorial spot: self-custody

Suggested ratio: 4:3
Suggested output: spots/spot-self-custody-v1

Prompt:

Create a small editorial spot illustration for a PEPEPOW self-custody guide. Show a wallet, key, backup notebook, and simple protective shelter metaphor. Hand-drawn ink and watercolor, bright background, no text, no mascot.

### 28 — Editorial spot: proof of work

Suggested ratio: 4:3
Suggested output: spots/spot-proof-of-work-v1

Prompt:

Create a small editorial spot illustration explaining Proof of Work through a simple visual metaphor of effort: a worker's pickaxe, stones, a completed path segment, and a secure chain or network marker. Keep it conceptual, friendly, and non-technical. Hand-drawn style, no text, no mascot.

### 29 — Editorial spot: blocks and confirmations

Suggested ratio: 4:3
Suggested output: spots/spot-blocks-confirmations-v1

Prompt:

Create a small hand-drawn educational illustration for blocks and confirmations. Show a sequence of simple stone or wooden markers linked along a path, with later markers making the earlier path feel more established. Avoid literal blockchain logos. Clean white background, no text.

### 30 — Editorial spot: open-source verification

Suggested ratio: 4:3
Suggested output: spots/spot-open-source-verification-v1

Prompt:

Create a small hand-drawn educational illustration for open-source verification. Show an open book or blueprint, magnifying glass, check marks, and a community workbench. The mood is transparent, practical, and collaborative. White background, no words, no mascot.

---

## 6. Batch 04 — Mascot accents, lettering, textures, and secondary assets

Goal: add character only after the landscape/icon system is stable.

### 31 — C-01 Seated PEPEPOW miner-frog corner accent

Suggested ratio: 1:1
Transparent background
Suggested output: mascot/mascot-miner-frog-seated-v1

Prompt:

Create a small standalone original PEPEPOW miner-frog mascot as a website corner accent. The character is a green frog wearing a yellow miner helmet, simple work jacket, boots, and a compact backpack. Pose: seated calmly on a small rock, looking away toward an unseen landscape. Give the character original facial proportions and a simple friendly expression distinct from recognizable Pepe meme artwork. Avoid close-up meme styling. Keep the silhouette compact and secondary. Transparent background.

### 32 — C-02 Standing miner-frog with pickaxe

Suggested ratio: 1:1
Transparent background
Suggested output: mascot/mascot-miner-frog-pickaxe-v1

Prompt:

Create a small original PEPEPOW miner-frog website accent. Green frog, yellow miner helmet, work jacket, boots, gloves, lightly holding a pickaxe. Use original facial proportions and clothing design that do not reproduce recognizable Pepe meme artwork. Relaxed standing pose, not heroic, not dominant. Transparent background.

### 33 — C-03 Backpack / map miner-frog

Suggested ratio: 1:1
Transparent background
Suggested output: mascot/mascot-miner-frog-map-v1

Prompt:

Create a small original PEPEPOW miner-frog website accent. Green frog with a yellow miner helmet, backpack, boots, and a folded map. Pose: checking a route or looking toward a sign. Keep expression simple and original, not a Pepe meme expression. Hand-drawn editorial style, compact silhouette, transparent background.

### 34 — C-04 Sign-pointing miner-frog

Suggested ratio: 1:1
Transparent background
Suggested output: mascot/mascot-miner-frog-sign-v1

Prompt:

Create a small original PEPEPOW miner-frog website accent standing beside a blank wooden direction sign. Green frog, yellow miner helmet, work clothes, simple friendly pose. Make the character visually distinct from recognizable Pepe meme artwork. The sign should have no text so HTML/CSS or later editing can supply labels. Transparent background.

### 35 — T-01 Main handwritten phrase

Suggested ratio: 3:1
Transparent background
Suggested output: lettering/lettering-small-chain-big-community-v1

Prompt:

Create a transparent-background hand-lettered phrase reading “Small Chain, Big Community”. Use bold organic marker lettering, dark ink, slightly imperfect human strokes, with one restrained green underline and a tiny warm-yellow sunburst accent. Friendly but not childish. No additional words.

### 36 — T-02 Mine Build Share Belong lettering

Suggested ratio: 4:1
Transparent background
Suggested output: lettering/lettering-mine-build-share-belong-v1

Prompt:

Create a transparent-background hand-lettered phrase reading “Mine · Build · Share · Belong”. Use clean compact handwritten lettering in dark ink with tiny green separators or underline accents. Keep it suitable as a website section divider. No additional words.

### 37 — T-03 People Power Progress note

Suggested ratio: 2:1
Transparent background
Suggested output: lettering/note-people-power-progress-v1

Prompt:

Create a transparent-background handwritten marginal note reading “People Power Progress”. Use casual notebook-like dark ink handwriting with a tiny heart or underline. Keep it light, natural, and readable. No other text.

### 38 — T-04 Brighter tomorrow note

Suggested ratio: 3:2
Transparent background
Suggested output: lettering/note-brighter-tomorrow-v1

Prompt:

Create a transparent-background handwritten marginal note reading “Together We Build a Brighter Tomorrow”. Use relaxed handwritten dark ink, one subtle green brush underline, and one tiny heart. Keep it readable and not overly decorative. No additional text.

### 39 — B-02 Light watercolor wash sheet

Suggested ratio: 4:3
Transparent background
Suggested output: textures/watercolor-washes-v1

Prompt:

Create a transparent asset sheet of very light watercolor wash shapes for website backgrounds. Include pale green, pale sky blue, warm beige, and soft grey-blue organic washes. Keep each shape separated, low contrast, and suitable behind HTML content. No text.

### 40 — B-03 Pale green brush-shape sheet

Suggested ratio: 4:3
Transparent background
Suggested output: textures/green-brush-shapes-v1

Prompt:

Create a transparent asset sheet of pale green hand-painted brush shapes for subtle website highlights behind headings and callouts. Use several widths and organic edges, low opacity feeling, no text, no icons.

---

## 7. Batch 05 — Production-review gaps

Goal: fill the specific visual gaps found after the first production rollout. Generate this batch only after reviewing the live homepage and core pages. These assets should match the accepted bright hand-drawn system rather than introducing a new style.

### 41 — P-07 About page header

Suggested ratio: 8:3  
Suggested output: headers/header-about-v1

Prompt:

Create a wide PEPEPOW About page header illustration in the established bright hand-drawn editorial style. Show a calm mountain-and-valley landscape with a winding path, bridge, small workshop or village, and subtle signs of long-term building and resilience. The scene should suggest PEPEPOW's journey, community participation, open-source development, adaptation, and persistence without becoming a historical infographic. Use warm white, natural greens, pale sky blue, muted mountain blue-grey, warm wood, and dark ink linework. Keep the composition airy and suitable for cropping inside an 8:3 website header. No words, no fake UI, no dominant mascot. If a miner-frog appears at all, keep it tiny, secondary, and wearing the yellow miner helmet.

### 42 — P-08 Market page header

Suggested ratio: 8:3  
Suggested output: headers/header-market-v1

Prompt:

Create a wide PEPEPOW Market page header illustration in the established bright hand-drawn editorial style. Depict practical market navigation rather than speculative trading: a calm junction or small market-reference scene with a wallet, route markers, a wooden signpost, simple coin or exchange-access cues, and a clear path between verified destinations. Communicate caution, verification, and third-party access. Use restrained green, warm wood, cream, pale blue, and dark ink. Keep the composition clean and suitable for the right side of a website header. Do not draw candlestick charts, exchange dashboards, casino imagery, neon, hype graphics, price arrows, or readable words. No dominant mascot.

### 43 — I-11 Market reference icon

Suggested ratio: 1:1  
Transparent background  
Suggested output: icons/icon-market-v1

Prompt:

Create a standalone hand-drawn website icon for Market in the established PEPEPOW icon family. Use a simple wallet or coin paired with a small route marker, signpost, or two-way exchange path to suggest verified market access. Keep the silhouette minimal and readable at small size. Dark ink outlines, restrained PEPEPOW green, warm neutral accents, transparent background. Avoid candlestick charts, speculative price arrows, casino styling, exchange logos, and text.

### 44 — S-05 About journey editorial spot

Suggested ratio: 4:3  
Suggested output: spots/spot-about-journey-v1

Prompt:

Create a small PEPEPOW editorial spot illustration representing journey, resilience, and gradual community growth. Show a winding path crossing a simple bridge toward a modest village or shared workshop, with a few milestone stones or construction cues. Use the established bright hand-drawn ink-and-watercolor style, white-integrated background, restrained detail, no words, and no dominant character.

### 45 — S-06 Verified market venues editorial spot

Suggested ratio: 4:3  
Suggested output: spots/spot-market-verified-venues-v1

Prompt:

Create a small PEPEPOW editorial spot illustration for verified market access and third-party risk. Use a wallet, a simple map or route, two or three destination markers, and a small verification/check motif. The mood should be cautious, practical, and trustworthy rather than promotional. Bright hand-drawn editorial style, white-integrated background, no charts, no exchange logos, no words, no mascot.

### 46 — S-07 Current mining setup editorial spot

Suggested ratio: 4:3  
Suggested output: spots/spot-mining-setup-v1

Prompt:

Create a small PEPEPOW editorial spot illustration for the current HooHash V110 mining guide. Show a compact CPU/GPU workstation, a pickaxe as a secondary metaphor, a wallet destination, and a simple connection path toward a mining pool node. Keep it instructional and calm rather than dramatic. Use the established bright hand-drawn editorial style with dark ink and restrained green/earth fills. No fake terminal text, no logos, no words, no mascot.

---

## 8. Regeneration rules

Regenerate an item if any of the following occurs:

- malformed or unreadable generated text
- unexpected extra words
- style shifts to 3D, photorealistic, anime, cyberpunk, or meme-heavy
- character becomes the focal point when it should be secondary
- character unintentionally drifts into a recognizable Pepe-like form when the prompt specifically requests the original-design path; a familiar-form fallback is allowed only when deliberately selected after review
- composition has no usable whitespace
- transparent asset includes unwanted scenery
- icons are inconsistent in stroke weight or palette
- page headers look like fake dashboards
- image contains irrelevant crypto logos, coins, exchange tickers, or speculative trading cues

For text-bearing assets, exact spelling matters. If text generation remains unreliable, replace generated lettering with a licensed handwritten font or manually traced vector lettering rather than repeatedly regenerating the entire scene.

---

## 9. Production note

Do not commit generated assets merely because they were produced. Only accepted, reviewed, optimized assets belong under public/media/visual/handdrawn/.

Concept images may remain outside production paths unless they have ongoing design-reference value.
