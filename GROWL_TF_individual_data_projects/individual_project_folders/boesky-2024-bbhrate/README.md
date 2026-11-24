# boesky-2024-bbhrate: Boesky, Broekgaarden & Berger (2024), BBH merger rate deviates from the cosmic SFR

**Team:** Sofia (MIT)

## Project log (Floor)

*Assignments and changes to this project, kept by Floor. Students: please write in **Notes** below.*

- **2026-11-18**: Added Boesky, Broekgaarden & Berger (2024) and assigned it to Sofia (MIT).
  Data: [GWlandscape publication page](https://gwlandscape.org.au/publication/Q29tcGFzUHVibGljYXRpb25Ob2RlOjYz/)
  (paper 1 points to <https://gwlandscape.org.au/compas/> for the data). Zenodo record: TBD.
  - **Papers** (two companion papers):
    1. "Investigating the Cosmological Rate of Compact Object Mergers from Isolated Massive Binary
       Stars", ApJ 976, 24, [doi:10.3847/1538-4357/ad7fe3](https://doi.org/10.3847/1538-4357/ad7fe3)
       ([arXiv:2405.01630](https://arxiv.org/abs/2405.01630)).
    2. "The Binary Black Hole Merger Rate Deviates from the Cosmic Star Formation Rate: A Tug of
       War between Metallicity and Delay Times", ApJ 976, 23,
       [doi:10.3847/1538-4357/ad7fe4](https://doi.org/10.3847/1538-4357/ad7fe4)
       ([arXiv:2405.01623](https://arxiv.org/abs/2405.01623)).
    - Also an APS April Meeting 2024 abstract:
      [2024APS..APRS12003B](https://ui.adsabs.harvard.edu/abs/2024APS..APRS12003B/abstract).
  - **Code:** probably <https://github.com/Adam-Boesky/Exploring_Parameter_Space> (config files,
    run + analysis scripts); COMPAS fork: <https://github.com/Adam-Boesky/COMPAS_merger_z_evolution>
    (confirm with Adam).
  - **COMPAS version:** v02.31.04 (stated in both papers; matches Adam's COMPAS fork). Check
    `Run_Details`.
  - **Run_Details in HDF5:** probably yes (v02.31.04 is newer than v02.19.00, when `Run_Details`
    was added to the HDF5 output); check the downloaded file.
  - **Models:** 12 submodels with 20 million simulated binaries. The config files in the GitHub
    repo vary the CE α and the mass-transfer efficiency fa.
  - **Sampling:** STROOPWAFEL (both papers), so expect weights.
- **2026-11-18**: Sofia notes that `Run_Details` records **v02.31.09** instead of v02.31.04.
- **2026-11-24**: ✅ Sofia uploaded `Run_Details` to the repository
  (`run_details_boesky_2024_bbh_rate.csv`); Floor checked the folder and everything is in there.
  **Next step:** upload a list of all the parameter header names (groups and columns) in the
  Boesky data file.

## Notes

*New entries go below, with your name and the date, e.g. `### 2026-12-01 (Name)`.*
