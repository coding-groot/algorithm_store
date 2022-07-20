import math
def solution(progresses, speeds):
    padding = [0]
    left_date = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    left_date = padding+left_date
    new = [i for i in range(1,len(left_date)) if left_date[i]>max(left_date[:i])]
    new.append(len(left_date))
    answer = [new[i]-new[i-1] for i in range(1,len(new))]
    
    return answer