'''
two sum in array

'''


def two_sum(array,target):

    n=len(array)
    for i in range(n):
        for j in range(i+1,n):
            if array[i] +array[j]==target:

                return array[i],array[j]

array_list=[1,2,3,4,5,6,7,8]
user_target=12
print(two_sum(array_list,user_target))

    