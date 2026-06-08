# CLAUDE.md — Muskego Point Resort Website

## Always Do First
- **Invoke the `frontend-design` skill** before writing any frontend code, every session, no exceptions.

## Project Context
- **Client:** Muskego Point Resort, Lake Vermilion, Tower, Minnesota
- **Address:** 8147 Bayview Rd, Cook, MN 55723
- **Vibe:** Warm, rustic, north-woods cabin resort. Authentic, not corporate. Lean on real photography and whitespace — not heavy effects or over-designed luxury.
- **Reference:** Ludlow's Island Resort (ludlowsresort.com) — use as quality benchmark
- **Final domain:** muskegopoint.com (currently on Weebly — being replaced)
- **No online booking** — all reservations by phone only. Primary CTA always: **218-666-5696** (`tel:+12186665696`)
- **Email (interim):** muskegopoint@gmail.com → will become info@muskegopoint.com
- **Season:** May–October. Summer weeks run Saturday–Saturday, check-in after 4pm, check-out before 9am.
- **Do NOT publish owner names** on the site until confirmed.
- **Do NOT list previous owners** Joe & Jenny Stanaway anywhere.

## Site Architecture — MULTI-PAGE (not single file)
Build each page as a separate HTML file. All pages share the same nav, footer, stylesheet, and JS.

```
index.html
cabins.html
fishing.html
map.html
about.html
contact.html
css/style.css
js/main.js
cabins/
  aspen.html
  balsam.html
  birches.html
  cedars.html
  conifer.html
  evergreens.html
  juniper.html
  pines.html
  ponderosa.html
  tamarack.html
  windswept.html
```

**Do not build a single index.html with anchor links. Build separate HTML files.**

## Navigation
Every page: Home | Cabins | Fishing | Map | About | Contact
Active page highlighted. Collapses to hamburger on mobile.

## Brand Colors
```
--color-forest:   #2F4A3C   /* forest green — primary, used site-wide */
--color-pine:     #1E3328   /* pine shadow — deep green for headers/footers */
--color-lake:     #3E6B7A   /* lake blue — fishing page primary, water accents */
--color-amber:    #c8922a   /* warm amber/gold — CTAs only */
--color-birch:    #C9B79C   /* birch/wood — warm neutral */
--color-linen:    #F4F0E8   /* off-white/linen — backgrounds */
--color-ink:      #1A1A1A   /* near-black — body text */
```
- **Forest green** is the primary color across the entire site.
- **Lake blue** is used as the dominant color on fishing.html and for water-related accents only.
- Amber for CTAs only. Never default Tailwind blue/indigo.

## Typography
- **Headings:** Warm humanist or slab serif (e.g. Playfair Display, Lora, Bitter — Google Fonts)
- **Body:** Clean readable sans (e.g. Inter, DM Sans)
- Tight tracking (`-0.02em`) on large headings
- Generous line-height (`1.7`) on body copy
- Never use the same font for headings and body

## Page Specs

### index.html — Home
- Full-bleed hero, real photo, headline, subhead, CTA → call 218-666-5696
- "Why Muskego Point" value props (4 cards: fishing, privacy, history, family)
- Cabin preview grid — all 11 cabins, photo + name + sleeps + "View Cabin" link
- Fishing callout section with link to fishing.html
- History teaser — gray mare pull quote, link to about.html
- Outdoor photo gallery strip — pull ALL photos from `Outdoor and Lake/` and `Outdoor and Lake/fwdoutsidepics (1)/` and display in a scrollable horizontal gallery
- Footer: phone, email, address, nav links

### cabins.html — Cabins Overview
- Intro with resort map thumbnail linking to map.html
- All 11 cabins grouped by size: Small (sleeps 4–5), Medium (sleeps 6–8), Large (sleeps 13–14)
- Each card: hero photo, name, sleeps, bed config, dock info, weekly rate, amenities, Call button, "View Details" link
- **Call button behavior:**
  - Mobile: `<a href="tel:+12186665696">Call for Availability</a>` — triggers phone call
  - Desktop: button displays "Call 218-666-5696" prominently — no auto-dial
- Rental policies section at bottom (rates, deposit, cancellation, pet policy, tax)

### cabins/[name].html — Individual Cabin Pages
- Full hero photo
- Name, sleeps, full bed config, bath count, dock info, weekly rate
- **Photo gallery — aim for 10 photos per cabin.** Pull all available photos from `Cabins/[cabin-name]/`. Use every photo available before falling back to placeholders.
- All amenities (every cabin has: full kitchen, wood-burning fireplace, screened porch or deck, Weber grill, lake view, quality bedding/towels/cookware, coffeemaker, microwave, toaster — no TV/radio, Wi-Fi in store only)
- Large Call for Availability button (same mobile/desktop behavior)
- Back to All Cabins link
- Related cabins at bottom

### fishing.html
- Lake Vermilion overview: 40,000 acres, 365 islands
- Species: 55" muskies, 30" walleyes, 20lb northern pike, smallmouth bass, crappie
- Tackle shop callout
- Fishing photos gallery (from `Fishing/`)
- CTA to call and book

### map.html — Interactive Resort Map
- Display resort map (`ResortMap.gif`)
- Each of the 11 cabins is a clickable hotspot → links to `cabins/[name].html`
- Non-rental structures (Fish Cleaning Station, Dock Boy, Office/Store) labeled but not linked
- Mobile: map scales, hotspots remain tappable
- Cabin index list below map as fallback

### about.html
- Resort history (full text from Kelly Berg — see History section below)
- Historical photos section (`Historical/`)
- Ownership intro — resort under new ownership; do not name owners yet
- CTA at bottom

