class char:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __str__(self):
        sen = self.name +"는 "+str(self.age)+"세 이고, "+self.sex+" 입니다."
        return sen

zzanggu = char("짱구", 5, "남자")
print(zzanggu)
dora = char("도라에몽", 14, "남자")
print(dora)
konan = char("코난",8, "남자")
print(konan)
shoc = char("쇼콜라", 15, "여자")
print(shoc)
amu = char("아무", 12, "여자")
print(amu)
gayoung = char("가영", 16, "여자")
print(gayoung)
