people=[
    {"name":"Prem","age":50},
    {"name":"sSurya","age":24},
    {"name":"Dk","age":60},
    {"name":"Shan","age":39}
]

people_name=[ data["name"] for data in people if data["age"]>40]
print(people_name)


nums=[1,2,3,4,5]
new=[ "Even" if n%2==0 else "Odd" for n in nums ]
print(new)

