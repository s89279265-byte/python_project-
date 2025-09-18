
#الترحيب  في المستخدم
name=str(input("ENTER YOUR NAME:"))
print(f"Welcom,{name}")
#ادخال النقاط للاعب 
point=int(input("ENTER YOUR POINT:"))
 #عمل fun من اجل زيادة النقاط بناء ع قاعده معينه
def points_status(point):
     if point >80:
         return point+2
     elif point in range(51,80):
         return point+5
     else:
         return point+10
new_point= points_status(point)  
#تحديد اذا كان الاعب خاسر ام فائز
if new_point>100:
    print('winner')
elif new_point  in range(51,100):
    print("close to winning")
else:
    print("loser")








