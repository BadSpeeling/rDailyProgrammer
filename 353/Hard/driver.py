import random

class Stochastic:
    
        #bits is the number of bits used for representation.  0 <= prob <= 1
    #this is a bi-polar representation, meaning that there will be 1 sign bit
    def __init__ (self, bits = 0, prob = None, neg=False, copy=False, other=None):
        
        if copy is True:
            if other is None:
                print('no copy given')
            self.num = [0] * len(other.num)
            for i in range(0,len(other.num)):
                self.num[i] = other.num[i]
        
        else:
            self.num = [0] * (bits+1) 
            
            if prob != None:
                number_of_ones = int(bits*prob)
                ctr = 0
                potential_index = range(1,bits+1)
                
                while (ctr < number_of_ones):
                    cur_index = random.choice(potential_index)
                    self.num[cur_index] = 1
                    del potential_index[potential_index.index(cur_index)]
                    ctr += 1
            
            if (neg):
                self.num[0] = 1
        
    def addBits (self, other):
        
        carry = 0
        ret = [0] * len(self.num)
        ret_obj = Stochastic(len(self.num))
        
        for i in reversed(range(1,len(self.num))):
            toAdd = self.num[i] + other.num[i] + carry
            if toAdd > 1:
                carry = 1
            else:
                carry = 0
            ret[i] = toAdd%2
        
        ret_obj.num = ret
        return ret_obj
    
    def invertBits (self):
        for i in range(0,len(self.num)):
            self.num[i] = (self.num[i]+1)%2
    
    #computes 1-num. in-place
    def invert (self):
        
        if (self.num[0] == 1):
            print("Cannot find inverse of a negative probability")
            return None
        
        for i in range(1,len(self.num)):
            self.num[i] = (self.num[i]+1)%2
    
    #DOES NOT WORK FOR NEGATIVE NUMBERS BECAUSE PROBABILITIES CANNOT BE NEGATIVE
    def mult (self, other):
        return self.andGate(other)
    
    def subtract (self, othr):
        
        othr.invertBits()
        
        return self.add(othr)
        
    def add (self, othr):
        
        half = Stochastic(len(self.num)-1, .5)
                
        v1 = self.mult(half)
        half.invert()
        v2 = othr.mult(half)
                
        #print (v1.num)
        #print (v2.num)
        
        return v1.addBits(v2)
    
    #logical and gate
    def andGate (self, other):
        
        ret = [0] * len(self.num)
        ret_obj = Stochastic(bits=len(self.num))
        
        if (len(self.num) != len(other.num)):
            return -1
        
        for i in range(1,len(self.num)):
            if (self.num[i] == 1 and other.num[i] == 1):
                ret[i] = 1
            else:
                ret[i] = 0
        
        ret_obj.num = ret
        return ret_obj
        
a = Stochastic(bits = 10,prob=.5)
b = Stochastic(bits = 10,prob=.4)

print(a.subtract(b).num)
