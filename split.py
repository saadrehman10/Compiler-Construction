def arrayConcatenation(array):
    index1 = 0
    index2 = 1
    for i in range(len(array)):
        if index2 >= len(array): 
            break  
        if array[index1] == "=" and array[index2] == "=":
            hold = array[index1] + array[index2]
            array[index1] = hold
            array.pop(index2)
        else:  
            index1 += 1
            index2 += 1

    return array

arr = ["=", "=", "+", "=", "=", "+", ">", "="]
print(arrayConcatenation(arr))

