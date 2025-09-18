#تم كتابة FUN يتم مناداته فقط في حالة اذا كان الطالب يريد المزيد من المواد
def add_extra_subjects(grades_dict):

    extra = int(input("How many extra subjects do you want to add? "))
    for i in range(extra):
        subject = input(f"Enter extra subject {i+1} name: ")
        mark = float(input(f"Enter {subject} grade: "))
        grades_dict[subject] = mark


# جملة ترحبيه
name = input("Enter your name: ")
print(f"Welcome, {name}! Let's calculate your grades.\n")

grades = {}   # عمل مكتبة من اجل حفظ العلامات و اسم الماده مثل مفتاح
i= 0     # العداد يبداء من صفر من اجل ع الاقل يجب ان بدخل 3 مواد
while i < 3:
    subject = input(f"Enter subject {i+1} name: ")
    mark = float(input(f"Enter {subject} grade: ")) # من الممكن ان تكون العلامه قيمة عشريه تحتوي ع فواصل
    grades[subject] = mark
    i += 1   # زيادة العداد عشان ما ندخل في infinite loop

#  بعد 3 مواد، نسأل المستخدم إذا بده يكمل يضغط ع الرقم واحد وفي حالة التوقف يج ان يتم الضغط ع الرقم صفر 
choice = int(input("Do you want to add more subjects? (1 = Yes, 0 = No): "))
if choice == 1:
    add_extra_subjects(grades)

# حساب المعدل
average = sum(grades.values()) / len(grades) # تم استخدام دالة ال value من اجل استدعاء العلامات فقط 

# تحديد مستوى الطالب
if average >= 85:
    grade = "Excellent"
elif average >= 70:
    grade = "Very Good"
elif average >= 60:
    grade = "Good"
elif average >= 50:
    grade = "Pass"
else:
    grade = "Fail"

# طباعة النتائج
print("Final Result")
print("Student:", name)
print("Grades:", grades)
print("Average:", average)
print("Final Grade:", grade)