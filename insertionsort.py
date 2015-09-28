
myArray = [3,1,2,8,2, 10,9]

print(myArray)


def insertionSort(array):
     newArray = []

     for i in range(0, len(array)):
        lookvalue = array[i]

        for n in range (0, len(newArray)):
            if lookvalue < newArray[n]:
                newArray.insert(n, lookvalue)
                break
        else:
            newArray.append(lookvalue)
                        
        print(newArray)

        
def selectionSort(array):
    for i in range(0, len(array)):
        smallest = array[i]
        position = i 
            
        for n in range(i, len(array)):
            #find next smallest
            if (smallest > array[n]):
                smallest = array[n]
                position = n

        #swap because this is the smallest
        array[position] = array[i]
        array[i] = smallest
            
    print(array)
    
#insertionSort(myArray)
selectionSort(myArray)
