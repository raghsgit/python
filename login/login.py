import getpass
import db

def main():
    
    while True:
        i=int(input(" 1=> add user, 2=> view user, 3=>remove user ,4=> view all 5=> quit"))
        if i==1:
            name=input("give user name: ")
            if db.contains(name):
                print("ERROR!! user {} already exists".format(name))
            else:
                pwd =getpass.getpass("give password:")
                pwd2 =getpass.getpass ("confirm passwd:")
                if pwd==pwd2:
                    db.add(name,pwd)
                    print("{} sucessfully added".format(name))
                    disc=input("give description:?? ")
                    db.adddisc(name,pwd,disc)
                else:
                    print("{} not added as typed password not matched".format(name))
        elif i==2:
            name=input("give user name: ")
            if db.contains(name):
                pwd=getpass.getpass("give password: ")
                if db.contain(name,pwd):
                    print("NAME:   ",name,'\nDISCRIPTION:   ',db.discription(name,pwd))
                else:
                    print("you entered a wrong password for user".format(name))
            else:
                print("user {} does not exist".format(name))
        elif i==3:
            name=input("give user name: ")
            if db.contains(name):
                pwd=getpass.getpass("give password: ")
                if db.contain(name,pwd):
                    db.delete(name,pwd)
                else:
                    print("you entered a wrong password for user {}".format(name))
            else:
                print("user {} does not exist".format(name))
        elif i==4:
            db.view()
        elif i==5:
            print("thank you")
            break
        else:
            print("not a choice")
    else:
        db.close()
if __name__=="__main__":main()

        
