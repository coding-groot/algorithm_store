def func(s):
    return s.count('0'), format(len(s.replace('0','')),'b')

def solution(s):
    zero_cnt = 0
    cnt = 0
    one_cnt = 0
    while one_cnt!=1:
        zero_cnt += func(s)[0]
        cnt +=1
        s= func(s)[1]
        if s=='1':
            one_cnt +=1
    answer = [cnt,zero_cnt]
    return answer