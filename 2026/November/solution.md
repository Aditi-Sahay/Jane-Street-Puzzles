# Solution — November 2026: Pressure Points

## 1. Overview

The November 2026 Jane Street Monthly Puzzle, *Pressure Points*, involves 76 scrambled letter sequences and 19 themes represented by emojis.

Each theme is associated with four words. The objective is to match these words to the scrambled sequences and identify the differences between their letters.

The central observation is that the sequences are not arbitrary: their letters correspond to the letters in the four words associated with each theme, with a specific pattern of additions and omissions.

## 2. Understanding the Structure

Each of the 19 themes contains four related words.

For every theme:

- Two words corresponds to a sequence containing exactly the same letters.
- One sequence contains one additional letter compared with its associated word.
- One sequence is missing one letter compared with its associated word.

Therefore, every theme follows this pattern:

| Match type | Number per theme |
|---|---:|
| Exact match | 2 |
| One additional letter | 1 |
| One missing letter | 1 |
| **Total** | **4** |

Across 19 themes, this accounts for all 76 sequences.

## 3. Matching Words to Sequences

The first challenge is comparing words and sequences without considering the order of their letters.

For example, `NORTH` and `HNORT` contain exactly the same letters, even though they are arranged differently.

To compare them programmatically, Python's `Counter` from the `collections` module is used.

```python
from collections import Counter

Counter("NORTH") == Counter("HNORT")
```

This returns `True` because both strings contain the same letter frequencies.

The comparison can identify three possible outcomes:

- `=`: The word and sequence contain exactly the same letters.
- `+`: The sequence contains one additional letter.
- `-`: The sequence is missing one letter.

Using letter frequencies rather than string positions makes it possible to identify these differences regardless of the original arrangement.

## 4. Applying the Theme Clues

The 19 emojis provide clues to the themes.

Each theme is associated with four words. For example, the *compass* theme contains:

- NORTH
- EAST
- SOUTH
- WEST

These words are compared against the available sequences.

The same process is repeated for all themes, using their respective four associated words.

The key constraint is that every theme must produce exactly two exact matches, one additional-letter match, and one missing-letter match.

## 5. Computational Approach

Python is used to automate the matching process and validate the constraints.

The main components are:

### A. Letter-frequency comparison

`Counter` compares the frequency of each letter in a word and a sequence.

This avoids problems caused by different letter arrangements.

### B. Candidate identification

For each word, the program searches the available sequences and identifies those satisfying one of the three matching conditions.

### C. Combination generation

The `itertools.product()` function generates possible combinations of candidate sequences for the four words in a theme.

Each combination is checked against the required pattern:

- Two exact matches
- One additional letter
- One missing letter

### D. Sequence tracking

A sequence cannot be used more times than it appears in the original input.

Python's `Counter` is also used to track the remaining available sequences and prevent invalid reuse.

### E. Extraction

Once the four matches for a theme have been established, the additional and missing letters are recorded separately.

The extracted letters are then read in the prescribed theme order.

## 6. Final Answer

Gained letters: NEWESTROUGHEXCHANGE
Lost letters:   LEUVENGHENTBRUSSELS

<escape>**ANTWERPSCHE DIAMANTKRING**</escape>

The final answer was submitted successfully.

## 7. Key Programming Concepts

This puzzle provides an opportunity to apply several Python concepts:

| Concept | Application |
|---|---|
| `Counter` | Comparing letter frequencies and tracking sequence usage |
| Dictionaries | Storing themes and their associated words |
| Lists and tuples | Organising words, positions and candidate matches |
| Functions | Separating comparison, candidate identification and solving logic |
| `itertools.product()` | Generating possible combinations |
| Loops and conditionals | Applying the puzzle's constraints |
| Assertions and exceptions | Checking assumptions and identifying invalid solutions |

## 8. Conclusion

The puzzle combines pattern recognition, combinatorial reasoning, and computational validation.

The important step was recognising that the scrambled sequences could be compared through letter frequencies rather than their original ordering.

Python then provided a systematic way to test candidate matches, enforce the constraints, track sequence usage, and extract the final answer.
