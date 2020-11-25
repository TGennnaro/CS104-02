names = []
for x in range(0,10):
    name = input("Insert a name into the queue: ")
    names.append(name)

for x in range(0,len(names)):
    print("Next in queue: "+names.pop(0))
