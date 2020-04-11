###
# Needleman/Wunsch calculator
#

import sys

class cls_NW_grid:
    def __init__(self, arg_aa1, arg_aa2):
        self.aa1 = arg_aa1
        self.aa2 = arg_aa2
        self.len_aa1 = len(self.aa1)
        self.len_aa2 = len(self.aa2)
        self.NW_grid = []  # row/column
        counter = 0
        ## Build a list of rows and place a list of columns within each row(index)
        for row in range(self.len_aa1 + 1):
            ## Fill the first row with the column negative counter
            ## Otherwise fill the remaining rows with zeros, except the first column
            if(row == 0):
                column = [-y for y in range(self.len_aa2 + 1)]
            else:
                column = [0 for y in range(self.len_aa2 + 1)] #fill the entire row with zeros, but...
                column[0] = -row   # now override just the first column with the negative row value/counter
            self.NW_grid.append(column)


cls_temp = cls_NW_grid('ATCG', 'ATCGATCG')
#print('print the entire grid')
#print(cls_temp.NW_grid)
print('Print individual grid value [0][2] (should result in -2)')
print(cls_temp.NW_grid[0][2])
print('Print grid as rows and columns')
for loop in range(cls_temp.len_aa1 + 1):
    print(loop, ' ', cls_temp.NW_grid[loop])
