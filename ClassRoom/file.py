def create_binary_file(filename) :
    with open(filename, 'wb') as file:
        binary_data = bytearray([0x48, 0x65, 0x6C, 0x6a,])
        file.write(binary_data)


def print_binary_file(filename) :
    with open(filename, 'rb') as file :
        binary_cont = file.read()
        print("Content os the binary file : ")
        print(binary_cont)


filename = 'binary_file.bin'

create_binary_file(filename)

print_binary_file(filename)