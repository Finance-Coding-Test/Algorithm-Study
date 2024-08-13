# stack 사용 문제였던것
def solution(s):
    stack=[]
    
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])

    if stack:
        return 0
    else:
        return 1
# 시간초과 발생
# def solution(s):
#     list_s=list(s)
#     while list_s:
#         origin_s=list_s.copy()
#         for i in range(len(s)-1):
#             if list_s[i]==list_s[i+1]:
#                 del list_s[i:i+2]
#                 break
#         if list_s==origin_s:
#             break
#     return 1 if not list_s else 0
