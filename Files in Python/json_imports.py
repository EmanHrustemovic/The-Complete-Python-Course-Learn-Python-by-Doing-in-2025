import json

'''HOW TO CONVERT FILE INTO JSON FILE'''
#file = open('friends_json.txt')
with open('friends_json.txt','r') as file :
    file_contents = json.load(file) # read the file and turns it into dictionary
    #file.close()

print(file_contents['friends'][0])

''' HOW TO CREATE NEW JSON FILE !!! '''
cars = [
    {'make' : 'Ford' , 'model' : 'Fiesta'},
    {'make' : 'Ford' , 'model' : 'Focus'}
]

with open('cars_json.txt','w') as new_file:
    json.dump(cars,new_file)
    #new_file.close()

'''Turn string into DICTIONARY'''

my_json_string = '[{"name" : "Alfa Romeo" , "released" : 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])