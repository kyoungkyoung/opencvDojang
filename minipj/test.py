def test():
    cnt = 2
    cnt2 = 3
    # if cnt == 2:
    angles = []
    for i in range(10):
        angles.append(i)
    
    # if cnt2 == 3:
    for i in range(2):
        for j in range(3):
            for angle in angles:
                print(angle)


test()