'''
Given an array, sort the array using recursion.
input in_arr = [7,8,2,3,4,1,5,6]
output = [1,2,3,4,5,6,7,8]

'''
def sort_input_arr(arr:list)->list:
    if len(arr) == 1:
        return arr
    last_element = arr.pop()
    sorted_arr = sort_input_arr(arr)
    
    new_arr = list()
    for idx in range(0,len(sorted_arr)):
        if sorted_arr[idx]>last_element:
            new_arr.append(last_element)
            last_element = float("inf")
        new_arr.append(sorted_arr[idx])
    if last_element!=float("inf"):
        new_arr.append(last_element)
    
    return new_arr
if __name__ == "__main__":
    input_arr = list(map(int, input().split(',')))
    print(sort_input_arr(input_arr))