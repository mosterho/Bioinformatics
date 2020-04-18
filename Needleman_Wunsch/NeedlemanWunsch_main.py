##
## Main program that calls Needleman-Wunsch modules

import sys, NeedlemanWunsch_create_grid

def fct_do_this(cls_temp):
    ###
    cls_temp.fct_calculate_grid()
    cls_temp.fct_print_grid('Y')
    cls_temp.fct_grid_walkback()
    cls_temp.fct_print_grid('Y')
    print('\n\n')

####  mainline  ####
## first argument is  row, second argument is left column
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', 'ABCDE')
fct_do_this(cls_temp)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', 'ABCABC')
fct_do_this(cls_temp)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', '12345')
fct_do_this(cls_temp)
## Example in book
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ACTCG', 'ACAGTAG')
fct_do_this(cls_temp)
## flip the example in the book :-)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ACAGTAG', 'ACTCG')
fct_do_this(cls_temp)

cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ACTCGACAGTAGGTAGACTCGACAGACTC', 'ACAGTAGACTACAG')
fct_do_this(cls_temp)
