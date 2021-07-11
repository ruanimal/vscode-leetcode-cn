MAX_LEVEL = 0

def get_data(args):
    return 1

def process_data(level, data):
    return 2

def set_state(level):
    pass

def revert_state(level):
    pass

def recursion(level, args):
    # Termial
    if level > MAX_LEVEL:
        return

    set_state(level)
    data = get_data(args)
    process_data(level, data)
    revert_state(level)
