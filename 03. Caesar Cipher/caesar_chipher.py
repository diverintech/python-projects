import string

import art

alphabet = list(string.ascii_lowercase)
print(art.logo)


def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        if encode_or_decode == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
        elif encode_or_decode == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode} result: {cipher_text}")


def ask_to_play_again():
    return (
        input(
            "Do you want to play again? Type 'yes' to continue or anything else to exit: "
        ).lower()
        == "yes"
    )


play_again = True
while play_again:
    encode_or_decode = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).lower()
    if encode_or_decode not in ["encode", "decode"]:
        print("Please choose a valid method and try again.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)
    caesar(text, shift, encode_or_decode)

    play_again = ask_to_play_again()

print("Goodbye")
