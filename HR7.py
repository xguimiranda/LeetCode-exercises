if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = [ ]
    for i in range (x+1):
        for j in range (y+1):
            for k in range (z+1):
                a = [i,j,k]
                lst.append(a)
    b = list(filter(lambda x:sum(x)!=n, lst))
    print(b)
