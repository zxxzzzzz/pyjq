import re
#print(re.match('(<input[^>]*)([>])','<input id="zzzz">').group(2))
s1 = re.sub('(<input[^>]*)([>])', lambda x: x.group(1) + '>' + '</input'+ x.group(2) , '<input id="zzzz">')
print(s1)
