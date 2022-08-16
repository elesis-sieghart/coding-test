# 3 9 10 11 14 15 20 21 시간 초과
def solution(id_list, report, k):
    # 중복 신고 제거
    check_report = set(report)
        
    # 특정 유저 중 리포트 받은 사람의 리포팅 수 카운트
    result = [0] * len(id_list)
    
    for index, user in enumerate(id_list):
        for reporting in check_report:
            if(user == reporting.split()[1]): result[index] += 1
    
    # 리포팅이 k 이상인 사람 색출
    re = [id_list[index] if value>=k else 0 for index, value in enumerate(result)]

    # 신고자가 받는 메시지 카운트
    answer = [0] * len(id_list)
    for index, bannedUser in enumerate(re):
        for reporting in check_report:
            if(bannedUser == reporting.split()[1]): 
                answer[id_list.index(reporting.split()[0])] += 1
            
    return answer


# 다른 풀이
def solution(id_list, report, k):
    s1 = [s.split()[1] for s in set(report)]
    s2 = [s for s in set(s1) if s1.count(s) >= k]
    s3 = [s.split()[0] for s in set(report) if s.split()[1] in s2]
    return [s3.count(i) for i in id_list]

# 위 풀이 참조해서 한번 더 풀기
def solution(id_list, report, k):
    dic = {key : 0 for key in id_list}
    
    banned = [value.split()[1] for value in set(report)]
    result = [value for value in set(banned) if banned.count(value) >= k]
    # print('유효신고한 사람들 count dic :', dic)
    # print('신고받은 사람 :', banned)
    # print('유효신고받은 사람 : ', result)
    
    mail = [value.split()[0] for value in set(report) if value.split()[1] in result]
    # print('유효신고한 사람들 : ', mail)
    
    for value in mail: dic[value]+=1
    # print('유효신고한 사람들 count : ', list(dic.values()))
    return list(dic.values())

# dictionary
# 이중 for문 줄이기
# 한줄 for ~ if 만족하는 값을 list받기
