#sort an array using bubble sort algorithm

def bubble_sort(array):

    n=len(array)
    for i in range(n):
        for j in range(0,n-1-i):
            if array[j]>=array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

    return array

def take_input():

    result=[]
    count=int(input("how many element you want add:"))
    for i in range(count):
        row=int(input("enter the number:"))
        result.append(row)
        

    return result

array_input=take_input()
print(array_input)

print(bubble_sort(array_input))
