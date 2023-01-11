def solution(num_list, n):
    answer = []
    count = 0

    for i in range(len(num_list)//n):  
        answer.append(num_list[n*i:n*(i+1)])

    return answer