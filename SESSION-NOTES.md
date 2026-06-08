# Muskego Point Resort — Build Status

Last updated: 2026-06-07 (Session 5)

---

## Deployment

- **GitHub:** https://github.com/saylor3/muskego-point-resort
- **Live site:** https://muskegopointresort.netlify.app (Netlify autodeploy from GitHub)
- **Target domain:** muskegopoint.com — not yet pointed to Netlify
- **To deploy future changes:** push to GitHub `main` branch → Netlify autodeploys

---

## What's Complete

### Shared files
- `css/style.css` — complete. All shared layout, nav, cabin page styles, lightbox.
- `js/main.js` — complete. Nav, scroll-reveal, gallery thumbnail switcher, drag-to-scroll, lightbox, active nav link detection.
- `.gitignore` — excludes `node_modules/` and `temporary screenshots/`

### Top-level pages
- `index.html` — complete. Hero overlay darkened for legibility. Gallery strip shows 5 unique outdoor photos in order: Store → Volleyball Court → Beach → Boathouse → IMG_3743. History teaser section removed entirely.
- `cabins.html` — complete. Map teaser section removed. Cabins flow without size group headers.
- `fishing.html` — complete. Lake blue dominant accent, hero, stats bar, species cards, 4-photo gallery (2×2), tackle shop callout, CTA.
- `about.html` — complete. Single history paragraph (Goodwill's origin only). 3 historical photos.
- `contact.html` — complete. Large amber phone button at top, info cards, season/policy block, Google Maps embed. "Reservations & Inquiries" eyebrow removed. "No online booking" phrasing removed from both locations.
- `map.html` — **DELETED.** Map page removed from the site entirely. All nav links and footer links to map.html removed from all 16 pages.

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

All cabin pages have a lightbox on the photo gallery. Map nav link removed from all cabin pages.

---

## Session 5 Changes

### map.html
- Deleted entirely. ResortMap.gif is still in the project root but no longer referenced.
- All nav links (desktop + mobile) and footer links removed from every page sitewide.
- Map teaser block (thumbnail + copy) removed from cabins.html.

### index.html
- Hero overlay darkened: gradient now 0.45–0.90 (was 0.18–0.82) for legible white text on hero photo.
- Gallery strip: duplicate photos removed (outdoor-6 through outdoor-10 were identical to lake-1 through lake-5). Now shows 5 unique photos ordered: Store, Volleyball Court, Beach, Boathouse, IMG_3743.
- History teaser section removed entirely (blockquote, text, and "Read Full History" button).

### contact.html
- "Reservations & Inquiries" eyebrow line removed.
- "No online booking." removed from hero subtext and info card note.

### Deployment
- Git initialized, `.gitignore` created, initial commit made.
- Pushed to GitHub: https://github.com/saylor3/muskego-point-resort
- Netlify autodeploy connected: https://muskegopointresort.netlify.app

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
- `800749622.233562.jpg` ✓ — available (not currently shown)
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
- `images/outdoor/` — lake-1.jpeg through lake-5.jpeg only (outdoor-6 through outdoor-10 are duplicates — no longer used in gallery)
- `images/fishing/` — old copies; superseded by direct `Fishing/` references
- `Fishing/` — source fishing photos; use only the 4 confirmed JPEGs listed above
- `Historical/` — 8 historical photos; 3 currently shown on about.html
- `ResortMap.gif` — still in project root but no longer used (map page deleted)

---

## Known Remaining Items

- **More cabin history** — Mark, Martha, and Judy may provide cabin-specific history. When received, add to about.html.
- **Email address** — currently `muskegopoint@gmail.com` everywhere. Will become `info@muskegopoint.com` — update sitewide when confirmed.
- **Custom domain** — point muskegopoint.com to Netlify when ready (add domain in Netlify dashboard, update DNS at registrar).
- **Owner names** — do not publish until confirmed by owners. Not shown anywhere currently.
- **Windswept cabin photos** — windswept.html references `images/cabins/windswept/` subfolder. Verify those photos exist and loaded correctly.
- **Netlify deploy token** — stored in Netlify dashboard. Future pushes to GitHub `main` autodeploy; no manual action needed.

---

## Local Dev

- Server: `node serve.mjs` → http://localhost:3000
- Screenshot: `node screenshot.mjs http://localhost:3000/[page]`
- Screenshots save to `./temporary screenshots/screenshot-N.png`
- Do NOT start a second server if one is already running
