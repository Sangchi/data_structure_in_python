# sort an array using insertion sort

def inserton_sort(array):

    for i in range(1,len(array)): #travesre whole array from first to last
        key=array[i]               #store current element

        for  j in range(i-1,-1,-1):    #traverse array reverse upto second last element of i loop

            if array[j]>key:
                array[j+1]=array[j]

            else:
                break

        array[j+1]=key

    return array


def take_input():
    
    result=[]
    count=int(input("enter number count:"))
    for i in range(count):
        row=int(input("enter the number:"))
        result.append(row)

    return result

input_array=take_input()
print(f"unsorted array:{input_array}")

print(f"sorted array{inserton_sort(input_array)}")
