text = "aryan tewatia"
print(text.upper())
print(text.lower())
print(text.replace("aryan", "akshay"))
print(text.find("tewatia"))

num= [5,13,8,11]
num.append(10)
print(num)
num.remove(8)
print(num)
num.sort()
print(num)

person= ("aryan","rahul","aman")
print(person)
print(person[0])
print(person[1])

person = {
    "name":"aryan",
    "age":20,
    "branch":"CSE core"
}

print(person)
print(person["name"])
print(person["branch"])

subjects = {"Python","Java","SQL"}
subjects.add("C++")
print(subjects)
subjects.remove("Java")
print(subjects)