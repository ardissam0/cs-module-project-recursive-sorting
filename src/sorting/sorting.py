# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_idx = 0
    arrB_idx = 0

    for i in range(elements):
        # if the array index is less than array A or B
        if arrA_idx < len(arrA) and arrB_idx < len(arrB):
            # then if that index of array A is less than or equal to the index of array B
            if arrA[arrA_idx] <= arrB[arrB_idx]:
                # then add what's at index A to merged array
                merged_arr[i] = arrA[arrA_idx]
                # keep going
                arrA_idx += 1
            else:
                # otherwise add what's add index B to merged array
                merged_arr[i] = arrB[arrB_idx]
                #keep going
                arrB_idx += 1
        # otherwise if the index at array B is good and what's at the index in array A is less than what's there
        elif arrA_idx < len(arrA) and arrB_idx is len(arrB):
            #then add what's at index in array A to merged array
            merged_arr[i] = arrA[arrA_idx]
            #keep going
            arrA_idx += 1
        # otherwise just add what's at array B index to the merged array
        else:
            merged_arr[i] = arrB[arrB_idx]
            #keep going
            arrB_idx += 1
    #after everything is sorted return the merged array
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #if the len of the array at index is greater than 1
    if len(arr) > 1:
        #mid is equal to the len of array at that index divded by 2
        mid = len(arr) //2
        # left is equal to the indexes up to the mid
        left = arr[:mid]
        # riht is equal to the indexes after the mid
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

