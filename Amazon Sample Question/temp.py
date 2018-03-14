X = [1,3,5]
N = 10

def find_unique_ways (val,nums,to_print):
    if (val == 0):
        print(to_print)
        return
    elif (val < 0):
        print("ya done goofed")
        return
    else:
        for cur in nums:
            if(val-cur >= 0):
              find_unique_ways(val-cur,nums,to_print+","+str(cur))
        return
    
find_unique_ways(N,X,"")
        