limits = {"red" : 12, "green": 13, "blue" : 14 }
part1 = 0
with open("input.txt", "r") as file :
   for line in file.readlines() :
      skip = False
      part = line.split(":")
      gameIndex = int((part[0].split(" "))[1])
      sequences = part[1].split(";")
      for seq in sequences :
         items = seq.split(",")
         for item in items :
            item_parts = item.split(" ")
            num = int(item_parts[1])
            label = item_parts[2].replace("\n", "")
            if limits.get(label) < num : 
               skip = True
               break
      if not skip : part1 += gameIndex
print(part1)

part2 = 0
with open("input2.txt", "r") as file :
   for line in file.readlines() :
      maxRed = 0
      maxGreen = 0
      maxBlue = 0
      skip = False
      part = line.split(":")
      gameIndex = int((part[0].split(" "))[1])
      sequences = part[1].split(";")
      for seq in sequences :
         items = seq.split(",")
         for item in items :
            item_parts = item.split(" ")
            num = int(item_parts[1])
            label = item_parts[2].replace("\n", "")
            if(label == "green") and num > maxGreen : maxGreen = num
            if(label == "blue") and num > maxBlue : maxBlue = num
            if(label == "red") and num > maxRed : maxRed = num
      gamePower = maxRed * maxGreen * maxBlue
      part2 += gamePower
print(part2)