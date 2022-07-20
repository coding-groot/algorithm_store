import math
def solution(progresses, speeds):
    left_date = [0] + [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    new = [i for i in range(1,len(left_date)) if left_date[i]>max(left_date[:i])]+[len(left_date)]
    answer = [new[i]-new[i-1] for i in range(1,len(new))]
    return answer