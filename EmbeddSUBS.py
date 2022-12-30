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
        
        
        #os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format(filename))
    else:
        continue
    
for filename in dir_list:
    if (filename.endswith(".srt")): #or .avi, .mpeg, whatever.
        DynamicArraysrt.append(filename)
        
        
        #os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format(filename))
    else:
        continue


#Problem=0
#x=0
#y=0
#pomoc=0

# print(DynamicArraymkv)
# print(DynamicArraysrt)
# print("")
# print(len(DynamicArraysrt))
# print(len(DynamicArraymkv))
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



#print(Pominietemkv)
#print(Pominietesrt)



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

        print("File is being converted to UTF-8 if necesserry...")
        os.system("enca -x utf8 -L polish \""+(DynamicArraysrtpaired[i])+"\"")
        #print("enca -x utf8 -L polish \""+(DynamicArraysrtpaired[i])+"\"")
        print("Preparing "+ str(i+1) +" file",end = "") 
        os.system("ffmpeg -i \""+(DynamicArraymkvpaired[i])+"\" -i \""+DynamicArraysrtpaired[i]+"\" -c copy -c:s ass -metadata:s:s:0 language=pol \""+DynamicArraymkvpaired[i][:-4]+" - EmbeddedSubs.mkv\" -hide_banner -loglevel error")
        print("         done")
        #print ("ffmpeg -i \""+(DynamicArraymkvpaired[i])+"\" -i \""+DynamicArraysrtpaired[i]+"\" -c copy -c:s srt -metadata:s:s:0 language=pol \""+DynamicArraymkvpaired[i][:-4]+"EmbeddedSubs.mkv\" -hide_banner -loglevel error")
        i+=1



# while x!=len(DynamicArraymkv) or y!=len(DynamicArraysrt) or pomoc != 2:
   
#     # print("")
#     # print(len(DynamicArraymkv))
#     # print(len(DynamicArraysrt))
    
#     # print("")   
    
#     print("")
#     print("Teraz rozpatrujemy:")

#     print(len(DynamicArraymkv))
#     print(DynamicArraymkv[3])
#     print(DynamicArraymkv[x])
#     print(DynamicArraysrt[y])
#     print("")   
#     print('pomoc='+str(pomoc))
#     print('x='+str(x))
#     print('y='+str(y))
#     print(len(DynamicArraymkv))
#     print(len(DynamicArraysrt))

#     if(DynamicArraymkv[x][:-4] != DynamicArraysrt[y][:-7]):
#         print('x='+str(x))
#         print('y='+str(y))
#         print(len(DynamicArraymkv))
#         print(len(DynamicArraysrt))
#         # print('DYNAMIC ARRAYs:')
#         # print(DynamicArraymkv)
#         # print(DynamicArraysrt)
#         if DynamicArraymkv[x][:-13] != FolderNameNoBrackets:
            
#             # print(DynamicArraymkv[x]+" != "+FolderNameNoBrackets)
#             # print(DynamicArraymkv[x][:-13]+" != "+FolderNameNoBrackets)
#             #print("pominieto "+DynamicArraymkv[x])
#             Pominietemkv.append(DynamicArraymkv[x])
#             if(len(DynamicArraymkv[x])-1==x):
#                 del DynamicArraymkv[x]
#                 x-=1
#             else:    
#                 del DynamicArraymkv[x]
                
#             # print("pominieto mkv x="+str(x))
#             #Problem+=1
#             #x+=1
#         else:
#             if(x<len(DynamicArraymkv)-1):
#                 x+=1
            
            

#         if DynamicArraysrt[y][:-16] != FolderNameNoBrackets:
            
            
#             # print("pominieto srt y="+str(y))
#             #print("pominieto "+DynamicArraysrt[y])
#             Pominietesrt.append(DynamicArraysrt[y]),
#             # print(DynamicArraysrt[y]+" != "+FolderNameNoBrackets)
#             # print(DynamicArraysrt[y][:-16]+" != "+FolderNameNoBrackets)
#             if(len(DynamicArraysrt[x])-1==y):
#                 del DynamicArraysrt[y]
#                 y-=1
#             else:    
#                 del DynamicArraysrt[y]
            
#             #Problem+=1
#             #y+=1  
#         else:

