# ukazka riesenia na nete
# https://www.educative.io/answers/the-valid-parentheses-problem

# TOTO je riesenie podla videa
# vytvorenie globalnej premmennej
# konvencia: globalne premenne piseme velkymi pismenami
# vytvorim dict povolenych znakov, resp. zatvoriek
PAIRS = {"(": ")", "[": "]", "{": "}"}


def is_valid(string):
    # vytvorim prazdny "stack" datova struktura (v podstate pole/list)
    stack = []
    for one_char in string:
        if one_char in PAIRS.keys():
            # do stacku pridame "opacnu" zatvorku, cize pre key z dict pridame jeho value
            stack.append(PAIRS[one_char])
        else:
            # overenie ci stack je prazdny
            if len(stack) == 0:
                return False
            # podmienka ci aktualny znak sa nerovna znaku na "chvoste" konci stacku
            if one_char != stack[-1]:
                return False
            # !! musim odstarnit posledny pridany znak
            stack.pop()
    # overenie ci sa este nachadza dalsi znak v stacku
    # cize ukoncil som for cyklus a stack by mal byt prazdny
    if len(stack) > 0:
        return False
    return True


# definujem hlavnu funkciu
if __name__ == "__main__":
    # string = "()" # True
    string = "([{([([({{}})])])}])"  # True
    # string = "([{()])}])" # False
    # string = "([{)])"  # False
    print(is_valid(string))
