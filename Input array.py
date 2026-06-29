
arr = list(map(int, input("Enter array elements: ").split()))


choice = int(input("Enter 1 for Ascending, 2 for Descending: "))

if choice == 1:
    arr.sort()
    print("Ascending order:", arr)
elif choice == 2:
    arr.sort(reverse=True)
    print("Descending order:", arr)
else:
    print("Invalid choice")