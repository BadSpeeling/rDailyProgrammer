way = 2

if way == 1:
    input = int(raw_input("Enter number: "))
    
    check_to = input/2
    
    best_val = input
    
    ctr = 1
    
    while ctr < check_to:
        if (input%ctr) == 0:
            second_num = input/ctr
            if ctr+second_num < best_val:
                best_val = ctr+second_num
        ctr += 1
        
    print best_val
    
elif way == 2:
    #factorization must be in form:([0-9]+)*\*[0-9]
    exp = raw_input("Enter factorization: ")
    lst = exp.split("*")
    
    for i in range(0,len(lst)):
        lst[i] = int(lst[i])
        
    while len(lst) > 2:
        print lst
        lst[1] *= lst[0]
        del lst[0]
        lst = sorted(lst)
        
    print(lst[0]+lst[1])