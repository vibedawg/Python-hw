#level1
#1
a=()
#2
bro=("Madi","Nuzhan","Aset")
print(bro)
sis=("Albina","Madina","Akniet")
print(sis)
#3
siblings=bro+sis
print(f"Full fam:{siblings}")
#4
print(len(siblings))
#5
family_members=("Alya","Nazar")
full_fam=siblings+family_members
print(full_fam)

#level2
#1
family_members = ("Madi","Nuzhan","Aset","Albina","Madina","Akniet","Alya","Nazar")
brother1 , brother2 , brother3 , sister1 , sister2 , sister3 , parent1 , parent2 = family_members
print(brother1)
print(brother2)
print(brother3)
print(sister1)
print(sister2)
print(sister3)
print(parent1)
print(parent2)
#2
fruits=("Banana","Mango","Kiwi")
vegetables=("Carrot","Potato","Onion")
meat=("Chiken","Beaf","Horsemeat")
food_stuff_tp=fruits+vegetables+meat
print(food_stuff_tp)
#3
food_stuff_tp=list(food_stuff_tp)
#4
food_stuff_tp = ("Banana","Mango","Kiwi","Carrot","Potato","Onion","Chiken","Beaf","Horsemeat")
print(food_stuff_tp[4])
print(food_stuff_tp[len(food_stuff_tp)//2])
#5
food_stuff_tp = ("Banana","Mango","Kiwi","Carrot","Potato","Onion","Chiken","Beaf","Horsemeat")
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[0:3])
print(food_stuff_lt[6:])
#6
food_stuff_tp = ("Banana","Mango","Kiwi","Carrot","Potato","Onion","Chiken","Beaf","Horsemeat")
del(food_stuff_tp)
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print('it is in nordic_countries')
else:
    print('it isn\'t in nordic_contries')

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if "Iceland" in nordic_countries:
    print('it is in nordic_countries')
else:
    print('it isn\'t in nordic_contries')

