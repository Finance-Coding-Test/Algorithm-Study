from collections import Counter
def solution(topping):
    dic=Counter(topping)
    # counter함수는 topping에 어떤 원소가 몇개 있나 dic 형태로 알려줌
    #ex) topping=[1,2,4,3,2,1,4]
    # Counter(topping)={1:2,2:2,3:1,4:2}
    set_dic=set()
    res=0
    for i in topping:
        dic[i]-=1
        # =>dic={1:1,2:2,3:1,4:2}
        set_dic.add(i)
        # =>set_dic=(1)
        if dic[i]==0:
            dic.pop(i)
        if len(dic)==len(set_dic):
            res+=1    
    return res