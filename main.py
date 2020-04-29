import cv2
import os 


def VidFrame(fname): 
    vidcap= cv2.VideoCapture(fname)
    success,image=vidcap.read()
    count=0
    print("Starting")
    while success:
        cv2.imwrite("./Result/frame"+str(count)+".jpg",image)
        success,image=vidcap.read()
        count+=1
        #print('Read frame: ',success)
    print("Done")

def listdir(fpath): 
    arr=os.listdir(fpath)
    for i in range(0,len(arr)):
        print(i,": ",arr[i])
    choice=input("Select file: ")
    fname=os.path.join(fpath,arr[int(choice)])
    return fname
    

def main():
    fpath='Video/'
    fname=listdir(fpath)
    VidFrame(fname)

    print("Hello")

if __name__ == "__main__":
    main()