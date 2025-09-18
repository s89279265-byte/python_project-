#جملة ترحبيه في الستخدم
name=str(input("Enter Your Name"))
print(f"Welcome,{name}:Letsstart entering the settings")
#سوف يتم انشاء قائمه من اجل حفظ الاعداد
numbers=[]
# الان سوف يتم استخدام جمل الدوران من اجل تسهيل عملية الدوران  لكن يجب ان يتم سؤال المستخدم عن عدد الارقام التي يجب ان يتم ادخالها
n=int(input("Enter The Number Of Number You Want TO Perfrom Operations:"))
for i in range(n):#بما انه لم يتم تحديد البدايه سوف يتم البدايه من الرقم 0
    number=float(input(f"ENTER NUMBER{i+1}"))
    numbers.append(number)#في كل مره يتم تخزين الرقم المدخل في القائمه
#البدء في عمل العمليات الحسابيه وفي التاكيد يتم استخدام ال builut in function
print("Average=",sum(numbers)/len(numbers))    
print("Sum=",sum(numbers))
print('Max=',max(numbers))
print('Min=',min(numbers))
# الان من اجل ان نعلم اذا كانت الاعداد الزوجيه اكثر او الفرديه نقوم في عمل عداد لكل واحد من اجل عملية المقارنه
x,y=0,0 # ا لبدايه من صفر 
for number in numbers:
    if number%2==0:
        x+=1
    else:
        y+=1
if x>y:
    print('Ther are more even numbers')
elif y>x:
    print("Ther are more odd numbers ")
else:
    print("even = odd")                
















