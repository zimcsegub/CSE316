import random

class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [0, 0, 1, -1]  
        self.y_move = [1, -1, 0, 0]
        self.found = False
        self.goal = None
        self.source = None
        self.path = [] 
        self.topological_order = []
        self.generate_grid()

    def generate_grid(self):
        self.N = random.randint(4, 7)
        self.grid = [[random.choice([0, 1]) for _ in range(self.N)] for _ in range(self.N)]
        
        while True:
            source_x, source_y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            goal_x, goal_y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            
            if (source_x, source_y) != (goal_x, goal_y) and self.grid[source_x][source_y] == 1 and self.grid[goal_x][goal_y] == 1:
                break  

        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, float('inf'))
        self.visited = [[False] * self.N for _ in range(self.N)]

        print(f"\nGrid Size: {self.N}x{self.N}")
        print("Generated Grid:")
        for row in self.grid:
            print(row)

        print(f"\nSource: ({source_x}, {source_y})")
        print(f"Goal: ({goal_x}, {goal_y})\n")

        self.dfs(self.source, [])

        if self.found:
            print("\nGoal found")
            print(f"Number of moves required = {self.goal.depth}")
            print("Path from source to destination:")
            for step in self.path:
                print(step)
        else:
            print("Goal cannot be reached from the starting block")
        
        print("\nTopological Order of Traversal:")
        for node in self.topological_order:
            print(node)

    def dfs(self, node, current_path):
        current_path.append((node.x, node.y))
        self.topological_order.append((node.x, node.y))
        
        if node.x == self.goal.x and node.y == self.goal.y:
            self.found = True
            self.goal.depth = node.depth
            self.path = current_path[:]
            return

        self.visited[node.x][node.y] = True

        for j in range(self.directions):
            v_x = node.x + self.x_move[j]
            v_y = node.y + self.y_move[j]

            if 0 <= v_x < self.N and 0 <= v_y < self.N and self.grid[v_x][v_y] == 1 and not self.visited[v_x][v_y]:
                child = Node(v_x, v_y, node.depth + 1)
                self.dfs(child, current_path)
                if self.found:
                    return 
        
        self.visited[node.x][node.y] = False
        current_path.pop()

class DFS_2D:
    def __init__(self):
        DFS()

if __name__ == "__main__":
    DFS_2D()
