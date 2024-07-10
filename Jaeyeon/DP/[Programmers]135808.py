def solution(k, m, score):
    answer = 0
    score.sort(key=lambda x:-x)
    a=len(score)//m
    for i in range (a):
        answer+=min(score[m*i:m*i+m])*m
    return answer