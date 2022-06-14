import re
regex = r'\b[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'
def check(email):
    if(re.fullmatch(regex, email)):
        return email
    else:
        mail_id = input("enter valid mailid")
        check(mail_id)
    
    
    
def valid_password(password):
    u=0
    l=0
    d=0
    s=0
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if (len(password)>5 and len(password)<16):
        for i in password:
            if (i.isupper()):
                u=u+1
            if (i.islower()):
                l=l+1
            if (i.isdigit()):
                d=d+1
            if i in special_characters:
                s=s+1
    if(u>=1 and l>=1 and d>=1 and s>=1 and u+l+d+s==len(password)):
            return password
    else:
            p=input("enter valid password")
            valid_password(p)
    
    
def register():
    #check if user already exists
    print("-------------USER REGISTRATION----------",'\n')
    username = check(input("Please enter your username: "))
    password = valid_password(input("please enter pass: "))
    file = open("accountfile.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print("successfully registed")
    main()
    
def login():
    print("-------------USER LOGIN----------",'\n')
    username = input("Please enter your username")
    password = input("Please enter your password")  
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        print(username, password)
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            return True
    print("Incorrect credentials.")
    return False

def forgot_password():
    print("-------------FORGOT PASSWORD----------",'\n')
    username = input("Please enter your username")  
    for line in open("accountfile.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0]:
            print("here is your password : ",login_info[1])
            return True
    print("no username please register")
    register()

def main():
    print("choose one option")
    print("Registration-->  1")
    print("Login-->  2")
    print("Forgot Pass-->  3")
    l = int(input())
    if(l==1):
        register()
    elif(l==2):
        login()
    elif (l==3):
        forgot_password()
    else:
        print("please enter any of the above option")
main()
