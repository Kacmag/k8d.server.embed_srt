#!/usr/bin/python3

import subprocess
import ffmpy
from array import array
import os

#path = "/"
dir_list = os.listdir()
dir_list.sort()
DynamicArraymkv=[]
DynamicArraysrt=[]
Pominietemkv=[]
Pominietesrt=[]

DynamicArraymkvpaired=[]
DynamicArraysrtpaired=[]

string1=os.getcwd()
string2=os.path.dirname(os.getcwd())

if string2 in string1:
    FolderName=string1.replace(string2,'')[1:]

FolderNameNoBrackets=FolderName[4:]

for filename in dir_list:
    if (filename.endswith(".mkv")): #or .avi, .mpeg, whatever.
        DynamicArraymkv.append(filename)
        
    else:
        continue
    
for filename in dir_list:
    if (filename.endswith(".srt")): #or .avi, .mpeg, whatever.
        DynamicArraysrt.append(filename)

    else:
        continue


print("Lista plikow:")

for mkv in DynamicArraymkv:
    #print(mkv)
    for srt in DynamicArraysrt:
        #print(srt)
        if(mkv[:-13]==FolderNameNoBrackets and srt[:-16]==FolderNameNoBrackets and mkv[:-4]==srt[:-7]):
            DynamicArraymkvpaired.append(mkv)
            DynamicArraysrtpaired.append(srt)
            print(mkv+"          "+srt)
            
          

Pominietemkv=DynamicArraymkv
Pominietesrt=DynamicArraysrt

for i in DynamicArraymkvpaired:
    if i in DynamicArraymkv:
        Pominietemkv.remove(i)


for i in DynamicArraysrtpaired:
    if i in DynamicArraysrt:
        Pominietesrt.remove(i)




if(len(Pominietemkv)==0 and len(Pominietesrt)==0):
    print("Brak zignorowanych plikow")

else:
    print("\nZignorowano:")
    for i in Pominietemkv:
        print(i)
    
    for i in Pominietesrt:
        print(i)
    print("")


i=0
for filename in DynamicArraymkvpaired:   
    if (filename.endswith(".mkv") and i<len(DynamicArraymkvpaired)):

        print("CO WYPISALA KONSOLA:")

        ps = subprocess.Popen(("ffmpeg","-i",DynamicArraymkvpaired[i],"2>&1"), stderr=subprocess.PIPE)
        output = subprocess.check_output(('grep','Stream #'), stdin=ps.stderr)
        ps.wait()
        
        #print(output)

        readfrom_output = output.decode("utf-8")

        print("ile wystapilo Subtitle:")
        print(readfrom_output.count('Subtitle'))
    

        print("")
        #ffmpeg -i "Boku no Hero academia - s02e03EmbeddedSubs.mkv" 2>&1 | grep "Subtitle:"

        print("File is being converted to UTF-8 if necesserry...")
        os.system("enca -x utf8 -L polish \""+(DynamicArraysrtpaired[i])+"\"")
        #print("enca -x utf8 -L polish \""+(DynamicArraysrtpaired[i])+"\"")
        print("Preparing "+ str(i+1) +" file",end = "") 
        os.system("ffmpeg -i \""+(DynamicArraymkvpaired[i])+"\" -i \""+DynamicArraysrtpaired[i]+"\" -map 0 -map 1 -c copy -c:s ass -metadata:s:s:"+str(readfrom_output.count('Subtitle'))+" language=pol \""+DynamicArraymkvpaired[i][:-4]+"EmbeddedSubs.mkv\" -hide_banner -loglevel error")
        print("         done")
        

        i+=1

