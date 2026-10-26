# Contributing to the GROWL Catalog

*Draft v0.1. Steps, file names, and tool names are proposals to iterate on.*

Each contributor owns **one catalog entry**: one population-synthesis study (one paper and its public data). You take that study through six steps, from "where is the data?" to "what does it predict for gravitational-wave sources?". Each step is its own GitHub issue, branch, and pull request.

Questions go to the GW Paleontology Discord, not to GitHub issues.

---

## Where things live

```
github.com/growl-lab/
│
├── .github/                    Org profile page (README shown on github.com/growl-lab)
│
├── growl-catalog/              THE CATALOG: one folder per study, plus the bootcamp
│   ├── README.md
│   ├── CONTRIBUTING.md         this file
│   ├── schema/
│   │   └── metadata.schema.json    rules every metadata.yaml must satisfy
│   ├── scripts/
│   │   └── validate_metadata.py    run before every pull request
│   ├── simulations/
│   │   ├── _template/          copy this to start a new entry
│   │   └── <id>/               one study, e.g. smith-2024-bns-delays
│   │       ├── metadata.yaml       machine-readable entry (data, code, physics assumptions)
│   │       ├── README.md           human summary + "Open questions"
│   │       ├── download.sh         step 1: tested download commands
│   │       ├── results.yaml        steps 4-6: key numbers (efficiencies, rates)
│   │       ├── notebooks/          one notebook per step (02-06)
│   │       └── figures/            small PNGs used in the README
│   ├── tutorials/              GW Paleontology Bootcamp notebooks
│   └── .github/
│       ├── workflows/validate.yml  automatic check on every pull request
│       ├── ISSUE_TEMPLATE/         "new catalog entry" form
│       └── PULL_REQUEST_TEMPLATE.md
│
└── growl-tools/                THE CODE: pip-installable Python package
    ├── src/growl_tools/
    │   ├── catalog.py              create a new entry, read/write metadata.yaml   [planned]
    │   ├── standard_format.py      convert code output to GROWL standard HDF5
    │   ├── formation_efficiency.py mergers per unit star-forming mass
    │   ├── cosmic_integration.py   S(Z,z) weighting, merger rate vs redshift
    │   └── properties.py           mass, mass-ratio, delay-time distributions     [planned]
    ├── tests/
    └── pyproject.toml
```

**Rule of thumb:** reusable code goes in `growl-tools`; anything specific to one study goes in that study's `simulations/<id>/` folder. If you find yourself copying a function between notebooks, it belongs in `growl-tools` (open an issue there).

**Data never goes in git.** Original data stays where its authors published it. The GROWL standard-format HDF5 file goes to Zenodo; the catalog stores the DOI and checksum.

---

## One-time setup

```bash
git clone https://github.com/growl-lab/growl-catalog.git
cd growl-catalog
python -m venv .venv && source .venv/bin/activate
pip install pyyaml jsonschema jupyter
pip install git+https://github.com/growl-lab/growl-tools.git
```

Keep downloaded data **outside** the repository, e.g. `~/growl-data/<id>/`.

---

## How the work is organized

A maintainer opens a **parent issue** for your entry with one **sub-issue per step** below. For each step:

```bash
git switch main && git pull
git switch -c <id>/<step>            # e.g. smith-2024-bns-delays/02-initial-conditions
# ... do the work inside simulations/<id>/ ...
python scripts/validate_metadata.py <id>
git add simulations/<id>
git commit -m "<id>: <what you did>"
git push -u origin <id>/<step>
```

Open a pull request, write `Closes #<sub-issue number>`, and fill in the checklist. A maintainer reviews; address comments by pushing more commits to the same branch.

Every step ends the same way: **compare with what the paper reports.** Agreement is a result; disagreement is a result too. Write disagreements and anything unclear under "Open questions" in your `README.md` and keep going.

---

## Step 0: Start your entry

1. Find your parent issue and note your catalog id: `<firstauthor>-<year>-<short-topic>`.
2. Create the folder:
   ```bash
   git switch -c <id>/00-setup
   cp -r simulations/_template simulations/<id>
   ```
3. Fill in `id`, `title`, `contributors`, and the `paper` section of `metadata.yaml`.

**Done when:** the validator passes and the PR is merged.

---

## Step 1: How to download the dataset

