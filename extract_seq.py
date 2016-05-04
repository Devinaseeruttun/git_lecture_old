

from import_fasta import *
from retrieve_slice import *
from import_gff import *
from export_seq import *

# User set parameters:

# Uncomment bellow
#gene_name = "Rv0024"




# Main part of the script


fasta_dict = import_fasta()


gff_coordinates = import_gff()


seq_slice =  retrieve_slice(fasta_dict, gff_coordinates, gene_name)

export_seq(seq_slice)


