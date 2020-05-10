# https://techdevguide.withgoogle.com/paths/advanced/compress-decompression#code-challenge

def find_end_bracket(s):

    numbrackets = 0
    for i in range(s.index('['), len(s)):
        if s[i] == '[':
            numbrackets += 1
        if s[i] == ']':
            numbrackets -= 1

        if numbrackets == 0:
            return i

def decompress(s):

    toreturn = ""

    i = 0
    # go through letters
    while i < len(s):
        if s[i].isalpha():
            toreturn += s[i]
            i += 1
        else:
            start_bracket = s.index('[')
            end_bracket = find_end_bracket(s)

            mult = int(s[i:start_bracket])

            toreturn += mult * decompress(s[start_bracket + 1:end_bracket])
            i = end_bracket + 1

    return toreturn


# print(find_end_bracket("5[as[[]]df]"))
print(decompress("b5[a2[f]]c"))

