from collections import defaultdict

def get_input():
	with open("d23.txt", "r") as file:
		return [tuple(x.split("-")) for x in file.read().splitlines()]

def p1(input):
	# 1) Build adjacency dict
	adj = defaultdict(set)
	for (a, b) in input:
		adj[a].add(b)
		adj[b].add(a)

	seen_triangles = set()
	t_triangles = 0
	for (a, b) in input:
		# Common neighbors of a and b
		common_neighbors = adj[a].intersection(adj[b])
		for c in common_neighbors:
			# Sort the triple to avoid duplicates
			tri = tuple(sorted([a, b, c]))
			if tri not in seen_triangles:
				seen_triangles.add(tri)
				if a[0] == "t" or b[0]=="t" or c[0] == "t":
					t_triangles += 1
	return t_triangles
	


if __name__ == "__main__":
	input = get_input()

	print(p1(input))
