# person= {
#     'first_name':'Akniet',
#     'last_name':'Rakhymbai',
#     'age':16,
#     'coutry':'Qazaqstan',
#     'adult':False,
#     'address':'Maulenova 92',
#     'school':84,
#     'language':{'Kazakh Kazakh,Rission,English'},
#     'family': {
#         'sisters':['Madina,Albina'],
#         'brothers':['Madi,Nurzhan'],
#         'parents':['Nazar,Aliya']
#     }
# }
# person["fav_singer"]=["the weeknd","moldanazar","kental"]
# print(person)

# person["age"]=17
# print(person)

# person["age"]+= 1
# print(person)

# person['family']['sisters'].append('Symbat')
# print(person)


# print(person.get('coutry'))

# print('fav_subject' in person)


# print(person.items())



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


