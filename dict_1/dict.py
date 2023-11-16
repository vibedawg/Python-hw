#HW
#1
dog=dict()
print(dog)
#2
dog["name"]=["Rex"]
dog["color"]=["brown"]
dog["legs"]=4
dog["age"]=9
print(dog)
#3
student = {
    'first_name':'Akniet',
    'last_name':'Rakhymbai',
    'gender':'Women',
    'age':16,
    'coutry':'Qazaqstan',
    'is_married':False,
    'skills':['Works','Study','Cook','Drive'],
    'address': {
        'city':'Almaty',
        'street':'Maulenova',
        'num': 92
    }
}
print(student)
#4
print(len(student))
#5
print(student['skills'])
#6
student['skills'].append('Program')
print(student)
#7
student_keys=student.keys()
print(student_keys)
#8
student_value=student.values()
print(student_value)
#9
student_lists = student.items()
print(student_lists)

#10
print(student.pop('address'))

#11
del student
print(student)

print()


