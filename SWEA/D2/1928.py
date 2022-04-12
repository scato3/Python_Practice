from base64 import b64decode

T = int(input())
for tc in range(1, T+1):
    print('#{} {}'.format(tc, b64decode(input()).decode('UTF-8')))