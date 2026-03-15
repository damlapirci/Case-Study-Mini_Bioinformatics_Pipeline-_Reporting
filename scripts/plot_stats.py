import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_plots(input_csv, output_prefix):
    df = pd.read_csv(input_csv)
    
    if df.empty:
        print("Warning: CSV is empty. No plots generated.")
        return
        
    print("=== Summary Statistics ===")
    print(df[['GC_Content', 'Read_Length', 'Mean_Quality']].describe())
    print("\n=== Medians ===")
    print(df[['GC_Content', 'Read_Length', 'Mean_Quality']].median())
    
    sns.set_theme(style="whitegrid")
    
    # Create a figure with 3 subplots
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # 1. GC Content
    sns.histplot(df['GC_Content'], bins=50, kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title('GC Content Distribution')
    axes[0].set_xlabel('GC Content (%)')
    axes[0].set_ylabel('Frequency')
    
    # 2. Read Lengths
    sns.histplot(df['Read_Length'], bins=50, kde=True, ax=axes[1], color='salmon')
    axes[1].set_title('Read Length Distribution')
    axes[1].set_xlabel('Read Length (bp)')
    axes[1].set_ylabel('Frequency')
    
    # 3. Mean Read Quality Scores
    sns.histplot(df['Mean_Quality'], bins=50, kde=True, ax=axes[2], color='lightgreen')
    axes[2].set_title('Mean Quality Score Distribution')
    axes[2].set_xlabel('Phred Quality Score')
    axes[2].set_ylabel('Frequency')
    
    plt.tight_layout()
    plot_path = f"{output_prefix}_summary_plots.png"
    plt.savefig(plot_path)
    print(f"\nPlots saved to {plot_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot summary statistics and calculate metrics.")
    parser.add_argument("-i", "--input", required=True, help="Input CSV file from calc_stats.py")
    parser.add_argument("-o", "--output_prefix", required=True, help="Prefix for output plot files")
    args = parser.parse_args()
    
    generate_plots(args.input, args.output_prefix)
