import json 
  
# Opening JSON file 
f = open('user.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
print(data)
print("----------------------------------")
print(type(data))
# Iterating through the json 
# list 
for i in data: 
    print(i,":",data[i]) 

print("----------------------------------")

print(data['username'])
print(data['password'])
print(data['api_secret'])
print(data['twoFA'])

print("----------------------------------")
username=data['username']
password=data['password']
api_secret=data['api_secret']
twoFA=data['twoFA']

print(username,password,api_secret,twoFA)
# Closing file 
f.close() 

