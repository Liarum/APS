# Software Expert Academy pb.5432 쇠막대기 자르기
T = int(input())

for t in range(1, T + 1):
    round_brackets = input()
    stack = []
    answer = 0
    for i in range(len(round_brackets)):

        if round_brackets[i] == '(':
            stack.append(i)
            answer += 1
        else:
            if i - stack[-1] == 1:
                tmp = stack.pop(-1)
                answer -= 1
                answer += len(stack)
            else:
                stack.pop(-1)

    print("#{} {}".format(t, answer))