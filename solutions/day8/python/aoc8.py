from math import lcm


file = open("input.txt", "r")
commands = [c  for c in (file.readline().strip())]
file.readline()
mappa = {}

for line in file.readlines() : 
    [s, destination] = line.strip().split(" = ")
    [L, R] = destination.split(", ")
    mappa[s] = [L[1:], R[:3]]

def trip(source, end):
    indexCommand = 0
    steps = 0
    while not source.endswith(end):
        source = mappa[source][0] if commands[indexCommand] == 'L' else mappa[source][1]
        steps += 1
        indexCommand += 1
        if indexCommand == len(commands): indexCommand = 0
    return steps

starts = [start for start in mappa if start.endswith('A')]
part2 = 1
for start in starts:
    part2 = lcm(part2, trip(start, 'Z'))
    
print("part1 :", trip("AAA", "ZZZ"))
print("part2 :", part2)