

class Mydataarray:
    uname=""
    upass=""
    udes=""
    def __init__(self,username,password,designation):

        self.uname=username
        self.upass=password
        self.udes=designation
        print("object created succesfully with instance variables uname upass and udes")

    def readdata(self):
        print("uname=",self.uname)
        print("upass=",self.upass)
        print("udes=",self.udes)

mydataarray=Mydataarray("arun","qwer","manager")
mydataarray1=Mydataarray("anu","asdf","clerk")
mydataarray2=Mydataarray("veena","zxcv","manager")

mydataarray.readdata()
mydataarray1.readdata()
mydataarray2.readdata()
