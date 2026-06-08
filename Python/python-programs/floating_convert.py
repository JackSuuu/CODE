
number = "110.1"


# convert floating point binary to decimal
def flo_convert(flo: str):
    base_flo = 0.5
    result = 0
    flo_arr = flo.split('.')
    int_part = int(flo_arr[0], 2)
    flo_part = flo_arr[1]
    for each in flo_part:
        if each == '1':
            result += base_flo
        base_flo /= 2
    result += int_part
    return result


print(flo_convert(number))
