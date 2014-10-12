w,h,m=256,256,64
print("P3"+str(w)+" "+str(h)+" 255")
for k in range(0,h):
     for b in range(0,w):
          c=z=(b/float(w)-.5)*3-.7+(k/float(h)-.5)*3j
          for i in range(0,(m+1)):
               z=z*z+c
               if abs(z)>2:break
          print i * 4 if i<m else 0,0,0