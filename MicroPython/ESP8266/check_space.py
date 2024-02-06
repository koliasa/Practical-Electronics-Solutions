import uos

def get_free_space():
    try:
        stat = uos.statvfs('/')
        block_size = stat[0]
        free_blocks = stat[3]
        free_space_bytes = block_size * free_blocks
        return free_space_bytes
    except OSError as e:
        print('Error getting free space information:', e)
        return None

def format_bytes(bytes_value):
    return '{} bytes'.format(bytes_value)

def format_megabytes(bytes_value):
    megabytes = bytes_value / (1024 ** 2)
    return '{:.3f} MB'.format(megabytes)

def format_gigabytes(bytes_value):
    gigabytes = bytes_value / (1024 ** 3)
    return '{:.3f} GB'.format(gigabytes)

free_space = get_free_space()

if free_space is not None:
    print('Free space in bytes:', format_bytes(free_space))
    print('Free space in megabytes:', format_megabytes(free_space))
    print('Free space in gigabytes:', format_gigabytes(free_space))
