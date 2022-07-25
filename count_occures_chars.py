from collections import defaultdict

def input_string():
    string = input("Masukkan string: ")
    
    chars = count_characters(string)
    
    for key in chars:
        print(f"{key} : {chars[key]}")

def count_characters(string) :
    chars = defaultdict(int)
    for char in string :
        chars[char] += 1
    
    return chars


if __name__ == "__main__" :
    input_string()