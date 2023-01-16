# Grid puzzle with obstacles with path tracking by Behrad Noorani (portfolio)
# Uses Breadth First Search

from collections import deque


def solve_puzzle(puzz, source, dest):
    ways = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    row = len(puzz)
    col = len(puzz[0])
    startx = source[0]
    starty = source[1]
    steps = [(startx, starty)]
    q = deque([(startx, starty, steps)])
    visited = []
    while q:
        x, y, step = q.popleft()
        if (x, y) in visited:
            continue
        if (x, y) == dest:
            strin = ''
            for i in range(len(step)-1):
                if step[i][0] < (step[i+1])[0]:
                    strin += 'D'
                if step[i][0] > (step[i+1])[0]:
                    strin += 'U'
                if step[i][1] < step[i+1][1]:
                    strin += 'R'
                if step[i][1] > step[i + 1][1]:
                    strin += 'L'
            return step, strin
        visited.append((x, y))
        for dx, dy in ways:
            nx = x + dx
            ny = y + dy
            nstep = step + [(nx, ny)]
            if 0 <= nx < row and 0 <= ny < col and puzz[x][y] != '#':
                q.append((nx, ny, nstep))
    return None



Puzzle = [
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['#', '-', '#', '#', '-'],
['-', '#', '-', '-', '-']
]

print(solve_puzzle(Puzzle, (0,2), (2,2)))