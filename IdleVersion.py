#PRIMES NUMBERS TO 100

def primes():
    lst = []    

    for nums in range (0,101):          #sets lower/upper bounds of loop.
        if nums > 1:                    #(one doesn't count as a prime number)
            
            for i in range (2, nums):   
                if (nums % i) == 0:     # checks for other products by seeing if any number
                                        # multiplies to give current element.
                    break                 
            else:
                lst.append(nums)            # if not...
                                            # add to list

    print("The primes 0 to 100 are: ",lst)
                
                
primes()

#README

