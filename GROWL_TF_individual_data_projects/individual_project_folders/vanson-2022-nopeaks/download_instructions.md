# Download instructions — van Son et al. (2022), *No peaks without valleys*

**Prepared by:** Maryam Ahsan  
**Date:** 2026-11-17

## Datasets and setup

| Dataset | Zenodo record | Archives |
|---|---|---:|
| Part 1 | [7080725](https://zenodo.org/records/7080725) | 13 `.tar.gz` files |
| Part 2 | [7080164](https://zenodo.org/records/7080164) | 12 `.tar.gz` files |

- **Operating system:** Windows 11
- **Browser:** Google Chrome
- **Terminal (when needed):** Windows PowerShell
- **Extraction software:** WinRAR

## Download recipe (both parts)

1. Opened the appropriate Zenodo record using the links in [Datasets and setup](#datasets-and-setup).

2. Under **Files**, clicked **Download** for each `.tar.gz` archive in Google Chrome. Typical download times were approximately **20–50 minutes per archive**, depending on file size and connection speed. The largest Part 2 archive took approximately 40 minutes. Some larger Part 1 archives took up to around 1.5 hours, excluding the repeatedly failing archive discussed in [Download issue in Part 1 and workaround](#download-issue-in-part-1-and-workaround). Additional observations are recorded in [Observations about download speed](#observations-about-download-speed).

3. Verified each downloaded `.tar.gz` archive against the MD5 checksum provided on Zenodo, using the PowerShell procedure in [Checksum verification](#checksum-verification).

4. Right-clicked each `.tar.gz` archive and extracted it using **WinRAR**. Extraction took roughly **30 seconds per archive**.

5. Renamed each extracted **submodel folder**, replacing decimal points in its name with underscores. For example:

   ```text
   faccFIXEDbeta0.5fcore1.2zetaHG6.0RemMassFRYER2012SNDELAYED
   →
   faccFIXEDbeta0_5fcore1_2zetaHG6_0RemMassFRYER2012SNDELAYED
   ```

   Kept the data filename unchanged: `COMPAS_Output_wWeights.h5`.

6. Stored the extracted submodel folders in these local directories:

   ```text
   Part 1: E:/GitHub/Data/vanSon22noPeaks_1/
   Part 2: E:/GitHub/Data/vanSon22noPeaks_2/
   ```

   Example file layout:

   ```text
   E:/GitHub/Data/vanSon22noPeaks_1/<submodel_folder>/COMPAS_Output_wWeights.h5
   E:/GitHub/Data/vanSon22noPeaks_2/<submodel_folder>/COMPAS_Output_wWeights.h5
   ```

7. Checked that the extracted `.h5` file could be opened, then deleted the corresponding `.tar.gz` archive.

8. Kept a PDF copy of the paper alongside the local part 1 submodel folders. The Zenodo records did not have a separate README attachment; its description supplied dataset documentation and filename conventions.

## Checksum verification

After downloading each `.tar.gz` archive, verified its integrity using **PowerShell**, comparing the local MD5 checksum with the checksum provided on Zenodo.

Replace the two placeholder values below with the actual local archive path and the corresponding Zenodo MD5 checksum:

```powershell
$archivePath = "path/to/downloaded/archive.tar.gz"
$expectedHash = "MD5 checksum copied from Zenodo"
$actualHash = (Get-FileHash -Algorithm MD5 -LiteralPath $archivePath).Hash

if ($actualHash -eq $expectedHash.Trim()) {
    Write-Host "MATCH: the archive matches Zenodo." -ForegroundColor Green
} else {
    Write-Host "MISMATCH: check the filename and copied checksum." -ForegroundColor Red
    Write-Host "Zenodo: $expectedHash"
    Write-Host "Local:  $actualHash"
}
```

Repeated this procedure for each archive, replacing `$archivePath` and `$expectedHash` with the corresponding file path and checksum.

## Download issue in Part 1 and workaround

One Part 1 archive repeatedly failed to finish downloading in Chrome:

```text
faccFIXEDbeta0.5fcore1.2zetaHG6.0RemMassFRYER2012SNDELAYED.tar.gz
```

Two browser attempts stopped near **2.9 GB** after approximately **two hours each**. I switched to PowerShell and used the following resumable download command from the directory where I wanted to save the archive:

```powershell
curl.exe -L -C - -o "faccFIXEDbeta0.5fcore1.2zetaHG6.0RemMassFRYER2012SNDELAYED.tar.gz" "https://zenodo.org/records/7080725/files/faccFIXEDbeta0.5fcore1.2zetaHG6.0RemMassFRYER2012SNDELAYED.tar.gz?download=1"
```

I ran the same command **four times** in the same directory, retaining the partially downloaded file between attempts. The `-C -` option tells `curl` to resume from the existing file size, if the server supports resuming. The PowerShell attempts took approximately **6–7 hours in total**, in addition to the failed browser attempts.

**Part 2:** No downloads failed, and no archive required resuming.

## Observations about download speed

During Part 2, consecutive Chrome downloads sometimes seemed to slow down even though the internet connection appeared unchanged. Clearing the browser cache and refreshing the Zenodo page between downloads seemed to keep speeds more consistent; some files then finished in **20 minutes or less**.

When refreshing did not help, I sometimes started a simultaneous `curl.exe` download in PowerShell. Chrome's download speed occasionally increased shortly afterward. Since `curl` itself was slower, I stopped the PowerShell download and continued in Chrome.

**These are anecdotal observations, not verified fixes; the speed changes may have had other causes.**

## Summary

| | Part 1 | Part 2 |
|---|---|---|
| Zenodo record | [7080725](https://zenodo.org/records/7080725) | [7080164](https://zenodo.org/records/7080164) |
| Archives downloaded | 13 | 12 |
| Extracted data size | ~53.62 GB | ~50.93 GB |
| Download experience | ~20 hours total, including retries for one problematic archive | No significant download or extraction issues |

**Combined extracted data size:** approximately **104.55 GB**.