import hashlib

class Cobrelet:
    def __init__(self, salt=b'complex_salt_value'):
        self.salt = salt
        self.char_map = {
            'a': 'af4', 'b': 'b5z', 'c': 'k9', 'd': 'd3x', 'e': 'e7y',
            'f': 'f2g', 'g': 'g8h', 'h': 'h1j', 'i': 'i9k', 'j': 'j4l',
            'k': 'k0m', 'l': 'l3n', 'm': 'm7o', 'n': 'n2p', 'o': 'o6q',
            'p': 'p1r', 'q': 'q4s', 'r': 'r9t', 's': 's3u', 't': 't8v',
            'u': 'u2w', 'v': 'v7x', 'w': 'w1y', 'x': 'x5z', 'y': 'y0a',
            'z': 'z3b', 'A': 'A5C', 'B': 'B2D', 'C': 'C8E', 'D': 'D1F',
            'E': 'E7G', 'F': 'F4H', 'G': 'G9I', 'H': 'H0J', 'I': 'I3K',
            'J': 'J6L', 'K': 'K1M', 'L': 'L8N', 'M': 'M4O', 'N': 'N9P',
            'O': 'O2Q', 'P': 'P7R', 'Q': 'Q1S', 'R': 'R3T', 'S': 'S5U',
            'T': 'T9V', 'U': 'U0W', 'V': 'V4X', 'W': 'W6Y', 'X': 'X3Z',
            'Y': 'Y8A', 'Z': 'Z2B', '0': '019', '1': '120', '2': '231',
            '3': '342', '4': '453', '5': '564', '6': '675', '7': '786',
            '8': '897', '9': '908', ' ': 'xyz', '!': 'mno', '@': 'abc',
            '#': 'rst', '$': 'uvw', '%': 'ghi', '^': 'klm', '&': 'nop',
            '*': 'qrs', '(': 'tuv', ')': 'wxy', '-': 'def', '_': 'opq',
            '=': 'cde', '+': 'efg', '[': 'hij', ']': 'jkl', '{': 'lmn',
            '}': 'mno', '|': 'pqr', '\\': 'stu', ':': 'uvw', ';': 'wxy',
            '\'': 'yza', '"': 'bcd', '<': 'efg', '>': 'ghi', ',': 'hij',
            '.': 'jkl', '?': 'klm', '/': 'lmn', '`': 'mno', '~': 'nop'
        }

    def hash(self, data):
        transformed_data = ''.join(self.char_map.get(char, char) for char in data)
        data = self.salt + transformed_data.encode('utf-8')
        hashed_data = hashlib.sha256(data).digest()
        xor_result = bytearray(hashed_data)
        for i in range(len(xor_result)):
            xor_result[i] ^= xor_result[i - 1]
            xor_result[i] = (xor_result[i] + i) % 256
        final_hash = xor_result.hex()
        return final_hash

def main():
    print("*********************************")
    print("*           COBRELET             *")
    print("*   Made by Wyrizon | Version V0.1  *")
    print("*********************************")
    password = input("Please enter the text to encrypt: ")

    cobrelet = Cobrelet()
    encrypted_text = cobrelet.hash(password)

    print(f"Encrypted text: {encrypted_text}")

    # Keep the console open
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
