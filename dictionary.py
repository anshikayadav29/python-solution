marks ={
    "Anamika":100,
    "Mini":56,
    "Rohan":23
}
#print(marks,type(marks))
#print(marks["Mini"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Anamika":88,"Renuka":100})
print (marks)
print(marks.get("Anamika"))