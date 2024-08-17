#Find the specific card in a list of cards that are in increasing and decreasing order.

def find_card(array,low,high,card):

    while low<=high:

        mid=low +(high-low)//2
        
        if array[mid]==card:
            return mid
        
        elif array[mid]<card:
            low=mid+1

        else:
            high=mid-1

    return -1

def sort_array():
    array_of_cards=[1,3,6,4,7,8]
    n=len(array_of_cards)
    for i in range(n):
        for j in range(0,n-i-1):
            if array_of_cards[j]>array_of_cards[j+1]:
                array_of_cards[j] ,array_of_cards[j+1]=array_of_cards[j+1],array_of_cards[j]

    return array_of_cards

sorted_array=sort_array()
print(sorted_array)
card=int(input("enter you card:"))

result=find_card(sorted_array,0,len(sorted_array)-1,card)
if result !=-1:
    print(f" card is present at index={result}")

else:
    print("card is not present")