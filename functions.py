
# ============= Function that check it is string or not =================
def is_string(input_val):
    """
    Checks if the input is a string.

    Parameters:
    input_val (any): The input to check.

    Returns:
    bool: True if the input is a string, False otherwise.
    """


# ============= Function that check it is integer or not =================
def is_integer(input_val):
    """
    Checks if the input is an integer.

    Parameters:
    input_val (any): The input to check.

    Returns:
    bool: True if the input is an integer, False otherwise.
    """
    return isinstance(input_val, int)


# ============= Function that check it is Character or not =================
def is_character(input_val):
    """
    Checks if the input is a single character.

    Parameters:
    input_val (any): The input to check.

    Returns:
    bool: True if the input is a single character, False otherwise.
    """
    return isinstance(input_val, str) and len(input_val) == 1



# ============= Function that check it is Boolean or not =================
def is_boolean(input_val):
    """
    Checks if the input is a boolean.

    Parameters:
    input_val (any): The input to check.

    Returns:
    bool: True if the input is a boolean, False otherwise.
    """
    return isinstance(input_val, bool)




# ================ Function that check keyword =================
def is_in_array(input_val, array):
    """
    Checks if the input is present in the array.

    Parameters:
    input_val (any): The input to check.
    array (list): The array to search.

    Returns:
    bool: True if the input is present in the array, False otherwise.
    """
    return input_val in array





