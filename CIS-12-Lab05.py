# Lab 5 assignment from https://github.com/THartmanOfTheRedwoods/PyLab005

# Part 1: Conditional Validation of IP Addresses

# Task 1: Validating IP Address Parts

def is_valid_part(part):
    if part[0] == "0" and len(part) > 1:
        return False
    elif 0 <= int(part) <= 255:
        return True
    else:
        return False

# print(is_valid_part("010"))

# Task 2: Validating the Full IP Address

def is_valid_ip(ip):
    ip_parts = ip.split('.')
    ip_part_number = len(ip.split('.'))
    if ip_part_number == 4:
        for i in ip_parts:
            if not is_valid_part(i):
                print('Invalid IP Address')
            else:
                pass            # TODO always prints false even when it's true?
    else:
        print('Invalid IP Address, not enough parts.')

#print(bool(is_valid_ip("192.168.1.1")))
#print(bool(is_valid_ip("192.168.256.1")))
#print(bool(is_valid_ip("192.168.1")))
#print(bool(is_valid_ip("192.168.01.1")))

# Part 2: Recursion and Number Conversion

# Task 1: Convert Decimal to Binary (Recursion)

def decimal_to_binary(n):
    if n == 0:
        return 0
    elif n >= 1:
        decimal_to_binary(n // 2)
    print(n % 2, end = '')

# decimal_to_binary(34)

# Task 2: Convert Binary to Decimal (Recursion)

def binary_to_decimal(b):
    if b == 0:
        return 0
    elif b >= 1:
        return b % 10 + 2 * binary_to_decimal(b // 10)

# print(binary_to_decimal(111000))

# Part 3: Combining Recursion and Conditionals (optional)

# I was hopeful about doing this because I couldn't get the second part to work
# but the part I can't get to work is integral to this part so there goes that
# I'll try anyway...

def ip_to_binary(ipb):
    ip_num = str(ipb.split('.'))
    if len(ip_num) != 4:             #TODO gets caught on this
        return "Invalid IP Address."
    else:
        for i in range(len(ip_num)):
            is_valid_ip(i)
            if not is_valid_part(i):
                print('Invalid IP Address')
            else:
                for t in range(len(ip_num)):
                    decimal_to_binary(t)
                    return

# print(ip_to_binary("192.168.253.1"))

# looking online everyone imports "ipaddress" so I can't find anyone trying it
# manually for reference to see if I'm even going in the right direction...
# I know what I want to do, but I don't have the coding vocabulary to do it yet
# next time I won't miss lab even if I'm this ill