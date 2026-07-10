Num_list="123456789"
s=Num_list[0:5]
print(s)

r=Num_list[:6]
print(r)

z=Num_list[3:9:2]
print(z)    
fruits= "apple,banana,cherry"
print(fruits.split(","))

Chai="  Garam Garam Chai  "
print(Chai.strip())
print(Chai.upper())
print(Chai.lower())
print(Chai.replace("Garam","Thanda"))
print(Chai.find("g"))
print(Chai.count("a"))

order=2
type="cheese"
for letter in type:
    print(letter)
print(f"I would like {order} {type} pizzas please.")

flowers=["rose","lily","jasmine"]
print(" , ".join(flowers))