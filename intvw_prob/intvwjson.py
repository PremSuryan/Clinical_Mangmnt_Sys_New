data = [
    {"id":1, "name":"Alice", "active":True},
    {"id":2, "name":"Bob", "active":False},
    {"id":3, "name":"Charlie", "active":True}
]

res=[]
for val in data:
    if val["active"] == True:
        res.append(val)

# print(res)

#-------------------------------------

dic = {"id":1, "name":"Alice", "active":True}
id, name, active = dic.values()
# print(name)

#-------------------------------------
employees = [
    {"name":"A","dept":"IT"},
    {"name":"B","dept":"HR"},
    {"name":"C","dept":"IT"}
]

dummy = {}

for emp in employees:
    dept = emp['dept']
    name = emp['name']

    if dept not in dummy:
        dummy[dept] = []

    dummy[dept].append(name)

# print(dummy)

#---------------------------

user = {
  "id":1,
  "profile":{
      "email":"a@test.com",
      "address":[{"city":"NY"},
                 {"city":"INDIA"}]
  }
}

# res = user['profile']['address']
res = user.get('profile',{}).get('address',[])
res = [re['city'] for re in res if re['city']]
# print(res)


#---------------------------------
orders = [
 {"user":"A","amount":100},
 {"user":"B","amount":50},
 {"user":"A","amount":70}
]

dummy = {}
for order in orders:
    user = order['user']
    amt = order['amount']

    if user not in dummy:
        dummy[user] = 0

    dummy[user] += amt

print(dummy)