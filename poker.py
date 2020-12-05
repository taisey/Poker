

play=Poker()
N=4
nowplayer=N
money=1000
dealmoney=0
playerNum=1
fieldmoney=0
dealerhandcntr=3
playerlist=[ Player() for i in range(0,N)]
playeralive=[ 1 for i in range(0,N)]
for i in range(0,playerNum):
    playerlist[i].is_human()
dealer=Dealer()

for i in playerlist:
    i.gethand(play.deal(2))
    i.moneychange(money)
dealer.gethand(play.deal(5))

while(dealerhandcntr<=5 and True):
    
    for i in range(0,N):
        if(playeralive[i]!=1):
            continue
        print("player%d" %(i+1))
        print("dealer: ",dealer.showhand(dealerhandcntr))
        print("yourhand: ",playerlist[i].showhand())
        print("bet: ",fieldmoney)

        s=input("choose call,raise,fold\n\n")
        #inputの例外処理をのちに追加する
        if (s=="fold"):
            playerlist[i].moneychange(fieldmoney*-1)
            print("accept")
            print("--------------\n")
            playeralive[i]=0
            continue
        elif(s=="call"):
            print("accept") 
            print("--------------\n")
            continue
        elif(s=="raise"):
            print("bet: ",fieldmoney)
            print("your money: ",playerlist[i].showmoney())
            s_raise=int(input("how much?"))
            if (s_raise>fieldmoney and s_raise<=playerlist[i].showmoney()):
                print("accept")
                print("--------------\n")
                fieldmoney=s_raise
            continue
 
    dealerhandcntr+=1

    





