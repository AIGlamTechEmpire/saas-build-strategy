# Template: 07 Archive Setup

This template generates `07_Archive_Setup.md`, the guide for organizing the user's raw materials in Google Drive (or any cloud storage) so Claude can pull from them on demand for specific tasks.

## Output filename
`07_Archive_Setup.md`

## Drafting notes for Claude

Before generating this file, look back at what you scraped and what the user uploaded. The Archive folder structure should reflect WHAT THE USER ACTUALLY HAS, not a generic template. If they uploaded sales call transcripts, the Archive has a sales-call-transcripts folder. If they didn't, don't include that folder.

Personalize the file with:
- `[BUSINESS_NAME]` from Company DNA
- Specific material categories the user actually has (pull from Phase 2 scraping)
- Mention any specific files they uploaded by name

## Template content

```markdown
# Archive Setup — [BUSINESS_NAME]

> The Brain (docs 01-06) holds your distilled, always-on context. The Archive holds your raw materials — full transcripts, complete testimonial database, historical content, big data dumps. Claude pulls from the Archive on demand when a specific task needs deeper context. This file shows you how to organize the Archive.

---

## Why the Archive matters

Your Brain is curated. Every page in it is high-signal. If you dumped everything you've ever written into the Brain, it would dilute the signal and AI output quality would drop.

So we split the knowledge into two layers:

- **The Brain (Claude Project)** — distilled, always-loaded, the 6 core docs
- **The Archive (Google Drive)** — raw, on-demand, the full materials

When you ask Claude to write a sales email, it uses the Brain. When you ask Claude to "find the testimonial from the customer who said the thing about pricing," Claude pulls from the Archive.

---

## The recommended folder structure

Create a top-level folder in Google Drive (or Dropbox, Box, OneDrive — anywhere Claude can access via MCP):

```
[BUSINESS_NAME] Archive/
├── 01_Sales_Calls/
│   └── (full sales call transcripts, organized by date)
├── 02_Customer_Voice/
│   ├── Survey responses
│   ├── Testimonials (complete database, not just top 10)
│   ├── Customer interview transcripts
│   └── Reviews and ratings exports
├── 03_Marketing_Materials/
│   ├── Past sales pages
│   ├── Email campaigns sent
│   ├── Social media archives
│   └── Ad creative library
├── 04_Content/
│   ├── Blog posts (full archive)
│   ├── Podcast appearances (transcripts)
│   ├── YouTube videos (transcripts)
│   └── Books and lead magnets
├── 05_Internal_Knowledge/
│   ├── SOPs and process docs
│   ├── Team training materials
│   ├── Meeting notes (selected high-value)
│   └── Decision logs
└── 06_Historical/
    ├── Deprecated offers (for context, not active reference)
    ├── Old branding materials
    └── Founder archive (early writing, original pitch decks)
```

**Customize this structure to match what you actually have.** If you don't have sales call transcripts, skip folder 01. If you have something the structure doesn't cover (e.g., regulatory filings, IP documentation), add a folder for it.

---

## What we extracted vs. what should live in the Archive

Based on the materials I scraped and you uploaded, here's the rough split:

### Made it into the Brain (the distilled 5-10%):
- Top 10 testimonials → `05_Proof_Library.md`
- 5 voice samples → `04_Brand_Voice.md`
- Founding story summary → `01_Company_DNA.md`
- ICP description and vocabulary → `02_ICP_Profile.md`
- Active offers with prices → `03_Offer_Stack.md`
- Operating principles → `06_Operating_Principles.md`

### Belongs in the Archive (the raw 90-95%):
[CLAUDE: PERSONALIZE THIS LIST BASED ON WHAT YOU ACTUALLY SCRAPED AND WHAT THEY ACTUALLY UPLOADED. If they uploaded a 30-page sales transcript, mention it here by name. If you scraped 20 blog posts and only used 3 as voice samples, the other 17 belong in the Archive.]

- [Specific items the user has that didn't make it into the Brain]

---

## How to populate the Archive

### Option A: Bulk upload (fastest)

Drag your existing files into the folders above. Don't reorganize unless you want to. The folder structure is what matters; file naming inside can be loose.

### Option B: Build it over time

If you don't have everything centralized yet, start by uploading what you have now. Add more as new materials are created. Every sales call transcript, every customer survey response, every podcast appearance can go straight into the Archive going forward.

### Option C: Mirror what's already organized

If your existing Google Drive already has materials in different folders, you don't need to move them. Just create symlinks or shortcuts inside `[BUSINESS_NAME] Archive` that point to the existing locations.

---

## Connecting the Archive to Claude

Once the Archive is populated, connect it to Claude so AI can pull from it on demand.

### Method 1: Google Drive connector (recommended)

1. In Claude Projects or Claude Desktop, enable the Google Drive connector
2. Grant access to the `[BUSINESS_NAME] Archive` folder
3. Test it: ask Claude *"Find the testimonial in my Archive from a customer who mentioned [specific topic]."*

### Method 2: Direct upload when needed

If you don't want to enable a permanent connector, upload specific Archive files to a Claude conversation when needed. Slower but more controlled.

### Method 3: MCP integration

For technical users: set up an MCP server pointing to the Archive for programmatic access from any AI tool.

---

## When to use the Archive vs. the Brain

| Task | Source |
|------|--------|
| Draft a sales email | Brain |
| Write a social post in your voice | Brain |
| Reply to a typical customer service ticket | Brain |
| Find the exact quote from the customer who mentioned [specific thing] | Archive |
| Pull stats from a survey we ran 6 months ago | Archive |
| Reference a specific case study we don't have in the Brain yet | Archive |
| Look up what was said on a specific sales call | Archive |
| Compare our current offer to what we ran last year | Archive |

**Rule of thumb:** if the answer would be the same for any prompt today, it's Brain. If the answer is "go look it up in the records," it's Archive.

---

## Maintenance

- **Weekly:** Drop new sales call transcripts, new testimonials, and new content into their folders.
- **Monthly:** Review what's in the Archive that should be promoted to the Brain. (A new hero testimonial, a new voice sample, a new offer.)
- **Quarterly:** Move outdated materials to `06_Historical/` so the active Archive stays clean.

---

## What's next

Your Brain is loaded. Your Archive is structured. From here on out, every AI conversation about [BUSINESS_NAME] has both layers of context behind it. The work that used to require you in the loop now runs on systems.

When you're ready to build your first AI employee, the Brain is the foundation. The Archive is the backup library. Both work together.
```
