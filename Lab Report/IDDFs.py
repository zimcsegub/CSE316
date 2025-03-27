class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.goalFound = False
        self.path = []

    def iterativeDeepening(self, grid, start, target):
        max_depth = len(grid) * len(grid[0])  
        for depth in range(max_depth):  
            self.goalFound = False
            self.depthLimitedSearch(grid, start, target, depth)
            if self.goalFound:
                print("Path found using IDDFS")
                print("Traversal Order:", self.path)
                return
        print("Path not found using IDDFS")

    def depthLimitedSearch(self, grid, start, target, maxDepth):
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        self.stack.append(start)
        self.path = []
        self.path.append(start)
        visited[start[0]][start[1]] = True

        depth = 0
        while self.stack:
            current = self.stack[-1]
            if current == target:
                self.goalFound = True
                return

            row, col = current
            found = False
            if depth < maxDepth:  # Only explore if the current depth is less than maxDepth
                for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and not visited[r][c] and grid[r][c] == 0:
                        visited[r][c] = True
                        self.stack.append((r, c))
                        self.path.append((r, c))
                        found = True
                        break

            if not found:  # Backtrack if no valid move is found
                self.stack.pop()
                self.path.pop()
                depth -= 1
            else:
                depth += 1

if __name__ == "__main__":
    try:
        # Case 1
        print("Enter maze size (rows, columns):")
        rows, cols = map(int, input().strip().split())

        print("Enter maze grid:")
        grid = [list(map(int, input().strip().split())) for _ in range(rows)]
        
        print("Enter start position (row, col):")
        start = tuple(map(int, input().strip().split()))
        
        print("Enter target position (row, col):")
        target = tuple(map(int, input().strip().split()))

        iterativeDeepening = IterativeDeepening()
        iterativeDeepening.iterativeDeepening(grid, start, target)

    except ValueError:
        print("Wrong Input format")
