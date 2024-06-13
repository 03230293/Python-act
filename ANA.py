matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
for i in matrix:
    # print(i)
    if target in matrix:
        if target==i:
            print('TRYE')
    else:
        print("false")