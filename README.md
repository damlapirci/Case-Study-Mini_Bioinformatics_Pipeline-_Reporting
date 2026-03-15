# Mini Bioinformatics Pipeline - FASTQ Reporting

A lightweight, reproducible Snakemake pipeline for analyzing and visualizing long-read sequencing FASTQ files. This project is built to accept sequencing data and rapidly generate key metrics for quality control (QC).

This repository was created as a case study for developing automated bioinformatics workflows.

## Features

- **Automated Workflow**: Uses Snakemake to manage the full data processing lifecycle.
- **Custom Statistics Calculation**: A custom Python script parses raw FASTQ files to calculate:
  - **GC Content (%)**
  - **Read Length (bp)**
  - **Mean Quality Score (Phred)**
- **Automated Visualization**: Generates detailed histograms with kernel density estimation (KDE) for the calculated metrics to give a quick overview of data quality.

## Project Structure

```text
├── config.yaml          # Snakemake configuration file pointing to the input data
├── environment.yml      # Conda environment definition for reproducibility
├── Snakefile            # Snakemake pipeline definition
├── README.md            # Project documentation
├── email_draft.txt      # Example report addressed to stakeholders
├── scripts/             # Custom Python analysis scripts
│   ├── calc_stats.py
│   └── plot_stats.py
└── data/                # Directory for placing the input FASTQ file
```

## Setup & Installation

The pipeline relies on Conda for environment management and Snakemake for workflow execution. You do not need Conda if you prefer to install the dependencies locally with Python's `pip`.

### Approach A: Using Python's built-in `pip`
If you prefer not to use Conda, you can easily run this pipeline by installing the dependencies using your local Python installation.

1. Install the required packages:
   ```bash
   pip install snakemake biopython pandas matplotlib seaborn
   ```
2. Navigate to the project directory and run Snakemake:
   ```bash
   snakemake --cores 1
   ```

### Approach B: Using Conda (Recommended for strict reproducibility)
This method ensures exact version matching by using the provided `environment.yml` file.

1. Ensure Conda (Miniconda or Anaconda) is installed.
2. Create and activate the pipeline environment:
   ```bash
   conda env create -f environment.yml
   conda activate fastq-pipeline
   ```
3. Run the pipeline:
   ```bash
   snakemake --cores 1
   ```

## How to Run

1. Place your target FASTQ file inside the `data/` directory. For example, `data/barcode77.fastq.gz`.
2. Edit the `config.yaml` to point to your data file:
   ```yaml
   input_fastq: "data/barcode77.fastq.gz"
   ```
3. Execute the pipeline using Snakemake as described in the **Setup** section.

## Expected Output

Once the pipeline successfully finishes execution, you will find a generated directory named `results/stats/` containing:

1. `read_stats.csv`: A structured database format of your analysis. It contains every individual read parsed from the FASTQ file alongside its exact GC percentage, read length, and mean quality score.
2. `read_stats_summary_plots.png`: A high-quality graphic comprising three subplots (distributions of GC Content, Read Length, and Mean Quality Scores). This file acts as an immediate visual summary of the sequencing run's success.

*A sample draft email summarizing these results, `email_draft.txt`, is also included for reporting purposes.*
