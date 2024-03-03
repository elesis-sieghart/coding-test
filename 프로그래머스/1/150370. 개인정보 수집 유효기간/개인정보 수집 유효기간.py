def solution(today, terms, privacies):
    # privacies를 반복문 돌아서 차일을 구한다.
    # 차일을 privacies의 terms와 매치해 결과를 도출한다.
    dict = {}
    t_year, t_month, t_day = list(map(int, today.split(".")))

    for term in terms:
        dict[term.split(" ")[0]] = int(term.split(" ")[1])
    
    answer = []
    for index, privacy in enumerate(privacies):
        p = privacy.split(" ")[0]
        p_year, p_month, p_day = list(map(int, p.split(".")))
        
        경과일 = 336*(t_year-p_year) + 28*(t_month-p_month) + t_day-p_day
        약관_경과일 = dict[privacy.split(" ")[1]] * 28
        if 경과일 >= 약관_경과일:
            answer.append(index+1)
    return answer