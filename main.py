
students = { 
    'id1': {'name': "Dibas", 'class': 7, 'subject': "math"}, 
    'id2': {'name': "Pranjol", 'class': 7, 'subject': 'History'}, 
    'id3': {'name': "Dibas", 'class': 7, 'subject': "math"},
    'id4': {'name': "Sarah", 'class': 7, 'subject': 'English'}}

diction = {}
for key, value in students.items():
    if value not in diction.values():
        diction[key]=value

print(diction)
