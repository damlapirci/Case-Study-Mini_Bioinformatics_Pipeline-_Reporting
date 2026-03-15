# FASTQ Processing Pipeline

This pipeline processes long-read FASTQ files, performs Quality Control using NanoPlot, and calculates basic statistics (GC content, read length, mean quality score) with custom Python scripts, followed by generating distribution plots.

## Dependencies

This pipeline uses Conda and Snakemake for reproducibility.

1. Ensure you have Conda installed (Miniconda or Anaconda).
2. Create the environment from the provided `environment.yml`:
   ```bash
   conda env create -f environment.yml
   ```
3. Activate the environment:
   ```bash
   conda activate fastq-pipeline
   ```

## Running the Pipeline

1. Place your input FASTQ file in the `data/` directory (e.g., `data/sample.fastq.gz`).
2. Update the `config.yaml` file to point to your input FASTQ file:
   ```yaml
   input_fastq: "data/sample.fastq.gz"
   ```
3. Run the Snakemake pipeline:
   ```bash
   snakemake --cores 1
   ```

## Outputs

- `results/qc/`: Contains NanoPlot's comprehensive QC reports for long reads (`NanoPlot-report.html`, `NanoStats.txt`, etc.).
- `results/stats/read_stats.csv`: A CSV file containing the calculated GC content, read length, and mean quality score for each read.
- `results/stats/read_stats_summary_plots.png`: Distribution plots of the three metrics.

## Version Control
To push this code to a public GitHub repository:
1. Initialize the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of FASTQ pipeline"
   ```
2. Create a new repository on GitHub.
3. Link the remote and push:
   ```bash
   git remote add origin https://github.com/USERNAME/REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```
