x = "У Маши есть рыжая корова"

s = [x[i:i + 4] for i in range(0, len(x), 4)]

print (s)