def countdown(start_number=10):
    for i in range(start_number, 0, -1):
        print(f"{i}", end=' ')
    print("Blast Off!")

countdown() 