# Mini Bioinformatics Pipeline - FASTQ Reporting

Hello! I developed this reproducible Snakemake pipeline to process and analyze raw long-read FASTQ files. My goal was to create an automated workflow that rapidly evaluates data quality and visualizes key metrics before proceeding to full sequence alignment.

I designed this repository specifically as a response to Professor Kılıç's request for a clear, non-technical overview of the raw sequencing data. 

## What My Pipeline Does

To ensure I provided exactly what was requested, my pipeline strictly fulfills the following objectives:

1. **Automated Long-Read QC**: The pipeline acts as a QC tool, automatically scanning the sequences to extract crucial metadata.
2. **Custom Python Statistics**: I wrote a custom Python script (`scripts/calc_stats.py`) that parses the exact FASTQ file read-by-read and strictly calculates only the requested metrics:
   - **GC Content (%)**
   - **Read Length (bp)**
   - **Mean Read Quality Score (Phred)**
3. **Data Visualization**: I built a second script (`scripts/plot_stats.py`) that reads the generated metrics and outputs beautiful, easy-to-understand distribution graphs (histograms with KDE curves) alongside key summary statistics (mean and median).

## Project Structure

```text
├── config.yaml          # Points to the target FASTQ file
├── Snakefile            # My Snakemake pipeline definition
├── README.md            # This documentation file
├── email_draft.txt      # My draft email to Professor Kılıç summarizing the results
├── scripts/             
│   ├── calc_stats.py    # Extracts GC, length, and quality
│   └── plot_stats.py    # Plots the metrics and prints summary statistics
└── data/                # Where the input FASTQ file should be placed (e.g., barcode77.fastq.gz)
```

## How to Run My Code (Windows Friendly)

I have optimized this setup to run native on Windows without complicated environment managers like Conda. 

### Step 1: Install Dependencies
Open your `Powershell` or `VS Code Terminal` and install the required Python libraries via `pip`:

```bash
pip install snakemake biopython pandas matplotlib seaborn
```

### Step 2: Configure the Data
Place the raw data you want to analyze inside the `data/` directory. Then, open my `config.yaml` file and make sure the `input_fastq` variable points to your file (for example, `data/barcode77.fastq.gz`).

### Step 3: Run the Pipeline
Navigate to this folder and run the entire workflow with a single command:

```bash
snakemake --cores 1
```

## Expected Outputs

Once my pipeline finishes running, it will automatically generate a `results/` folder with the following:

- **`results/stats/read_stats.csv`**: The raw calculations for every single read.
- **`results/stats/read_stats_summary_plots.png`**: The final visual representation of the GC Content, Read Lengths, and Mean Quality Scores. This PNG file is perfect for showing to the Professor!
