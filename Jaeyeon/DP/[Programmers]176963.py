def solution(name, yearning, photo):
    answer = []
    map_dict={key:value for key, value in zip(name, yearning)}
    for i in range(len(photo)):
        total=0
        for j in range(len(photo[i])):
            if photo[i][j] in map_dict:
                total+=map_dict[photo[i][j]]
        answer.append(total)
    return answer