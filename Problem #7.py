'''Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.'''

def countWays(n):
    tempArray  = [-1]* n
    return totalWays(n, tempArray)

def totalWays( n, tempArray ):
    if n<0:
        return 0
    elif n == 0:
        return 1
    elif tempArray[n-1]> -1:
        print("hello")
        return tempArray[n-1]
    else:
        tempArray[n-1] = totalWays(n-1, tempArray)+totalWays(n-2, tempArray)+totalWays(n-3, tempArray)
        #return totalWays(n-1) + totalWays(n-2)+ totalWays(n-3)
        return tempArray

print (countWays(6))




    #     return 1
    # elif n ==2 or n == 3:
    #     return 2
    #
    # else:
    #     while n>=0:
    #         no_of_ways(self, )





