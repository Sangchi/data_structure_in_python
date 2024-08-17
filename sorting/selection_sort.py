# sort an array uisng selection sort

def selection_sort(array):

    for i in range(0,len(array)):
        minimum_index=i

        for j in range(i+1,len(array)):
            if array[j]<array[minimum_index]:
                minimum_index=j

        array[i],array[minimum_index]=array[minimum_index],array[i]


    return array


def take_input():

    result=[]
    count=int(input("enter the number count:"))
    for i in range(count):
        row=int(input("enter the number:"))
        result.append(row)

    return result

input_array=take_input()
print(f"unsorted array:{input_array}")

print(f"sorted array:{selection_sort(input_array)}")