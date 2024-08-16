'''
Find the missing number in a sequence:

'''

def missing_number(array):

    n=len(array)+1
    array_sum=0
    total_sum=n*(n+1)//2
    for i in array:
        array_sum+=i
        
    mising_num=total_sum-array_sum
    return mising_num

array_list=[1,2,3,4,6]
print(missing_number(array_list))