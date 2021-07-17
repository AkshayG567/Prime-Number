for i in range(25, 51) :
    if i > 2 :
        for j in range(2 , i ):
            if i%j == 0 :
                break
        else :
              print(i)
