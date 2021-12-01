# 문제 제목: 단어 뒤집기 2

# https://www.acmicpc.net/problem/17413


# 먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

# 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
# 문자열의 시작과 끝은 공백이 아니다.
# '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
# 태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고,
# '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다. 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

# 1. space bar를 만날 때까지 문자열을 받는다.
# 2. space bar를 만나면 그 전까지 담긴 문자열을 뒤집어 저장한다
# 3. '<'를 만날 경우 '>'를 만날 때까지 문자열을 저장한다
# 4. '>' 이후 나오는 문자열이 알파벳 또는 숫자 일 경우, '<' 또는 ' '를 만날 때까지 받는다.
# 5. '<' 또는 ' '를 만날 때 이전까지 담긴 알파벳을 꺼내 뒤집어 저장한다

S = input()

# 등호를 나타날 때
tmp, answer, check = "", "", False

for i in S:
    # case 1: 공백
    if i == ' ':
        # 등호가 닫혀있을 경우
        if not check:
            answer += tmp[::-1] + " "
            tmp = ""
        # 등호가 열려있을 경우
        else:
            answer += " "

    # case 2: 등호
    elif i == '<':
        check = True
        answer += tmp[::-1] + "<"
        tmp = ""
    elif i == '>':
        check = False
        answer += ">"

    # 알파벳 또는 숫자
    else:
        if check:
            answer += i
        else:
            tmp += i

answer += tmp[::-1]
print(answer)
