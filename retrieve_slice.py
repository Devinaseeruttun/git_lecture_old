# Uncomment the lines bellow

def retrieve_slice(fasta_obj, gff_dict, gene_name):
	print "return a slice of a fasta file"
	return fasta_obj[gff_dict[gene_name][0]:gff_dict[gene_name][1]]
