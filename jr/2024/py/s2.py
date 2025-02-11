d = int(input())
r = -1

while True:
    try: n = int(input())
    except: break
    if d > n:
        d += n
    elif r == -1:
        r = d

print(r)
