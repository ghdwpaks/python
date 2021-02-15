if 1 == 1 :
    print("맞습니다1!")
    print("맞습니다2!")
    print("맞습니다3!")
print("if문이 끝났습니다.")

in1 = int(input("숫자를 입력해주세요 :")) 
if in1 > 10 :
    print("입력한 숫자가 10보다 큽니다!")
else :
    print("입력한 숫자가 10보다 작습니다.")



if in1 in (0,1,2,3,4,5,6,7,8,9) :
    print("1의 자리 숫자를 입력하셨습니다!")
else :
    print("입력하신 숫자가 1의 자리 양의 정수가 아닙니다!")

if type(in1) is int :
    print("입력하신것이 숫자입니다!")


    
print("프로그램을 끝냅니다.")