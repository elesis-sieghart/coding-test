# 3 9 10 11 14 15 20 21 시간 초과
def solution(id_list, report, k):
    dic = {key : 0 for key in id_list}
    
    banned = [value.split()[1] for value in set(report)]
    result = [value for value in set(banned) if banned.count(value) >= k]
    # print('신고받을 놈들 :', dic)
    # print('신고받은 놈 :', banned)
    # print('유효 신고 받은 놈들 : ', result)
    
    mail = [value.split()[0] for value in set(report) if value.split()[1] in result]
    # print('메일 받을 놈들 : ', mail)
    
    for value in mail: dic[value]+=1
    # print('메일 받을 놈들을 dic에 count : ', list(dic.values()))
    return list(dic.values())