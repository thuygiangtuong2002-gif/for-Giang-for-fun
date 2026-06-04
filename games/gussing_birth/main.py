
# 結構分為「主選單」「遊戲函式」「main 入口」結構化，好擴充

def play_game():

    ANS = "2002/08/01"
    MAX_TRIES = 3   
    
    print("您好，進入猜生日遊戲")
    

    for i in range(MAX_TRIES):
        print(f"請問Thùy Giang的生日是多少？你有{MAX_TRIES-i}次機會可以猜喔")
        
        # 放入一個.strip()，以免使用者多輸入空格
        s = input().strip()

        if s == ANS:
            print("猜對！我愛你")
            break
        else:
            # 猜錯時給回饋，否則程式會直接進下一輪
            print("猜錯了，再試試看")
    
    # 如果迴圈全部跑完，還是沒有成功就給一個結束訊息，使用for...else:
    else:
        print(f"真可惜，答案是{ANS}")



    return 0



def main():
 
    print("Anh Kun, Muốn đi chơi không?")
    

    while True:
        print("1.玩")
        print("2.不玩離開")
        
        options = input("輸入數字: ").strip()
        # 如使用者輸入 " 1" 或 "1 "，有空白時，strip()會幫你清掉，程式就比較不容易出錯。
        if options == "1":
            play_game()
        elif options == "2":
            break
        else:
            print("輸入1或2喔！")
        
    
    print("很棒！期待下次的遊戲喔")


main()


    






