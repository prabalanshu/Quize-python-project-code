def Reg():
    global store
    
    a=input("Enter Your Name: ")
    b=input("Enter Your Email: ")
    c=input("Enter Your Phone Number: ")
    d=input("Create Your Username: ")
    e=input("Create Your Password: ")
    store={"Name":a,"Email":b,"Phone Number":c,"Username":d,"Password":e}

def Login():
    
    global User,passs
    
    User=input("Enter Your Username: ")
    passs=input("Enter Your Password: ")
    if User==store['Username'] and passs==store['Password']:
        print("Welcome " + store['Name'] + " in Quiz")
        afterlog()
    else:
        print("something is wrong plz try again............. :)")
        Login()

def afterlog():
    print("[1]Quiz Room: [2]Search Room: [3]Logout:")
    cho=input("Choose the option:")
    if cho=="1":
        print("Welcome To Quiz Room:")
        quizroom()               
    elif cho=="2":
        print("Welcome To Search Room:")
        ser()
    elif cho=="3":
        print("Thank You For Visiting:" + store["Name"])
        logout()
    else:
        print("something is wrong plz try again ............. :)")
        afterlog()

def ser():
    book=("[1].C++   [2].C   [3].Ruby   [4].Jango   [5].Xml    [6].Javascript    [7].C#    [8].Kotalen    [9].Wordpress    [10].Java")
    a = input("Search the book : ")
    for x in book:
        if a in book:
            print("Welcome To: " + a)
            ser()
            break
        else:
            print("Something Went's Wrong Please Try Again...................... :)")
            afterlog()
            break

def quizroom():
    print("[1]PHP: [2]CSS: [3]HTML: [4]PYTHON:")
    cho=input("Choose the option:")
    if cho=="1":
        print("Welcome To PHP Qiuz:")
        php()
    elif cho=="2":
        print("Welcome To CSS Quiz:")
        css()            
    elif cho=="3":
        print("Welcome To HTML Quiz:")
        html()
    elif cho=="4":
        print("Welcome To PYTHON Quiz:")
        python()
    else:
        print("something is wrong plz try again............. :)")
        quizroom()

def php():
    print("[1].Full Form PHP ? \n[1]. preprossersor [2]. hypertext \n[3]. hypertextpreprossor [4]. none of these ")
    a=input("Choose Right Ans : ")

    if a=="3":
        ans="yes"
    else:
        ans="no"

    print("[2].What is PHP ? \n[1]. script lang. [2]. programming lang. \n[3]. scripting lang. [4]. none of these ")
    b=input("Choose Right Ans : ")
    if b=="3":
        ans1="yes"
    else:
        ans1="no"
    print("[3]. Who is the father of PHP? \n [1]. Drek Kolkevi    [2]. Rasmus Lerdorf    \n[3]. Willam Makepiece   [4]. List Barely")
    c=input("Choose Right Ans: ")

    if c=="2":
        ans2="yes"
    else:
        ans2="no"
    print("[4]. Which of the following is the correct syntax to write a PHP code? \n [1]. <?php ?>    [2]. < php >    \n[3]. < ? php ?>    [4]. <? ?>")
    d=input("Choose Right Ans: ")
    if d=="4":
        ans3="yes"
    else:
        ans3="no"
    print("[5]. Which of the following is the correct way to add a comment in PHP code?\n [1]. #    [2]. //    \n[3]. /* */    [4]. All of the mentioned")
    e=input("Choose Right Ans: ")
    if e=="4":
        ans4="yes"
    else:
        ans4="no"
    print("[6]. Which of the following is the default file extension of PHP files?\n [1]. .php    [2]. .ph    \n[3]. .xml    [4]. .html")
    f=input("Choose Right Ans: ")
    if f=="1":
        ans5="yes"
    else:
        ans5="no"
    print("[7].Which is the right way of declaring a variable in PHP?\n [1]. $3hello    [2]. $_hello    \n[3]. $this    [4]. $5_Hello")
    g=input("Choose Right Ans: ")

    if g=="2":
        ans6="yes"
    else:
        ans6="no"


    mylist=[ans,ans1,ans2,ans3,ans4,ans5,ans6]
    aps=[]
    for x in mylist:
        if x=="yes":
            aps.append(x)
    print("Your Scroe is : " , len(aps))
    afterlog()
         
