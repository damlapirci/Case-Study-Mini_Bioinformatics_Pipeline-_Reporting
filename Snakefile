configfile: "config.yaml"

rule all:
    input:
        "results/qc/NanoStats.txt",
        "results/stats/read_stats_summary_plots.png"

rule nanoplot:
    input:
        fastq = config["input_fastq"]
    output:
        report = "results/qc/NanoPlot-report.html",
        stats = "results/qc/NanoStats.txt"
    log:
        "logs/nanoplot.log"
    # NanoPlot creates an output directory specified by -o
    shell:
        "NanoPlot --fastq {input.fastq} -o results/qc/ > {log} 2>&1"

rule calculate_stats:
    input:
        fastq = config["input_fastq"],
        script = "scripts/calc_stats.py"
    output:
        csv = "results/stats/read_stats.csv"
    log:
        "logs/calc_stats.log"
    shell:
        "python {input.script} -i {input.fastq} -o {output.csv} > {log} 2>&1"

rule plot_stats:
    input:
        csv = "results/stats/read_stats.csv",
        script = "scripts/plot_stats.py"
    output:
        plots = "results/stats/read_stats_summary_plots.png"
    log:
        "logs/plot_stats.log"
    shell:
        "python {input.script} -i {input.csv} -o results/stats/read_stats > {log} 2>&1"
