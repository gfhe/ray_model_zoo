def camel_to_kebab(camel_str):
    """
    驼峰转小写、中划线分隔
    """
    kebab_str = ''
    for i in range(len(camel_str)):
        if i == 0:
            kebab_str += camel_str[i].lower()
        elif camel_str[i].isupper():
            kebab_str += '-' + camel_str[i].lower()
        else:
            kebab_str += camel_str[i]
    return kebab_str


def rand_str():
    import random
    import hashlib
    val = random.randbytes(500)
    hash_value = hashlib.md5(val)
    return hash_value.hexdigest()[:6]
