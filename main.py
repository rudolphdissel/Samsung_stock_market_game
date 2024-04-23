import random

#변수설정
money=300000 #초기 자금
money_first=money 
day=0 


samsung_price=random.randint(40000,60000) #삼성의 초기주가
lg_price=random.randint(150000,200000) #엘지의 초기주가
han_price=random.randint(35000,45000) #한화의 초기주가
lot_price=random.randint(60000,70000) #롯데의 초기주가
doo_price=random.randint(9000,11000) #두산의 초기주가

stock_have=0
day_set=10 #플레이 할 날짜
yesterday_price=[0]*5 #0~4번 삼성~두산순서

#삼성 주가 구하기함수
def get_samsung_stock_price(samsung_price):
    randpercent=random.random()*10 #10퍼의 주가변동
    randpercent*=random.choice([-1,1]) #부호결정
    samsung_price*=1+randpercent/100
    samsung_price="{:.0f}".format(samsung_price) #소숫점 짜르기
    samsung_price=int(samsung_price) #format쓰니까 문자열로 바뀜.
    return samsung_price

#한화 주가 구하기함수
def get_han_stock_price(han_price):
    randpercent=random.random()*5 #5퍼의 주가변동
    randpercent*=random.choice([-1,1]) #부호결정
    han_price*=1+randpercent/100
    han_price="{:.0f}".format(han_price) #소숫점 짜르기
    han_price=int(han_price) #format쓰니까 문자열로 바뀜.
    return han_price

#롯데 주가 구하기함수

#엘지 주가 구하기함수

#두산 주가 구하기함수
    

#게임진행
while day<day_set:
    #각 회사의 금일 주가 구하기
    yesterday_price[0]=samsung_price
    samsung_price=get_samsung_stock_price(samsung_price)
    han_price=get_samsung_stock_price(han_price)
    
    
    dif_price=samsung_price-yesterday_price
    day+=1
    if day==day_set:
        print("금일은 마지막 날 입니다")
    else:
        print(f"오늘은 {day}일 차입니다")
        
    print(f"금일 삼전의 가격은 {samsung_price}원 입니다.")
    if day!=1:
        print(f"어제대비 {dif_price}원 입니다.")
    #거래 상황 (유저가 거래 종료 입력할 때 까지 지속)
    while True:
        print(f"당신은 {stock_have}주,{money}원을 보유하고 있습니다.")
        print("*"*30)
        print("구매할 것이라면 b를 파실꺼면 s를, 내일로 넘어가려면 n을 눌러주세요.")
        user_choice=input()
        #구매 구현
        if user_choice=="b":
            if money>=samsung_price:
                money-=samsung_price
                stock_have+=1
                print("거래가 완료됐습니다")
                
            else:
                print("돈이 부족하시군요...") # 구매행동 선택으로 돌아가기.
                continue
        #판매 구현
        elif user_choice=="s":
            if stock_have>=1:
                money+=samsung_price
                stock_have-=1
            else:
                print("보유하고 계신 주식이 없습니다.") # 보유주가 없다면 선택화면으로 돌아가기.
                continue
        #내일로 넘어가기 구현
        elif user_choice=="n":
            if day==day_set and stock_have!=0:
                print("마지막 날 입니다.남은 주식을 모두 정리해주세요.")
                continue
            else:     
                print("내일로 넘어갑니다.")
                print("="*30)
                break
        else:
            print("올바른 형식으로 입력해주세요.")
            continue
print(f"게임결과 : 당신의 돈은 {money}원 입니다.")
print(f"당신의 성과는 {money-money_first}원 입니다.")

    