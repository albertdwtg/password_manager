def check_length(word: str, min_length: int = 8) -> bool:
    """Function that checks if a word is longer than a given length

    Args:
        word (str): word to check
        min_length (int, optional): Minimum length to have. Defaults to 8.

    Returns:
        bool: True if the length is greater or equal than min_length
    """
    if len(word) < min_length:
        return False
    else:
        return True

def check_uppercase(word: str) -> bool:
    """Function to check if there is any uppercase in a word

    Args:
        word (str): word to check

    Returns:
        bool: True if there is any uppercase in the word, False otherwise
    """
    res = any(ele.isupper() for ele in word)
    return res

def check_lowercase(word: str) -> bool:
    """Function to check if there is any lowercase in a word

    Args:
        word (str): word to check

    Returns:
        bool: True is any lowercase in the word, False otherwise
    """
    res = any(ele.islower() for ele in word)
    return res

def check_special_char(word: str) -> bool:
    """Function that checks if a word contains any special characters

    Args:
        word (str): word to check

    Returns:
        bool: True if there is a special character
    """
    for character in word:
        if not (character.isalpha() or character.isdigit()):
            return True
    return False

def check_if_digit(word: str) -> bool:
    """Function that checks if a word contains any digit

    Args:
        word (str): word to check

    Returns:
        bool: True if word contains any digit
    """
    for character in word:
        if (character.isdigit()):
            return True
    return False