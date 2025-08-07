# 🔤 Anagram Finder in Python

A Python script that loads a dictionary file and finds all valid **anagrams** for every word in that dictionary. For example:  
`listen → silent, enlist, tinsel`  
`dog → god`  
`evil → live, veil, vile`

---

## 🚀 Features

- ✅ Reads words from any `.txt` dictionary file
- ✅ Finds **all possible anagrams** for each word
- ✅ Ignores duplicate anagram sets
- ✅ Skips self-matches (e.g., "stop" is not its own anagram)
- ✅ Optional saving to `.txt` file
- ✅ Clean, readable output

---

## 🧠 DSA Concepts Used

| Concept              | Purpose                                           |
|----------------------|---------------------------------------------------|
| **Set**              | Fast O(1) lookups for word existence             |
| **Permutations**     | Generates all possible rearrangements of letters |
| **Dictionary (dict)**| To store and print anagram groups cleanly        |
| **Checked set**      | Avoids processing duplicate anagram groups       |
| **File I/O**         | Reads from and optionally writes to a file       |

---

## 🛠️ Tech Stack

- Python 3.x
- No external libraries (uses `itertools`, `set`, and `dict`)

---

## 📄 Example Input (`words.txt`)

listen
silent
enlist
tinsel
inlets
evil
vile
veil
live
god
dog

---

## 💡 Example Output

All anagrams found:

dog: god
evil: live, veil, vile
listen: enlist, inlets, silent, tinsel
