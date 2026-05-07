steps = input()
grid = [[1,2],[3,4]]
for s in steps:
    if s == 'H':
        grid[0][1], grid[0][0] = grid[0][0], grid[0][1]
        grid[1][1], grid[1][0] = grid[1][0], grid[1][1]
    else:
        grid[0], grid[1] = grid[1], grid[0]

print("{} {}\n{} {}".format(*grid[0], *grid[1]))
