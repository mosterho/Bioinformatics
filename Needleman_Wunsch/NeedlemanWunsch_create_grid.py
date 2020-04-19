###
# Needleman/Wunsch calculator - Build an empty grid based on
# lengths of both arguments passed in, but
# load the first row and column with negative numbers
#

from operator import itemgetter, attrgetter  # use for "sorted()"
import sys

class cls_NW_grid:
    def __init__(self, arg_aa1, arg_aa2):
        ## __init__ will build an empty grid of zeros based on row/column length
        self.aa1 = arg_aa1
        self.aa2 = arg_aa2
        self.len_aa1 = len(self.aa1)
        self.len_aa2 = len(self.aa2)
        self.NW_grid = []  # row/column
        counter = 0
        ## Build a list of rows and place a list of columns within each row(index)
        for row in range(self.len_aa2 + 1):
            ## Fill the first row with the column negative counter
            ## Fill the remaining rows with zeros, except the first column which has a negative counter
            if(row == 0):
                column = [-y for y in range(self.len_aa1 + 1)]
            else:
                column = [0 for y in range(self.len_aa1 + 1)] #fill the entire row with zeros, but...
                column[0] = -row   # now override the first column with the negative row value/counter
            self.NW_grid.append(column)

    def fct_calculate_grid(self):
        # Needleman-Wunsch calculate grid
        # See "Fundmental Concepts of Bioinformatics" book by Dan E. Krane
        # assigned by Dr. Bagga for Bioinformatics I class
        # pages 41-45 for Needleman-Wunsch algorithm
        #
        ## Begin row/column testing and calculations
        for current_row in range(1, self.len_aa2 + 1):
            for current_column in range(1, self.len_aa1 + 1):
                ## obtain left, diagonal, and upper values adjacent to current position
                left_value = self.NW_grid[current_row][current_column - 1]
                diagonal_value = self.NW_grid[current_row - 1][current_column - 1]
                top_value = self.NW_grid[current_row - 1][current_column]
                ## compare current value of individual string location's nucleotides/AA to be compared, are they equal?
                ## (note the use of ""- 1", because of the difference in using grid column/row versus data position)
                if(self.aa1[current_column - 1] == self.aa2[current_row - 1]):
                    aa_equivalent = True
                else:
                    aa_equivalent = False
                ## calculate "what if" numbers based match/mismatch/gap possibilities
                tmp_value = left_value - 1
                if(top_value -1 > tmp_value):
                    tmp_value = top_value - 1
                if((diagonal_value + 1 > tmp_value and aa_equivalent) or (diagonal_value > tmp_value and not aa_equivalent)):
                    if(aa_equivalent):
                        tmp_value = diagonal_value + 1
                    else:
                        tmp_value = diagonal_value
                #print('current_row:', current_row, 'current_column:', current_column, 'left_value:',  left_value, 'diagonal_value:', diagonal_value, 'top_value:', top_value, 'final value:', tmp_value)
                self.NW_grid[current_row][current_column] = tmp_value

    def fct_grid_walkback(self):
        ## perform the reverse of loading the grid with match/mismatch/gap numbers
        ## to find the best possible match
        #
        # set far-right/lower row column positions in grid
        row = self.len_aa2
        column = self.len_aa1
        # print far-right/lower row column positions to start before loop
        print('row:', row, 'column:', column, 'value:', self.NW_grid[row][column], ' ', end='')
        self.NW_grid[row][column] = 'X'
        while(row > 1 or column > 1):
            # determine if left, diagonal or upper grid values have the highest values
            ## Place grid values and their positions in a temporary list,
            ## then sort the list by value (descending) then position (in case of a tie with value).
            list_grid = [(self.NW_grid[row-1][column-1], 'diagonal'), (self.NW_grid[row-1][column], 'up'), (self.NW_grid[row][column-1], 'left')]
            sorted_LG = sorted(list_grid, key=itemgetter(0), reverse=True)
            sorted(sorted_LG, key=itemgetter(1))
            ## Test values, try to go diagonal first, then either up or left
            ## if current AA values match, just use "diagonal" regardless of sorted value
            if(self.aa1[column - 1] == self.aa2[row - 1] and row >= 2 and column >= 2):
                tmp_direction = 'diagonal'
            elif(sorted_LG[0][1] == 'diagonal' and row >= 2 and column >= 2):
                tmp_direction = 'diagonal'
            elif(sorted_LG[0][1] == 'up' and row >= 2):
                tmp_direction = 'up'
            elif(sorted_LG[0][1] == 'left' and column >= 2):
                tmp_direction = 'left'
            # print direction of current grid position as relates to
            # the calculated next grid position
            print('Direction:', tmp_direction)
            self.NW_grid[row][column] = 'X'
            if(tmp_direction == 'diagonal'):
                row -= 1
                column -= 1
            elif(tmp_direction == 'up'):
                row -= 1
            else:
                column -= 1
            print('row:', row, 'column:', column, 'value:', self.NW_grid[row][column], ' ', end='')
        self.NW_grid[row][column] = 'X'
        print('Direction:', 'complete')


    def fct_print_grid(self, arg_print_full_grid):
        ## print the grid, along with both AA values
        print('Print the grid, along with both AA values')
        width = len(str(self.len_aa2)) + 2  ## picked +2 just for aesthetics
        for row in range(self.len_aa2 + 1):
            ## print column first, then...
            if(row == 0):
                print('{0:>{width}}'.format(' ', width=width), end='')  #
                print('{0:>{width}}'.format(' ', width=width), end='')  #
                for column in range(self.len_aa1):
                    print('{0:>{width}}'.format(self.aa1[column], width=width), end='')
                print(' ', end='\n')
            ## ... print grid values
            for column in range(self.len_aa1 + 1):
                if(column == 0):
                    if(row < 1):
                        print('{0:>{width}}'.format(' ', width=width), end='')  # allows print blank column
                    else:
                        print('{0:>{width}}'.format(self.aa2[row - 1], width=width), end='')
                print('{0:>{width}}'.format(self.NW_grid[row][column], width=width), end='')
            print(' ', end='\n')
