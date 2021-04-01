the_answer = {"현숙": "이화여대 멋사 대표님", "세은": "파이썬 세션 튜터", "두희": "멋사 창립자", "마루": "야옹"}
for i in the_answer:
    print("다음은 누구에 대한 설명일까요?")
    print(the_answer[i])
    n=input()
    if the_answer[i]==the_answer.get(n):
        print("정답입니다.")
    else:
        print("오답입니다.")
        continue
