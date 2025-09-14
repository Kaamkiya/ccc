S = input()
N = int(input())

letters = []
amounts = []

for i, c in enumerate(S):
    if c.isnumeric():
        num = ""
        while i < len(S) and S[i].isnumeric():
            num += S[i]
            i += 1
        num = int(num)
        amounts.append(num)
        if i == len(S):
            break
        continue

    letters.append(c)

S = "".join([l * amounts[i] for i, l in enumerate(letters)])
print(S[N % len(S)])
