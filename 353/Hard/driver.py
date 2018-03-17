import random

class Stochastic:
    
    #bits is the number of bits used for representation.  0 <= prob <= 1
    def __init__ (self, bits, prob):
        
        number_of_ones = int(bits*prob)
        ctr = 0
        potential_index = range(0,bits)
        self.num = [0] * bits 
        
        while (ctr < number_of_ones):
            cur_index = random.choice(potential_index)
            self.num[cur_index] = 1
            del potential_index[potential_index.index(cur_index)]
            ctr += 1
    
    def mult (self, other):
        
        ret = [0] * len(self.num)
        
        if (len(self.num) != len(other.num)):
            return -1
        
        for i in range(0,len(self.num)):
            if (self.num[i] == 1 and other.num[i] == 1):
                ret[i] = 1
            else:
                ret[i] = 0
        
        return ret
        
a = Stochastic(10,.64)
b = Stochastic(10,.5)

print(a.num)
print(b.num)
print (a.mult(b))