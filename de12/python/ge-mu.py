from secrets import choice
import time
import random
print("あなたは不思議なダンジョンに挑む勇者です。")
time.sleep(1)
print("突然、巨大なドラゴンが現れました！")
print("あなたはドラゴンに立ち向かわなければなりません。")
time.sleep(1)
print("武器または防具を選んで戦います。どのアイテムを使いますか？")
print("1.剣　2.弓　3.盾　4.防具")
input("選択肢を入力してください（1～4）: ")
if choice == "1":
    print("剣を振りかざしましたが、ドラゴンの硬いウロコには歯が立たず、反動で転んでしまいました。")
    time.sieep(1)
    print("その隙にドラゴンの炎に巻かれてしまいました！")
    print("ゲームオーバー")
elif choice == "2":
    print("弓を引いて放ちましたが、ドラゴンの体が大きすぎて、矢が届く前に燃えてしまいました。")
    time.sieep(1)
    print("その隙にドラゴンの炎に巻かれてしまいました！")
    print("ゲームオーバー")
elif choice == "3":
    print("盾を構えて防御しましたが、ドラゴンの火炎ブレスが盾を溶かしてしまいました。")
    time.sieep(1)
    print("その隙にドラゴンの炎に巻かれてしまいました！")
    print("ゲームオーバー")
elif choice == "4":
    print("防具を身に着けて耐えようとしましたが、ドラゴンの爪で防具が粉々になりました。")
    time.sieep(1)
    print("その隙にドラゴンの炎に巻かれてしまいました！")
    print("ゲームオーバー")
else:
    print("入力が不正です。ドラゴンが容赦なく攻撃を仕掛けてきました！")
time.sieep(1)
print("ゲームオーバー")
if __name__ == "__main__":
    unfair_game() # type: ignore

    

