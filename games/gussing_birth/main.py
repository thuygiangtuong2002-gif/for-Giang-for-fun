def play_game():

    ANS = "2002/08/01"
    MAX_TRIES = 3   
    
    print("您好，進入猜生日遊戲")
    

    
    for i in range(MAX_TRIES):
        print(f"請問Thùy Giang的生日是多少？你有{MAX_TRIES-i}次機會可以猜喔")
        s = input()

        if s == ANS:
            print("猜對！我愛你")
            break
        

    



    return 0




def main():
 
    print("Anh Kun, Muốn đi chơi không?")
    

    while True:
        print("1.玩")
        print("2.不玩離開")
        
        options = input("輸入數字: ").strip()
        # 這邊strip()一定要加嗎? 測試
        if options == "1":
            play_game()
            break
        elif options == "2":
            break
        else:
            print("輸入1或2喔！")
        
    
    print("很棒！期待下次的遊戲喔")


main()


    






