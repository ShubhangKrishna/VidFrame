import cv2

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

def main():
    fname='Video/ADev.mp4'
    VidFrame(fname)
    print("Hello")

if __name__ == "__main__":
    main()