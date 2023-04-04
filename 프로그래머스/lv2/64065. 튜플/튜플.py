import re
def solution(s):
    s=re.sub("{","[",s)
    s=re.sub("}","]",s)
    s=sorted(eval(s),key=len)
    answer=[s[0][0]]
    for i in range(1,len(s)):
        answer.append(list(set(s[i])-set(s[i-1]))[0])
    return answer