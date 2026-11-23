---
name: "GROWL TF Step 1 checklist"
about: "Progress checklist for one dataset (Step 1: download and investigate). A mentor opens one per dataset."
title: "[TF Step 1] <dataset name>"
labels: ["task force", "step 1"]
---

**Dataset:** <dataset name>
**Folder:** `GROWL_TF_individual_data_projects/individual_project_folders/<dataset name>/`
**Team:** <@github-name-1>, <@github-name-2>
**Instructions:** `GROWL_TF_individual_data_projects/instructions_task_force/step1_download_and_investigate_data.ipynb`

Tick a box when it's done (no pull request needed for ticking). Put the GitHub name of whoever
owns an item after it, e.g. `(@joseph)`, so it's clear who does what. Questions and cool updates go
on Discord, and bring what you find to the hands-on sessions.

### 0. Names (do this first)
- [ ] Proposed the **dataset name** (lowercase `<first author>-<yyyy>-<tag>`, e.g. `vanson-2022-nopeaks`), and checked `individual_project_folders/` for an existing folder (if there is one, use that name)
- [ ] Proposed the **submodel folder names** (as close as possible to the download names) and **short labels** for plots
- [ ] Names **confirmed by a mentor** in this issue, before downloading, creating or renaming any folders

### A. Where the dataset comes from
- [ ] Paper found: **paper DOI** and arXiv recorded (the paper's DOI, not the Zenodo DOI)
- [ ] Data archive(s) found: data DOI of the version actually downloaded recorded
- [ ] Checked that the archive cites the right paper (compared titles, not only arXiv numbers)
- [ ] Simulation code and **exact version** recorded
- [ ] All submodels listed, fiducial marked ⭐, submodel names decoded

### B–C. Paths and download
- [ ] `PATH` dictionary cell runs and finds every file
- [ ] Data downloaded (checksum verified: optional)
- [ ] Download instructions written in `download_instructions.md` so someone else can follow them literally, with the real commands
- [ ] Difficulties and gotchas written down
- [ ] Paper PDF and archive README saved next to the data

### D–E. Paper and methods
- [ ] Paper goal, findings and DCO types summarised in `README.md`, in our own words
- [ ] Figures we can **compare with the data** listed (formation efficiency, number of systems, or rates in Gpc⁻³ yr⁻¹); other figures skipped
- [ ] `metadata.csv` filled in (tier 1: code version, ZAMS mass range, IMF, mass ratio distribution, metallicities), each entry with **where in the paper** it comes from
- [ ] Every entry checked by a person against the paper (LLM suggestions verified)

### F. The data file
- [ ] All groups and columns listed; noted which standard ones exist (e.g. `Run_Details`, system parameters, DCOs, RLOF, CE, weights)
- [ ] Weights checked: are systems weighted? (sum weights, never count rows)
- [ ] Sanity plot made and compared with the tutorial file
- [ ] Quantities the paper plots that are **not** in the file noted

### G. Wrap-up
- [ ] Summary card in `README.md`
- [ ] Results shown at a hands-on session
- [ ] Pull request(s) opened, reviewed and merged
