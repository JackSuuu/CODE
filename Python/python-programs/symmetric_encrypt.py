
key = 4291362856

# if word encrypt Z overflow , goes back to A
# ord() 转换Ascii


def encrypt(a_key, text):
    count = 0
    encrypt_arr = []
    result = ''
    key_str = str(a_key)
    for each in text:
        if each != ' ':
            if 'A' <= each <= 'Z':
                if count >= len(key_str):
                    count = 0
                ascii_num = ord(each)
                ascii_num += int(key_str[count])
                if ascii_num > 90:
                    ascii_num -= 26
                encrypt_arr.append(chr(ascii_num))
                count += 1
            else:
                encrypt_arr.append(each)
        else:
            encrypt_arr.append(' ')
    for i in encrypt_arr:
        result += i
    return result


plain_text = "COMPUTER SCIENCE IS EXCITING!"
# print(encrypt(key, plain_text))


def decode(a_key, text):
    count = 0
    decode_arr = []
    result = ''
    key_str = str(a_key)
    for each in text:
        if each != ' ':
            if 'A' <= each <= 'Z':
                if count >= len(key_str):
                    count = 0
                ascii_num = ord(each)  # get the ascii value
                ascii_num -= int(key_str[count])
                if ascii_num < 65:
                    ascii_num += 26
                decode_arr.append(chr(ascii_num))
                count += 1
            else:
                decode_arr.append(each)
        else:
            decode_arr.append(' ')
    for i in decode_arr:
        result += i
    return result


encrypt_text = 'GQVQXZGZ XIMGWDH OU MCIMVROJ!'
print(decode(key, encrypt_text))
