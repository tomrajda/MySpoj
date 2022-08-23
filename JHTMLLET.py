import re

txt = input()

regex = re.compile(r'<.*?>')

regexes = regex.findall(txt)

up_regexes = [x.upper() for x in regexes]

for replace in up_regexes:
    res = regex.sub(replace, txt)

print(res)


