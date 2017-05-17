# coding_shorts_python
Python scripts to do quick and dirty parsing 
Each script parses a distinct dataset from a pacbio modifications gff.
Attached is a test gff file (196_test.gff)
To run (chmod 775 script)
./scriptxxxxx.py <input_file> > <output_file>
e.g. Methylation_no_motifs.py
./Methylation_no_motifs.py 196_test.gff > 196_5000bins.txt
or print to screen
./Methylation_no_motifs.py 196_test.gff

It creates a couple of temp files, which can be removed, but helps with troubleshooting as the gff files weren't all consistent with there formating?!
