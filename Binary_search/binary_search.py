# Binary search algorithm

def binary_search(arr,low,high,target):

    while low<=high:

        mid=low +(high-low)//2

        if arr[mid]==target:
            return mid
        
        elif arr[mid] < target:
            low=mid + 1

        else:
            high= mid - 1

    return True


if __name__=='__main__':
    array=[10,2,3,4,5,6]
    target_value=5

    result=binary_search(array,array[0],len(array)-1,target_value)

    if result ==True:
        print("the element is present in array")

    else:
        print(f"element not present in array")