**Goal:** anyone can get the exact same data by following your instructions.

- Find where the data is published (Zenodo, journal supplement, author website) and which version matches the paper.
- Write the commands in `download.sh` (wget/curl, no manual clicking) and run it yourself on a clean folder.
- Record in `metadata.yaml` (`data` section): URL/DOI, version, file names, total size, file format, and a checksum (`shasum -a 256 <file>`).
- Note which parts of the paper the data covers (all metallicities? all model variations?).

**Deliverables:** `download.sh`, `data` section of `metadata.yaml`.
**Done when:** a maintainer can run `download.sh` and the checksums match.

---

## Step 2: Investigate the initial conditions

**Goal:** know exactly which binaries were simulated and how they were sampled.

- Plot the sampled distributions: primary mass, mass ratio, separation or period, eccentricity, metallicity grid.
- Identify the sampling method (e.g. Monte Carlo vs. importance sampling) and whether each system carries a **weight**.
- Work out the **total star-forming mass** each simulation represents, including stars and binaries that were not simulated. Step 4 depends on this number.
- Compare everything with the paper's stated initial conditions.

**Uses:** `growl_tools.standard_format` (reading the data).
**Deliverables:** `notebooks/02_initial_conditions.ipynb`, initial-conditions fields in `metadata.yaml`, figures.
**Done when:** each distribution matches the paper or the mismatch is explained in "Open questions".

---

## Step 3: Verify the metadata table

**Goal:** every physics assumption in `metadata.yaml` is correct and traceable to the paper.

- The entry's assumptions may be pre-filled. Check every parameter against the paper (and the code version's documentation for defaults).
- Every parameter needs `source_in_paper` (section, table, or equation). If the paper is silent and a code default applies, say so and cite the code version.
- Mark anything you could not confirm instead of guessing.
- Review the finished table with a metadata expert.

**Deliverables:** completed `metadata.yaml`.
**Done when:** the validator passes, no parameter lacks a source, and the metadata reviewer approves.

---

## Step 4: Calculate formation efficiencies

**Goal:** how many mergers each simulation produces per unit star-forming mass.

- Convert the data to the GROWL standard HDF5 format.
- Select double compact objects that merge within a Hubble time, split by type (BBH, BHNS, BNS).
- Compute the formation efficiency (mergers per M☉ of star-forming mass) at each metallicity, using the weights and total mass from step 2.
- Plot efficiency vs. metallicity per type and compare with the paper.

**Uses:** `growl_tools.standard_format`, `growl_tools.formation_efficiency`.
**Deliverables:** `notebooks/04_formation_efficiency.ipynb`, efficiencies in `results.yaml`, figure.
**Done when:** efficiencies match the paper where it reports them; the standard-format file is ready for Zenodo upload by a maintainer.

---

## Step 5: Calculate merger rates

**Goal:** what the simulation predicts for the merger rate across cosmic time.

- Run cosmic integration with the GROWL default star-formation history S(Z, z), and record that choice in `results.yaml`.
- Compute the merger rate vs. redshift and the local rate (z ≈ 0.2) for BBH, BHNS, BNS.
- Compare with the paper's rates (if any) and with the latest LVK estimates (GWTC).

**Uses:** `growl_tools.cosmic_integration`.
**Deliverables:** `notebooks/05_merger_rates.ipynb`, rates in `results.yaml`, figures.
**Done when:** rates are computed for all types present, and differences from the paper are explained (often a different S(Z, z)).

---

## Step 6: Calculate properties

**Goal:** what the merging population looks like.

- Distributions of primary mass, chirp mass, mass ratio, and delay time (plus spins if the data has them), weighted by the merger rate from step 5.
- Compare with the paper and with LVK population results; note where they agree and disagree.

**Uses:** `growl_tools.properties` (planned; use notebook code until it exists).
**Deliverables:** `notebooks/06_properties.ipynb`, figures, a short summary in `README.md`.
**Done when:** the README summarizes the entry in a few plots and paragraphs a newcomer can read.

---

## Rules of thumb

- Only edit files inside your own `simulations/<id>/` folder. Changes to the schema, template, or shared code go through a separate issue.
- Clear large notebook outputs before committing; keep figures as small PNGs.
- Run the validator locally before pushing. The automatic check must pass before review.
- Unclear is useful information. Write it down and keep going.
