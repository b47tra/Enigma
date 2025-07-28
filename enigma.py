import string

rotor_1 = list("HJOTXERUPINSQVCDWBALYGMZFK")
notch_1 = "P"
rotor_2 = list("PNBDJHYESQKTIAFWVGZRUMLOCX")
notch_2 = "G"
rotor_3 = list("LGEYAQDPCTRXOKSFJVUWIMZBNH")
notch_3 = "O"
rotor_4 = list("MGINJDCZPVAUBWQYSLHRFTKOEX")
notch_4 = "N"
rotor_5 = list("PHBUELFVZQYMDGIRCSKAOXWTJN")
notch_5 = "F"
plugs = {
    'A': 'M', 'M': 'A',
    'B': 'Q', 'Q': 'B',
    'C': 'T', 'T': 'C',
    'D': 'R', 'R': 'D',
    'E': 'Y', 'Y': 'E',
    'F': 'L', 'L': 'F',
    'G': 'Z', 'Z': 'G',
    'H': 'P', 'P': 'H',
    'I': 'V', 'V': 'I',
    'J': 'W', 'W': 'J'
}

alphabet = list(string.ascii_uppercase)
reverse_alphabet = alphabet[::-1]

def rotate_left(x):
    return x[1:] + x[:1]

def rotate_right(x):
    return x[-1:] + x[:-1]

def inverse_rotor(x):
    return [alphabet[x.index(i)] for i in alphabet]

def reflector(x):
    return reverse_alphabet[alphabet.index(x)]

def enigma(txt, rotor_1, rotor_2, rotor_3, notch_1, notch_2, pos_1, pos_2, pos_3):
    cipher = ""
    rotor_1 = rotor_1[pos_1:] + rotor_1[:pos_1]
    rotor_2 = rotor_2[pos_2:] + rotor_2[:pos_2]
    rotor_3 = rotor_3[pos_3:] + rotor_3[:pos_3]
    rot_1_count = 0
    rot_2_count = 0
    rot_3_count = 0
    txt = txt.replace(" ", "")
    for i in txt:
        if rotor_1[0] == notch_1:
            rotor_2 = rotate_left(rotor_2)
        if rotor_2[0] == notch_2:
            rotor_3 = rotate_left(rotor_3)
        rotor_1 = rotate_left(rotor_1)
        rot_1_count += 1
        if rot_1_count % 26 == 0:
            rotor_2 = rotate_left(rotor_2)
            rot_2_count += 1
        if rot_2_count % 26 == 0 and rot_2_count != 0:
            rotor_3 = rotate_left(rotor_3)
            rot_3_count += 1
        inv_rotor_1 = inverse_rotor(rotor_1)
        inv_rotor_2 = inverse_rotor(rotor_2)
        inv_rotor_3 = inverse_rotor(rotor_3)
        if i in plugs.keys():
            i = plugs[i]
        i = rotor_1[alphabet.index(i)]
        i = rotor_2[alphabet.index(i)]
        i = rotor_3[alphabet.index(i)]
        i = reflector(i)
        i = inv_rotor_3[alphabet.index(i)]
        i = inv_rotor_2[alphabet.index(i)]
        i = inv_rotor_1[alphabet.index(i)]
        if i in plugs.keys():
            i = plugs[i]
        cipher += i
    cipher = ' '.join([cipher[i:i + 5] for i in range(0, len(cipher), 5)])
    return cipher

print(enigma("ENIGMA", rotor_1, rotor_2, rotor_3, notch_1, notch_2, 0, 0, 0))
