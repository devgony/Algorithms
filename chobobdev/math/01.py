# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

# 예제 입력 1 
# 734 893
# 예제 출력 1 
# 437
# 예제 입력 2 
# 221 231
# 예제 출력 2 
# 132
# 예제 입력 3 
# 839 237
# 예제 출력 3 
# 938

# Initial Thought(68ms)
def solution_1():
    a,b = input().split()
    if int(a[::-1]) > int(b[::-1]):
        print(int(a[::-1]))
    else:
        print(int(b[::-1]))

# Simillar to Soulution 1 (68ms)
def solution_2 ():
    a,b = input().split()
    a , b = int(a[::-1]) ,int(b[::-1])
    if a > b:
        print(a)
    else :
        print(b)

# Using lambda function (72ms)
def solution_3():
    a,b = map(lambda x : int(x[::-1]),input().split())
    if a > b:
        print(a)
    else :
        print(b)
        