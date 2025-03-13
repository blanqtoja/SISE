#odległość pomiędzy ciągami 10011101 i 10111001 wynosi 2.
def odleglosc():
    cnt = 0
    s1 = "10011101"
    s2 = "10111001"
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt

# podejmowanie decyzji o rozwoju węzła w algorytmie a*