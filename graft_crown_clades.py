''' This script is intended to graft ultrametric subtrees into an ultrametric (time-calibrated)
    backbone phylogeny as a means to combine different phylogenetic datasets (e.g. grafting 
    Sanger-sequenced species level trees onto an NGS backbone) into a so-called meta-tree (sensu 
    Funk & Specht, 2007) or glomogram (sensu Soltis et al., 2009), but since the procedure used 
    here is different and relies on ultrametric/dated trees, we refer to them as metachronograms. 
    
    Instructions:
    Specify a file with a set of backbone trees in newick format and a tab-delimited text file 
    that specifies MRCAs (by stating two descendent terminal taxa to define the MRCA, separated 
    by a space) and paths to newick formatted files with subtrees. Note that the number of 
    backbone trees and subtrees in the specified files need to be equal. Hierarchical grafting 
    (i.e. grafting subtrees into subtrees in the backbone) is also possible, but make sure the 
    grafting order in as listed in the MRCA file is correct (going from least to most nested 
    subtree).

    The Phyx toolkit (https://github.com/FePhyFoFum/phyx) needs to be installed and in your path.
    
    Example MRCA file: 
    MRCA1 = taxon1 taxon2	<path_to_subtree_newick1>
    MRCA2 = taxon3 taxon4 taxon5	<path_to_subtree_newick2>
    etc. 
    
    usage: python graft_trees.py <backbone_tree_file> <MRCA_subtree_file> output
    example: python graft_trees.py sd100_concat_FLC6.subsampled100.tre.relabeled MRCA_file mimo_metachronograms100.tre'''

import subprocess
import sys

### define functions ###

def pxt2new():
	newtree = subprocess.Popen(['pxt2new', '-t', 'TREE'], stdout=subprocess.PIPE)
	output_newtree = newtree.stdout.read()
	return output_newtree

def mrcacut():
	cuttree = subprocess.Popen(['pxmrcacut', '-t', 'TREE', '-m', 'MRCA'], stdout=subprocess.PIPE)
	output_cuttree = cuttree.stdout.read()
	return output_cuttree 

def get_node_depth():
	depth = subprocess.Popen(['pxlstr', '-t', 'CUTTREE', '-a'], stdout=subprocess.PIPE)
	output_depth = depth.stdout.read()
	return output_depth

def subtree_rescale(node_depth):
	scale_tree = subprocess.Popen(['pxtscale', '-t', 'SUBTREE', '-r', node_depth], stdout=subprocess.PIPE)
	output_scale_tree = scale_tree.stdout.read()
	return output_scale_tree

### start script ###

# read in the backbone phylogenies
backbone_newick = sys.argv[1]
with open(backbone_newick) as f:
	backbone_trees = f.read().splitlines()

print("Backbone tree file contains " + str(len(backbone_trees)) + " trees")

# read in a MRCAs and subtrees into a list
mrca_subtree_file = sys.argv[2]
with open(mrca_subtree_file) as f:
	mrcas_subtrees = f.read().splitlines()
for i in range(len(mrcas_subtrees)):
	mrcas_subtrees[i] = mrcas_subtrees[i].split('\t')
	with open(mrcas_subtrees[i][1]) as f:
		mrcas_subtrees[i][1] = f.read().splitlines()

print(str(len(mrcas_subtrees)) + " subtrees to graft")

# loop through the trees, cut out mrcas, rescale and graft subtrees	
outfile = open(sys.argv[3], 'w')
for i in range(len(backbone_trees)):
	glomogram = backbone_trees[i]
	print("Processing tree " + str(i+1))
	for j in range(len(mrcas_subtrees)):
		tree = open('TREE', 'w')
		tree.write(glomogram)
		tree.close()
# this is needed to reformat newick with pxt2new to make sure branch lengths are compatible with phyx
		glomogram = pxt2new()
		tree = open('TREE', 'w')
		tree.write(glomogram)
		tree.close()
		print(mrcas_subtrees[j][0])
		mrca = open('MRCA', 'w')
		mrca.write(mrcas_subtrees[j][0])
		mrca.close()
		cuttree = mrcacut()
		cuttree_file = open('CUTTREE', 'w')
		cuttree_file.write(cuttree)
		cuttree_file.close()
		node_depth = get_node_depth()
		print("age of mrca: " + node_depth)
		subtree = open('SUBTREE', 'w')
		subtree.write(mrcas_subtrees[j][1][i])
		subtree.close()
		rescaled_subtree = subtree_rescale(node_depth)
		glomogram = glomogram.replace(cuttree.rstrip(';\n'),rescaled_subtree.rstrip(';\n'))
	outfile.write(glomogram + "\n")
	
outfile.close()
	
print("Done, enjoy your grafted metachronograms!")	
	
	
