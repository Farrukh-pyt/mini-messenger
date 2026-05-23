messages = []

print("Welcome to Mini Messenger")

while True:
    print("\n===== MENU =====")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Delete All Messages")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter your name: ")
        text = input("Enter your message: ")

        message = username + ": " + text
        messages.append(message)

        print("Message sent!")

    elif choice == "2":
        print("\n===== CHAT =====")

        if len(messages) == 0:
            print("No messages yet.")
        else:
            for msg in messages:
                print(msg)

    elif choice == "3":
        messages.clear()
        print("All messages deleted!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")

    else:
        print("Invalid choice")
