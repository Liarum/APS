import sys
sys.stdin = open('swe_4406.txt', 'r')

for t in range(1, int(input()) + 1):
    string = input()
    moeums = 'aeiou'
    N = len(string)
    ret = ''
    
    for i in range(N):    
        if string[i] in moeums:
            continue
        else:
            ret += string[i]
    
    print(f'#{t} {ret}')
