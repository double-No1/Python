
def drawsq(n):
    line = n * n + 1
    for i in range(1, line+1):
        if i % n == 1:
            print(n*"+----", end="")
            print("+")
        else:
            print("|    "*n, end="")
            print("|")

if __name__ == "__main__":
    n = eval(input("请输入阶数:"))
    drawsq(n)
