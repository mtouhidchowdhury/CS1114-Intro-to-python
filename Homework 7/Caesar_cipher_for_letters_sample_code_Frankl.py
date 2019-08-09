##plain_text = input("Enter the plaintext (a positive integer) " )
##shift = int(input("Enter an integer between 0 and  9 " ))
##cipher_text = ""
##for cur_char in plain_text:
##    cur_cipher = int(cur_char) + shift
##    print (cur_cipher)
##    if cur_cipher >= 10 :
##        cur_cipher = cur_cipher - 10
##        #cur_cipher is now between 0 and 9, inclusive
##    cipher_text = cipher_text + str(cur_cipher)
##print(cipher_text)
##
###VERSION 2
##print("version 2: ")
##cipher_text = ""
##for cur_char in plain_text:
##    cur_cipher = (int(cur_char) + shift) % 10
##    print (cur_cipher)
##    cipher_text = cipher_text + str(cur_cipher)
##print(cipher_text)

print("version 3")
plain_text = input("Enter the plaintext (a string of capital letters):  " )
shift = int(input("Enter an integer between 0 and  25: " ))
cipher_text = ""
for cur_char in plain_text:
    cur_cipher = ord(cur_char) + shift
    print (cur_cipher)
    if cur_cipher >= 91 :  # shifted past 'Z'
        cur_cipher = cur_cipher - 26 # "wrap around"
        #cur_cipher is now between ord('A') and ord('Z'), inclusive
    cipher_text = cipher_text + chr(cur_cipher)
print(cipher_text)


#VERSION 4
print("version 4: ")
cipher_text = ""
for cur_char in plain_text:
    #cur_cipher = (int(cur_char) + shift) % 10
    shifted = ord(cur_char) - 65 + shift  #between shift and 25 + shift
    shifted_wrapped = shifted % 26  #between0 and 25
    regular_encoding = shifted_wrapped + 65
    cur_cipher = chr(regular_encoding)
    print (cur_cipher)
    #cipher_text = cipher_text + str(cur_cipher)
    cipher_text = cipher_text + cur_cipher
print(cipher_text)
