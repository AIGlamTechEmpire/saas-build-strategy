# Template: 00 How To Load Your Brain

This template generates `00_How_To_Load_Your_Brain.md`, the foolproof setup guide that ships alongside the 6 Brain docs. Personalize it with the user's business name, their largest offer name, and one quick reference to their ICP so it feels like it was written for them specifically.

## Output filename
`00_How_To_Load_Your_Brain.md`

## Template content

Replace `[BUSINESS_NAME]`, `[FLAGSHIP_OFFER_NAME]`, and `[ICP_ONE_LINER]` with values from the drafted Brain docs. Keep everything else verbatim unless the user is technical enough to skip the explanations.

```markdown
# How To Load Your AI Brain — [BUSINESS_NAME]

> Read this first. 10 minutes from now, your Brain is live inside a Claude Project and every prompt you run from here on out has the full context of [BUSINESS_NAME] behind it.

---

## What you have

Eight files just landed in your outputs folder:

1. **`00_How_To_Load_Your_Brain.md`** — this file
2. **`01_Company_DNA.md`** — who you are, why you exist, what you stand for
3. **`02_ICP_Profile.md`** — who you serve, how they think, what they need
4. **`03_Offer_Stack.md`** — every offer you sell, with prices and promises
5. **`04_Brand_Voice.md`** — how you sound, with real voice samples
6. **`05_Proof_Library.md`** — testimonials, case studies, objection-to-proof mapping
7. **`06_Operating_Principles.md`** — how you decide, communicate, and ship work
8. **`07_Archive_Setup.md`** — how to organize raw materials in Google Drive so Claude can pull from them when needed

Files 01 through 06 are your Brain. Load all six into a Claude Project.

---

## Step-by-step setup

### Step 1: Download all six Brain files

If you're reading this in Claude.ai or a chat window, click the download link or copy each file's contents to your computer first. You need them as actual `.md` files on your machine.

### Step 2: Create a new Claude Project

1. Go to [claude.ai](https://claude.ai)
2. Click **Projects** in the left sidebar
3. Click **+ Create Project**
4. Name it: **[BUSINESS_NAME] Brain** (or whatever you want — the name is for you)
5. Add a short description: *"AI Brain for [BUSINESS_NAME]. [ICP_ONE_LINER]."*

### Step 3: Upload your Brain docs

Inside the new Project:

1. Click **Add Content** (or the equivalent upload button)
2. Upload all six files: `01_Company_DNA.md` through `06_Operating_Principles.md`
3. Confirm all six show up in the Project's knowledge

### Step 4: Add the system prompt

In the Project's instructions section (the "Custom instructions" or "Project instructions" field), paste this:

```
You are an AI employee for [BUSINESS_NAME].

You have access to six knowledge documents that describe this business:
- Company DNA (identity)
- ICP Profile (audience)
- Offer Stack (products)
- Brand Voice (tone and style)
- Proof Library (testimonials and case studies)
- Operating Principles (how this business operates)

When you respond, always:
1. Match the voice in Brand Voice. Never use em-dashes. Never use the banned words.
2. Reference offers by their exact names and prices from Offer Stack.
3. Pull testimonials verbatim from Proof Library when proof is needed.
4. Speak to the audience as described in ICP Profile, using their vocabulary.
5. Make decisions consistent with Operating Principles.

If something is marked [TO REFINE] in a document, do not invent the missing information. Ask the user.
```

### Step 5: Test it

Start a new conversation INSIDE the Project (not a generic Claude chat). Run this prompt:

```
Write a short marketing message inviting my audience to learn more about [FLAGSHIP_OFFER_NAME]. 150 words. Match my voice.
```

Read the output. Does it sound like [BUSINESS_NAME]? Does it reference real details from your offer? Does it use language your ICP would recognize?

If yes — your Brain is live.

If no — the most common gap is the Brand Voice doc. Re-read `04_Brand_Voice.md` and add 2-3 more real writing samples. Then try the test again.

---

## When to use this Project

From now on, anytime you (or your team) want AI help with anything related to [BUSINESS_NAME], **start the conversation inside this Project**. Don't use a generic Claude chat.

Examples of when to use it:

- Drafting sales emails
- Writing social posts in your voice
- Replying to customer service tickets
- Creating proposals or quotes
- Brainstorming new offers
- Coaching team members on how you'd handle a situation

Anything where the AI needs to know who you are, who you serve, or how you sound — start the chat in the Project.

---

## When to update the Brain

The Brain is a living document. Update it when:

- AI output drifts off-brand → tighten `04_Brand_Voice.md`
- AI mentions the wrong offer or wrong price → update `03_Offer_Stack.md`
- AI gets the ICP wrong → revise `02_ICP_Profile.md`
- A new testimonial or case study lands → add it to `05_Proof_Library.md`
- A new offer launches → add it to `03_Offer_Stack.md`
- A team policy or standard changes → update `06_Operating_Principles.md`

The Brain compounds. Every update makes every future AI conversation a little better.

---

## What about the Archive?

`07_Archive_Setup.md` is a separate guide for organizing your raw materials (full transcripts, complete testimonial database, old marketing materials, historical content) in Google Drive. Those don't go into the Brain — they go into the Archive, and Claude pulls from them only when a specific task needs them.

Read `07_Archive_Setup.md` after you've finished loading the Brain. The Archive is optional for Week 1 but worth setting up within your first month.

---

## You're done.

Open a new conversation in your Project and start working.

Welcome to running on AI.
```
