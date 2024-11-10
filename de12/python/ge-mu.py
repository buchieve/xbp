def start_game():
    print("=== 選択ゲーーム ===")
    print("あなたは奇妙な冒険に巻き込まれました。しかし、どの道を選んでも 、、、。")

    while True:
        print("\nあなたの選択肢:")
        print("1) 進む  2) 待つ  3) 攻撃する  4) 逃げる  5) ゲームを終了する")
        choice = input("選んでください（1, 2, 3, 4, または 5）：")

        if choice == "5":
            print("ゲームを終了します。")
            break
        elif choice in ["1", "2", "3", "4"]:
            print("何をしても運命は変えられません…。ゲームオーバーです")
        else:
            print("無効な入力です。")

if __name__ == "__main__":
    start_game()
