def get_formed_name(first, last):
    """Generate a nestly formed full name"""
    full_name = first+' '+last
    return full_name.title()

def get_new_name(first, last, middle=''):
    if middle:
        full_name = first+" "+middle+" "+last
    else:
        full_name = first+" "+last
    return full_name.title()