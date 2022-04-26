# metachronogram
building metachronograms by grafting ultrametric subtrees on a time-calibrated backbone tree

This repository contains the python script "graft_crown_clades.py", which can be used to create a large timescaled phylogeny by combining multiple densely sampled species-level phylogenies and a higher level backbone tree, as used by Ringelberg et al. (in prep.) "Precipitation is the main axis of tropical phylogenetic turnover across space and time". All in- and output files from that study are included as an example.

**explanation and usage:**
    This script is intended to graft ultrametric subtrees into an ultrametric (time-calibrated)
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
    
    usage: python graft_trees.py <backbone_tree_file> <MRCA_subtree_file> <output>
    example: python graft_trees.py LPWG2017_BEAST.trees MRCA_file.txt Legume_glomograms.tre
