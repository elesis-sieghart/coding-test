## input()  
파이썬에서 가장 자주 쓰는 입력 함수 

## sys.stdin.readline()  
하지만 입력 값을 많이 받을 때는 속도를 위해 해당 입력 함수를 사용하는게 좋다.  
→ 파이썬 알고리즘 문제를 풀때, 시간초과 에러가 나오는 경우 해결 방법  
  
기본적으로 readline()은 개행문자(줄 바꿈 문자)를 포함하고 있다.  
문자열 마지막에 개행문자의 공백을 처리하는 함수가 아래와 같다.  
#### rstrip(): 오른쪽 공백을 삭제
#### lstrip(): 왼쪽 공백을 삭제
#### strip(): 왼쪽, 오른쪽 공백을 삭제

### lambda: sys.stdin.readline().rstrip()
이와 같은 꼴로 자주 사용한다.  


[참고 링크](https://yang-wistory1009.tistory.com/54)

~ for _ in range(N)
_ 각각에대해 ~  
