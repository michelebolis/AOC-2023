from collections import defaultdict
from math import prod
from re import finditer

parts = defaultdict(list) # contains all the parts 
star = defaultdict(list) # contains only the parts of *
board = list(open('input.txt'))
chars = {(r, c) for r in range(len(board) - 1)
                for c in range(len(board) - 1)
                if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for m in finditer(r'\d+', row): # find the number of the row
        adjusts = {(r + x_offset, c + y_offset) 
                            for x_offset in (-1, 0, 1) 
                            for y_offset in (-1, 0, 1)
                            for c in range(*m.span())} # *m iterate over the matches span(begin, end)
        for c in adjusts & chars:  # iterate over all adjusts of numbers that are also chars
            parts[c].append(int(m[0])) 
            if board[c[0]][c[1]] == "*" : star[c].append(int(m[0]))

print("part1:", sum(sum(p) for p in parts.values()))
print("part2:", sum(prod(p) for p in star.values() if len(p)==2))