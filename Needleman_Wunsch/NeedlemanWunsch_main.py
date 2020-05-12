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
## first try to trick loop in calculate grid
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('A', 'A')
fct_do_this(cls_temp)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('A', 'B')
fct_do_this(cls_temp)

cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', 'ABC')
fct_do_this(cls_temp)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', 'ABCDE')
fct_do_this(cls_temp)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', 'ABCABC')
fct_do_this(cls_temp)
#cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', 'CBA')
#fct_do_this(cls_temp)
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ABC', '12345')
fct_do_this(cls_temp)

## Example in book
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ACTCG', 'ACAGTAG')
fct_do_this(cls_temp)

# some random sequence I created
cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('ACTCGACAGTAGGTAGACTCGACAGACTC', 'ACAGTAGACTAGTAGGTAGACTCAG')
fct_do_this(cls_temp)

## something real from NP_000007.1 and NP_00008.1
#cls_temp = NeedlemanWunsch_create_grid.cls_NW_grid('MAAGFGRCCRVLRSISRFHWRSQHTKANRQREPGLGFSFEFTEQQKEFQATARKFAREEIIPVAAEYDKTGEYPVPLIRRAWELGLMNTHIPENCGGLGLGTFDACLISEELAYGCTGVQTAIEGNSLGQMPIIIAGNDQQKKKYLGRMTEEPLMCAYCVTEPGAGSDVAGIKTKAEKKGDEYIINGQKMWITNGGKANWYFLLARSDPDPKAPANKAFTGFIVEADTPGIQIGRKELNMGQRCSDTRGIVFEDVKVPKENVLIGDGAGFKVAMGAFDKTRPVVAAGAVGLAQRALDEATKYALERKTFGKLLVEHQAISFMLAEMAMKVELARMSYQRAAWEVDSGRRNTYYASIAKAFAGDIANQLATDAVQILGGNGFNTEYPVEKLMRDAKIYQIYEGTSQIQRLIVAREHIDKYKN', 'MAAALLARASGPARRALCPRAWRQLHTIYQSVELPETHQMLLQTCRDFAEKELFPIAAQVDKEHLFPAAQVKKMGGLGLLAMDVPEELGGAGLDYLAYAIAMEEISRGCASTGVIMSVNNSLYLGPILKFGSKEQKQAWVTPFTSGDKIGCFALSEPGNGSDAGAASTTARAEGDSWVLNGTKAWITNAWEASAAVVFASTDRALQNKGISAFLVPMPTPGLTLGKKEDKLGIRGSSTANLIFEDCRIPKDSILGEPGMGFKIAMQTLDMGRIGIASQALGIAQTALDCAVNYAENRMAFGAPLTKLQVIQFKLADMALALESARLLTWRAAMLKDNKKPFIKEAAMAKLAASEAATAISHQAIQILGGMGYVTEMPAERHYRDARITEIYEGTSEIQRLVIAGHLLRSYRS')
#fct_do_this(cls_temp)
