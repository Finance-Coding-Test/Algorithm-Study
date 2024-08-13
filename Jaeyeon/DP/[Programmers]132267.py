def solution(a, b, n):
    answer = 0
    while n>=a:
        time=n//a
        n=n+time*(b-a)
        answer+=b*time
    return answer