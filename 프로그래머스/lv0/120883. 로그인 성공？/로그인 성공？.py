def solution(id_pw, db):
    for x in db:
        if id_pw[0] in x:
            if id_pw[1] == x[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

    answer = ''
    return answer