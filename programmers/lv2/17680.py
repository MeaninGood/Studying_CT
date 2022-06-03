size = 3
ref = [4, 2, 3, 4, 5, 6, 5, 4, 7]
che = []

for r in ref:
    if not r in che:
        if len(che) < size:
            che.append(r)
            print('사이즈 작을 때')
            print(che)
        else:
            print('============')
            che.pop(0)
            print(che)
            che.append(r)
            print(che)
            print('============')
    else:
        print('**********')
        che.pop(che.index(r))
        print(che)
        che.append(r)
        print(che)
        print('**********')
        