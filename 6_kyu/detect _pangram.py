import string


def is_pangram(s):
    # a_z = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # for word in s.lower():
    #     if word in a_z:
    #         a_z.remove(word)
    # return True if not a_z else False
    return string.ascii_lowercase <= s.lower()


pangram = "The quick, brown fox jumps over the lazy dog!"

print(is_pangram(pangram))
