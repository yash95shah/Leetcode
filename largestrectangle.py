from itertools import islice, tee

def maxrectangle(input_array):
    temp_max = final_answer = 1
    temp = final = 0
    n = len(input_array)
    for sli in range(1,n):
   
        combs = slices(input_array, sli)
        #print (combs)
        for each in combs: 
            print (each)
            temp = min(each)
            print (temp)
            if temp > final:
                final = temp
        temp_max = sli * final
        if temp_max > final_answer:
            final_answer= temp_max

    return final_answer

            









def slices(iterable, n):
    return (list(zip(*(islice(it, i, None) for i, it in enumerate(tee(iterable, n))))))


# 
print (maxrectangle([2,1,5,6,2,3]))