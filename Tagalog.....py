def find_smallest_factor(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return n

while True:
    try:
        print("________________________________________________")
        n = int(input("Enter a number that isn't a negative number: "))
        if n > 0:
            print(f"The smallest factor of {n} is {find_smallest_factor(n)}")
            print("________________________________________________")
        else:
            print("Invalid input. Enter a number greater than 0.")
            print()
            continue
    except ValueError:
        print()
        print("________________________________________________")
        print("Invalid input. Please enter a number.")
        continue


    while True:
        print()
        want_to_continue = input("Do you want to try another number? (yes/no): ").strip().lower()


        if want_to_continue in ('yes', 'y'):
            break
        elif want_to_continue in ('no', 'n'):
            print()
            print("________________________________________________")
            print("Program has ended.")
            print("Thank you for using the smallest factor finder!")
            print("________________________________________________")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
