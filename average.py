# average
def main():
    pass
    import math
    n=input()
    u=list(map(int,input().split()))
    count=0
    for i in u:
        count+=i
    k=len(u)
    print(math.floor(count/k))

if __name__ == '__main__':
    main()
