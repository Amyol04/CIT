def findInitials(first, surname):
    first_initial = first[0].upper()
    surname_initial = surname[0].upper()

    initials = f"{first_initial}.{surname_initial}."

    return initials

def main():
    first = "Anne"
    surname = "Murphy"

    result = findInitials(first, surname)

    print("The initials are", result)

main()