##
## Main program that calls Needleman-Wunsch modules

import sys, NeedlemanWunsch_create_grid

def fct_do_this(cls_temp):
    ###
    #print('Print empty grid as rows and columns')
    #cls_temp.fct_print_grid('Y')
    cls_temp.fct_calculate_grid()
    #print('Print the grid with assigned match/mismatch/gap penalties')
    #cls_temp.fct_print_grid('Y')
    cls_temp.fct_grid_walkback()
    #print('Print the completed grid')
    cls_temp.fct_print_grid('Y')

####  mainline  ####
## first argument is  row, second argument is left column
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', 'ABCDE')
fct_do_this(cls_temp)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', 'ABCABC')
fct_do_this(cls_temp)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ATCGAATCCCGTGATGCTGATGCTGGTGA', 'ATCGATCGTTCGATCGGTCAGCTA')
fct_do_this(cls_temp)
