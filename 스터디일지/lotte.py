import random
      
def makeRottoNumber(r, c):
    return random.sample(r, c)

win1 = 1000000000
win2 = 50000000
win3 = 1000000
win4 = 50000
win5 = 5000

win3Count = 0
win4Count = 0
win5Count = 0

spandMoney = 0
getMoney = 0

winWithBonusNumber = makeRottoNumber(range(1,47), 7)
winNumber = winWithBonusNumber[:6]
bonusNumber = winWithBonusNumber[6]

print("당첨번호: " , winNumber , "보너스번호: " , bonusNumber)

while True:
    spandMoney += 1000
    myNumber = makeRottoNumber(range(1,47), 6)

    matchCount = 0
    for number in myNumber:
        if number in winNumber:
            matchCount += 1
    if matchCount == 6:
        print("내 로또:" , myNumber)
        print("1등 입니다.")
        getMoney += win1
        break
    elif matchCount == 5:
        print("내 로또:" , myNumber)
        if bonusNumber in myNumber:
            print("2등 입니다.")
            getMoney += win2
            break
        else:
            ###print("3등 입니다.")
            getMoney += win3
            win3Count += 1
    elif matchCount == 4:
        ###print("내 로또:" , myNumber)
        ###print("4등 입니다.")
        getMoney += win4
        win4Count += 1
    elif matchCount == 3:
        ###print("내 로또:" , myNumber)
        ###print("5등 입니다.")
        getMoney += win5
        win5Count += 1

print("로또 구매 금액 :" , spandMoney)
print("총 상금 :", getMoney)
print("3등 :", win3Count, "4등 :", win4Count, "5등 :" , win5Count)
