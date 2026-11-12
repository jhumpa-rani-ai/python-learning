# # READING A FILE
# f=open('myfile.txt','r')  
# #r=read  , if we read  pdf ,jpg, imaginary file we have to use rb instead of r
# # print, (f)
# text=f.read()
# print(text)
# f.close

# WRITING A FILE
f=open("myfile.text","a")
f.write("hello,World!")
f.close()

with open("myfile.text","a") as f:
    f.write("\nHey I am inside with")