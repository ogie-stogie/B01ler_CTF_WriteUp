# You can install these packages to help w/ solving unless you have others in mind
# i.e. python3 -m pip install {name of package}
from pwn import *
import codecs
from base64 import b64decode
from string import ascii_lowercase
import decrypt_bacon

HOST = "chal.ctf.b01lers.com"
PORT = 2008

r = remote(HOST, PORT)

lookup_table = {
    "a": "z",
    "b": "y",
    "c": "x",
    "d": "w",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "s",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "o",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "h",
    "t": "g",
    "u": "f",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "a",
}


def bacon(s):
    dict1 = decrypt_bacon.generate_dict()
    output = decrypt_bacon.decode(s, dict1)
    i = 0
    the_real_output = ""
    for letter in output:
        the_real_output += chr(ord(letter) + 32)
    print(output)
    print(the_real_output)
    return the_real_output


def rot13(s):
    shift = 13
    old_data = s
    decoded = ""
    for letter in old_data:
        raw_letter = ord(letter)  # change letter to unicode value
        if raw_letter > 64 and raw_letter < 91:  # only shift capital letters
            raw_letter = raw_letter - shift
            if raw_letter < 65:  # bring it back to the top of the capital letters
                raw_letter += 26
        elif raw_letter > 96 and raw_letter < 123:  # shift lowercase
            raw_letter = raw_letter - shift
            if raw_letter < 97:  # bring it back to the top of the lowercase
                raw_letter += 26
        shifted_letter = chr(raw_letter)
        decoded += shifted_letter
    return decoded


def atbash(message):
    cipher = ""
    for letter in message:
        # checks for space
        if letter != " ":
            # adds the corresponding letter from the lookup_table
            cipher += lookup_table[letter]
        else:
            # adds space
            cipher += " "
    print("Our msg{}", cipher)
    return cipher


def Base64(s):
    return b64decode(s).decode("utf-8")


if __name__ == "__main__":
    count = 0
    while True:
        r.recvuntil("Method: ")
        method = r.recvuntil("\n").strip()
        r.recvuntil("Ciphertext: ")
        argument = r.recvuntil("\n").strip()
        print(method)
        result = globals()[method.decode()](argument.decode())  # :)
        r.recv()
        r.sendline(result.encode())
        count += 1
        print(count)
        if count == 1000:
            print(r.recv())
            exit(0)
