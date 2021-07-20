
def tab_dp(arr, total):
    
    table = [[0 for x in range(total+1) ] for x in range(len(arr)+1)]
    
    for i in range(len(table)):
        table[i][0] = 'T'
    
    for i in range(len(table[0]) -1):
        table[0][i+1] = 'F'
    

    

    
    print(table)




arr = [2,4,6,10]
total = 16

tab_dp(arr, total)