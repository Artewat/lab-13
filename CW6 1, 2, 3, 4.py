
#Задание 1
rept = {"python" : " питон",
"anaconda" : "анаконда",
"tortoize" : " черепаха" }
rept["snake"] = " змея"
rept["tortoise"] = rept.pop("tortoize")
for key in rept:
    print(f"{rept[key].title().replace(" ", "")} по английски будет: {key}")



#Задание 2
cnt = ["Andorra", "Belarus", "Denmark",
"Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]
cntfh = []
for x in range(len(cnt)):
    a = []
    a.append(cnt[x])
    a.append(fh[x])
    cntfh.append(a)
print(dict(cntfh))



#Задание 3
pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
calc = []
for x in range(len(pairs)):
    a = []
    a.append(str(pairs[x]))
    a.append(pairs[x][0]*pairs[x][1])
    calc.append(a)
print(dict(calc))



#Задание 4
grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
'Ursula': 4, 'Viktor': 5}
excel = []
good = []
satisf = []
bad = []
for key in grades:
    print(f"Студент {key} имеет оценку: {grades[key]}")
    if grades[key] == 5:
        excel.append(key)
    if grades[key] == 4:
        good.append(key)
    if grades[key] == 3:
        satisf.append(key)
    if grades[key] == 2:
        bad.append(key)
print(f" 5: {excel}\n 4: {good}\n 3: {satisf}\n 2: {bad}")
    
    
