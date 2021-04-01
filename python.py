n=int(input("구구단 몇 단 계산" ))
while(n!=0):
    for i in range(10):
        if n>=1 and n<=9:
            print("{}x{}={}".format(n, i, n*i))
            continue
        else:
            print("잘못 입력했습니다. 1~9사이의 숫자를 입력하세요.")
            break
    n=int(input("구구단 몇 단 계산" ))
print("구구단을 종료합니다.")