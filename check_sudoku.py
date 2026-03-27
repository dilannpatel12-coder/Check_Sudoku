
def check_column(column, slist):
    sudoku = True
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in slist:
        if i[column] not in nums:
            sudoku = False
        else:
            nums.pop(nums.index(i[column]))
        
    return sudoku
                                                                                             
def check_row(row, slist):                                                                                             
    sudoku = True                                                                                                                                                    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                                                                                                                                       


    for i in slist[row]:
        if i in nums:
            nums.pop(nums.index(i))
        else:
            sudoku = False

                                                                                                                                                           
    return sudoku                                                                                                                                                       
                                                                                                                                                   
def check_boxes(slist):
    sudoku = True
                                                                                                                                                          
    boxes = [
        [slist[0][0], slist[0][1], slist[0][2], slist[1][0], slist[1][1], slist[1][2], slist[2][0], slist[2][1], slist[2][2]],
        [slist[0][3], slist[0][4], slist[0][5], slist[1][3], slist[1][4], slist[1][5], slist[2][3], slist[2][4], slist[2][5]],
        [slist[0][6], slist[0][7], slist[0][8], slist[1][6], slist[1][7], slist[1][8], slist[2][6], slist[2][7], slist[2][8]],
        [slist[3][0], slist[3][1], slist[3][2], slist[4][0], slist[4][1], slist[4][2], slist[5][0], slist[5][1], slist[5][2]],
        [slist[3][3], slist[3][4], slist[3][5], slist[4][3], slist[4][4], slist[4][5], slist[5][3], slist[5][4], slist[5][5]],
        [slist[3][6], slist[3][7], slist[3][8], slist[4][6], slist[4][7], slist[4][8], slist[5][6], slist[5][7], slist[5][8]],
        [slist[6][0], slist[6][1], slist[6][2], slist[7][0], slist[7][1], slist[7][2], slist[8][0], slist[8][1], slist[8][2]],
        [slist[6][3], slist[6][4], slist[6][5], slist[7][3], slist[7][4], slist[7][5], slist[8][3], slist[8][4], slist[8][5]],
        [slist[6][6], slist[6][7], slist[6][8], slist[7][6], slist[7][7], slist[7][8], slist[8][6], slist[8][7], slist[8][8]]]
    for i in boxes:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for l in i:
            if l in nums:
                nums.pop(nums.index(l))
            else:
                sudoku = False
        
    
    return sudoku

def check_sudoku(slist):
    sudoku = True
    for x in range(9):
        y = check_column(x, slist)
        sudoku = sudoku and y
    
    for x in range(9):
        y = check_row(x, slist)
        sudoku = sudoku and y
    
    y = check_boxes(slist)

    return sudoku and y

print(check_sudoku([
    [5, 3, 4,   6, 7, 8,   9, 1, 2], 
    [6, 7, 2,   1, 9, 5,   3, 4, 8],
    [1, 9, 8,   3, 4, 2,   5, 6, 7],
      
    [8, 5, 9,   7, 6, 1,   4, 2, 3],
    [4, 2, 6,   8, 5, 3,   7, 9, 1],
    [7, 1, 3,   9, 2, 4,   8, 5, 6],
        
    [9, 6, 1,   5, 3, 7,   2, 8, 4],
    [2, 8, 7,   4, 1, 9,   6, 3, 5],
    [3, 4, 5,   2, 8, 6,   1, 7, 9]
]))   