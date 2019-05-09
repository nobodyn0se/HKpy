if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split(" ")))
    m = max(arr)
    arr.sort(reverse = True)
    for a in range(n):
        if(arr[a] < m and arr[a] != m):
            print(arr[a])
            break
            
    

