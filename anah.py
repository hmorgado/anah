def check(w1, w2):
    m1, m2 = {}, {}

    for i in w1:
        m1.update({i: w1.count(i)})

    print(m1)

    for i in w2:
        m2.update({i: w2.count(i)})

    print(m2)
    print(m1 == m2)

check("amor", "roma")