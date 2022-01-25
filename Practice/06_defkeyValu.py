def parrot (kind, *argument, **keyword):
    print("Do u have any", kind, "?")
    print("--i am sorry, we are not", kind)
    for arg in argument:
        print(arg)
    
    print("-" * 40)

    for kw in keyword:
        print(kw, ":", keyword[kw])

parrot("wing", "Hello sir good morning", "Kem cho", "All right", Name= "Sarju Kathiriya", Status="Student")