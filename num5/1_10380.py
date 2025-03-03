for n in range(10000, 1000, -1):
    res = []
    digits = [int (d) for d in str(n)]
    a = int(digits[0] + digits[1]) # 14
    b = int(digits[1] + digits[2]) # 12
    c = int(digits[2] + digits[3]) # 12
    res.append(a) # [14]
    res.append(b) # [14, 12]
    res.append(c) # [14, 12, 12]
    res = sorted(res) # [12, 12, 14]
    number = str(res[1]) + str(res[2]) # 1214
    if number == '1517':
        print(n)
        break