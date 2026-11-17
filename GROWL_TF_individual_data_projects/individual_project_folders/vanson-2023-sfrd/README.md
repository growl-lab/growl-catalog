# vanson-2023-sfrd: van Son et al. (2023), Zenodo 7612755

**Team:** Edward Vu (since 2026-11-16). Mike Steele worked on this dataset until November 2026
and handed it off; his results so far are below.

| | |
|---|---|
| 📄 **Paper** | van Son et al. (2023), *The Locations of Features in the Mass Distribution of Merging Binary Black Holes Are Robust against Uncertainties in the Metallicity-dependent Cosmic Star Formation History*, ApJ 948, 105 · [doi:10.3847/1538-4357/acbf51](https://doi.org/10.3847/1538-4357/acbf51) · [arXiv:2209.03385](https://arxiv.org/abs/2209.03385) |
| 💾 **Data** | [Zenodo 7612755](https://zenodo.org/records/7612755): `COMPAS_Output_wWeights.tar.gz` (3.0 GB), one HDF5 file. This is also the file used in onboarding Tutorials 2 and 3. |
| 💻 **Authors' code** | [github.com/LiekeVanSon/SFRD_fit](https://github.com/LiekeVanSon/SFRD_fit) (named in the paper's Software & Data section) |
| 💻 **Simulation code** | COMPAS v02.26.03, according to the Zenodo record and the 2023 paper; **cannot be verified from the file** (no `Details` / `Run_Details` group) |
| 🔗 **Related dataset** | [`vanson-2022-weightymatter`](../vanson-2022-weightymatter/) (Zenodo 5544170): a **different** simulation, see below |

## Project log (Floor)

*Assignments and changes to this project, kept by Floor. Students: please write in **Notes** below.*

- **2026-10-27**: Gave Mike Steele the van Son et al. (2022) "weighty matter" dataset, with a
  Task 0: check whether its Zenodo release (5544170) and the tutorial file (Zenodo 7612755) are the
  same simulation.
- **2026-11-05**: Mike's Task 0 showed they are **different simulations**. Mike's dataset became
  Zenodo 7612755 (this one, released with van Son et al. 2023); Zenodo 5544170 went to Tanmoy
  ([`vanson-2022-weightymatter`](../vanson-2022-weightymatter/)).
- **2026-11-16**: Moved the project to growl-catalog; folder renamed from
  `vanSon22weightyMatter_1__Mike_Steele`. Mike handed the dataset off (see below).
- **2026-11-16**: Assigned this dataset to **Edward Vu**, starting from Mike's hand-off. Added
  `step1_Edward_Vu.ipynb`.

In Mike's notes, "2022a" means van Son et al. (2022), *The redshift evolution of the binary black
hole merger rate: a weighty matter*, ApJ 931, 17 (the paper behind Zenodo 5544170).

---

## Hand-off from Mike Steele (November 2026)

Mike's notebooks (on his own GitHub, not in this repository):
- Task 0 (A vs B comparison): [growl-task0](https://github.com/steele-stats/growl-task0/blob/main/step1_vanSon22weightyMatter_Mike_Steele.ipynb)
- Last snapshot, including Task E: [growl_last_update_mike](https://github.com/steele-stats/growl_last_update_mike)

`step1_Mike_Steele.ipynb` in this folder is the instructions copy that was prepared for him; his
filled-in work is in the links above. Edward works in `step1_Edward_Vu.ipynb`. **Tasks A–D, F and G have not been started** for this dataset.

### Task 0 result: this is NOT the same simulation as Zenodo 5544170

Zenodo 7612755 describes its file as a "stripped-down version of van Son et al. 2022". Mike
compared the two files (A = Zenodo 5544170, B = this dataset) and found they are **two separate
simulations**, not one simulation released twice:

| | A: Zenodo 5544170 | B: Zenodo 7612755 (this dataset) |
|---|---|---|
| COMPAS version | v02.19.04 (from its `Details` group) | v02.26.03 (Zenodo record + 2023 paper only) |
| Binaries simulated | 10,000,000 | 10,000,000 |
| Primary ZAMS mass range in the data | starts at 10 M☉ | starts at **5** M☉ (min `Mass@ZAMS(1)` = 5.0000008) |
| Double compact objects | 4,342,215 | 2,523,122 |
| Groups | `Details` (346 run-setting columns), `SystemParameters`, `DoubleCompactObjects`, 3 `Rates_…` groups | `BSE_System_Parameters`, `BSE_Double_Compact_Objects`, `BSE_RLOF` (31.9 M rows), 1 `Rates_…` group |
| DCO table columns | 19 (adds `SemiMajorAxis@DCO`, `Eccentricity@DCO`, `Recycled_NS(1/2)`) | 15 |
| Archive md5 matches Zenodo | ✅ | ✅ |

- Primary ZAMS masses at the same row index disagree for **> 99.99%** of rows; coalescence times
  and weights don't match either.
- ⚠️ **`SEED` is just a row counter** (0 … 9,999,999) in both files, so matching SEEDs carry no
  information. Only 1,208,104 DCO SEEDs appear in both.
- The pre-computed rates were **not** compared (the `Rates_…` groups use different star formation
  history parameters).

### Provenance checks (Task A, partly)

- **Paper:** correct as listed above. The paper's Software & Data section points to Zenodo
  7612755, and the file's `Rates_…` group name matches the paper's Table 1 best-fit S(Z,z)
  parameters.
- **Data link:** correct; md5 of the downloaded archive matches the Zenodo page.
- **Run_Details:** none. The file has only `BSE_System_Parameters`, `BSE_Double_Compact_Objects`,
  `BSE_RLOF` and one `Rates_…` group.
- **Authors' code:** correct (SFRD_fit, see table above).

### Task E: metadata found so far

Mike verified these against the papers. ⚠️ **Whoever takes over: spot-check each value in the
paper before copying it into `metadata.csv`.** The sources are listed, so this should be quick.

**Tier 1**

| Property | Value | Source | Status |
|---|---|---|---|
| Code and version | COMPAS v02.26.03 (Riley et al. 2022) | 2023 Sec. IV + footnote 5 (links Zenodo 7612755); Zenodo metadata agrees; not verifiable from the file | ✅ |
| Number of binaries | 10,000,000 (rows in `BSE_System_Parameters`). Not stated in the 2023 paper; 2022a Sec. II says 10⁷ (+10⁶ convergence set), but for the v02.19.04 run | the file; 2022a Sec. II | 🤔 |
| Primary ZAMS mass range | 2022a Sec. 2.2 says 10–150 M☉, but this file reaches 5.00 M☉, so the rerun probably used ≈5–150 M☉ | 2022a Sec. 2.2, contradicted by the data | 🤔 open question |
| Initial mass function | Kroupa (2001). The 0.01–200 M☉ limits in 2023 Sec. I are the IMF normalisation for the analytic model, not the COMPAS sampling range | 2023 Sec. I; 2022a Sec. 2.2 | ✅ |
| Mass ratio distribution | *not filled in yet* | | |
| Metallicities | *not filled in yet* (Task 0: the data spans Z = 0.0001–0.03) | | |
| Sampling method | *not filled in yet* | | |

**Tier 2**

| Property | Value | Source |
|---|---|---|
| Separations | Öpik's law (flat in log a), 0.01–1000 AU; systems already in RLOF at ZAMS discarded | 2022a §2.2 |
| Eccentricity | circular at birth | 2022a §2.2 |
| Binary fraction | ❓ not stated in either paper | |
| Winds | hot stars: Vink / Kudritzki; cool/AGB: Vassiliadis & Wood; Belczynski et al.; LBV winds | 2022a §2.1 |
| Mass transfer efficiency + angular momentum loss | highly non-conservative (up to ~10× the thermal rate), accretion Eddington-limited; angular momentum lost from the vicinity of the accretor | 2022a §2.1 |
| Mass transfer stability | ζ_ad = 2 for MS donors, 6.5 for Hertzsprung-gap donors (Ge et al. 2015); Soberman et al. 1997 for post-He stars | 2022a §2.1 |
| Common envelope | α_CE = 1, Nanjing λ (Xu & Li 2010), pessimistic (HG donors do not survive CE) | 2022a §2.1 |
| Remnant masses | Fryer et al. 2012 delayed; PPISN/PISN per Farmer et al. 2019 | 2022a §2.1 |
| Kicks | Maxwellian (Hobbs et al. 2005), scaled by fallback; full fallback (no kick) for M_CO > 11 M☉ | 2022a §2.1 |
| Maximum evolution time | ❓ not stated in either paper | |
| Cosmology + star formation history | flat ΛCDM, Planck (Ω_M = 0.31, Ω_Λ = 0.69, H₀ = 67.7); analytic S(Z,z) = Madau & Dickinson SFRD × skewed log-normal, best fit from 2023 Table 1: μ₀ = 0.025, μ_z = −0.049, α = −1.778, ω₀ = 1.122, ω_z = 0.049, a = 0.02, b = 1.48, c = 4.44, d = 5.90 | 2023 §I + Table 1 ✅ |

### Open questions for the next person

- 2022a Sec. 2.2 says M1 is sampled from 10–150 M☉, but this file reaches 5.00 M☉. Was the rerun
  5–150 M☉?
- Binary fraction and maximum evolution time are not stated in either paper.
- Mike's Task 0 conclusion mentions a "flat IMF", while his Task E row says Kroupa (2001). Check
  which is right (the "flat" may refer to the metallicity sampling).
- Minor: the `Rates_…` group name carries rounded S(Z,z) parameters (μ_z −0.05, σ₀ 1.125,
  c 4.45) instead of the exact Table 1 digits; the same rounding issue as the paper's footnote 7.

---

## Notes

*New entries go below, with your name and the date, e.g. `### 2026-12-01 (Edward)`.*
