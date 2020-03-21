##

#import sys
import re

'''
search_this = '>gi|53828740|ref|NP_001005484.1| olfactory receptor 4F5 [Homo sapiens]'
print(search_this)
wrk_fieldbreak  = re.findall('(?<=[|]).+(?=[|])', search_this, re.DOTALL)
print('fieldbreak: ', wrk_fieldbreak)
wrk_fieldbreak  = re.findall('([^|]*)$', search_this)
print('fieldbreak: ', wrk_fieldbreak)
wrk_fieldbreak  = re.findall('(\w)', search_this)
print('fieldbreak: ', wrk_fieldbreak)
wrk_fieldbreak  = search_this.split('|')
print('fieldbreak: ', wrk_fieldbreak)

search_this = '>NP_000005.2 alpha-2-macroglobulin isoform a precursor [Homo sapiens]'
wrk_fieldbreak  = re.findall(r'(?<=[>])\w+', search_this)
print('fieldbreak2: ', wrk_fieldbreak)
wrk_fieldbreak  = re.findall(r'(?<=[>])\w+[.]\n', search_this)
print('fieldbreak2: ', wrk_fieldbreak)
wrk_fieldbreak  = re.findall(r'(?<=[.])(?<=[1-9])*.+$', search_this)
print('fieldbreak2: ', wrk_fieldbreak)
'''

search_this = '>NP_000005.2 alpha-2-macroglobulin isoform a precursor [Homo sapiens]\nNNNN\nNNNN\nNNNN\n>NP_000005.9 alpha-2-macroglobulin isoform a precursor [Homo sapiens]\nNNNN\nNNNN\nNNNN'
#wrk_fieldbreak  = re.findall(r'[>].+(?=[>])?', search_this, re.DOTALL)
wrk_fieldbreak = search_this.split('>')
print('fieldbreak3: ', wrk_fieldbreak)
for i in wrk_fieldbreak:
    print('fieldbreak3 acc#: ', re.findall('\w', i))

#>gi|53828740|ref|NP_001005484.1| olfactory receptor 4F5 [Homo sapiens]
#>gi|1034563939|ref|XP_016858498.1| PREDICTED: uncharacterized protein LOC102725121 isoform X1 [Homo sapiens]
#>gi|767901762|ref|XP_011542108.1| PREDICTED: uncharacterized protein LOC102725121 isoform X1 [Homo sapiens]
#>gi|767901764|ref|XP_011542109.1| PREDICTED: uncharacterized protein LOC102725121 isoform X1 [Homo sapiens]
#>gi|767901766|ref|XP_011542110.1| PREDICTED: uncharacterized protein LOC102725121 isoform X1 [Homo sapiens]
#>gi|1034563943|ref|XP_016858499.1| PREDICTED: putative ATP-dependent RNA helicase DDX12 isoform X2 [Homo sapiens]
#>gi|119943152|ref|NP_001005221.2| olfactory receptor 4F3/4F16/4F29 [Homo sapiens]
#>gi|767908050|ref|XP_011540840.1| PREDICTED: proline-rich extensin-like protein EPR1 isoform X1 [Homo sapiens]

#b'>NC_000001.11 Homo sapiens chromosome 1, GRCh38.p13 Primary Assembly\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN\nNNNNNNN'
