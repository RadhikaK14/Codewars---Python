def to_camel_case(text):
    camel_case = list(text)
    for pos, i in enumerate(text):
        if i == '-' or i == '_':
            caps = text[pos + 1].upper()
            camel_case[pos+1] = caps
    camel_case = ''.join(i for i in camel_case if i !='-' and i !='_')
    return camel_case

word = to_camel_case('the_Cat-Is-evil')
print(word)