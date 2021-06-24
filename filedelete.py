import os
def deletefile():
    try:
        os.remove("C:/Users/Raj/Desktop/python/docu/cal.py")
    except:
        print("file doesnot exist")

def deletefolder():
    try:
        os.remove("C:/Users/Raj/Desktop/python/doc1/cal.py")
        os.rmdir("C:/Users/Raj/Desktop/python/doc1")
    except:
        print("folder doesnot exist")

def deletefolders():
    if os.path.exists("C:/Users/Raj/Desktop/python/doc1/cal.py"):
        os.remove("C:/Users/Raj/Desktop/python/doc1/cal.py")
    else:
        print("file doesnot exist")
    if os.path.exists("C:/Users/Raj/Desktop/python/doc1"):
        os.rmdir("C:/Users/Raj/Desktop/python/doc1")
    else:
        print("folder doesnot exist")
deletefolders()    
    

