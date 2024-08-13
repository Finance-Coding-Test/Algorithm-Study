def solution(x, y, n):
    answer = 0
    result=set()
    result.add(x)
    
    while result:
        if y in result:
            return answer
        else:
            result_cal=set()
            for i in result:
                if i+n<=y:
                    result_cal.add(i+n)
                if i*2<=y:
                    result_cal.add(2*i)
                if i*3<=y:
                    result_cal.add(i*3)
            answer+=1
            result=result_cal
    return -1