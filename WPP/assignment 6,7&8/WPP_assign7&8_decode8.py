'''Decode the message:
A message containing the letters from A-Z can be encoded into the numbers using the mapping
A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits
and do the reverse mapping. You are required to display all the possible decoded messages.
For example: "11106" can be decoded into:
a. "AAJF" with the grouping (1 1 10 6)
b. "KJF" with the grouping (11 10 6)
'''

def decode_message(encoded_message):
    def decode_helper(index, current_decoded_message):
        if index == len(encoded_message):  
            decoded_messages.append(current_decoded_message)
            return

        if index < len(encoded_message):
            one_digit = int(encoded_message[index])
            if 1 <= one_digit <= 9:  
                decode_helper(index + 1, current_decoded_message + chr(one_digit + ord('A') - 1))

        if index + 1 < len(encoded_message):
            two_digits = int(encoded_message[index:index + 2])
            if 10 <= two_digits <= 26:
                decode_helper(index + 2, current_decoded_message + chr(two_digits + ord('A') - 1))

    decoded_messages = []
    decode_helper(0, "")
    return decoded_messages

def main():
    while True:
        encoded_message = input("Enter an encoded message (or 'exit'): ").strip()
        
        if encoded_message.lower() == 'exit':
            print("Exit")
            break

        if not encoded_message.isdigit():
            print("Invalid input. Please enter a valid encoded message containing only numbers.")
            continue
        
        decoded_messages = decode_message(encoded_message)
        
        if decoded_messages:
            print("All possible decoded messages:")
            for message in decoded_messages:
                print(message)
        else:
            print("No valid decoding possible for the given message.")

if __name__ == "__main__":
    main()


