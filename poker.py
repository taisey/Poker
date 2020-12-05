import random
import re
class PlayCard():
    def __init__(self):
        self.deck=[]
    def deckset(self):
        self.deck=[a+str(b) for a in ["♤ ","♧ ","♡ ","♢ "] for b in range(1,14)]
    def deckset_j1(self):
        self.deck=[a+str(b) for a in ["♤ ","♧ ","♡ ","♢ "] for b in range(1,14)]
        self.deck.append("joker")

    def deckset_j2(self):
        self.deck=[a+str(b) for a in ["♤ ","♧ ","♡ ","♢ "] for b in range(1,14)]
        self.deck.append("joker")
        self.deck.append("joker")

    def deckshuffle(self):
        random.shuffle(self.deck)
    def decklen(self):
        return len(self.deck)
    def deckcount(self):
        checker={str(king):0 for king in range(1,14)}
        checker["joker"]=0
        for i in range(0,len(self.deck)):
            checker[re.sub(r"\W", "", card[i])]+=1
        return checker
    def cardshuffle(self,card):
        random.shuffle(card)
    def cardlen(self,card):
        return len(card)
    def cardcount(self,card):
        checker={str(king):0 for king in range(1,14)}
        checker["joker"]=0
        for i in range(0,len(card)):
            checker[re.sub(r"\W", "", card[i])]+=1
        return checker
    def card_to_number(self,card):
        ans=[]
        for i in range(0,len(card)):
            if(card[i]!="joker"):
                ans.append(int(re.sub(r"\W", "", card[i])))
        return ans
        #jokerが入っていた場合その数だけ返すリストが短くなる
        #listの中身はint型
    def card_to_suit(self,card):
        ans=[]
        for i in card:
            if(i!="joker"):
                ans.append((re.sub("[0-9]+","",i)))
        return ans
    def showdeck(self):
        print(self.deck)
    
    def deal(self,num):
        ans=[]
        self.deckshuffle()
        for i in range(0,num):
            ans.append(self.deck.pop(0))
        return ans
    def drow(self,num,card):

        a=self.deal(num)
        card=card + a
    def discard(self,num,card):
        cntr=0
        for i in sorted(num):
            card.pop(i-1-cntr)
            cntr+=1
        #渡すリストは何番目を消すかが入ったリスト
        #関数内部で昇順に変えているので順番はなんでも良い
        #リストの中身はint型
    def cardchange(self,num,card):
        self.discard(num,card)
        self.drow(len(num),card)
        
        
            
        
        
        
        

class Poker(PlayCard):
    def __init__(self):
        self.deck=[a+str(b) for a in ["♤","♧","♡","♢"] for b in range(1,14)]
        self.bet=0
    def pair_is_init(self):
        self.onepair_is=False
        self.twopair_is=False
        self.threecard_is=False
        self.fourcard_is=False
    def straight_is_init(self):
        self.straight_is=False
        self.royal_straight_is=False
    def flush_is_init(self):
        self.flush_is=False
    def royal_straight_flush_is_init(self):
        self.royal_straight_flush_is=False
    def fullhouse_is_init(self):
        self.fullhouse_is=False
    def paircheck(self,card):
        self.pair_is_init()
        checklist=self.cardcount(card)
        
        for t in checklist.values():
            if t>=2:
                if t==3:
                    self.threecard_is=True
                elif t==4:
                    self.fourcard_is=True
                else:
                    if(self.onepair_is==False):
                        self.onepair_is=True
                    else:
                        self.twopair_is=True

    def straightcheck(self,card):
        self.straight_is_init()
        checklist=sorted(self.card_to_number(card))
        if(checklist[0]+len(checklist)-1==checklist[-1]):
            self.straight_is=True
        
        if(checklist==[1,10,11,12,13]):
            self.royal_straight_is=True
        elif(checklist[0]==1 and checklist[-1]==13):
            checklist_2=[]
            for i in checklist:
                if i>=10:
                    checklist_2.append(i-13)
                else:
                    checklist_2.append(i)
            checklist_2=sorted(checklist_2)
            if(checklist_2[0]+len(checklist_2)-1==checklist_2[-1]):
                self.straight_is=True
    
    def flushcheck(self,card):
        self.flush_is_init()
        checklist=self.card_to_suit(card)
        checklist=sorted(checklist)
        if(checklist[0]==checklist[-1]):
            self.flush_is=True
    def royal_straight_flushcheck(self):
        self.royal_straight_flush_is_init()
        if(self.royal_straight_is and self.flush_is):
            self.royal_straight_flush_is=True
            self.royal_straight_is=False
            self.flush_is=False
    def fullhousecheck(self):
        self.fullhouse_is_init()
        if(self.twopair_is and self.threecard_is):
            self.fullhouse_is=True
            self.twopair=False
            self.threecard=False
    def checkresult(self,card):
        self.paircheck(card)
        self.straightcheck(card)
        self.flushcheck(card)
        self.royal_straight_flushcheck()
        self.fullhousecheck()
        print('one_pair_is: {: >20}'.format(str(self.onepair_is)))
        print("two_pair_is: {: >20}".format(str(self.twopair_is)))
        print("threecard_is: {: >19}".format(str(self.threecard_is)))
        print("fourcard_is: {: >20}".format(str(self.fourcard_is)))
        print("straight_is: {: >20}".format(str(self.straight_is)))
        print("flush_is: {: >23}".format(str(self.flush_is)))
        print("royal_straight_is: {: >14}".format(str(self.royal_straight_is)))
        print("royal_straight_flush_is: {: >8}".format(str(self.royal_straight_flush_is)))
        
    def getscore(self,card):
        self.paircheck(card)
        self.straightcheck(card)
        self.flushcheck(card)
        self.royal_straight_flushcheck()
        self.fullhousecheck()
        score=self.onepair_is*1+self.twopair_is*2+self.threecard_is*3+self.flush_is*4
        +self.fullhouse_is*5+self.fourcard_is*6+self.straight_is*7+self.royal_straight_is*8
        +self.royal_straight_flush_is*9
        return score
    

        
    def gamestart(self):
        player1=play.deal(5)
        print(player1)
        print("score: ",self.getscore(player1))
        
class Player():
    def __init__(self):
        self.hand=[]
        self.money=0
        self.human=False
    def gethand(self,hand):
        self.hand=hand
    def moneychange(self,money):
        self.money=self.money+money
    def showhand(self):
        tmp_hand=self.hand
        return tmp_hand
    def is_human(self):
        self.human=True
    def showmoney(self):
        return self.money
    def drow(self,hand):
        self.hand=self.hand+hand

class Dealer():
    def __init__(self):
        self.hand=[]
        self.money=0
    def gethand(self,hand):
        self.hand=hand
    def moneychange(self,money):
        self.money=self.money+money
    def showhand(self,num):
        tmp_hand=[]
        for i in range(0,num):
            tmp_hand.append(self.hand[i])
        return tmp_hand
    def drow(self,hand):
        self.hand=self.hand+hand


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

    





