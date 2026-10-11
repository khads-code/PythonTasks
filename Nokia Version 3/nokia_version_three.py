def options_menu():
    while True:
        print("""
        1. Memory in use
        2. Type of view
        3. Memory status
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Memory in use")
            case '2':
                print("Type of view")
            case '3':
                print("Memory status")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def phone_book_menus():
    while True:
        print("""
        1. Search
        2. Services Nos
        3. Add name
        4. Erase
        5. Edit
        6. Copy
        7. Assign tone
        8. Send b card
        9. Options
        10. Speed dials
        11. Voice tags
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Search")
            case '2':
                print("Services Nos")
            case '3':
                print("Add name")
            case '4':
                print("Erase")
            case '5':
                print("Edit")
            case '6':
                print("Copy")
            case '7':
                print("Assign tone")
            case '8':
                print("Send b card")
            case '9':
                result = options_menu()
                if result == "home":
                    return "home"
            case '10':
                print("Speed dials")
            case '11':
                print("Voice tags")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def message_settings_no():
    while True:
        print("""
        1. Message centre number
        2. Message sent as
        3. Message validity
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Message centre number")
            case '2':
                print("Message sent as")
            case '3':
                print("Message validity")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def message_common():
    while True:
        print("""
        1. Delivery reports
        2. Reply via same centre
        3. Character support
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Delivery reports")
            case '2':
                print("Reply via same centre")
            case '3':
                print("Character support")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def message_settings_menu():
    while True:
        print("""
        1. Set
        2. Common
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                result = message_settings_no()
                if result == "home":
                    return "home"
            case '2':
                result = message_common()
                if result == "home":
                    return "home"
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_messages():
    while True:
        print("""
        1. Write messages
        2. Inbox
        3. Outbox
        4. Picture messages
        5. Templates
        6. Smileys
        7. Message settings
        8. Info service
        9. Voice mailbox number
        10. Service command editor
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Write messages")
            case '2':
                print("Inbox")
            case '3':
                print("Outbox")
            case '4':
                print("Picture messages")
            case '5':
                print("Templates")
            case '6':
                print("Smileys")
            case '7':
                result = message_settings_menu()
                if result == "home":
                    return "home"
            case '8':
                print("Info service")
            case '9':
                print("Voice mailbox number")
            case '10':
                print("Service command editor")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_show_call_duration():
    while True:
        print("""
        1. Last call duration
        2. All calls duration
        3. Received calls duration
        4. Dialled calls duration
        5. Clear timers
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Last call duration")
            case '2':
                print("All calls duration")
            case '3':
                print("Received calls duration")
            case '4':
                print("Dialled calls duration")
            case '5':
                print("Clear timers")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_show_call_cost():
    while True:
        print("""
        1. Last call cost
        2. All calls cost
        3. Clear counters
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Last call cost")
            case '2':
                print("All calls cost")
            case '3':
                print("Clear counters")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_call_cost():
    while True:
        print("""
        1. Call cost limit
        2. Show costs in
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Call cost limit")
            case '2':
                print("Show costs in")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_call_register():
    while True:
        print("""
        1. Missed calls
        2. Received calls
        3. Dialled numbers
        4. Erase recent call lists
        5. Show call duration
        6. Show call cost
        7. Call cost settings
        8. Prepaid credit
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Missed calls")
            case '2':
                print("Received calls")
            case '3':
                print("Dialled numbers")
            case '4':
                print("Erase recent call lists")
            case '5':
                result = menu_show_call_duration()
                if result == "home":
                    return "home"
            case '6':
                result = menu_show_call_cost()
                if result == "home":
                    return "home"
            case '7':
                result = menu_call_cost()
                if result == "home":
                    return "home"
            case '8':
                print("Prepaid credit")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def tones():
    while True:
        print("""
        1. Ringing tone
        2. Ringing volume
        3. Incoming call alert
        4. Computer
        5. Message alert tone
        6. Keypad tones
        7. Warning and game tones
        8. Vibrating alert
        9. Screen saver
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Ringing tone")
            case '2':
                print("Ringing volume")
            case '3':
                print("Incoming call alert")
            case '4':
                print("Computer")
            case '5':
                print("Message alert tone")
            case '6':
                print("Keypad tones")
            case '7':
                print("Warning and game tones")
            case '8':
                print("Vibrating alert")
            case '9':
                print("Screen saver")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_call_settings():
    while True:
        print("""
        1. Automatic redial
        2. Speed dialling
        3. Call waiting options
        4. Own number sending
        5. Phone line in use
        6. Automatic answer
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Automatic redial")
            case '2':
                print("Speed dialling")
            case '3':
                print("Call waiting options")
            case '4':
                print("Own number sending")
            case '5':
                print("Phone line in use")
            case '6':
                print("Automatic answer")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_phone_settings():
    while True:
        print("""
        1. Language
        2. Cell info display
        3. Welcome note
        4. Network selection
        5. Confirm SIM service action
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Language")
            case '2':
                print("Cell info display")
            case '3':
                print("Welcome note")
            case '4':
                print("Network selection")
            case '5':
                print("Confirm SIM service action")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_security_settings():
    while True:
        print("""
        1. PIN code request
        2. Call barring service
        3. Fixed dialling
        4. Closed user group
        5. Security level
        6. Change access codes
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("PIN code request")
            case '2':
                print("Call barring service")
            case '3':
                print("Fixed dialling")
            case '4':
                print("Closed user group")
            case '5':
                print("Security level")
            case '6':
                print("Change access codes")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_settings():
    while True:
        print("""
        1. Call settings
        2. Phone settings
        3. Security settings
        4. Restore factory settings
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                result = menu_call_settings()
                if result == "home":
                    return "home"
            case '2':
                result = menu_phone_settings()
                if result == "home":
                    return "home"
            case '3':
                result = menu_security_settings()
                if result == "home":
                    return "home"
            case '4':
                print("Restore factory settings")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_music():
    while True:
        print("""
        1. Music player
        2. Radio
        3. Recorder
        4. Track list
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Music player")
            case '2':
                print("Radio")
            case '3':
                print("Recorder")
            case '4':
                print("Track list")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def menu_clocks():
    while True:
        print("""
        1. Alarm clock
        2. Clock settings
        3. Date setting
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        0. Return
        99. Home
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                print("Alarm clock")
            case '2':
                print("Clock settings")
            case '3':
                print("Date setting")
            case '4':
                print("Stopwatch")
            case '5':
                print("Countdown timer")
            case '6':
                print("Auto update of date and time")
            case '0':
                return
            case '99':
                return "home"
            case _:
                print("Invalid")


def nokia_manual():
    while True:
        print("""
        ============== Main Menu ==============

        1. PhoneBook
        2. Messages
        3. Chat
        4. Call Register
        5. Tones
        6. Settings
        7. Call divert
        8. Music
        9. Games
        10. Calculator
        11. Reminders
        12. Clocks
        13. Profile
        14. Services
        15. SIM services
        0. Exit
        """)

        choice = input("Enter number: ")

        match choice:
            case '1':
                result = phone_book_menus()
                if result == "home":
                    continue

            case '2':
                result = menu_messages()
                if result == "home":
                    continue

            case '3':
                print("Chat")

            case '4':
                result = menu_call_register()
                if result == "home":
                    continue

            case '5':
                result = tones()
                if result == "home":
                    continue

            case '6':
                result = menu_settings()
                if result == "home":
                    continue

            case '7':
                print("Call divert")

            case '8':
                result = menu_music()
                if result == "home":
                    continue

            case '9':
                print("Games")

            case '10':
                print("Calculator")

            case '11':
                print("Reminders")

            case '12':
                result = menu_clocks()
                if result == "home":
                    continue

            case '13':
                print("Profiles")

            case '14':
                print("Services")

            case '15':
                print("SIM services")

            case '0':
                break

            case _:
                print("Invalid")


nokia_manual()
