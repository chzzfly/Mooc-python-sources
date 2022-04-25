def greet(greeting, name):
    """returns a greeting

    Args:
        greeting (string): a greet word
        name (string): a persons name

    Returns:
        string: A greeting with a name
    """
    return f'{greeting} {name}'


print(greet("hello", "zhaohui"))
