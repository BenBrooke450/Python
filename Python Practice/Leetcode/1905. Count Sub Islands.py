




def countSubIslands(grid1: list[list[int]], grid2: list[list[int]]) -> int:

    rows, cols = len(grid1), len(grid1[0])
    visited = set()
    visited2 = set()
    g1 = set()
    g2 = set()

    def dfs1(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid1[r][c] == 0 or (r, c) in visited):
            return

        visited.add((r, c))
        g1.add((r, c))

        # Explore in all 4 directions
        dfs1(r+1, c)
        dfs1(r-1, c)
        dfs1(r, c+1)
        dfs1(r, c-1)

    def dfs2(r, c):

        if (r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0 or (r, c) in visited2):
            return

        visited2.add((r, c))
        g2.add((r, c))

        # Explore in all 4 directions
        dfs2(r + 1, c)
        dfs2(r - 1, c)
        dfs2(r, c + 1)
        dfs2(r, c - 1)


    count = 0

    for r in range(rows):
        for c in range(cols):
            print((r,c))
            if grid2[r][c] == 1 and (r, c) not in visited2:

                dfs1(r, c)
                dfs2(r, c)

                print("G1:",g1,"    G2:",g2,"    Visted:",visited,"    Visted2:",visited2, count)

                if all(i in visited for i in g2):
                    count += 1

                g1 = set()
                g2 = set()

    return count


print(countSubIslands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))

