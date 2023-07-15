# codon-translation-split

ABSTRACT
-----------------------
Translates input database in FASTA format in AA sequence based on coding table loaded as a CSV file,
then it splits peptides basing on presence of any Amber, ochre and opal stop-codons.
Finally it generates files for 3-frame translation and split-out files with pepetides without stop-codons inside
-----------------------

USAGE
-----------------------
First configure file paths in config.py
CODING_FILE = "res/codon.csv" < CODON TRANSLATION MAP>
INPUT_FILE = "input/TAIR10_cds_20101214.fasta" <NUCLEOTIDE SEQUENCES FILE, FASTA mRNA FORMAT>
FRAME1_OUTPUT_FILE = "output/Frame1.fasta" <OUTPUT FILE FOR FRAME 1 READOUT>
FRAME2_OUTPUT_FILE = "output/Frame2.fasta" <OUTPUT FILE FOR FRAME 2 READOUT>
FRAME3_OUTPUT_FILE = "output/Frame3.fasta" <OUTPUT FILE FOR FRAME 2 READOUT>
FRAME1_SPLIT_OUTPUT_FILE = "output/Frame1_split.fasta"  <OUTPUT FILE FOR FRAME 1 SPLTI-OUT>
FRAME2_SPLIT_OUTPUT_FILE = "output/Frame2_split.fasta"  <OUTPUT FILE FOR FRAME 2 SPLTI-OUT>
FRAME3_SPLIT_OUTPUT_FILE = "output/Frame3_split.fasta"  <OUTPUT FILE FOR FRAME 2 SPLTI-OUT>

By now you need to create subforlders by yourself: the program needs existing forlder paths to work

TO DO
-----------------------
- Create path that are not existing
- Manage exceptions to input file non-existance and errors in wrtiing files
- Optionally read config from other files or command-line
