"""Message Encryption Module using Caesar Cipher

This module provides encryption and decryption functionality using 
the Caesar cipher algorithm with configurable shift values.
"""

def encode_message(message, shift):
    """Encode a message using Caesar cipher with given shift value
    
    Args:
        message (str): The message to encode
        shift (int): The shift value (0-25)
    
    Returns:
        str: Encoded message
    """
    encoded = ""
    for char in message:
        if char.isalpha():
            # Determine if uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and handle wrap-around
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encoded += shifted_char
        else:
            # Keep non-alphabet characters as they are
            encoded += char
    return encoded

def decode_message(coded_message, shift):
    """Decode a message using Caesar cipher with given shift value
    
    Args:
        coded_message (str): The coded message to decode
        shift (int): The shift value used during encoding (0-25)
    
    Returns:
        str: Decoded message
    """
    # Decoding is just encoding with negative shift
    return encode_message(coded_message, -shift)

def get_valid_shift():
    """Get a valid shift number from user
    
    Returns:
        int: Valid shift value between 0 and 25
    """
    while True:
        try:
            shift = int(input("Enter shift number (0-25): "))
            if 0 <= shift <= 25:
                return shift
            else:
                print("Please enter a number between 0 and 25.")
        except ValueError:
            print("Please enter a valid integer.")

def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n" + "="*40)
        print("SECRET CODE GENERATOR")
        print("="*40)
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        print("-"*40)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            encode_interface()
        elif choice == '2':
            decode_interface()
        elif choice == '3':
            print("Thank you for using Secret Code Generator! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def encode_interface():
    """Interface for encoding messages"""
    print("\n--- ENCODE MESSAGE ---")
    message = input("Enter the message to encode: ")
    shift = get_valid_shift()
    encoded_message = encode_message(message, shift)
    print(f"Original message: {message}")
    print(f"Encoded message: {encoded_message}")
    print(f"Shift used: {shift}")

def decode_interface():
    """Interface for decoding messages"""
    print("\n--- DECODE MESSAGE ---")
    coded_message = input("Enter the coded message to decode: ")
    shift = get_valid_shift()
    decoded_message = decode_message(coded_message, shift)
    print(f"Coded message: {coded_message}")
    print(f"Decoded message: {decoded_message}")
    print(f"Shift used: {shift}")

if __name__ == "__main__":
    main_menu()
