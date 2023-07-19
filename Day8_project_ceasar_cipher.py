alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your mmessage: \n").lower()
    shift = int(input("Type the shift number: \n"))
    if shift>26:
        shift = shift%26

    def ceaser(start_text,shift_amount, cipher_direction):
        end_text = ""
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                if cipher_direction == "decode":
                    new_position = position - shift_amount
                else:
                    new_position = position + shift_amount
            else:
                end_text += char
            end_text += alphabet[new_position]
        print(f"The {cipher_direction} text is {end_text}")
    ceaser(text, shift, direction)
    end = input("Type 'yes' if you want to go again, otherwise type 'no'").lower()
    if end == "no":
        should_continue = False
        print("Good Bye")

