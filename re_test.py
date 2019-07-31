import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

func = 'AddBonusToListFromArray(bytes32[],uint256[],uint256[])'
func1 = 'AddBonusToListFromArray(bytes32[])'

funcRegex = re.compile(r'(.*)\((.*)\)')

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.findall(message)

name = funcRegex.search(func1)
print(name.group())
print(name.group(2).split(','))

print(mo)
#print(mo.group())
