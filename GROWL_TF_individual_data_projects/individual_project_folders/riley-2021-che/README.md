# riley-2021-che: Riley et al. (2021), chemically homogeneous evolution

**Team:** Hamza

## Project log (Floor)

*Assignments and changes to this project, kept by Floor. Students: please write in **Notes** below.*

- **2026-10-30**: Assigned to Hamza: Riley et al. (2021), MNRAS 505, 663,
  [Zenodo 5595426](https://zenodo.org/records/5595426) (built with a special COMPAS version,
  v02.11.01a). `COMPAS_Output` holds 30 metallicities × 4 values of f_WR in one file. Extra task
  (Task H): reproduce Table 1 and Fig. 4.
- **2026-11-16**: Moved the project to growl-catalog; folder renamed from `Riley21CHE_1__Hamza`.
- **2026-11-24**: Check-in with Hamza. **Next step:** list all the parameter headers (groups and
  columns) that exist in the data file, in a text or `.csv` file, and upload it to this folder.

## Notes

### 2026-11-26 (Hamza Ghani)

I downloaded the updated `step1_Hamza.ipynb` from the GROWL catalog project folder and inspected the local Riley et al. (2021) `COMPAS_Output.h5` file without loading the full datasets into memory. The archive checksum matches the Zenodo checksum (`bf25e5083efbe36cd4048797db88531b`). The file contains four groups: `CommonEnvelopes`, `DoubleCompactObjects`, `Supernovae`, and `SystemParameters`; it does not contain a `Run_Details` group. The system-parameter group has 12,000,000 rows, and the `SEED` values are unique from 0 through 11,999,999. The `WR_Multiplier` column has four equally sized values (`0.0`, `0.2`, `0.6`, and `1.0`), with 3,000,000 rows for each value. The two ZAMS metallicity columns contain 30 discrete values from 0.0001 to 0.01496236, with 400,000 rows at each value. The file has 291,253 double-compact-object rows and no obvious weight column.

The complete group/column listing, including data types and row counts, is in `metadata_headers.csv`. The local data files remain outside this submission folder and are not being uploaded.

### What is clear

- The four wind submodels can be separated with `SystemParameters/WR_Multiplier`.
- The metallicity grid is discrete and shared by both ZAMS metallicity columns.
- The dataset uses the older COMPAS-style group names shown above rather than a `Run_Details` group.

### Unclear or limited

- Because `Run_Details` is absent, the COMPAS version and run settings must be documented from the paper, archive metadata, and per-binary parameter columns.
- The data file does not contain a standard `mixture_weight`, `weight`, or `sampling_weight` column; the paper and archive should be used to confirm the sampling interpretation.
- The exact relationship between the `COMPAS_Output_SampledZ.zip` file and the four `WR_Multiplier` models remains an open question for a later task.

### Questions for the team

1. Should `COMPAS_Output_SampledZ.zip` be cataloged as a separate sampling variant or as a fifth submodel?
2. Which paper section should be cited as the authoritative source for the special build `v02.11.01a` when `Run_Details` is absent?
3. Is there an author-provided post-processing or plotting repository that should be linked in the catalog?
