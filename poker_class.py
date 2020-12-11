import random
import re
import time
class PlayCard():
    def __init__(self):
        self.deck=[]
    def deckset(self):
        self.deck=[a+str(b) for a in ["♤","♧","♡","♢"] for b in range(1,14)]
    def deckset_j1(self):
        self.deck=[a+str(b) for a in ["♤","♧","♡","♢"] for b in range(1,14)]
        self.deck.append("joker")

    def deckset_j2(self):
        self.deck=[a+str(b) for a in ["♤","♧","♡","♢"] for b in range(1,14)]
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
    def card_strangth_conpete(self,card):
        checker=[0]*13
        for i in card:
            checker[int(re.sub(r"\W", "", i))-1]+= 1
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
        card=card+a
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

    def card_count(self,card):
        card=self.card_count_tolist(card)
        print(card)

    def strength_compare(self,card1,card2):
        checker1=[0]*13
        checker2=[0]*13

        for i in card1:
            checker1[int(re.sub(r"\W", "", i))-1] += 1
        for i in card2:
            checker2[int(re.sub(r"\W", "", i))-1] += 1 

        #for i in card1:
        #    checker1[i-1]+=1
        #for i in card2:
        #    checker2[i-1]+=1
        max1=max(checker1)
        max2=max(checker2)
        checker1=checker1[0:1]+list(reversed(checker1[1:]))
        checker2=checker2[0:1]+list(reversed(checker2[1:]))
        #print("checker1:",checker1)
        #print("checker2:",checker2)
        for max_tmp in reversed(range(1,max1+1)):
            for k in range(len(checker1)):
                i=checker1[k]
                j=checker2[k]
                if(i==max_tmp or j==max_tmp):
                    if(i>j):
                        return 0
                    elif(j>i):
                        return 1
        return -1

    def strongest_card(self,card_list):
        ans_card=card_list[0]
        for i in range(1,len(card_list)):
            if(self.strength_compare(ans_card,card_list[i])):
                ans_card=card_list[i]
        return ans_card
    def extract(self,list_,num):
        ans_list=[]

        if(list_==[] or num==0):
            return [[]]
        if(len(list_)<num):
            return [[]]

        for i in self.extract(list_[1:],num-1):
            ans_list.append(list_[0:1]+i)
        for i in self.extract(list_[1:],num):
            ans_list.append(i)
        if len(ans_list)>1 and [] in ans_list:
            ans_list.remove([])
        return ans_list
    #５つ以上のカードの中で一番scoreの高いものを選ぶ
    def max_hands(self,cards):
        possible_hand=self.extract(cards,5)
        score=[]
        for i in possible_hand:
            score.append(self.getscore(i))
        max_hands=[]
        for i,j in enumerate(score):
            if(j==max(score)):
                max_hands.append(possible_hand[i])
        return max_hands
    
    def max_hands_not_extract(self,cards):
        score=[]
        for i in possible_hand:
            score.append(self.getscore(i))
        max_hands=[]
        for i,j in enumerate(score):
            if(j==max(score)):
                max_hands.append(possible_hand[i])
        return max_hands

        
    def gamestart(self):
        player1=play.deal(5)
        print(player1)
        print("score: ",self.getscore(player1))
        
        
#play=Poker()
#play.gamestart()  
        
class Player():
    def __init__(self):
        self.hand=[]
        self.money=0
        self.human=False
        self.bet=0
        self.name=""
        self.tmp_bet=0
    def name_set(self,name):
        self.name=name
    def get_hand(self,hand):
        self.hand=hand
    def moneyadd(self,money):
        self.money=self.money+money
    def show_hand(self):
        tmp_hand=self.hand
        return tmp_hand
    def bet_change(self,money):
        if(self.money+self.tmp_bet>=money):
            self.bet=money
        else:
            return -1
    
    def is_human(self):
        self.human=True
    def showmoney(self):
        return self.money
    def drow(self,hand):
        self.hand=self.hand+hand
    def tmp_bet_init(self):
        self.tmp_bet=0

class Dealer():
    def __init__(self):
        self.hand=[]
        self.money=0
    def get_hand(self,hand):
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
        
