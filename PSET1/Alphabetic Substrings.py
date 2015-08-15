s= raw_input('Enter:')
lengthS=len(s)
current = 1
char=''
result= ''

while current < lengthS:
    if len(char) < 1:
        char = s[current - 1]

    if s[current - 1] <= s[current]:
        char += s[current]

        if len(char)>len(result):
            result=char
    else:
        char=''

    current += 1

if len(result)==0:
    result = s[0]


print('Longest substring in alphabetical order is: ' + result)






