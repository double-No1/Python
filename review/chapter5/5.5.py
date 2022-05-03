def isPrime(n):
    try:
        idex = 0
        if n == 0 or n == 1:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    idex += 1
                    return False
                if idex == 0:
                    return True
    except:
        return False
n = int(input("请输入一个数:"))
print(isPrime(n))