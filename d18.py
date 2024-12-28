from heapq import heappush,heappop

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_input():
	with open("d18.txt", "r") as file:
		lines =  [x for x in file.read().splitlines()]
		return  [(y[0], y[1]) for x in lines for y in x.split(",")]
        

def move_in_maze(maze,start,end,direction):
	
    # Input maze, start node, and goal node

    # Define frontier as a queue of tuples (c,(x,y)) "What haven't I explored yet"
    # Append start node to frontier and visited
    queue:list[tuple[int, tuple, tuple]] = [(0,start,direction)]

    # Define visited as a list
    visited = set()

    # While the frontier is not empty:
    while queue:
        # 	Dequeue the frontier and store the value in the selected node
        cost, position, direction = heappop(queue)
        print(cost, position, end, direction)
        # 	If the selected node is equal to the goal node, break from the loop, and return the cost at the goal.
        if position == end:
            print("we did it")
            return cost
        
        # If we've already vistied this point from this direction, skip.
        if (position, direction) in visited:
              continue
        
        # Add the selected node to visted
        visited.add((position, direction))
        
        # If not goal or in visited, find the neighbors.
        # Loop through the graph and find what is in every cardinal direction
        for dir in DIRS:
            if (dir[0] + direction[0], dir[1]+ direction[1]) != (0,0):
                nx, ny = position[0]+dir[0], position[1]+dir[1]
                #don't do this if dir is the opposite of direciton
                if maze[nx][ny] != "#":
                    if dir != direction:
                        marginal_cost = 1001
                    else:
                        marginal_cost = 1
                    # For each neighbor that is blank, compute the cost to get to it, and add it to the queue
                    heappush(queue, (cost + marginal_cost, (nx,ny), dir))
        # if we empty frontier, the maze is impossible

if __name__ == "__main__":
	input = get_input()
	print(input)