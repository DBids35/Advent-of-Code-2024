# Open the file and read line by line
with open("d1.txt", "r") as file:
    l1 = []
    l2 = []
    for line in file:
        # Split each line into two numbers and convert to integers
        col1, col2 = map(int, line.split())
        l1.append(col1)
        l2.append(col2)
sortedl1 = sorted(l1)
sortedl2 = sorted(l2)

diff = 0

for i in range(len(sortedl1)):
    diff += abs(sortedl1[i] - sortedl2[i])

# print(diff)
###############################
# Part 2
from collections import Counter

l2Counts = Counter(l2)

sim = 0

for num in l1:
    sim += num*l2Counts[num]
print(sim)