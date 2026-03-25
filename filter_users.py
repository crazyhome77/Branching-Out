import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """Filtert Benutzer nach Alter."""
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        # Wandlung zu Integer falls als String ankommt
        target_age = int(age)
        filtered_users = [user for user in users if user.get("age") == target_age]

        if not filtered_users:
            print(f"Keine Benutzer mit dem Alter {target_age} gefunden.")
        else:
            for user in filtered_users:
                print(user)

    except ValueError:
        print("Fehler: Bitte gib eine gültige Zahl für das Alter ein.")
    except FileNotFoundError:
        print("Fehler: Die Datei 'users.json' wurde nicht gefunden.")


def filter_users_by_email(email):
    """Filtert Benutzer nach E-Mail-Adresse."""
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        # Suche nach exakter E-Mail (case-insensitive)
        filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

        if not filtered_users:
            print(f"Keine Benutzer mit der E-Mail '{email}' gefunden.")
        else:
            for user in filtered_users:
                print(user)

    except FileNotFoundError:
        print("Fehler: Die Datei 'users.json' wurde nicht gefunden.")


if __name__ == "__main__":
    filter_option = input("Nach was möchtest du filtern? (name/age/email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Gib den Namen ein: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = input("Gib das Alter ein: ").strip()
        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Gib die E-Mail ein: ").strip()
        filter_users_by_email(email_to_search)

    else:
        print(f"Die Option '{filter_option}' wird noch nicht unterstützt.")