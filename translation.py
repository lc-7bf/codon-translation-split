
import csv
import config as conf


class transcode:
    
    
    
    def nucleotides3FramesToAAs(nucleotides :str):
        '''
        Use codon map to convert from nucleotides to aminoacids
        Returns protein string or zero-length string on error
        Uses X for stop codons
        '''
        translated = dict()
        nucleotides = nucleotides.replace('T','U')
        with open(conf.CODING_FILE, "r") as codings:
            line = codings.readline().split(",")
            while line:
                if (len(line) == 2):
                    translated[line[0]] = line[1].strip("\n") 
                    line = codings.readline().split(",")
                else:
                    break
        #print ("Translation dictionary loaded...\nStarting codon translation in 3 frames...")
        
        protein_frame_1 = []
        protein_frame_2 = []
        protein_frame_3 = []
        
        for codon in range(0,len(nucleotides),3):
            if len(nucleotides) >= codon + 3 :
                frame1 = nucleotides[codon : codon + 3]
                if (frame1 in translated.keys()):
                    aa1 = translated[frame1]
                else:
                    print ("Degenerate Frame 1 Codon: " + frame1 + " could not be translated to an AA: introducing X")
                    aa1 = "X"  
                if len(protein_frame_1) % 80 == 0:
                    protein_frame_1.append('\n')
                protein_frame_1.append(aa1)
                #print ("F1: " + nucleotides[codon : codon + 3] + " -> " + aa1)
            
            if len(nucleotides) >= codon + 4 :
                frame2 = nucleotides[codon + 1 : codon + 4]
                if (frame2 in translated.keys()):
                    aa2 = translated[frame2]
                else:
                    print ("Degenerate Frame 2 Codon: " + frame2 + " could not be translated to an AA: introducing X")
                    aa2 = "X"
                if len(protein_frame_2) % 80 == 0:
                    protein_frame_2.append('\n')
                protein_frame_2.append(aa2)
                #print ("F2: " + nucleotides[codon + 1 : codon + 4] + " -> " + aa2)
            
            if len(nucleotides) >= codon + 5 : 
                frame3 = nucleotides[codon + 2 : codon + 5]
                if (frame3 in translated.keys()):
                    aa3= translated[frame3]
                else:
                    print ("Degenerate Frame 3 Codon: " + frame3 + " could not be translated to an AA: introducing X")
                    aa3 = "X"
                if len(protein_frame_3) % 80 == 0:
                    protein_frame_3.append('\n')
                protein_frame_3.append(aa3)      
                #print ("F3: " + nucleotides[codon + 2 : codon + 5] + " -> " + aa3)
            
        #print ("Done. Translated in 3 frames...")


        return [''.join(protein_frame_1),''.join(protein_frame_2),''.join(protein_frame_3)]












if __name__ == "__main__":
    #print(transcode.nucleotides3FramesToAAs("ATGAGGGCCACTAGG"))
    pass