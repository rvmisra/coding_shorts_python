# coding_shorts_python
USE AT OWN RISK
Python scripts to do quick and dirty parsing. 
These scripts a far from optimised and generate lots of temp files -for debugging purposes.
Later versions will be more pythonic and cleaner....


Each script parses a distinct dataset from a pacbio modifications gff.

Attached is a test gff file (196_test.gff)

To run (chmod 775 script)

./scriptxxxxx.py <input_file> > <output_file>

e.g. Methylation_no_motifs.py
./Methylation_no_motifs.py 196_test.gff > 196_5000bins.txt

or print to screen
./Methylation_no_motifs.py 196_test.gff

It creates a couple of temp files, which can be removed, but helps with troubleshooting as the gff files weren't all consistent with there formating?!
