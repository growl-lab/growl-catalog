# vanson-2022-nopeaks: van Son et al. (2022), "No peaks without valleys"

**Team:** Maryam Ahsan

## Project log (Floor)

*Assignments and changes to this project, kept by Floor. Students: please write in **Notes** below.*

- **September 2026** *(exact date to check)*: First task force dataset: van Son et al. (2022),
  "No peaks without valleys", ApJ 940, 184 ([arXiv:2209.13609](https://arxiv.org/abs/2209.13609)).
  Maryam started with the ζ_eff = 4.5 submodel from [Zenodo 7080725](https://zenodo.org/records/7080725),
  with a starter notebook (`starter_beta0_5_zetaHG4_5_RMS_Delayed.ipynb`). ⚠️ Both Zenodo records
  cite arXiv:2209.03385, which is a different paper (a typo).
- **2026-10-30**: Maryam also took the second record, [Zenodo 7080164](https://zenodo.org/records/7080164),
  which includes the fiducial model (previously given to Harry). Starter notebook:
  `starter_part2_zetaHG6_0_fiducial.ipynb`.
- **2026-11-16**: Moved the project to growl-catalog and merged the two folders
  (`vanSon22noPeaks_1__Maryam_Ahsan`, `vanSon22noPeaks_2__Maryam_Ahsan`) into this one. The two
  step 1 notebooks are now `step1_Maryam_Ahsan_part1.ipynb` (Zenodo 7080725) and
  `step1_Maryam_Ahsan_part2.ipynb` (Zenodo 7080164).
- **2026-11-24**: Floor is transferring all the original data files to Floor's cluster, so that
  Maryam will have access to them there.
- **2026-11-24**: Floor is working on the next steps and will add them here within the next two days.

## Notes (Maryam)

- **2026-10-04 (Maryam):** Cloned the original GROWL repository and began reading van Son et al. (2022),
  "No peaks without valleys", ApJ 940, 184 ([arXiv:2209.13609](https://arxiv.org/abs/2209.13609)).
- **2026-10-10 (Maryam):** Completed a first reading of the paper and downloaded all 13 datasets for part 1 from [Zenodo 7080725](https://zenodo.org/records/7080725).
- **2026-10-19 (Maryam):** Completed tasks A-G in `step1_Maryam_Ahsan_part1` notebook for, working with ζ_eff = 4.5 submodel. Identified several discrepancies and limitations in the publicly available data:
  - The paper describes a mass range of approximately 10–150 M☉, whereas the dataset contains objects with masses extending down to approximately 5 M☉.
  - Several important parameters are unavailable in Zenodo files, including initial orbital separation, eccentricity, coalescence time, and delay time.
  - The Zenodo files do not contain the complete simulated population, including systems that did not form binaries. Consequently, although merger rates are provided, the available data is insufficient to independently reconstruct the merger rates through cosmic integration.
- **2026-10-29 (Maryam):** Contacted Lieke van Son, paper's first author, to clarify the discrepancies and inquire about access to the missing simulation data.
- **2026-11-04:** Began downloading dataset part 2 from [Zenodo 7080164](https://zenodo.org/records/7080164).
- **2026-11-11 (Maryam):** Received a response from Lieke van Son, who kindly offered to share the additional simulation data. We are currently exploring suitable methods for transferring the files.
- **2026-11-16 (Maryam):** Completed the `step1_Maryam_Ahsan_part2` notebook.
- **2026-11-17 (Maryam):** Cloned the new `growl-catalog` repository and began updating the project documentation: updated `README.md` with notes thus far and created`download_instructions.txt`.

**Outstanding items / Next steps:**

- Arrange the transfer of the additional simulation data from Lieke van Son.
- Revisit the missing parameters and merger-rate calculations once the complete data become available.
- Explore the paper's corresponding [LowMBH_and_StableChannel repository](https://github.com/LiekeVanSon/LowMBH_and_StableChannel) to reproduce paper figures.
- Transfer the completed `step_1...` work into the updated notebooks in `growl-catalog`, incorporating any changes to the instructions.