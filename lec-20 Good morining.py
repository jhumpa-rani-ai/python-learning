letter="hey my name is {1} and I m from {0}"
country="india"
name="yashna"
print(letter.format(country,name))
print(f"Hey my name is {name} and I am from { country}")
price= 49.09999
txt=f"For only price{price:2f} dollars!"
print(txt)
print(type(f"{2*30}"))