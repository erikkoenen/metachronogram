# metachronogram
building metachronograms by grafting ultrametric subtrees on a time-calibrated backbone tree

This repository contains the python script "graft_crown_clades.py", which can be used to create a large timescaled phylogeny by combining multiple densely sampled species-level phylogenies and a higher level backbone tree, as used by Ringelberg et al. (in prep.) "Precipitation is the main axis of tropical phylogenetic turnover across space and time". All in- and output files from that study are included as an example.

**Explanation and usage:**
    This script is intended to graft ultrametric subtrees into an ultrametric (time-calibrated)
    backbone phylogeny as a means to combine different phylogenetic datasets (e.g. grafting 
    Sanger-sequenced species level trees onto an NGS backbone) into a so-called meta-tree (sensu 
    Funk & Specht, 2007) or glomogram (sensu Marazzi et al., 2010), but since the procedure used 
    here is different and relies on ultrametric/dated trees, we refer to them as metachronograms. 
   
**Instructions:**
    Specify a file with a set of backbone trees in newick format and a tab-delimited text file 
    that specifies MRCAs (by stating two descendent terminal taxa to define the MRCA, separated 
    by a space) and paths to newick formatted files with subtrees. Note that the number of 
    backbone trees and subtrees in the specified files need to be equal. Hierarchical grafting 
    (i.e. grafting subtrees into subtrees in the backbone) is also possible, but make sure the 
    grafting order in as listed in the MRCA file is correct (going from least to most nested 
    subtree).

**Dependancies:**
    The Phyx toolkit (https://github.com/FePhyFoFum/phyx) needs to be installed and in your path.
    
    Example MRCA file: 
    MRCA1 = taxon1 taxon2	<path_to_subtree_newick1>
    MRCA2 = taxon3 taxon4 taxon5	<path_to_subtree_newick2>
    etc. 
    
    usage: python graft_trees.py <backbone_tree_file> <MRCA_subtree_file> <output>
    example: python graft_trees.py LPWG2017_BEAST.trees MRCA_file.txt Legume_glomograms.tre



**Files included in this repository:**

The folder **subclades** contains separate folders for each clade with all subtrees that are grafted onto the backbone, and the alignments and MrBayes execution files or BEAST xml files.

**MRCA_file** specifies for each clade which mrca needs to be pruned and replaced with the subtrees, and the file locations of these.

**graft_crown_clades.py** is the python script that carries out the grafting of subtrees onto a backbone tree.

**mimo_metachronograms100.tre** is the example output file of the script.

**mimo_metachronograms100.tre.relabeled** is the example output file but with tip labels of grafted subtrees relabeled with pxrlt (from the Phyx package).

**sd100_concat_FLC6.subsampled100.tre.relabeled** contains 100 time-calibrated backbone trees from a posterior sample of a BEAST analysis, onto which the subtrees are grafted.



**References:**

Funk VA, & CD Specht. (2007). Meta-trees: grafting for a global perspective. Proceedings of the Biological Society of Washington, 120(2), 232-240.

Marazzi B, & MJ Sanderson. (2010). Large‐scale patterns of diversification in the widespread legume genus Senna and the evolutionary role of extrafloral nectaries. Evolution: International Journal of Organic Evolution, 64(12), 3570-3592.

Ringelberg JJ, EJM Koenen, B Sauter, A Aebli, J Rando, JR Iganci, LPG Queiroz, DJ Murphy, M Gaudeul, A Bruneau, M Luckow, GP Lewis, J Miller, MF Simon, L Jordão, M Morales, O Loiseau, RT Pennington, KG Dexter, NE Zimmermann & CE Hughes (in prep.) Precipitation is the main axis of tropical phylogenetic turnover across space and time.
