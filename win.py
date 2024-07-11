print("Welcome to the world largest show 'Kon Bane Ga Cror Pati'In this show you will win up to 10 cror")
w=input('''Are you ready
        1 Yes
        2 No
        ''')
if w=="1":
    a=input('''What is the capital of Pakistan
        A) Lahore       B)Karachi
        C) Islamabad    D)Faisalabad  
            ''')
    if a=="C":
        print("you won this round and now you qualify for second round")
    else:
        print("sorry wrong answer")
        exit()
        
    b=input('''In which year,Pakistan win first world cup 
            A)1987       B)1992
            C)1996       D)1999
            ''')
    if b=="B":
        print("you won this round and qualify for third round")
    else:
        print("sorry wrong answer")
        exit()
        
    c=input('''In which year, pakistan became the atomic power
            A)1988           B)1991
            C)1998           D)2001
            ''')
    if c=="C":
        print("You won this round and qualify for fourth round")
    else:
        exit()
    d=input('''What is the meaning of friend
            A)NO meaning      B)Love
            C)Enjoyment        D)Everything
            ''')
    if d=="A":
        print("congtatulation You won all round and the prize of RS 10 cror")
    else:
        print("sorry wrong answer")
        exit()
elif w=="2":
    exit()
else:
    print("invallid choice")
