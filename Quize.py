print("WELCOM TO THE QUIZE".center(100,"*"))
print('''this quize the mcq bassed quize every question having 4 option out of these one is correct
enter the number of right ans to answer the quwestion \n each question carry 2 marks  ''')
m1=0
enter=str(input("enter < y > to start the quize : "))
if "y" in enter  :
    print('''1. the highest indivedual score in ODI is \n a> m.s dhoni \n b> sachin tendulkar \n c> rohit sharma \n d> suresh raina  ''')
    ans1=input("enter your ans :")
    if "c" in ans1 :
        print("your ans is correct ")
        m1+=1
    else :
        print("your ans is wrong \n the correct ans is : c> rohit sharma ")
    print("2. which is the highest score of rohit sharma \n a> 164 \n b> 209 \n c> 200 \n d> 264")
    ans2=input("enter your ans : ")
    if "d" in ans2 :
        print("your ans is correct ")
        m1 += 1
    else :
        print("your ans is wrong \n tne correct ans is a>264")
    print("3. who score highest number of centuries in the histry of cricket \n a> sachin tendulkar \n b> rickey ponting  \n c> don bradman \n d> savrav ganguli")
    ans3=input("enter tour ans : ")

    if "a" in ans3:
        print("your ans is correct ")
        m1 += 1
    else:
        print("your ans is wrong \n tne correct ans is a> sachin tendulkar")
    print("4. how many centuries where scored by sachin tendulkar in his cricket carier \n a> 67 \n b> 100 \n c> 102 \n d> 89")
    ans4 = input("enter your ans : ")
    if "b" in ans4:
        print("your ans is correct ")
        m1 += 1
    else:
        print("your ans is wrong \n tne correct ans is b> 100")
    print("5. which cricketer known as little master \n a> sachin tendulkar \n b> virat kohli \n c> m.s dhoni  \n d> no one")
    ans5 = input("enter your ans : ")
    if "a" in ans5:
        print("your ans is correct ")
        m1 += 1
    else:
        print("your ans is wrong \n tne correct ans is a> sachin tendulkar")

    print("number of question attempted : 5 ")
    print("number of corect ans : ",m1)
    print("your score : ",m1*2)
else :
    print("thanks for visiting ")


