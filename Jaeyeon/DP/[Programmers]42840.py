def solution(answers):
    answer = []
    grade=[]
    def grades(person,answers):
        a=len(person)
        b=len(answers)
        submit=person*(b//a)+person[:b%a]
        count=0
        for i in range (len(answers)):
            if answers[i]==submit[i]:
                count+=1
        return count
    grade.append([1,grades([1,2,3,4,5],answers)])
    grade.append([2,grades([2, 1, 2, 3, 2, 4, 2, 5],answers)])
    grade.append([3,grades([3,3,1,1,2,2,4,4,5,5],answers)])
    
    grade.sort(key=lambda x: (-x[1], x[0]))
    highest=grade[0][1]
    for i in range(3):
        if grade[i][1]==highest:
            answer.append(grade[i][0])
    return answer