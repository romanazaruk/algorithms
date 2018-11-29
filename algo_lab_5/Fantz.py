array_of_numbers = []
binary_input= '110011011'
input_number = 5

def generate_binary_array(target_number,array_length):
    i = 0
    binary_number = ""

    while binary_number.__len__() <= array_length :
        powered_number = pow(target_number, i)
        binary_number = bin(powered_number)[2:]
        array_of_numbers.append(binary_number)
        i += 1
        print(array_of_numbers.__len__())

def get_minimum_number(str):
    first_binary_number = 1
    count = 0

    while first_binary_number <= str.__len__():
        if str[:first_binary_number] in array_of_numbers:
            if first_binary_number is str.__len__():
                return 1

            seperate_numbers = get_minimum_number(str[first_binary_number:])

            if seperate_numbers is not 0:
                if count is 0 or count > seperate_numbers + 1:
                    count = seperate_numbers + 1

        first_binary_number += 1

    return count


generate_binary_array(input_number,binary_input.__len__())
print(get_minimum_number('110011011'))
print(bin(5))
