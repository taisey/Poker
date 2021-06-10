from poker_class import Poker,Player,Texas_Holdem,color_pr
from extract import extract
from strength_compare import strength_compare

play=Poker()
N=4
money=10000
player_list=[ Player() for i in range(0,N)]

for k,i in enumerate(player_list):
    i.is_human()
    i.moneyadd(money)
    i.name_set(k)

player_list[0].moneyadd(20000)
game=Texas_Holdem(player_list)

color_pr("red","game_start")
bb=game.bb
play.deckset()
#初期カード配る
for i in player_list:   
    i.get_hand(play.deal(2))
    game.get_hand(play.deal(5))


section = "preflop"
#preflopのBBとSBの処理
bb_num=0
sb_num=1
finish_flag=0
game.bet_bb()
player_list[bb_num].bet_change(bb)
player_list[sb_num].bet_change(bb/2)

while(finish_flag==0):
    #UTGからの順番に変更
    turn=game.turn_change(sb_num+1)
    if(game.action_flow(turn)==1):
        print("preflop-end\n")
        print("\npod: ",game.pod)
        print("-----------------\n")
    else:
        winner=game.alive_list()[0]
        print("winner_name",winner.name)
        finish_flag=1
        break

    color_pr("green","flop-start")
    game.show_hand(3)
    turn=game.turn_change(sb_num)

    if(game.action_flow(turn)==1):
        print("flop-end\n")
        print("\npod: ,",game.pod)
        print("-----------------\n")
    else:
        winner=game.alive_list()[0]
        print("\nwinner_name",winner.name)
        finish_flag=1
        break

    color_pr("green","turn-start")
    game.show_hand(4)
    turn=game.turn_change(sb_num)
    if(game.action_flow(turn)==1):
        print("turn-end\n")
        print("\npod: ",game.pod)
        print("-----------------\n")
    else:
        winner=game.alive_list()[0]
        print("\nwinner_name",winner.name)
        finish_flag=1
        break

    color_pr("green","river-start")
    game.show_hand(5)
    turn=game.turn_change(sb_num)
    if(game.action_flow(turn)==1):
        print("river-end")
        print("\npod: ",game.pod)
        print("-----------------\n")
    else:
        winner=game.alive_list()[0]
        print("\nwinner_name",winner.name)
        finish_flag=1
        break
    break

#勝敗判定
print("\njudge_start")
#for i in game.turn_change(0):
win_hand,win=game.judge_win(play)
print("win_hand:",win_hand)
print("win:",[i.name for i in win])
print("bet:",[i.bet for i in win])

game.pay_money(win)


#All inのときの処理
