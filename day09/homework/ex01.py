print("Hello world!")

exit = False

words = []

while not exit :
    print("\n\n\n")
    print("단어 기록 프로그램의 기능은 다음과 같습니다.")
    print("1. 단어 삽입")
    print("2. 단어 출력")
    print("3. 프로그램 종료")
    in1 = input("작업 선택 : ")
    if "삽입" in in1 or in1 == "1" :
        while(True) :
            t = input("삽입할 단어 : ")
            #print(a.isdigit())
            if t == " " :
                print("입력이 잘못됐습니다.\n다시 입력해주세요.")
                continue
            else :
                words.append(t)
                break
    elif "출력" in in1 or in1 ==  '2' :
        if len(words) <= 0 :
            print("먼저 단어들을 입력해주세요.")
        else :
            i = 0
            while i < len(words) :
                #print("i =",i)
                print("words[{}] = {}".format(i,words[i]))
                i += 1
    elif "종료" in in1 or  in1 == '3' :
        print("프로그램을 종료합니다.")
        break
    else :
        print("메뉴를 보시고 다시 입력해주세요")








