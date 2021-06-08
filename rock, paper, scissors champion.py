# -*- coding: utf-8 -*-

from random import randint

hands = {0:"グー", 1:"チョキ", 2:"パー"}
judge = ["DRAW", "LOSE", "WIN"]

hp = 5
cp_hp = 5

while True:
    print("\nあなたのHPは{}です\n相手のHPは{}です".format(hp,cp_hp))

    if hp <= 0:
        print("YOU LOSE")
        break
    if cp_hp <= 0:
        print("YOU WIN")
        break
    if hp and cp_hp <= 0:
        print("DRAW")
        break

    cp_hand = randint(0, 2)
    user_hand = input("0:グー 1:チョキ 2:パー 3:やめる")

    if user_hand == "3":
        print("Thanks for playing")
        break
    if user_hand not in ("0", "1", "2"):
        print("「0,1,2,3のどれか一つを入力してください」")
        continue
    user_hand = int(user_hand)
    

    print('-'*16)
    print("あなた:{}\nコンピュータ:{}".format(hands[user_hand], hands[cp_hand]))

    j = (user_hand - cp_hand + 3) % 3

    if j == 0:
        hp -= 1
        cp_hp -= 1
        print(judge[j]+":お互いに1ダメージ受けた!")
    if j == 1:
        hp -=2
        print(judge[j]+":相手に攻撃された!")
    if j == 2:
        cp_hp -= 2
        print(judge[j]+":相手に2ダメージを与えた!")
    print('-'*32)
    