while True:

    user_country = input("What country are you from? ")

    match user_country:
        case "USA":
            print('Hello')
        case "India":
            print('Namaste')
        case "Germany":
            print('Hallo')