def css():
    print("[1]. What is CSS ? \n [1].style sheet  [2]. casding sheet  \n[3]. it is use to design the webpage  [4]. none of these ")
    a = input("Choose Right Ans : ")

    if a=="3":
        ans="yes"
    else:
        ans="no"
        
    print("[2]. Full Form Of Css ? \n[1]. caasdstyle sheet  [2]. casdcasding sheet  \n[3]. cascading style sheet  [4]. none of these ")
    b =input("Choose Right Ans : ")
    if b=="3":
        ans1="yes"
    else:
        ans1="no"
    print("[3]. Which of the following tag is used to embed css in html page?\n [1]. <css>    [2]. <!DOCTYPE html>    \n[3]. <script>    [4]. <style>")
    c=input("Choose Right Ans : ")
    if c=="4":
        ans2="yes"
    else:
        ans2="no"
    print("[4]. Which of the following CSS selectors are used to specify a group of elements?\n [1]. tag    [2]. id    \n[3]. class    [4]. both class and tag")
    d=input("Choose Right Ans : ")
    if d=="3":
        ans3="yes"
    else:
        ans3="no"
    print("[5]. Which of the following CSS framework is used to create a responsive design?\n [1]. django    [2]. rails    \n[3]. larawell    [4]. bootstrap")
    e=input("Choose Right Ans : ")
    if e=="4":
        ans4="yes"
    else:
        ans4="no"
        
        
    mylist=[ans,ans1,ans2,ans3,ans4]
    aps=[]
    for y in mylist:
        if y=="yes":
            aps.append(y)
    print("Your Score is: ",len(aps))
    afterlog()
    
def html():
    print('[1]. Full Form Of HTML :\n[a]. no    [b]. yes    \n[c]. hypertextmarkup language     [d]. none of these')
    a = input("Choose an option: ")
    if a=="c":
        ans="yes"
    else:
        ans="no"
        
    print('[2]. What is use of Html :\n[a]. no    [b]. yes    \n[c]. use of html in making website    [d].none of thesse')
    b = input("Choose an option :")
    if b=="c":
        ans1="yes"
    else:
        ans1="no"
    print("[3]. Who is the father of HTML : \n [a]. Rasmus Lerdorf    [b]. Tim Berners-Lee    \n[c]. Brendan Eich    [d]. Sergey Brin")
    c=input("Choose an option :")
    if c=="b":
        ans2="yes"
    else:
        ans2="no"
    print("[4]. Which of the following is used to read an HTML page and render it : \n [a]. Web server    [b]. Web network    \n[c]. Web browser    [d]. Web matrix")
    d=input("Choose an option :")
    if d=="c":
        ans3="yes"
    else:
        ans3="no"
    print("[5]. Which of the following tag is used for inserting the largest heading in HTML : \n [a]. head    [b]. <h1>    \n[c]. <h6>    [d]. heading")
    e=input("Choose an option :")
    if e=="b":
        ans4="yes"
    else:
        ans4="no"
    
    mylist=[ans,ans1,ans2,ans3,ans4]
    aws=[]
    for x in mylist:
        if x=="yes":
            aws.append(x)
    print("Your Score is: ",len(aws))
    afterlog()
            

def python():
    print('[1]. What is PYHTON :\n[1]. python is good     [2]. python is bad    \n[3]. python is a high level programming language    [4]. none of these')
    a = input("Choose an option: ")
    if a=="3":
        ans="yes"
    else:
        ans="no"
        
    print('[2]. Python is a Case Sensitive Language:\n[1]. Yes    [2]. No    \n[3]. Both a and b    [3]. none of these')
    b = input("Choose an option: ")
    if b=="1":
        ans1="yes"
    else:
        ans1="no"
    print("[3].Who developed Python Programming Language:\n [1]. Wick van Rossum    [2]. Rasmus Lerdorf    \n[3]. Guido van Rossum    [4]. Niene Stom")
    c=input("Choose an option: ")
    if c=="3":
        ans2="yes"
    else:
        ans2="no"
    print("[4]. Is Python case sensitive when dealing with identifiers:\n [1]. no    [2]. yes    \n[3]. machine dependent    [4]. none of the mentioned")
    d=input("Choose an option: ")
    if d=="1":
        ans3="yes"
    else:
        ans3="no"
    print("[5]. Which of the following is the correct extension of the Python file:\n [1]. .python    [2]. .pl    \n[3]. .py    [4]. .p")
    e=input("Choose an option: ")
    if e=="3":
        ans4="yes"
    else:
        ans4="no"

    mylist=[ans,ans1,ans2,ans3,ans4]
    awp=[]
    for z in mylist:
        if z=="yes":
            awp.append(z)
    print("Your Score is: ",len(awp))
    afterlog()
        
def logout():
    Login()
                     
def About():
    
    a="Prabal"
    
    print("Developer Name:" + a)

    sv="1.25.253"

    print("Software Version:" + sv)

    cd="25.02.2025"

    print("Create Date:" + cd)

    des="This is a good software Ok"

    print("Description:" + des)

def softwareversion():
    sv = "1.2.00.56"
    print("Software Version : " + sv)
    name = "Prabal Pratap Singh"
    print("Developer Name : " + name)
    des = "This is a good Platform for Quiz :)"
    print("Description:" + des)

def choo():
    print("[1]Registration: [2]Login: [3]About: [4]Software Version:")
    cho=input("Choose the option:")
    if cho=="1":
        print("Welcome To Registration :========================================================================= ")
        Reg()
        choo()
    elif cho=="2":
        print("Welcome To Login :================================================================================ ")
        Login()
        #choo()
    elif cho=="3":
        About()
    elif cho=="4":
        softwareversion()
    else:
        print("Something Went's Wrong Please Try Again :)================")
        choo()

choo()

        



























    
    

