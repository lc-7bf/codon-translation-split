import config as conf
import translation as tr

class fastaHandler:
    
    def _processProtein(self, proteinHeader, proteinSequence):
        
        final_protein_string = ""
        final_header_string= ""
        proteinSequence += "*"
        start = 1
        count = 0
        pos = 0
        start_AUG = False
        proteinSeq = proteinSequence.strip("\n")
        for c in range(len(proteinSeq)):
            pos += 1
            if (proteinSeq[c] == "*"):
                
                count +=1
  
                final_header_string = (proteinHeader + 
                                       " PEPTIDE-" + str(count))

                if (len(proteinSeq[start - 1 : pos - 1]) >= 1
                    ):
                    
                    final_protein_string += (final_header_string + 
                                            "\n" + proteinSeq[start - 1 : pos - 1] + 
                                            "\n")
                
                start = pos + 1
                
        return final_protein_string    
    
    def translate_dna_2_protein(self):
        '''
        Open input file from config, translate DNA to Protein
        return protein file in fasta format
        '''
        f1_file = open(conf.FRAME1_OUTPUT_FILE, "a+")
        f2_file = open(conf.FRAME2_OUTPUT_FILE, "a+")
        f3_file = open(conf.FRAME3_OUTPUT_FILE, "a+")
        
        with open(conf.INPUT_FILE, "r") as fin:
            protein :str = fin.readline()
            proteinFASTA = ""
            f1_proteinHeader = ""
            f2_proteinHeader = ""
            f3_proteinHeader = ""
            protein_3_frame = ""

            while protein:
                if ">" in protein:
                    
                    if len(proteinFASTA) > 0:
                        
                        protein_3_frame = tr.transcode.nucleotides3FramesToAAs(proteinFASTA)
                        f1_file.write(f1_proteinHeader)
                        f1_file.write(protein_3_frame[0])
                        f2_file.write(f2_proteinHeader)
                        f2_file.write(protein_3_frame[1])
                        f3_file.write(f3_proteinHeader)
                        f3_file.write(protein_3_frame[2])
                        proteinFASTA = ""
                        f1_proteinHeader = ""
                        f2_proteinHeader = ""
                        f3_proteinHeader = ""
                        
                    f1_proteinHeader = '\n' + protein.strip('\n')
                    f2_proteinHeader = '\n' + "> FRAME 2 - ex FRAME 1 - " + protein.strip('\n').strip(">")
                    f3_proteinHeader = '\n' + "> FRAME 3 - ex FRAME 1 - " + protein.strip('\n').strip(">")
                else:

                    proteinFASTA += protein.strip('\n')
                
                protein = fin.readline()
                
            if len(proteinFASTA) > 0:
                protein_3_frame = tr.transcode.nucleotides3FramesToAAs(proteinFASTA)
                f1_file.write(f1_proteinHeader)
                f1_file.write(protein_3_frame[0])
                f2_file.write(f2_proteinHeader)
                f2_file.write(protein_3_frame[1])
                f3_file.write(f3_proteinHeader)
                f3_file.write(protein_3_frame[2])
                proteinFASTA = ""
                f1_proteinHeader = ""
                f2_proteinHeader = ""
                f3_proteinHeader = ""
                f1_proteinHeader = '\n' + protein.strip('\n')
                f2_proteinHeader = '\n' + "> FRAME 2 - ex FRAME 1 - " + protein.strip('\n').strip(">")
                f3_proteinHeader = '\n' + "> FRAME 3 - ex FRAME 1 - " + protein.strip('\n').strip(">")
                
    def split_peptides(self):
        '''
        Parse output file and writes out _split fasta files with
        single peptides produced by a frame encoding traslation
        whenever a stop-codon gets inserted in translation protein 
        sequence.
        '''    
        proteinHeader = ""
        proteinSeq = ""
             
        with open(conf.FRAME1_SPLIT_OUTPUT_FILE, "a+") as split_out_file1:   
            with open(conf.FRAME1_OUTPUT_FILE, "r") as f1_file:     
                line = f1_file.readline()
                while (line):
                    if ">" in line:
                        if len(proteinSeq) > 3:
                            #split_out_file.write(proteinSeq)
                            split_out_file1.write(self._processProtein(proteinHeader, proteinSeq))
                            proteinSeq = ""
                        proteinHeader = line.strip("\n")  
                    else:
                        proteinSeq += line.strip("\n")
                    line = f1_file.readline()
                if len(proteinSeq) > 3:
                    #split_out_file.write(proteinSeq)
                    split_out_file1.write(self._processProtein(proteinHeader, proteinSeq))
                    proteinSeq = ""
        
        proteinHeader = ""
        proteinSeq = ""
        
        with open(conf.FRAME2_SPLIT_OUTPUT_FILE, "a+") as split_out_file2:   
            with open(conf.FRAME2_OUTPUT_FILE, "r") as f2_file:     
                line = f2_file.readline()
                while (line):
                    if ">" in line:
                        if len(proteinSeq) > 3:
                            #print(proteinSeq)
                            split_out_file2.write(self._processProtein(proteinHeader, proteinSeq))
                            proteinSeq = ""
                        proteinHeader = line.strip("\n")  
                    else:
                        proteinSeq += line.strip("\n")
                    line = f2_file.readline()
                if len(proteinSeq) > 3:
                    #split_out_file.write(proteinSeq)
                    split_out_file2.write(self._processProtein(proteinHeader, proteinSeq))
                    proteinSeq = ""
        
        proteinHeader = ""
        proteinSeq = ""
        
        with open(conf.FRAME3_SPLIT_OUTPUT_FILE, "a+") as split_out_file3:   
            with open(conf.FRAME3_OUTPUT_FILE, "r") as f3_file:     
                line = f3_file.readline()
                while (line):
                    if ">" in line:
                        if len(proteinSeq) > 3:
                            #split_out_file.write(proteinSeq)
                            split_out_file3.write(self._processProtein(proteinHeader, proteinSeq))
                            proteinSeq = ""
                        proteinHeader = line.strip("\n")  
                    else:
                        proteinSeq += line.strip("\n")
                    line = f3_file.readline()
                if len(proteinSeq) > 3:
                    #split_out_file.write(proteinSeq)
                    split_out_file3.write(self._processProtein(proteinHeader, proteinSeq))
                    proteinSeq = ""
               
                
           
            
           
                                              
                
                
            


if __name__ == "__main__":
    
    #fHandler = fastaHandler()
    #fHandler.translate_dna_2_protein()
    #fHandler.split_peptides()
    pass