s = (''.join([input().strip() for _ in range(int(input()))])).lower()

print('English' if s.count('t') > s.count('s') else 'French')
