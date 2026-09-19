# Public migration manifests

These files contain sanitized, reproducible migration metadata derived from the canonical 2026-09-18 WordPress WXR export.

They intentionally exclude WordPress author emails/login names and raw post bodies.

- `legacy-routes.json`: published legacy page/post paths and their planned same-path targets.
- `media-manifest.json`: attachment URLs/paths plus referenced PDFs used for media recovery and availability checks.

The manifests are migration inputs only. Recovered content remains review-only until explicitly promoted.