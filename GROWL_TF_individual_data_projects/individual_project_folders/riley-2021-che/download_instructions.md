# Download instructions — Riley et al. (2021) CHE dataset

## Source

- Zenodo record: https://zenodo.org/records/5595426
- File used for Task 0: `COMPAS_Output.zip`
- Expected MD5 checksum: `bf25e5083efbe36cd4048797db88531b`
- The updated instruction notebook is in the project folder as `step1_Hamza.ipynb`.

## Recipe

1. Open the Zenodo record and download `COMPAS_Output.zip`.
2. In the directory containing the download, list the archive before unpacking:

   ```bash
   unzip -l COMPAS_Output.zip
   ```

3. Check the archive checksum:

   ```bash
   md5 COMPAS_Output.zip
   ```

   The verified local copy returned `bf25e5083efbe36cd4048797db88531b`.

4. Unpack the archive:

   ```bash
   unzip COMPAS_Output.zip
   ```

5. Open the resulting HDF5 file with `h5py` and list its groups and datasets. The local file used for the inspection was:

   ```text
   research_project_data/Riley21CHE/COMPAS_Output.h5
   ```

6. Keep the large `.zip` and `.h5` files on the local machine. Do not add them to the GitHub project folder.

## Difficulties / notes

| Item | Note |
|---|---|
| File size | The local archive is about 2.8 GB and the unpacked HDF5 file is about 6.6 GB, so the download and extraction need substantial free space. |
| Run metadata | The file has no `Run_Details` group, so the run version/settings cannot be read from that group. |
| Submodels | The four wind models are mixed in one HDF5 file; use `SystemParameters/WR_Multiplier` to distinguish them. |
| Notebook | The updated notebook was downloaded separately as `step1_Hamza.ipynb`; its path settings should be edited locally if the data is moved. |
