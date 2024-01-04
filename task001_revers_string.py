# Complete the solution so that it reverses the string passed into it.
#
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'
string = 'world'


def solution(string):
    rev = ''
    for i in string:
        rev = i + rev

    return rev

    pass


print(solution(string))


# Правильно

def solution(string):
    return string[::-1]

print(solution(string))
