

# def in_order(grid_transpose):
#     print("Inside in_order()\n")
#     return True
#     col_flag = True
#     for item in transpose_grid:
#         print(f"current item {item}")
#         prev_val=0
#         for alpha in item:
#             ascii_val = ord(alpha)
#             if ascii_val > prev_val:
#                 prev_val = ord(alpha)
#             elif ascii_val < prev_val:
#                 col_flag = False 

def sort_grid(grid):
    sorted_grid=[]
    for item in grid:
        lst=[]
        re_lst=[]

        print(f"current item {item}")
        for alpha in item:
                lst.append(ord(alpha))
        lst.sort()
        for alpha in lst:
            re_lst.append(chr(alpha))
        sorted_item= "".join(re_lst)
        sorted_grid.append(sorted_item)
    print(f"sorted item {sorted_grid}")   
    return sorted_grid


def transpose_grid_check(grid):
    flag=True
    col_len =len(grid)
    row_len = len(grid[0])
    for i in range(row_len):
        prev_val=0
        item=[]
        for j in range(col_len):
            curr_val = ord(grid[j][i])
            item.append(curr_val)
            if curr_val>prev_val:
                prev_val = curr_val
            elif curr_val<prev_val:
                flag = False
            # print(grid[j][i])
        #     item.append(grid[j][i])
        # "".join(item)
        # lst.append(item)
    return flag
    # print(f"Transpose grid: {lst}")
    
    
    

def gridChallenge(grid):
    # Write your code here
    sorted_grid = sort_grid(grid)
    
    if transpose_grid_check(sorted_grid):
            print("YES")
    else:
            print("NO")
    
# print(gridChallenge(['ebacd', 'fghij', 'olmkn','xywuv', 'trpqs', ]))
print(gridChallenge(['abc', 'hjk', 'mpq', 'rtv']))