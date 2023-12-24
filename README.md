# GeneExpression-DataParser
## Overview
This repository contains a Python script for parsing and analyzing gene expression data from RNAseq experiments. It combines information from Gene Ontology annotations and differential expression data to identify genes associated with specific biological processes. The project is designed for educational purposes and demonstrates fundamental concepts in Python programming and data handling. Follow the provided instructions to run the script and generate informative output files for your analysis.

## Objective
The main goal is to process these data files to identify genes that are differentially expressed and associated with a specific Gene Ontology term (GO0003723).

## Data Source
* Gene Ontology annotations: GO0003723.genelist
* Differential expression data: diffexp.tsv

## Implementation
* The project is implemented in Python. 
* The script reads data from the provided files, processes it, and generates an output file with the required information.

## Output
The output includes:
* A list of genes with gene name, description, and p-value in TAB-separated columns.
* The gene with the lowest p-value is displayed on the terminal.

## Instructions for Use
* Download the data files.
* Run the Python script GOdiff_209017390.py.
* The script will generate an output file GOdiff_209017390.out with the required data.

## Requirements
Python 3.x

## Disclaimer
This project is part of an academic assessment and is designed for educational purposes only.
