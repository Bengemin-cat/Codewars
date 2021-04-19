import string


def alphabet_position(text):
    s_asci = string.ascii_lowercase
    ind_asci = [s_asci.find(i) for i in text.lower() if i in s_asci]
    return ' '.join(str(x + 1) for x in ind_asci)
    # return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position("The sunset sets at twelve o' clock."))
