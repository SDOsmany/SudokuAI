src_filename = 'sudoku_boards_solved.txt'
srcfile = open(src_filename, "r")
sudoku_list = srcfile.read().split("\n")

outputfile = 'output.txt'
srcfile = open(outputfile, "r")
output_list = srcfile.read().split("\n")
for i, x in enumerate(output_list):
    print(sudoku_list[i],"\n" + output_list[i]+"\n")

