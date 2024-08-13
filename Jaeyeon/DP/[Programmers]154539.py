from collections import deque
def solution(numbers):
    answer = []
    number=deque(numbers)
    while number:
        current= number.popleft()
        if number and current==max(number):
            answer.append(-1)
        else:
            for num in number:
                if num>current:
                    answer.append(num)
                    break
            else:
                answer.append(-1)   
    # for i in range(len(numbers)):
        # if numbers[i]==max(numbers[i:]):
        #         answer.append(-1)
        # else:
        #     for j in range(1,len(numbers[i:])):
        #         if numbers[i+j]>numbers[i]:
        #             answer.append(numbers[i+j])
        #             break
    return answer