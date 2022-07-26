import threading
def printcube(num):
    print("cube:",num*num*num)
def printSquare(num):
    print("Square:",num*num)
if __name__=="__main__":
    t1=threading.Thread(target=printcube,args=(10,))
    t2=threading.Thread(target=printSquare,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done")
