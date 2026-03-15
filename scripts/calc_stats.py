import argparse
import gzip
from Bio import SeqIO
import pandas as pd

def calculate_gc(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100 if len(seq) > 0 else 0

def calculate_stats(input_fastq, output_csv):
    records_data = []
    
    # Handle gzipped fastq
    open_func = gzip.open if input_fastq.endswith('.gz') else open
    
    with open_func(input_fastq, "rt") as handle:
        for record in SeqIO.parse(handle, "fastq"):
            gc_content = calculate_gc(record.seq)
            length = len(record.seq)
            # phred_quality is a list of integers
            mean_quality = sum(record.letter_annotations["phred_quality"]) / length if length > 0 else 0
            
            records_data.append({
                "Read_ID": record.id,
                "GC_Content": gc_content,
                "Read_Length": length,
                "Mean_Quality": mean_quality
            })
            
    df = pd.DataFrame(records_data)
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate statistics from a FASTQ file.")
    parser.add_argument("-i", "--input", required=True, help="Input FASTQ file (can be .gz)")
    parser.add_argument("-o", "--output", required=True, help="Output CSV file path")
    args = parser.parse_args()
    
    calculate_stats(args.input, args.output)
