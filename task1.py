"""
===================   TASK 1   ====================
* Name: Caesar Cipher
*
* Caesar Cipher is encryption technique in which
* each letter in the plaintext is replaced by a
* letter some fixed number of positions down the
* alphabet. The method is named after Julius Caesar,
* who used it in his private correspondence.
*
* Write a script that will accept number of positions
* that should be shifted down the Unicode code points
* of character. White spaces and punctuation marks
* should be ignored during encryption process.
*
* Hint: `ord()` returns integer representing Unicode
* code point for single character.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your functions here




def encrypt(word):


    broj_pomjeranja = input("Unesi broj: ")


    enc_word = ""
    zabranjene_rijeci = ["!", " ", ",", "."]
    for character in word:
        if character in zabranjene_rijeci:
            enc_char = character
        else:
            enc_char = chr(ord(character)+ broj_pomjeranja)
        enc_word += enc_char

    return enc_word

def decrypt(enc_word):



    word = ""
    zabranjene_rijeci = ["!", " ", ",", "."]


    for enc_char in enc_word:
        if enc_char in zabranjene_rijeci:
            character = enc_char


        else:
            character = chr(ord(enc_char)- broj_pomjeranja)
        word += character

    return word






if __name__ == "__main__":
    kriptovana_rijec = encrypt("Anja Andric 16!024")
    print(kriptovana_rijec)

    rijec = decrypt(kriptovana_rijec)
    print(rijec)
