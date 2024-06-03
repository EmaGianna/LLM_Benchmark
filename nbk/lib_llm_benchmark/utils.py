#lista a diccionario
def list_to_dict(in_list):
    """
    The function `list_to_dict` converts a list into a dictionary where the index of each element in the
    list becomes the key in the dictionary.
    
    :param in_list: Thank you for providing the code snippet. Could you please provide an example of the
    `in_list` that you would like to convert to a dictionary using the `list_to_dict` function?
    :return: The function `list_to_dict` is returning a dictionary where the keys are the indices of the
    elements in the input list `in_list`, and the values are the elements themselves.
    """
    dict_ = {}
    for i, valor in enumerate(in_list):
        dict_[i] = valor

    return dict_