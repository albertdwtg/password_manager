import bcrypt

def inverse_string(string_object: str) -> str:
    """Take a string in input and reverse it, to loose sense

    Args:
        string_object (str): string to invert

    Returns:
        str: string inverted
    """
    mid_word = len(string_object) // 2
    if((len(string_object) % 2) !=0) : 
        reverse_word = string_object[-(mid_word+1):] + string_object[:mid_word]
    else:
        reverse_word = string_object[-mid_word:] + string_object[:mid_word]
    return reverse_word

def string_to_unicode(string_object: str) -> str:
    """Function that converts a string object to its unicode, based on its characters

    Args:
        string_object (str): string object to convert

    Returns:
        str: unicode of the object, as a string
    """
    res = ""
    for character in string_object:
        res += str(ord(character))
    return res

def gen_salt(rounds: int=12) -> bytes:
    """Function that generates a salt

    Args:
        rounds (int, optional): Number of rounds to proceed for the salt creation. Defaults to 12, max 31

    Returns:
        bytes: salt created
    """
    return bcrypt.gensalt(rounds)

def hash_password(input_password: str,
                  shuffle_password: bool = True,
                  append_unicode: bool = True,
                  add_salt: bool = True,
                  salt_rounds: int = 12) -> bytes:
    
    final_password = input_password
    if shuffle_password:
        final_password = inverse_string(input_password)
    if append_unicode:
        final_password += string_to_unicode(final_password)
    
    final_password = final_password.encode('utf-8')
    if add_salt:
        salt = gen_salt(salt_rounds)
        final_password = bcrypt.hashpw(final_password, salt)
    else:
        final_password = bcrypt.hashpw(final_password)
    
    return final_password