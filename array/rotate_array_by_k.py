'''
Rotate an array by k positions

'''
def reverse(arr,start,end):

    while start <end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end -=1

def rotate(arr,k):

    n=len(arr)
    k=k%n  # k>n

    reverse(arr,0,n-1) # reversing whole array

    reverse(arr,0,k-1) #reverse first element

    reverse(arr,k,n-1) #reverse remaining element
    return arr

array_list=[1,2,3,4,5,6,7]
print(rotate(array_list,3))