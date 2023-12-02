to_replace = {
    "one" : "o1e",
    "two" : "t2o",
    "three" : "t3e",
    "four" : "f4r",
    "five" : "f5e",
    "six" : "s6x",
    "seven" : "s7n",
    "eight" : "e8t",
    "nine" : "n9e",
}
part1 = 0
with open("input.txt", "r") as file :
    for line in file.readlines() :
        num = ''
        current = ''
        for char in line :
            try : 
                int(char)
                current = char
                if num == '' : num = char
            except ValueError : ""
        part1 += int(num+current)
print(part1)

part2 = 0
with open("input.txt", "r") as file :
    for line in file.readlines() :
        for key in to_replace :
            line = line.replace(key, to_replace.get(key))
        num = ''
        current = ''
        for char in line :
            try : 
                int(char)
                current = char
                if num == '' : num = char
            except ValueError : ""
        part2 += int(num+current)
print(part2)