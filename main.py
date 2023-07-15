import os, errno
import config as conf

from fasta import fastaHandler as Handler


def main():
    
    print ("Removing previous leftover files from output folder...")
    try:
        os.remove(conf.FRAME1_OUTPUT_FILE)
    except OSError:
        pass
    try:
        os.remove(conf.FRAME2_OUTPUT_FILE)
    except OSError:
        pass
    try:
        os.remove(conf.FRAME3_OUTPUT_FILE)
    except OSError:
        pass
    try:
        os.remove(conf.FRAME1_SPLIT_OUTPUT_FILE)
    except OSError:
        pass
    try:
        os.remove(conf.FRAME2_SPLIT_OUTPUT_FILE)
    except OSError:
        pass
    try:
        os.remove(conf.FRAME3_SPLIT_OUTPUT_FILE)
    except OSError:
        pass
    
    print ("\nCreating FASTA reader engine...")
    handler = Handler()
    print ("\nStarting in-silico translation...")
    handler.translate_dna_2_protein()
    print ("\n3-frames translation done, FASTA frames file created")
    print ("\n\nStarting peptide splitting on out frame stop-codons...")
    handler.split_peptides()
    print ("\nPeptides calculation done, split files created in output folder." )
    print ("\n\nHave a good day ;)")









if __name__ == "__main__":
    main()