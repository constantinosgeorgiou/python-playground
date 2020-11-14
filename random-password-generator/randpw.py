from random import shuffle as random_shuffle
import secrets


def generate(length=16, uppercase=1, numbers=1, characters=1):
    """
    Generates a random password of given length. Default length (16)

    Arguments:
        uppercase:   Number of uppercase letters.  Default (1)
        numbers:     Number of numbers.            Default (1)
        characters:  Number of special characters. Default (1)

    """

    assert (
        length > (uppercase + numbers + characters)
    ), "length is less than the number of uppercase letters, numbers, characters combined"

    lowercase_list = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i",
        "j", "k", "l", "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    uppercase_list = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    numbers_list = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]

    characters_list = [
        "!", "@", "#", "$", "%", "^", "&", "*"
    ]

    password = []

    # Add uppercase letters to password
    for _u in range(uppercase):
        password.append(secrets.choice(uppercase_list))

    # Add numbers to password
    for _n in range(numbers):
        password.append(secrets.choice(numbers_list))

    # Add special characters to password
    for _c in range(characters):
        password.append(secrets.choice(characters_list))

    # Add lowercase letters to password
    for _i in range(length - uppercase - numbers - characters):
        password.append(secrets.choice(lowercase_list))

    # Shuffle password
    random_shuffle(password)

    return ''.join(password)


if __name__ == "__main__":

    length = int(input("Password length (default 16): ") or "16")

    uppercase = int(
        input("How many uppercase letters do you want? (default 1): ") or "1")

    numbers = int(input("How many numbers do you want? (default 1): ") or "1")

    characters = int(input(
        "How many special characters do you want? (default 1): ") or "1")

    pw = generate(length, uppercase, numbers, characters)

    print("\n 🔒 Keep this safe: ", pw)
