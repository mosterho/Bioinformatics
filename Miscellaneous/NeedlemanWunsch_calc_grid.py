###
# Needleman-Wunsch calculate grid
#

import sys, NeedlemanWunsch_create_grid

def fct_calculate_grid(arg_class_NW_grid):
    ## loop through the class's data for both sequences submitted
    ## assign scores based on Needleman-Wunsch algorith.
    ## match = 1
    ## mismatch = 0
    ## gap penalty = -1

    ## sequence of algorith:
    ## compare the two individual data points (nucleotide, AA, etc.)
    ## are they the same? set var to "T", otherise set var to "F"
    ## Now look at above, left and diagonal scores. Which is highest value?
    ##   (if diagonal is the highest, but same as upper or left, use diagonal) 
    ## set flag to "U", "L", "D"
    ## Use the following table to decide how to assign the scores
    ##
