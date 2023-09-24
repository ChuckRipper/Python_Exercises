for i in range(1, 11):
    for j in range(1, 11):
        if int(input(f"{i}x{j}=")) != i*j:
            print("SPRÓBUJ JESZCZE RAZ")
            break
    else:
        continue
    break
else:
    print("SUKCES")
