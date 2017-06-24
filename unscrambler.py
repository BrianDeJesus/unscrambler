import argparse

def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--the_key', '-k', type=str, required=True)
    arg = parser.parse_args()
    return arg.the_key

#check if word is unscramblable
def is_in_dict(key, words):
    for word in words:
        if len(key) == len(word) and sorted(key) == sorted(word):
            return True
    return False

def find_and_unscramble(key):
    with open('scrabble-dictionary.txt', "r+") as f:
        words = f.read()
        words = words.split('\n')
    #key1 is the committed key
    key1 = [key.upper() for key in list(key)]
    key1 = ''.join(map(str, key1))
    unscrambled_words = []

    if is_in_dict(key1, words):
        for word in words:
            if len(key1) == len(word) and sorted(key1) == sorted(word):
                unscrambled_words.append(word)
        unscrambled_words = ', '.join(map(str, unscrambled_words))
        print("\nScrabble words that matched with {0}: {1}" .format(key, unscrambled_words))
    else:
        print("\nSorry, no such word matched with \"{}\"" .format(key))

def main():
    key = get_arg()
    find_and_unscramble(key)

if __name__ == "__main__":
    main()
