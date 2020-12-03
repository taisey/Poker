from poker_ver2 import Poker,Player,Dealer


play=Poker()
N=4
nowplayer=N
money=1000
dealmoney=0
playerNum=1
fieldmoney=0
dealerhandcntr=3
whilecntr=0
raisecntr=-1
paysum=0
s_raise="ta"
playerlist=[ Player() for i in range(0,N)]
playeralive=[ 1 for i in range(0,N)]
for i in range(0,playerNum):
    playerlist[i].is_human()
dealer=Dealer()

for i in playerlist:
    i.gethand(play.deal(2))
    i.moneychange(money)
dealer.gethand(play.deal(5))



while(dealerhandcntr<=5 and sum(playeralive)>1):
    
    for i in range(0,N):
        tmp_dealerhandcntr=dealerhandcntr
        if(i==raisecntr):
            tmp_dealerhandcntr+=1
            dealerhandcntr+=1
        if(raisecntr<0):
            raisecntr=i
        if(playeralive[i]!=1):
            continue
        print("player%d" %(i+1))
        print("dealer: ",dealer.showhand(dealerhandcntr))
        print("yourhand: ",playerlist[i].showhand())
        print("bet: ",fieldmoney)
        #whilecntr=0
        while(True):
            s=input("choose call,raise,fold\n\n")
            #inputの例外処理をのちに追加する
            if (s=="fold"):
                print("accept")
                print("--------------\n")
                playeralive[i]=0
                dealerhandcntr=tmp_dealerhandcntr
                break
            elif(s=="call"):
                print("accept") 
                print("--------------\n")
                playerlist[i].moneychange(fieldmoney*-1)
                paysum=+fieldmoney
                dealerhandcntr=tmp_dealerhandcntr
                break
 
 ################## raise処理部#########################
            elif(s=="raise"):
                raisecntr=i         
                whilecntr=0
                print("bet: ",fieldmoney)
                print("your money: ",playerlist[i].showmoney())
                 
            
                while(s_raise.isdecimal()!=True or whilecntr==0):
                    if(whilecntr==1):
                        print("##################\n#value is invalid#\n###############")    
                    whilecntr=1
                    s_raise=(input("how much? "))
                    if(str(s_raise).isdecimal()!=True):
                        continue
                    else:
                        s_raise=int(s_raise)
                
                    if (s_raise>fieldmoney and s_raise<=playerlist[i].showmoney()):
                        print("accept")
                        print("--------------\n")
                        fieldmoney=s_raise
                        playerlist[i].moneychange(fieldmoney*-1)
                        paysum=+fieldmoney
                        s_raise=str(s_raise)
                        break
                    else:
                        s_raise=str(s_raise)
                        print("##################\n#value is invalid#\n###############")
                        whilecntr=0
                        continue
                   
                dealerhandcntr=tmp_dealerhandcntr    
                break
###################################################
            else:
                print("##################\n#value is invalid#\n###############")

        continue
        s_raise=str(s_raise)
    

