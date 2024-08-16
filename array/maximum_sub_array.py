'''
Find the maximum subarray sum

'''
def maximum_subarray(array):

    max_array_end=array[0]
    max_so_far=array[0]
    start=0
    end=0
    index=0

    for i in range(1,len(array)):

        if max_array_end +array[i] >array[i]:
            max_array_end +=array[i]

        else:
            max_array_end=array[i]
            index=i

        if max_array_end >max_so_far:
            max_so_far=max_array_end
            start=index
            end=i

    return max_so_far,array[start:end+1]

array_list=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maximum_subarray(array_list))