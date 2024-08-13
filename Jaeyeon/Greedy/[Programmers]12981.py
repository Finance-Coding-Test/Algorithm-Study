def solution(n, words):
    answer = []
    wrong=0
    wrong_person=0
    for i in range(1,len(words)):
        if (i==len(words)-1) and (words[i] not in words[0:i]):
            return [0,0]
        elif  (words[i-1][-1]!=words[i][0]) or (words[i] in words[0:i]):
            wrong=i+1
            break
    if wrong%n==0:
        wrong_person=n
    else:
        wrong_person=wrong%n
    answer=[wrong_person,i//n+1]
    return answer