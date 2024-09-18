from freq_sortinput import input_arr, output_arr

def countingSort(arr):
    f_arr = [0 for i in range(100)]
    arr.sort()
    for item in arr:
        f_arr[item] += 1
    return f_arr
        
  
def test(result):
    if result == output_arr:
        print("Test case passed")
    else:
        print("Test case fails") 
    
result = countingSort(input_arr)
test(result)
input_arr.sort()
print(f"Input sorted\n {input_arr} \n")
print(f"Output \n {output_arr} \n")
print("\n***********************\n")
print(f"freq array: {len (result)}")