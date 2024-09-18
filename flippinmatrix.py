





    #col-sort
def tranpose_matrix(matrix,n):
    temp_mat = [[0 for i in range(n)] for j in range(n)]
    print(temp_mat)
    
    for i in range(n):
        for j in range(n):
            temp_mat [i][j] = matrix[j][i]
    return temp_mat  
            
def sort_rows(matrix, n):
    for i in range(n):
          matrix[i].sort(reverse=True)     
            
def flippingMatrix(matrix):
    orig_matrix = matrix
    n = len(matrix)
    max_sum = 0
    tmat= matrix
    
    '''
    1. Tranpose of matrix 
    2. Sort rows
    3. Again tranpose matrix
    4. Sort rows
    5. Take and return sum
    '''
    print("\n Step 0: \n")
    print(tmat) 
    
    tmat = tranpose_matrix(matrix,n)
    
    print("\n After Step 1: \n")
    print(tmat) 
    
    # col-wise sort
    sort_rows(tmat,n)
    
    print("\n After Step 2: \n")
    print(tmat) 
    
    tmat = tranpose_matrix(tmat,n)
    
    print("\n After Step 3: \n")
    print(tmat) 
    
    # row sort
    sort_rows(tmat,n)
    
    print("\n After Step 4: \n")
    print(tmat) 
    
    for i in range(2):
        for j in range(2):
            print(f"arr{i, j} = {tmat[i][j]}")
            max_sum = max_sum + tmat[i][j]
            
    print("\n After Step 5: \n")
    print(f"Sum ={max_sum}")    
    
    return max_sum

# mat_transpose = 


matrix= [[112,42,83,119],
[56,125,56,49],
[15,78,101,43],
[62,98,114,108]]
# print(matrix)
# print(len(matrix))

print(f"Len m[] {len(matrix[0])}")
result = flippingMatrix(matrix)
# print(result)


# Input (stdin)
# 1
# 2
