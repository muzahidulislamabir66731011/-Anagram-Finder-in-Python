def load_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            words = {line.strip() for line in f if line.strip()}
        return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return set()

def find_anagrams(word, dictionary):
    from itertools import permutations
    anagrams = set()
    
    for p in permutations(word):
        joined = ''.join(p)
        if joined != word and joined in dictionary:
            anagrams.add(joined)
    
    return anagrams

def main():
    dictionary_file = input("Enter the dictionary filename (e.g., words.txt): ").strip()
    dictionary = load_words(dictionary_file)

    if not dictionary:
        print("No words loaded. Exiting.")
        return

    all_anagrams = {}
    checked = set()

    for word in dictionary:
        if word in checked:
            continue
        anagrams = find_anagrams(word, dictionary)
        if anagrams:
            all_anagrams[word] = anagrams
            checked.update(anagrams)
            checked.add(word)

    if not all_anagrams:
        print("No anagrams found for any word.")
        return

    print("\nAll anagrams found:\n")
    for word, anagrams in sorted(all_anagrams.items()):
        print(f"{word}: {', '.join(sorted(anagrams))}")

    save_choice = input("\nDo you want to save all anagrams to a text file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        filename = input("Enter the filename to save (e.g., all_anagrams.txt): ").strip()
        with open(filename, 'w', encoding='utf-8') as f:
            for word, anagrams in sorted(all_anagrams.items()):
                f.write(f"{word}: {', '.join(sorted(anagrams))}\n")
        print(f"All anagrams saved to '{filename}'")
    else:
        print("Not saved.")

if __name__ == "__main__":
    main()

    