def get_count(input_str):
    num_vowels = 0
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    for i in input_str:
        if i in list_vowels:
            num_vowels += 1

    return num_vowels


print(get_count('o a kak ushakov lil vo kashu kakao'))