class Texas_Holdem():
    def __init__(self,player_list):
        self.pod=0
        self.bb=100
        self.player_list=player_list
        self.flop=[]
        self.bet=0
        self.turn=0
        self.player_num=len(player_list)
        self.player_alive=[1]*self.player_num
        self.temp_list=player_list
        self.all_in_list=[]
    def max_bet(self):
            money_list=sorted([i.money + i.tmp_bet for i in self.player_list],reverse=True)
            return money_list[1]
    def pod_money_add(self,add):
        self.pod += add
    def get_hand(self,hand):
        self.flop=hand
    def bet_bb(self):
        self.bet=self.bb
    def bet_change(self,bet):
        self.bet=bet
    def show_hand(self,num):
        if(len(self.flop)>=num):
            return print(self.flop[:num])
        else:
            return []
    def fold_flag(self,player_number):
        self.player_alive[player_number]=0
    def turn_change(self,start):
        player_num=self.player_num
        turn_1=[i for i in range (start % player_num, player_num )] +  [j for j in range (0 , start % player_num )]
        for i,j in enumerate(self.player_alive):
            if(j==0):
                turn_1.remove(i)
        return turn_1
    def alive_list(self):
        alive_list=[]
        for i in self.turn_change(0):
            alive_list.append(self.player_list[i])
        return alive_list
    def action_flow(self,turn):

        if(turn==[]):
            return -1
        N=self.player_num
        last_turn=turn[-1]
        end_flag=0
        raise_flag=0
        this_turn_raise_flag=0
        #UTGからアクション開始
        while(end_flag!=1):
            now_bet=self.bet
            this_turn_raise_flag=0
            #一人一人やるところ
            #print("start new_turn")
            for k in turn:
                
                if(len(self.alive_list())==1):
                    return 0
                print("\n=====================")
                np=self.player_list[k]
                #player情報表示
                print("player",k,":")
                print("your_bet:",np.bet)
                print("your_money:",np.money)
                print("your_card:",np.hand)
                print("=====================\n")
                #print("all-in,alive",len(self.all_in_list),len(self.alive_list()))
                if(np in self.all_in_list):
                    print("you are all-in")
                    #print("now_turn:",k," last_turn:",last_turn)
                    #print("turn:",turn)
                    if(k==last_turn):
                        return 1
                    #all-inしてるから次のkにするためのcontinue
                    continue
                
                elif(self.player_num -1 ==len(self.all_in_list)+(self.player_num-len(self.alive_list()) and np.bet == self.bet)):
                    print("everyone is all-in except for you")
                    if(k==last_turn):
                        return 1
                    #他のひとがall-inしてるから次のkにするためのcontinue
                    continue
                    #テーブルベットの方が大きくて、所持金より小さいとき
                if(self.bet>np.bet and self.bet - np.tmp_bet < np.money):
                    print("table_bet: ",self.bet)
                    input_flag=1
                    while(input_flag==1):
                        input_flag=0
                        choice = input("\ncall, raise, fold: ")
                        #call,raise,foldから選ぶ
                        if choice == "call":
                            #ifの部分はself.bet<np.moneyが保証されているので死文
                            if (np.bet_change(self.bet)== -1):
                                    print("plz re input")
                            else:
                            #精算
                                #print("tmp_bet:",np.tmp_bet,"np.bet",np.bet)
                                np.moneyadd(-(np.bet-np.tmp_bet))
                                self.pod_money_add(np.bet-np.tmp_bet)
                                np.tmp_bet=np.bet

                        elif choice == "fold":
                            #fold_flag立てる
                            self.fold_flag(k)
                        
                        elif choice == "raise":
                            raise_flag=1
                            this_turn_raise_flag=1
                            #金額を入力（例外処理必要）
                            while(1):
                                try:
                                    in_money=int(input("your bet: "))
                                except ValueError:
                                    print("plz re input")
                                    #金額再入力用のwhileループにもう一回入るためのcontinue
                                    continue
                                print("max_bet",self.max_bet())
                                if (np.bet_change(in_money) == -1 or in_money > self.max_bet()):
                                    color_pr("red","plz re input less than " + str(min(np.money+np.tmp_bet,self.max_bet())))
                                    #金額再入力用のwhileループにもう一回入るためのcontinue
                                    continue
                                #ここにall-inの処理を入れる
                                if(self.bet>in_money):
                                    print("your bet is too small")
                                    color_pr("red","plz re input more than " + str(self.bet))
                                    #金額再入力用のwhileループにもう一回入るためのcontinue
                                    continue
                                if(self.bet == in_money):
                                    print("you call")
                                    break
                                #正しく入力できた時に金額再入力用のwhileループから抜け出すためのbreak
                                break
                                
                            if(in_money - np.tmp_bet == np.money):
                            #all-inの確認入れたい
                                print("all-in")
                                raise_flag=1
                                self.all_in_list.append(np)
                            np.bet_change(in_money)
                            self.bet=in_money
                            #print("np.tmp_bet",np.tmp_bet,"np.bet",np.bet)
                            np.moneyadd(-(np.bet-np.tmp_bet))
                            self.pod_money_add(np.bet-np.tmp_bet)
                            np.tmp_bet=np.bet
                            turn = self.turn_change(k+1)[:-1]
                            print("turn",turn)
                            last_turn=turn[-1]
                            #for文から抜け出すためのbreak
                            #print("break the for")
                            break
                        else:
                            #選択肢以外の入れられた時の例外処理必要
                            print("\nplz re input")
                            input_flag=1
                        
                    if(np == last_turn):
                        end_flag=1
                        #for文を終わらすためのbreak
                        break
                    if(this_turn_raise_flag==1):
                        break
                    #次のkにするためのcontinue
                    #continue
                #テーブルベットの方が小さくて、所持金よりも小さいとき
                elif(self.bet - np.tmp_bet < np.money or raise_flag==0):
                    print("table_bet: ",self.bet)
                    input_flag=1
                    while(input_flag==1):
                        input_flag=0
                        choice = input("\ncheck, raise, fold: ")
                        #call,raise,foldから選ぶ
                        if choice == "check":
                            pass

                        elif choice == "fold":
                            #fold_flag立てる
                            self.fold_flag(k)
                        
                        elif choice == "raise":
                            raise_flag=1
                            this_turn_raise_flag=1
                            #金額を入力（例外処理必要）
                            while(1):
                                try:
                                    in_money=int(input("your bet: "))
                                except ValueError:
                                    print("plz re input")
                                    #金額再入力用のwhileループに入るためのcontinue
                                    continue
                                print("max_bet",self.max_bet())
                                if (np.bet_change(in_money) == -1 or in_money > self.max_bet()):
                                    color_pr("red","plz re input less than " + str(min(np.money+np.tmp_bet,self.max_bet())))
                                    #金額再入力用のwhileループに入るためのcontinue
                                    continue
                                #ここにall-inの処理を入れる
                                if(self.bet>in_money):
                                    print("your bet is too small")
                                    color_pr("red","plz re input more than " + str(self.bet))
                                    #金額再入力用のwhileループに入るためのcontinue
                                    continue
                                if(self.bet == in_money):
                                    print("you call")
                                    break
                                #無事に入力できたとき用のbreak
                                break
                            np.bet_change(in_money)
                            self.bet=in_money
                            np.moneyadd(-(np.bet-np.tmp_bet))
                            self.pod_money_add(np.bet-np.tmp_bet)
                            np.tmp_bet=np.bet
                            turn = self.turn_change(k+1)[:-1]
                            last_turn=turn[-1]
                            #for文から抜け出すためのbreak
                            #print("break the for")
                            break
                        else:
                            #選択肢以外の入れられた時の例外処理必要
                            color_pr("red","plz re input")
                            input_flag=1
                    if(np == last_turn):
                        end_flag=1
                        #for文を終わらすためのbreak
                        break
                    if(this_turn_raise_flag==1):
                        break
                #allinとfoldの選択肢のみ
                #テーブルベットが所持金以上のとき
                elif(self.bet-np.tmp_bet >= np.money):
                    print("table_bet: ",self.bet)
                    input_flag=1
                    while(input_flag==1):
                        input_flag=0
                        choice = input("\nall-in, fold: ")
                        #call,raise,foldから選ぶ
                        if choice == "all-in":
                            #table_betの方が大きいときのall-inにはtable_betの変更は必要ない
                            self.all_in_list.append(np)
                        #精算
                            np.bet_change(np.tmp_bet+np.money)
                            np.moneyadd(-(np.bet-np.tmp_bet))
                            self.pod_money_add(np.bet-np.tmp_bet)
                            np.tmp_bet=np.bet

                        elif choice == "fold":
                            #fold_flag立てる
                            self.fold_flag(k)
                        else:
                            print("plz re input")
                            break
                    
                #print("k: ",k," last_turn",last_turn )
                #print("turn:",turn)
                #last-turnの人が終わったら次のセクションへ
                if(k == last_turn):
                    return 1
                    end_flag=1
                    #for文を終わらせるためのbreak
                    break

    #foldしてない人に対して勝敗を決定する
    def judge_win(self,play):
        #生存している人リスト
        player_alive_list=self.alive_list()
        all_max_hands=[]
        for np in player_alive_list:
            max_hands=play.max_hands(np.show_hand()+self.flop)
            max_hand=play.strongest_card(max_hands)
            print("player-",np.name," max_hand:",max_hand)
            all_max_hands.append(max_hand)
        
        #全ての手からmax_scoreを選ぶ
        scores=[]
        for i in all_max_hands:
            scores.append(play.getscore(i))
        max_score=max(scores)
        win_players=[i for i, x in enumerate(scores) if x == max_score]
        if(len(win_players)==1):
            return [[all_max_hands[win_players[0]]]],[player_alive_list[win_players[0]]]
        else:
            win_hands=[all_max_hands[i] for i in win_players]

            win=[player_alive_list[win_players[0]]]
            win_hand=[all_max_hands[win_players[0]]]
            for i in range(1,len(win_players)):
                #右の方が強い
                if(play.strength_compare(win_hand[0],all_max_hands[i])):
                    win_hand=[all_max_hands[i]]
                    win=[player_alive_list[i]]
                #左の方が強い
                elif(play.strength_compare(win_hand[0],all_max_hands[i])==0):
                    pass
                #どっちもおんなじ
                elif(play.strength_compare(win_hand[0],all_max_hands[i])==-1):
                    win_hand.append([all_max_hands[i]])
                    win.append([player_alive_list[i]])

        return win_hand,win

    def pay_money(self,win):
        all_in_flag=0
        only_one_flag=0
        all_in_winner=[]
        not_all_in_winner=[]
        get=0
        for i in win:
            if i in self.all_in_list:

                all_in_flag=1
                all_in_winner.append(i)
            else:
                not_all_in_winner.append(i)
                
        if len(win)==1:
            only_one_flag=1

        #1人でかつall-inである
        if(only_one_flag and all_in_flag):
            for i in self.player_list:
                if(i == win[0]):
                    continue
                else:
                    if(i.bet <= win[0].bet):
                        win[0].moneyadd(i.bet)
                        self.pod_money_add(-i.bet)
                        get+=i.bet
                    else:
                        win[0].moneyadd(win[0].bet)
                        i.moneyadd(i.bet - win[0].bet)
                        self.pod_money_add(-i.bet)
                        get+=win[0].bet
            print("player",win[0].name,"get",": ",self.pod -win[0].bet)
        
        #1人でかつall-inでない
        elif(only_one_flag):
            win[0].moneyadd(self.pod)
            print("player",win[0].name,"get",": ",self.pod-win[0].bet)
            self.pod_money_add(-self.pod)
        
        #複数でかつall-inがいる
        elif(all_in_flag):
            pay=0
            win_bet={i:i.bet for i in win}
            win_bet_sorted=sorted(win_bet.items(), key=lambda x:x[1])
            all_bet={i:i.bet for i in self.player_list}
            count=0
            for key,value in win_bet_sorted.items():
                for key_a,value_a in all_bet.items():
                    if(i<=value):
                        pay+=i
                        all_bet[key_a]=0
                    else:
                        pay += value
                for k in win_bet.keys[count:]:
                    k.moneyadd(pay/len(win_bet.leys[count:]))
                
                count+=1
            
            self.pod_money_add(-self.pod)





            


            





            pass
        #複数であってall-inがいない
        else:
            for i in win:
                i.moneyadd(self.pod/2)
            self.pod_money_add(-self.pod)

                
            pass

        return 0



            

def color_pr(color,str):
    if(color=="green"):
        print( '\033[32m' + str + '\033[0m')
    elif(color=="blue"):
        print('\033[34m' + str + '\033[0m')
    elif(color=="red"):
        print('\033[31m' + str + '\033[0m')
    elif(color=="white"):
        print( '\033[37m' + str + '\033[0m')
    elif(color=="yellow"):
        print( '\033[33m' + str + '\033[0m')
    else:
        print(str)