#             if(y<len(DynamicArraysrt)-1):
#                 y+=1
#     else:
#         if DynamicArraysrt[y][:-16] == FolderNameNoBrackets:
        
            
            
#             if(y<len(DynamicArraysrt)-1):
#                 y+=1

            
#         if  DynamicArraymkv[x][:-13] == FolderNameNoBrackets:   
                
#             if(x<len(DynamicArraymkv)-1):
#                 x+=1

#         if(y==len(DynamicArraysrt)-1 and x==len(DynamicArraymkv)-1):
#                 print('kupa')
#                 print('x='+str(x))
#                 print('y='+str(y))
#                 print(len(DynamicArraymkv))
#                 print(len(DynamicArraysrt))
#                 print('kupa')



#                 print("")
#                 print("Teraz rozpatrujemy:")
#                 print(DynamicArraymkv[x])
#                 print(DynamicArraysrt[y])
#                 print("")   
#                 print('pomoc='+str(pomoc))
#                 print('x='+str(x))
#                 print('y='+str(y))
#                 print(len(DynamicArraymkv))
#                 print(len(DynamicArraysrt))
#                 print("pomagam")
#                 pomoc+=1
#                 # y+=1
#                 # x+=1
# k=0
# l=0 
# print('x='+str(x))

# while k<len(DynamicArraysrt) and l<len(DynamicArraymkv):
#     if(len(DynamicArraymkv)):
#         print(DynamicArraymkv[k])
#         k+=1
#     if(len(DynamicArraysrt)):
#         print(DynamicArraysrt[l])
#         l+=1


# print("\nZignorowano:")

# for i in Pominietemkv:
#     print(i)
 
# for i in Pominietesrt:
#     print(i)
   

#print()  


#print(FolderName)
#print(os.getcwd())
# print(DynamicArraymkv[1][:-4])
# print(DynamicArraysrt[1][:-7])

#i=0

##print("")
#while i<len(DynamicArraysrt):

#del DynamicArraymkv[2]
#print(DynamicArraymkv)

# print(DynamicArraymkv)

# # for filename in os.listdir():   
# #     if (filename.endswith(".mkv") and i<len(DynamicArraymkv)):

# #         print("Preparing "+ str(i+1) +" file",end = "") 
# #         os.system("ffmpeg -i \""+(DynamicArraymkv[i])+"\" -i \""+DynamicArraysrt[i]+"\" -c copy -c:s srt -metadata:s:s:0 language=pol \""+DynamicArraymkv[i][:-4]+"\"EmbeddedSubs.mkv -hide_banner -loglevel error")
# #         print("    "+str(i)+"     done")
# #         i+=1

#print(Problem)
#print("ffmpeg -i \""+(DynamicArraymkv[1])+"\" -i \""+DynamicArraysrt[1]+"\" -c copy -c:s srt -metadata:s:s:0 language=pol ouptut_english.mkv")

# if Problem>0:
#     if (filename.endswith(".mkv")): #or .avi, .mpeg, whatever.
#         os.system("ffmpeg -i "+(DynamicArraymkv[1])+" -i "+DynamicArraysrt[1]+" -c copy -c:s srt -metadata:s:s:0 language=pol ouptut_english.mkv")
#     else:
#         print('ffmpeg -i '+(DynamicArraymkv[1])+'-i' +DynamicArraysrt[1]+' -c copy -c:s srt -metadata:s:s:0 language=pol ouptut_english.mkv')
# else:
#      print('ffmpeg -i '+(DynamicArraymkv[1])+' -i ' +DynamicArraysrt[1]+' -c copy -c:s srt -metadata:s:s:0 language=pol ouptut_english.mkv')



#for x in DynamicArraysrt:   
#    print(x)
#for y in DynamicArraymkv:   
#    print(y)

#print(DynamicArraymkv[1])
#print(DynamicArraysrt[2])

   # if (filename.endswith(".mkv")): #or .avi, .mpeg, whatever.
    #    os.system("ffmpeg -i Gintama\ -\ s01e03.mkv -i Gintama\ -\ s01e03.pl.srt -c copy -c:s srt -metadata:s:s:0 language=pol ouptut_english.mkv")
        #os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png".format(filename))
    #else:
     #   continue