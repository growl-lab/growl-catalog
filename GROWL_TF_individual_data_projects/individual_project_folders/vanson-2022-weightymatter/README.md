# vanson-2022-weightymatter: van Son et al. (2022) "weighty matter", Zenodo 5544170

**Team:** Tanmoy Bhowmik

| | |
|---|---|
| 📄 **Paper** | van Son et al. (2022), *The redshift evolution of the binary black hole merger rate: a weighty matter*, ApJ 931, 17 · [doi:10.3847/1538-4357/ac64a3](https://doi.org/10.3847/1538-4357/ac64a3) · [arXiv:2110.01634](https://arxiv.org/abs/2110.01634) |
| 💾 **Data** | [Zenodo 5544170](https://zenodo.org/records/5544170): `COMPAS_Output_wRates.tar.gz` (8.1 GB). Note: the archive contains a file named `COMPAS_Output_wWeights.h5` |
| 💻 **Authors' code** | [github.com/LiekeVanSon/RedshiftEvolution_BBHMergers_WeightyMatter](https://github.com/LiekeVanSon/RedshiftEvolution_BBHMergers_WeightyMatter) |
| 💻 **Simulation code** | COMPAS v02.19.04 (from the file's `Details` group and the paper) |
| 🔗 **Related dataset** | [`vanson-2023-sfrd`](../vanson-2023-sfrd/) (Zenodo 7612755, the tutorial file): a **different** simulation, see below |

## Project log (Floor)

*Assignments and changes to this project, kept by Floor. Students: please write in **Notes** below.*

- **2026-10-27**: Gave this dataset to Mike Steele, with a Task 0: check whether this Zenodo release
  (5544170) and the tutorial file (Zenodo 7612755) are the same simulation.
- **2026-11-05**: Mike's Task 0 showed they are different simulations. Assigned this dataset
  (Zenodo 5544170) to **Tanmoy Bhowmik**; Mike continued with Zenodo 7612755
  ([`vanson-2023-sfrd`](../vanson-2023-sfrd/)).
- **2026-11-16**: Moved the project to growl-catalog; folder renamed from
  `vanSon22weightyMatter_2__Tanmoy_Bhowmik`.
- **2026-11-24**: ✅ Tanmoy checked the entries of our COMPAS catalog checklist. **Next steps:**
  1. Check whether the file has a `Run_Details` group. Here it is probably the group called
     `Details` (see Mike's Task 0 below). If so, export its first row to a CSV in this folder, one
     line per setting (`option,value`), like Sofia's
     [`run_details_boesky_2024_bbh_rate.csv`](../boesky-2024-bbhrate/run_details_boesky_2024_bbh_rate.csv).
  2. List all the parameter headers (groups and columns) in the data file in a text file, and
     upload that too.

---

## What we already know: Mike Steele's Task 0 (November 2026)

Mike Steele compared this dataset (A) with the tutorial file (B, Zenodo 7612755), which Zenodo
describes as a "stripped-down version of van Son et al. 2022". **They are two separate
simulations**, so B now has its own folder, [`vanson-2023-sfrd`](../vanson-2023-sfrd/).
Full details are in [Mike's Task 0 notebook](https://github.com/steele-stats/growl-task0/blob/main/step1_vanSon22weightyMatter_Mike_Steele.ipynb).

What Task 0 found about **this** dataset:

- **COMPAS v02.19.04**, read from the `Details` group (346 run-setting columns). That group is the
  best source for Task E: it records how the simulation was actually run.
- **10,000,000 binaries**; primary ZAMS mass starts at **10 M☉** (B starts at 5 M☉).
- **4,342,215 double compact objects** (B: 2,523,122).
- Groups: `Details`, `SystemParameters`, `DoubleCompactObjects` and **three** `Rates_…` groups (B has
  `BSE_RLOF` instead of `Details`, and only one `Rates_…` group).
- The DCO table has 19 columns, including `SemiMajorAxis@DCO`, `Eccentricity@DCO` and
  `Recycled_NS(1/2)`, which B lacks.
- The archive md5 matches the Zenodo page.
- ⚠️ **`SEED` is just a row counter** (0 … 9,999,999), so SEEDs cannot be used to match binaries
  between files.
- Not checked yet: whether the pre-computed rates agree with the paper.

Many of the tier-2 physics settings Mike collected for B come from **this** paper (Sec. 2.1–2.2),
so his list in [`vanson-2023-sfrd/README.md`](../vanson-2023-sfrd/README.md#task-e-metadata-found-so-far)
is a useful starting point. ⚠️ Check every value against the paper **and** the `Details` group:
the two simulations differ, so values cannot simply be copied.

---

## Notes

*New entries go below, with your name and the date, e.g. `### 2026-12-01 (Tanmoy)`.*
