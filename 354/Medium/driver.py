def find_factors (input):
    check_to = input/2
    
    best_val = input
    best_num = 0
    
    ctr = 1
    
    while ctr < check_to:
        if (input%ctr) == 0:
            second_num = input/ctr
            if ctr+second_num < best_val:
                best_val = ctr+second_num
                best_num = ctr
        ctr += 1
    if (best_num != 0):
        return (best_num,input/best_num)
    else:
        return None

def calc_complexity (cur_num,cmpl):
    
    if (cur_num in cmpl.keys()):
        return cmpl[cur_num]
    
    returned_val = find_factors(cur_num)
    
    #this number is a prime number.  therefore we will do addition to attempt to further break this number down 
    if (returned_val is None):
        num1 = 1
        num2 = cur_num-1
        return calc_complexity(num1,cmpl) + calc_complexity(num2,cmpl)
    else:
        (num1,num2) = returned_val
        return calc_complexity(num1,cmpl) + calc_complexity(num2,cmpl)


#val = int(raw_input("Enter number: "))

cmpl = {1:1}
tot = 0

for i in range(1,101):
    ret = calc_complexity(i,cmpl)
    print(i)
    print(ret)
    cmpl[i] = ret
    tot += ret
    
print (tot)