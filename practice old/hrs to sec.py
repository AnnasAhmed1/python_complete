##a=input("enter time in hh:mm:ss format")
##a=a.split(":")
##b=[]
##for i in range(len(a)):
##    x=int(a[i])
##    b.append(x)
##sec=b[0]*3600+b[1]*60+b[2]
##print(a,b,sec)



a=int(input("second"))
hh=a//3600
a=a-hh*3600
mm=a//60
a=a-mm*60
ss=a
print("%f:%f:%f",format(hh,mm))
