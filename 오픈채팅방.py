#https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    id_table = {i.split(' ')[1]:i.split(' ')[2] for i in record if len(i.split(' '))==3}
    sp_record = [i.split(' ') for i in record]
    
    sp_record_no_change = [i for i in sp_record if i[0]!="Change"]
    answer = []
    for i in sp_record_no_change:
        res = ""
        res+=id_table[i[1]]
        if i[0]=="Enter":
            res+="님이 들어왔습니다."
        else:
            res+="님이 나갔습니다."
        answer.append(res)

    return answer