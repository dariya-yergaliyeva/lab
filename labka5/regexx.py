import re
fi='row.txt'
with open(fi, 'r', encoding='utf-8') as file:
    text = file.read()
#1
e1=re.match(r'a+b*', text)
print(e1)
#2
text2="abbb"
e2=re.match(r'ab{2,3}', text2)
print(e2)
#3
e3=re.findall(r'[a-z]+_[a-z]', text)
print(e3)
#4
e4=re.findall(r'[A-Z]+[a-z]+', text)
print(e4)
#5
text1 = "andron ab"
e5=re.fullmatch(r'^a.*b$', text1)
print(e5)
#6
e6=re.sub(r'[ ,.]', ':', text)
print(e6)
#7
w=text.split('_')
e7=w[0]+''.join(x.capitalize() for x in w[1:])
print(e7)
#8
e8 = re.findall(r'[A-Z][^A-Z]*', text)
print(e8)
#9
result9 = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
print(result9)
#10
e10 = re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()
print(e10) 