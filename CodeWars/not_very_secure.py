def alphanumeric(password):
    return password.isalnum()

def alphameric1(pas):
    import re
    patten = re.compile('^[0-9a-zA-Z]+$')
    return patten.match(pas) is not None


