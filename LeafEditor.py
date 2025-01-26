from sys import argv

print('* * *  DWAYNE \'LEAF\' JOHNSON  * * *')

path = argv[1]

FLAG = b'ri-hu'
OFFSET = 15

new_file = bytearray()

with open(path, 'rb') as file:
    new_file = buffer = bytearray(file.read(len(FLAG)))
    while buffer != FLAG:
        buffer = buffer[1:] + file.read(1)
        new_file.append(buffer[-1])
    new_file += file.read(OFFSET)
    level_size = int.from_bytes(file.read(1))
    level = int.from_bytes(file.read(level_size), 'little')

    print(f'- Current Leaf level is {level}.')
    while True:
        new_level = int(input('- What level should be set?\n> '))
        if new_level > 0:
            break
        print('- No.')

    print('- Give me a second!')

    size = 1
    while True:
        try:
            level_bin = new_level.to_bytes(size, 'little')
            break
        except OverflowError:
            size *= 2
            if size > 4:
                print('- The value is too big.\n- OverflowError')
                print('- Hit Enter to exit.')
                input()
                exit(0)

    size_bin = size.to_bytes(1)

    new_file += size_bin + level_bin
    new_file += file.read()

with open(f'{path}.modified', 'wb') as file:
    file.write(new_file)

print('- Done! Hit Enter to exit.')
input()