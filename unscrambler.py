import argparse

def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--the_key', '-k', type=str, required=True)
    arg = parser.parse_args()
    return arg.the_key


def find_and_unscramble(key):
    with open('scrabble-dictionary.txt') as f:
        words = f.read()
        words = words.split('\n')
    key = key.upper()
    unscrambled_words = []

    for word in words:
        if len(key) == len(word) and sorted(key) == sorted(word):
            unscrambled_words.append(word)
    unscrambled_words = ', '.join(map(str, unscrambled_words))

    if len(unscrambled_words) == 0:
        print("\nSorry, no such word matched")
    else:
        print("\nScrabble words that matched with input: ", unscrambled_words)



def main():
    key = get_arg()
    find_and_unscramble(key)

if __name__ == "__main__":
    main()
