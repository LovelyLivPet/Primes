#PRIMES NUMBERS TO 100

def primes():
    lst = []    

    for each in range (0,101):          #sets lower/upper bounds of loop.
        if each > 1:                    #if item is above one...
            
            for i in range (2, each):       #for every item from 2, up until current item,...
                if (each % i) == 0:             #if the remainer of (item divied by current element) it is 0...
                    break                           # go to top of loop,
            else:
                lst.append(each)            # else the only product must be one,  so is therefore prime
                                            # add to list

    print("The primes 0 to 100 are: ",lst)
                
                
primes()
