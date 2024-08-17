# sort an array with help of merge sort

def merge_sort(array):

    if len(array)<=1:
        return f"array not more element to sort"
    
    mid=len(array)//2           #divdie the array in two parts

    left_half=array[:mid]        #araray from 0 to mid
    right_half=array[mid:]       #remaining array
    merge_sort(left_half)        #recursevely call function
    merge_sort(right_half)

    i=j=k=0                        # initialize the three varibale for travesring two  array and storing it f rom [i],[j] to [k]

    while i<len(left_half)and j <len(right_half):        #traverse array and sort it
        if left_half[i]<right_half[j]:
            array[k]=left_half[i]
            i +=1

        else:
            array[k]=right_half[j]
            j +=1

        k +=1

    while i<len(left_half):                 # traverse the remaining element of array
        array[k]=left_half[i]
        i +=1
        k +=1

    while j < len(right_half):              # traverse remainig element of array
        array[k]=right_half[j]
        j +=1
        k +=1

    return array





def take_input():
    
    result=[]
    count=int(input("enter the count:"))
    for i in range(count):
        row=int(input("enter the number:"))
        result.append(row)

    return result

if __name__=='__main__':
    input_array=take_input()
    print(input_array)

    print(f"sorted aray :{merge_sort(input_array)}")



    


