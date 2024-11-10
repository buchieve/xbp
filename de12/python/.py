for i in range(1,4):
    print(i,"人目")

#　出力結果
# 1 人目
# 2 人目

    name=input("名前を教えて下さい")
    waist=input("腹囲は？")
    age=input("年齢は？")


    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>=86:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")



