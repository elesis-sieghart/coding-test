a, b = map(int, input().split())
print(abs(a-b))

# 시간 0ms: Fortran(1954), Pascal(1969), Lua(1993), C99(1999), C11(99후속, 2011), C++17(2018), Rust(2010), Kotlin(2011)
# 메모리: 저 중에서도 압도적인 메모리 Pascal(336KB)
# 메모리: 그외에는 C와 C++들(1112KB), Clang들(1124KB), Fortran(1408KB), Lua(9764KB), Rust들(13024KB), Kotlin(14256KB)
# 파이썬은 제일 빠른게 29056KB, 52ms 이었다.

'''
C99
C언어의 표준은 ANSI라는 이름의 미국 표준 협회에서 제정하고, 이렇게 ANSI에서 제정한 C언어의 1999년도 최신 표준안을 가리켜 C99라고 한다.
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=skout123&logNo=50115714050

Pascal, Delphi
흐름: Pascal 출시 -> Pascal로 개발할 수 있는 델파이 IDE 출시(1990년대) -> 영향력이 강해진 IDE 개발사
-> Pascal의 업그레이드 버전인 Object Pascal과는 별도로 IDE 개발사에서 Pascal에 독자적 기능을 업데이트(Object Pascal이라고 부르기 어려움) 
-> 시간이 흐르며 Object Pascal과 구분하기위해 Delphi언어라 부르게됨 -> 결론은 Delphi는 언어이자 IDE 입니다.
요약: 기본적인 문법은 파스칼 문법과 같지만 파스칼에 여러 기능들이 추가되어 현재는 델파이라는 언어로 존재
https://tech.devgear.co.kr/delphi_qna/451028
'''

# 참고로 C(1972), C++(1983), Java(1995), C#(2000)

'''
Pascal ? C ?
Pascal이 해결하려는 작업과 C가 해결하려는 작업이 달랐다.
Pascal: 당시의 슈퍼컴퓨터 시스템 대상 -> 적은 수의 기관이 장비 보유, 학계의 지지기반으로 학생들을 가르치는데 쓰임.
C: 전문적인 사용을 목표로 제작됨 -> 시스템 프로그래머가 시스템 프로그래밍을 수행하기위한 도구로 설계됨.
Pascal은 세계적으로 왈가왈부되어 많은 아종 구현이 있었고 이는 QA적으로 좋지못했다.
C는 심지어 Pascal의 기능들도 추가하며 성숙해졌다.
Pascal은 결국 업계 필수 기능이 부족해 시스템언어로 사용하기 어려웠다.

https://www.quora.com/What-is-the-difference-between-C-and-Pascal
'''
