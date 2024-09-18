def towerBreakers(n, m):
    # Write your code here
    # no of towers -> n
    # height of tower -> m
    a = n%2
    if m==1 or n%2 == 0:
       return 2
    else:
       return 1


print(towerBreakers(2,2))