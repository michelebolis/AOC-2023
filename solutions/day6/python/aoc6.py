def get_possibilities(time, record):
    possibilities = 0
    for off in range(time) :
        if off * (time - off) > record : possibilities +=1
    return possibilities

with open("input.txt", "r") as file : 
    times = [time for time in file.readline().split("Time:")[1].strip().split(" ") if time!=""]
    temp = ""
    for time in times : temp += time
    time_part2 = int(temp)
    times = [int(time) for time in times]

    records = [record for record in file.readline().split("Distance:")[1].strip().split(" ") if record!=""]
    temp = ""
    for record in records : temp += record
    record_part2 = int(temp)
    records = [int(record) for record in records]
    part1 = 1

    for i, time in enumerate(times) : part1 *= get_possibilities(time, records[i])
    
    print("part1:", part1)
    print("part2:", get_possibilities(time_part2, record_part2))
