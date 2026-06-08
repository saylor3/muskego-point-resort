# Muskego Point Resort — Build Status

Last updated: 2026-06-07 (Session 4)

---

## What's Complete

### Shared files
- `css/style.css` — complete. Includes all shared layout, nav, cabin page styles, and lightbox.
- `js/main.js` — complete. Nav, scroll-reveal, gallery thumbnail switcher, drag-to-scroll, lightbox, active nav link detection.

### Top-level pages
- `index.html` — complete. Horizontal scrolling photo gallery now shows all 10 outdoor photos (5 originals + 5 from `Outdoor and Lake/fwdoutsidepics (1)/`, copied to `images/outdoor/`).
- `cabins.html` — complete. Small/Medium/Large group heading labels removed; cabins flow without section headers.
- `fishing.html` — complete. Lake blue dominant accent, hero, stats bar, species cards, 4-photo gallery (2×2), tackle shop callout, CTA. Gallery references `Fishing/` folder directly.
- `map.html` — complete. ResortMap.gif displayed with 11 amber CSS hotspot dots (percentage-positioned by viewing the actual map image), Fish Cleaning and Office/Store labeled but not linked, cabin index list below as fallback.
- `about.html` — complete. Top header shows resort name + phone/email/address (no hero). Single history paragraph (Goodwill's only — no Ludlow family, no gray mare sentence, no timeline). 3 confirmed historical photos.
- `contact.html` — complete. Large amber phone button at top, 3 info cards (phone/email/address), season/policy block, Google Maps embed. No inquiry form.

### All 11 cabin pages — complete
- `cabins/aspen.html`
- `cabins/balsam.html`
- `cabins/birches.html`
- `cabins/cedars.html`
- `cabins/conifer.html`
- `cabins/evergreens.html`
- `cabins/juniper.html`
- `cabins/pines.html`
- `cabins/ponderosa.html`
- `cabins/tamarack.html`
- `cabins/windswept.html`

All cabin pages have a lightbox on the photo gallery (built in shared JS/CSS — no per-page duplication).

---

## What Was Fixed This Session

### fishing.html
- Two photos (`IMG_1098.HEIC.jpeg`, `IMG_7509.heic.jpeg`) were HEIC format incorrectly named as .jpeg — confirmed broken in browser, removed. Gallery uses only the 4 confirmed JPEGs: `IMG_7927`, `IMG_7928`, `IMG_7933`, `IMG_8738`.
- All fishing photo references updated to point directly at `Fishing/` folder (not `images/fishing/`).
- Hero overlay darkened significantly (`rgba(10,28,38, 0.42–0.96)`) for legible white text.
- Gallery grid changed from 3-col (6 photos) → 2×2 (4 confirmed photos).

### index.html
- Fishing callout photo updated to `Fishing/IMG_7927.jpeg`.
- Gallery strip replaced: fixed 5-photo grid → horizontal scroll showing all 10 outdoor photos. Drag-to-scroll added.

### about.html
- Hero replaced with a clean contact info block: resort name, phone (tel: link), email, address.
- History trimmed to one paragraph covering only: Goodwill's origin, Isaac Goodwill, wealthy guests by steamboat, Sunday dinner for 100. Gray mare sentence removed. All Ludlow family content, timeline, and sidebar removed.
- Historical photos reduced from 8 → 3 (corrected broken filename `.233612` → `.233562`).

### cabins.html
- Removed "Small", "Medium", "Large" group heading labels. Cabins flow in grouped order without size category text.

### All cabin pages
- Lightbox added to photo galleries via shared `css/style.css` and `js/main.js`. Click hero or any thumbnail to open full-size overlay. Left/right arrows, Escape key, and backdrop click all close/navigate.

---

## Fishing Photo Status

**Valid JPEGs in `Fishing/`:**
- `IMG_7927.jpeg` ✓
- `IMG_7928.jpeg` ✓
- `IMG_7933.jpeg` ✓
- `IMG_8738.jpeg` ✓

**Broken (HEIC disguised as JPEG — do not use):**
- `IMG_1098.HEIC.jpeg` ✗
- `IMG_7509.heic.jpeg` ✗

---

## Historical Photo Status

**Valid files in `Historical/` (all confirmed JPEG):**
- `800749477.690463.jpg` ✓ — used on about.html
- `800749534.529601.jpg` ✓ — used on about.html
- `800749555.861829.jpg` ✓ — used on about.html
- `800749622.233562.jpg` ✓ — available (not currently shown — note: earlier sessions had a typo `.233612`, correct name is `.233562`)
- `800749654.576066.jpg` ✓ — available
- `800758523.465317.jpg` ✓ — available
- `800758610.962293.jpg` ✓ — available
- `IMG_3825.jpeg` ✓ — available

---

## Confirmed Cabin Specs

| Cabin | Sleeps | Bedrooms / Beds | Bath | Dock | Rate/wk |
|-------|:------:|-----------------|:----:|------|--------:|
| Aspen | 5 | 2 BR (1 queen, 1 double, 1 sofa-sleeper in LR) | 1 | Covered dock | $1,600 |
| Balsam | 10 | 5 BR (10 single, can be kinged) | 2 | Covered dock | $2,400 |
| Birches | 4 | 2 BR (1 double, 2 single) | 1 | Shares dock w/ Pines | $1,250 |
| Cedars | 8 | 4 BR (2 double, 4 single) | 1 | Uses main dock | $1,250 |
| Conifer | 6 | 3 BR (1 double, 2 single, 1 single bunk) | 1 | Shares dock w/ Windswept | $1,500 |
| Evergreens | 6 | 3 BR (1 queen, 4 twins — no bunk) | 1 | Dock | $1,650 |
| Juniper | 8 | 3 BR (1 queen, 1 double, 2 single, 1 single bunk) | 1 | Covered dock | $1,800 |
| Pines | 4 | 2 BR (1 double, 2 single) | 1 | Shares dock w/ Birches | $1,250 |
| Ponderosa | 10 | 5 BR (twins in each room — no bunk bed) | 2 | Covered dock | $2,400 |
| Tamarack | 6 | 3 BR (6 single, can be kinged) | 2 | Dock | $1,850 |
| Windswept | 6 | 2 BR (1 queen, 2 single, 2 daybeds in LR) | 1 | Shares dock w/ Conifer | $1,600 |

---

## Image Structure

- `images/cabins/[cabin-name]/` — numbered photos (1.jpeg, 2.jpeg, etc.) used on individual cabin pages
- `images/cabins/[cabin-name].jpeg` — cover thumbnail used in grids on index.html and cabins.html
- `images/outdoor/` — lake-1.jpeg through lake-5.jpeg + outdoor-6 through outdoor-10.jpeg (copied from `Outdoor and Lake/fwdoutsidepics (1)/`)
- `images/fishing/` — old copies (fish-1.jpg–fish-4.jpg); superseded by direct `Fishing/` references
- `Fishing/` — source fishing photos; use only the 4 confirmed JPEGs listed above
- `Historical/` — 8 historical photos; 3 currently shown on about.html
- `ResortMap.gif` — resort map used on map.html

---

## Known Remaining Items

- **Map hotspot positions** — currently set by approximate percentage coordinates from visual inspection of ResortMap.gif. Should be verified against the live page and fine-tuned if any dots are off-target.
- **More cabin history** — CLAUDE.md notes that Mark, Martha, and Judy will provide cabin-specific history. When received, add to about.html.
- **Email address** — currently `muskegopoint@gmail.com` everywhere. Will become `info@muskegopoint.com` — update sitewide when confirmed.
- **Domain** — target is `muskegopoint.com`; currently on localhost. Push to GitHub → Vercel when client approves.
- **Owner names** — CLAUDE.md says do not publish until confirmed. Not shown anywhere currently.
- **No Windswept cabin photo subfolder found** in `images/cabins/` — windswept.html uses a 3-photo gallery from `images/cabins/windswept/`. Verify those photos exist.

---

## Local Dev

- Server: `node serve.mjs` → http://localhost:3000
- Screenshot: `node screenshot.mjs http://localhost:3000/[page]`
- Screenshots save to `./temporary screenshots/screenshot-N.png`
- Do NOT start a second server if one is already running
