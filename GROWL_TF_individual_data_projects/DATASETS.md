# Datasets in the GROWL Task Force projects

The current list of datasets: who is working on each one, where the data is, and the checks done
so far. Each dataset has its own folder in [`individual_project_folders/`](individual_project_folders/);
details and open questions for one dataset go in **that folder's `README.md`**, not here.

*Kept by the GROWL mentors. Students: if something here is wrong or out of date, say so on Discord
or in your folder's README.*

## Who works on what

| Dataset (folder) | Paper | Data | Students | Status |
|---|---|---|---|---|
| [boesky-2024-bbhrate](individual_project_folders/boesky-2024-bbhrate/) | Boesky, Broekgaarden & Berger (2024), ApJ 976, 23 and 24, [arXiv:2405.01623](https://arxiv.org/abs/2405.01623), [arXiv:2405.01630](https://arxiv.org/abs/2405.01630) | [GWLandscape publication 63](https://gwlandscape.org.au/publication/Q29tcGFzUHVibGljYXRpb25Ob2RlOjYz/) | Sofia (MIT) | Step 1: Run_Details exported to CSV |
| [broekgaarden-2022-dcorates](individual_project_folders/broekgaarden-2022-dcorates/) | Broekgaarden et al. (2022), MNRAS 516, 5737, [arXiv:2112.05763](https://arxiv.org/abs/2112.05763) | Zenodo [5651073](https://zenodo.org/records/5651073) (BBH), [5178777](https://zenodo.org/records/5178777) (BHNS), [5189849](https://zenodo.org/records/5189849) (BNS) | Joseph, Jayjanth, Hsin-Yu Ho | Step 1 |
| [compas-2022-methods1](individual_project_folders/compas-2022-methods1/) | Team COMPAS (2022), ApJS 258, 34, [arXiv:2109.10352](https://arxiv.org/abs/2109.10352), Fig. 16 data | Zenodo [5655483](https://zenodo.org/records/5655483) | Nicholas Rodriguez | Step 1 |
| [compas-2022-repz](individual_project_folders/compas-2022-repz/) | No results paper; cite the COMPAS methods paper (ApJS 258, 34) | Zenodo [6346444](https://zenodo.org/records/6346444) (`Z_all.zip`) | Ethan | Step 1 |
| [gwlandscape-default](individual_project_folders/gwlandscape-default/) | No paper | [GWLandscape publication 27](https://gwlandscape.org.au/publication/Q29tcGFzUHVibGljYXRpb25Ob2RlOjI3/) (log-uniform file) | Tanush | Step 1: download instructions and metadata submitted |
| [riley-2021-che](individual_project_folders/riley-2021-che/) | Riley et al. (2021), MNRAS 505, 663, [arXiv:2010.00002](https://arxiv.org/abs/2010.00002) | Zenodo [5595426](https://zenodo.org/records/5595426) | Hamza | Step 1 |
| [vanson-2022-nopeaks](individual_project_folders/vanson-2022-nopeaks/) | van Son et al. (2022), ApJ 940, 184, [arXiv:2209.13609](https://arxiv.org/abs/2209.13609) | Zenodo [7080725](https://zenodo.org/records/7080725) (part 1), [7080164](https://zenodo.org/records/7080164) (part 2, incl. fiducial) | Maryam Ahsan | Step 1 done (both parts, in the older notebooks); waiting for the full simulation data from Lieke van Son; first step 2 example |
| [vanson-2022-weightymatter](individual_project_folders/vanson-2022-weightymatter/) | van Son et al. (2022), ApJ 931, 17, [arXiv:2110.01634](https://arxiv.org/abs/2110.01634) | Zenodo [5544170](https://zenodo.org/records/5544170) | Tanmoy Bhowmik | Step 1 |
| [vanson-2023-sfrd](individual_project_folders/vanson-2023-sfrd/) | van Son et al. (2023), ApJ 948, 105, [arXiv:2209.03385](https://arxiv.org/abs/2209.03385) | Zenodo [7612755](https://zenodo.org/records/7612755) (the onboarding tutorial file) | Edward Vu (Mike Steele until Nov 2026) | Step 1 (started 2026-11) |
| [vanson-2025-notjustwinds](individual_project_folders/vanson-2025-notjustwinds/) | van Son et al. (2025), ApJ 979, 209, [arXiv:2411.02484](https://arxiv.org/abs/2411.02484) | Zenodo [14508864](https://zenodo.org/records/14508864) (paper cites older version 13999532) | Prathmesh Shaswat | Step 1 |
| [willcox-2023-amloss](individual_project_folders/willcox-2023-amloss/) | Willcox et al. (2023), ApJ 958, 138, [arXiv:2308.06666](https://arxiv.org/abs/2308.06666) | Zenodo [8386385](https://zenodo.org/records/8386385) | Harry | Step 1 |

## Checks so far

What we know about each file. "?" means nobody has checked yet. **Verified** means someone opened the
file; everything else comes from Zenodo or the paper. These checks decide what each dataset can be
used for. For example, without the group of all simulated binaries (`BSE_System_Parameters`), the
number of simulated binaries for the formation efficiency has to come from the paper.

| Dataset | Code version | Run_Details in the file? | All simulated binaries in the file? | Weights? | Metallicities | Submodels |
|---|---|---|---|---|---|---|
| boesky-2024-bbhrate | v02.31.04 (papers) | yes, exported to `run_details_boesky_2024_bbh_rate.csv` | ? | yes, STROOPWAFEL (papers) | ? | 12 (2e7 binaries) |
| broekgaarden-2022-dcorates | legacy COMPAS (pre-v02) | no (legacy output) | ? | ? | ? | 20 (A–T) per DCO type |
| compas-2022-methods1 | v02.21.00 (tag, commit c61a6db) | yes per Zenodo; check | ? | yes, STROOPWAFEL | log-uniform, 1e-4 to 0.03 | none (1e7 binaries) |
| compas-2022-repz | v02.27.05 (no tag, commit 6161c3e) | yes per Zenodo; a text Run_Details is overridden by a grid file | ? | no, plain Monte Carlo | log-uniform (`Z_all.zip`) | none (5e6 binaries) |
| gwlandscape-default | v02.39.01 (no tag, commit aa3f463) | probably; check | ? | ? | log-uniform file | 1 |
| riley-2021-che | v02.11.01a (special build) | probably not (added in v02.19.00); check | ? | ? | 30, log-spaced | 4 (f_WR = 0, 0.2, 0.6, 1.0) in one file; SampledZ file is a possible 5th |
| vanson-2022-nopeaks | v02.26.03 (Zenodo) | **no** (verified, ζ = 4.5 file) | **no** (verified, ζ = 4.5 file): take N = 1e7 from the paper. Maryam: files are stripped down (no initial separation or eccentricity); full data requested from Lieke van Son | yes, STROOPWAFEL | log-uniform, 1e-4 to 0.03 (verified) | 25 (13 + 12) |
| vanson-2022-weightymatter | v02.19.04 | yes, as group `Details` (Mike's Task 0; Tanmoy to confirm) | yes, as `SystemParameters` (older name) | yes, STROOPWAFEL | log-uniform | 1 (+ 3 rate groups) |
| vanson-2023-sfrd | v02.26.03 (Zenodo; not in the file) | **no** (verified) | **yes** (verified, 1e7) | **yes**, `mixture_weight` (verified) | log-uniform, 1e-4 to 0.03 (verified) | 1 |
| vanson-2025-notjustwinds | v03.01.02 | probably; check | ? | ? | 12 (5e6 binaries each, same seeds) | fiducial + 9 variations (check that the archive holds all) |
| willcox-2023-amloss | v02.38.07 (verified from Run_Details) | **yes** (verified) | ? | ? | **one** (Z = 0.0142): fails the "more than 2 metallicities" rule | 19 files |

## Notes and updates

*Newest at the bottom. Start each entry with the date and your name.*

### 2026-11-24 (Floor)

- Floor is transferring all the original data files to Floor's cluster, so that students
  (starting with Maryam) can access them there.

- This list replaces the spreadsheet `instructions_task_force/COMPAS models for GROWL catalog.xlsx`
  (not in git). Assignments are updated to match the folder READMEs.
- Step 2 is being prepared: (a) compare each file with the GROWL standard columns
  ([growl-tools](https://github.com/growl-lab/growl-tools), `docs/standard_columns.md`) and upload
  the resulting `column_check.csv`; (b) compute the formation efficiency. Maryam's dataset is the
  first worked example.
