while(1):
    print("1.Index\n2.Rindex\n3.Find\n4.Rfind\n5.Split\n6.Rsplit\n7.Replace\n8.Count\n9.exit")
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            text=input("Enter the string: ")
            sub=input("Enter the substring: ")
            print(f"First occurance is at {text.index(sub)}")
        case 2:
            text=input("Enter the string: ")
            sub=input("Enter the substring: ")
            print(f"Last occurance is at {text.rindex(sub)}")
        case 3:
            text=input("Enter the string: ")
            sub=input("Enter the substring: ")
            print(f"First occurance is at {text.find(sub)}")
        case 4:
            text=input("Enter the string: ")
            sub=input("Enter the substring: ")
            print(f"Last occurance is at {text.rfind(sub)}")
        case 5:
            text=input("Enter the string: ")
            sub=input("Enter the substring: ")
            print(f"Split order is {text.split(sub)}")
        case 6:
            text=input("Enter the string: ")
            sub=input("Enter the substring: ")
            print(f"Last split order is {text.rsplit(sub)}")
        case 7:
            text=input("Enter the string: ")
            old=input("Enter the substring: ")
            new=input("Enter the substring: ")
            print(f"First occurance is at {text.replace(old,new)}")
        case 8:
            text=input("Enter the string: ")
            sub=input("Enter the substring: ")
            print(f"Occurances is {text.count(sub)}")
        case 9:
            exit(1)
        case _:
            print("Invalid choice!")