### contact.html
- Phone **218-666-5696** displayed large at top; `tel:` link on mobile
- Simple inquiry form: Name, Email, Phone, Preferred dates, Message
- Note: inquiries only — bookings confirmed by phone
- Address: 8147 Bayview Rd, Cook, MN 55723
- Google Map embed of Lake Vermilion / Tower, MN area

## Call Button Implementation
```html
<a href="tel:+12186665696" class="call-btn">
  <span class="mobile-label">Call for Availability</span>
  <span class="desktop-label">Call 218-666-5696</span>
</a>
```
```css
@media (min-width: 768px) {
  .mobile-label { display: none; }
  .desktop-label { display: inline; }
}
@media (max-width: 767px) {
  .desktop-label { display: none; }
}
```

## Cabin Details (all 11 — use exactly, do not invent)

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
| Ponderosa | 10 | 5 BR (twins in each room) | 2 | Covered dock | $2,400 |
| Tamarack | 6 | 3 BR (6 single, can be kinged) | 2 | Dock | $1,850 |
| Windswept | 6 | 2 BR (1 queen, 2 single, 2 daybeds in LR) | 1 | Shares dock w/ Conifer | $1,600 |

**Every cabin includes:** full kitchen, wood-burning fireplace, screened porch or deck, Weber charcoal grill, lake view, quality bedding, towels, pots/pans, utensils, coffeemaker, microwave, toaster. No TVs or radios. Wi-Fi in the store only.

## Rental Policies
- Rates based on 2 people; $100/person/week per additional guest. Children under 3 free.
- Daily rate = 1/5 of weekly rate.
- No pets. Rentals subject to tax.
- $500 deposit per cabin per week; refundable if cancelled 90+ days before start.
- 3.5% cash discount built into pricing (credit card payments don't receive the discount).
- Spring/Fall (before Memorial Day / after Labor Day): 15% lodging discount, 2-night minimum.

## Photos
All photos live in `NEW Muskego/` — reference subfolders below. **Aim for 10 photos per cabin.**

- `Cabins/[cabin-name]/` — cabin-specific photos (exterior + interior). Use every available photo.
- `Lodge/` — lodge photos
- `Fishing/` — fishing photos for fishing.html
- `Outdoor and Lake/` — hero images, gallery strips, general resort feel
- `Historical/` — about.html only
- `Logo/` — logo files

**Logo:** black pine-tree wordmark — no color version exists (owner confirmed). Use on forest green, pine, or linen backgrounds. Reversed white on dark photos only where legibility requires.

**Branded placeholders** (only where real photos are unavailable):
`https://placehold.co/WIDTHxHEIGHT/2F4A3C/F4F0E8`

## Resort History (About page)
Keep the history brief and understated — a short written callout, not a sentimental timeline. No Ludlow family connection. Just the origin story in a few sentences:

- Originally called **Goodwill's**, started by **Isaac Goodwill**
- Rumored that Isaac Goodwill traded an old gray mare for Muskego Point
- Wealthy guests arrived by steamboat from Tower, traveling by train, to spend the whole summer
- Isaac fed up to 100 people for Sunday dinner
- The resort has changed hands over the years and is now under new ownership — the same spirit of northwoods hospitality remains

**Tone:** warm and brief. One short paragraph maximum. No bullet points on the actual page. No timeline. Nothing too sentimental.

**Historical photos:** use exactly 3 photos from `Historical/` — pick the 3 that look best. If any photo fails to load, skip it and do not show a broken image.

## What NOT to Do
- Do not build a single index.html with anchor links — build separate HTML files
- Do not publish owner names until confirmed
- Do not list previous owners Joe & Jenny Stanaway
- No "Book Now" or "Reserve Online" buttons — phone call only
- No generic lakeside clip art or cheesy fishing graphics
- No overly rustic or western-style fonts
- No default Tailwind blue/indigo
- Do not invent cabin specs, rates, or amenities
- Do not use `transition-all`

## Local Server
- Always serve on localhost — never screenshot a `file:///` URL
- Start: `node serve.mjs` (project root → http://localhost:3000)
- Do not start a second instance if already running

## Screenshot Workflow
- `node screenshot.mjs http://localhost:3000`
- Screenshots → `./temporary screenshots/screenshot-N.png`
- **After building or updating any page:** take ONE screenshot, analyze it, fix any obvious issues with colors, spacing, typography, or layout, then stop. Do not loop or take additional screenshots unless explicitly asked.
- When asked for additional review: take ONE screenshot, analyze, fix, then stop.
- Review pages in this order when asked: index → cabins → one sample cabin page → fishing → map → about → contact
- Clear the temporary screenshots folder before starting each new page review.

## Anti-Generic Guardrails
- **Approach:** lean on real photography and whitespace. Fewer gradients, softer shadows, calmer motion than a luxury site.
- **Shadows:** Layered, color-tinted, low opacity — never flat `shadow-md`
- **Gradients:** Subtle. Layer radial gradients sparingly. SVG noise only where it adds warmth.
- **Animations:** Only `transform` and `opacity`. Spring-style easing. Never `transition-all`.
- **Interactive states:** Every clickable element needs hover, focus-visible, and active states.
- **Images:** Gradient overlay (`bg-gradient-to-t from-black/40`) on hero images
- **Spacing:** Consistent intentional tokens — not random Tailwind steps
- **Depth:** Base → elevated → floating layering system

## Output
- Separate HTML files per page (see Site Architecture)
- Shared `css/style.css` and `js/main.js`
- Tailwind CSS via CDN: `<script src="https://cdn.tailwindcss.com"></script>`
- Mobile-first responsive

## Deployment
- GitHub → Vercel autodeploy
- Test on localhost first — only push to GitHub when explicitly told to
- Target domain: muskegopoint.com
