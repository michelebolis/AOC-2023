from collections import defaultdict
mappe = defaultdict(list)
with open("input.txt", "r") as file :
    seeds = [int(seed) for seed in file.readline().strip().split(": ")[1].split(" ")]
    file.readline()
    newMap = True
    mappa_key = ""
    mappa_value = ""
    for line in file.readlines() : 
        if newMap :
            splitted = line.strip().split(" map:")[0].split("-to-")
            mappa_key = splitted[0]
            mappa_value = splitted[1]
            newMap = False
            mappa = defaultdict(int)
        elif(line=="\n") :
            newMap = True
            mappe[mappa_key+"-to-"+mappa_value] = mappa 
        else :
            [destination, source, offset] = line.strip().split(" ")
            mappa[int(source)] = [int(destination), int(offset)]
    mappe[mappa_key+"-to-"+mappa_value] = mappa 
pos = []

def get(mappa, key) :
    for source in mappa :
        [destination, offset] = mappa[source]
        #print(key, destination, source, offset)
        if source+offset >= key and key>=source:
            return [key+(destination-source), key-(source+offset)]
    return [key, 1] 
conversions = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
def getPosition(mappe, seeds) : 
    lastmin = float('inf')
    for seed in seeds : 
        temp = seed
        for conversion in conversions :
            temp = get(mappe[conversion], temp)[0]
        lastmin = min(temp, lastmin)
    return lastmin
print("parte1", getPosition(mappe, seeds))

lastseed=-1
newseeds = []
for seed in seeds : 
    if lastseed == -1 : 
        lastseed = seed
        continue
    newseeds.append([lastseed, seed])
    lastseed = -1

lastmin = float('inf')
for seed in newseeds :
    print(seed)
    seedToAnalyze = seed[0]
    while seedToAnalyze < seed[0] + seed[1] :
        temp = seedToAnalyze
        for conversion in conversions :
            [temp, offset] = get(mappe[conversion], temp)
        if temp < lastmin : 
            lastmin = temp 
            seedToAnalyze +=1
        else :
            seedToAnalyze += offset
print(lastmin)