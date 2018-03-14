class Process ():
    def __init__(self, allocated, max, name):
        self.allocated = allocated
        self.max = max
        self.name = name
    
    #determines how many resources are available to the process
    def maxResources (self, free):
        ret = []
        for i in range(0, len(free)):
            ret.append(self.allocated[i]+free[i])
        return ret
    
    #checks if a process is being given enough resources
    def cleared (self, avail):
        for i in range(0,len(avail)):
            if (self.max[i] > avail[i]):
                return False
        return True
    
def convertList (lst):
    
    ret = []
    
    for i in lst:
        ret.append(int(i))
        
    return ret
   
reader = open("input.txt", "r")
text = reader.read().split("\n") #seperate the input

#remove the brackets
for index in range(0,len(text)): 
    text[index] = text[index][1:len(text[index])-1]

free = convertList(text[0].split(" "))
allProcesses = []

#set up processes
for index in range(1,len(text)):
    cur = convertList(text[index].split(" "))
    toAdd = Process(cur[0:len(free)], cur[len(free):], "P"+str(index-1))
    allProcesses.append(toAdd)

#we want to check if the process are continually being performed.  if not, we do not have proper resources allocated
prev_size = len(allProcesses)+1

to_rem = []

#Assumptions made: a process will complete as soon as it receives the resources it needs.  therefore we can simply remove that process are reallocate its resources
while (prev_size != len(allProcesses)):
    prev_size = len(allProcesses)
    for index in range(0,len(allProcesses)):
        
        resc = allProcesses[index].maxResources(free)
        if (allProcesses[index].cleared(resc)):
            print (allProcesses[index].name)            
            #add freed rescources
            for j in range(0,len(free)):
                free[j] += allProcesses[index].allocated[j]        
            to_rem.append(allProcesses[index])
    
    for i in to_rem:
        allProcesses.remove(i)
        to_rem = []
        
if (len(allProcesses) == 0 ):
    print("Deadlock cannot be avoided")