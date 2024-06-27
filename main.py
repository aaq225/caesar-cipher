from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, cipher_direction):
    
    end_text = ""
    if cipher_direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            index = ( index + shift ) % len(alphabet)
            end_text += alphabet[index]
        else:
            end_text += char
    print(end_text)
             
    
loop = True
while loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  
    shift  = shift % 26
    caesar(text=text, shift=shift, cipher_direction=direction)
    
    restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart.lower() != 'yes':
        loop = False
        print("Goodbye!")
    
    