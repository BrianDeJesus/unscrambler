import argparse

def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('the_key')
    arg = parser.parse_args()
    return arg.the_key

# generator
def open_dictionary():
    with open('scrabble-dictionary.txt') as f:
        for word in f:
            yield word.strip()

def find_and_unscramble(key):
    unscrambled_words = []
    sorted_key = sorted(key)

    for word in open_dictionary():
        if len(key) == len(word) and sorted_key == sorted(word):
            unscrambled_words.append(word)

    if len(unscrambled_words) == 0:
        print("\nSorry, no such word matched")
    else:
        print("\nScrabble words that matched with input: ", ', '.join(unscrambled_words))

def main():
    key = get_arg().upper()
    find_and_unscramble(key)

if __name__ == "__main__":
    main()
