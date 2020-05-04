from moviepy.editor import *

limit=200
sTime=1
etime=0
count=0
looper=True
while looper:
    orignal=VideoFileClip("Allu Arjun Aarya Video Songs - Edo Priyaragam Song.mp4")
    if etime <  orignal.duration-limit:
        etime=sTime+limit
    else :
        etime=orignal.duration
        looper=False
    fi=orignal.subclip(sTime,etime)
    stre="no{}.mp4"
    
    res=stre.format(count)
    count=count+1
    print(res)
    fi.write_videofile(res)
    fi.close()  
    sTime=etime
    if sTime==orignal.duration:
        break 

  
print("finish")
