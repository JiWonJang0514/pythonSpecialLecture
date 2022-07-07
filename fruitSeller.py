# 과일장수 클래스
class FruitSelller:
    price = 800
    def __init__(self):
        self.apple = 50
        # 판매수익 or 판 개수
        # 판매수익 = 판개수 * 단가
        # 판 개수 = 판매수익 / 단가
        
        # 판 개수
        self.sellCnt = 0

    def sell(self, money):
        sellCnt = int(money//self.price)

        if sellCnt > self.apple:
            raise Exception
        else:
            self.apple -= sellCnt
            self.sellCnt += sellCnt

appleSeller = FruitSelller()

for i in range(12):
    money = int(input("받은 금액:"))

    try:
        appleSeller.sell(money)

        print("현재까지 판매 개수:",appleSeller.sellCnt)
        print("현재까지 판매 수익:",appleSeller.sellCnt*FruitSelller.price)
    except:
        print("재고가 없습니다")

print("판매 개수:",appleSeller.sellCnt)
print("판매 수익:", appleSeller.sellCnt*FruitSelller.price)
    

