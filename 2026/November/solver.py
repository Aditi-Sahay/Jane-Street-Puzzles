
"""
Jane Street — November 2026: Pressure Points

This script matches the scrambled letter sequences
to the four sets of each identified theme/emoji.

For each set:
- Two words must match exactly. 
- One word must contain one additional letter.
- One word must be missing one letter.

"""


from collections import Counter
from itertools import product


# --------------------------------------------------
# 1. INPUT DATA
# --------------------------------------------------

SEQUENCES = """
Ø AAAABBIRRST AAACDEGHHHILMPRS AABCIILPTY AABDEHNNOORRSTTUY AABDORRST
AADEILPSS AADERRSUVY AADIMNTU AADMNNOT AAEEEHLNOOPRRSSTTTT AAGJRTU AAKNSS
ABBDEELOSSSU ABEEGLNSTW ABIIILNSTTY ABOW ACCGRUX ACDENO ACEILP
ACFINRRRSTTUU ACRX AEEFGIKNPRRR AEEHNV AEGHRT AEGILNRST AEHHLT AEIINST
AEILLNPSU AEQRSU AGIJLOOT AHTU AIIIIJJLNSSTTUV AIIM AIINSSSTTUX AIMMOS AIX
AMNY AORTY AST BEQSSTUU CCDNOOTU CCILR CDENOOS CEIMNOWX CEINOPRSSUX CEMRRUY
CIIMTV CORSS DIRT DNOW EEFIR EEHLTVW EEHRT EEIMSS EFL EHMO EHNORT EINN ENRT
ESTW FIRST GHIRT GIMNNOWY GO HOSTU HPU IILNOSV IPTTU IX MOO NSU OPRT SW T V
""".split()

# Convert the empty sequence symbol into an empty string.
SEQUENCES = ["" if sequence == "Ø" else sequence
             for sequence in SEQUENCES]


# Each theme contains:
# 1. Its name
# 2. Four associated words
# 3. The position of each word in the theme, where known.

THEMES = {
    "👸": ("Queen (the band)", [
        ("MAY", "?"),
        ("MERCURY", "?"),
        ("DEACON", "?"),
        ("TAYLOR", "?")
    ]),

    "🧭": ("Compass", [
        ("NORTH", "T"),
        ("EAST", "R"),
        ("SOUTH", "B"),
        ("WEST", "L")
    ]),

    "🐷": ("Pigpen cipher X-grid", [
        ("S", "T"),
        ("U", "R"),
        ("V", "B"),
        ("T", "L")
    ]),

    "⚽": ("Barça diamond midfield", [
        ("MESSI", "T"),
        ("XAVI", "R"),
        ("BUSQUETS", "B"),
        ("INIESTA", "L")
    ]),

    "🎮": ("PlayStation face buttons", [
        ("TRIANGLE", "T"),
        ("CIRCLE", "R"),
        ("CROSS", "B"),
        ("SQUARE", "L")
    ]),

    "🖼️": ("Raphael's Sistine Madonna", [
        ("MADONNA", "T"),
        ("SAINTBARBARA", "R"),
        ("PUTTI", "B"),
        ("SAINTSIXTUS", "L")
    ]),

    "🧐": ("Monopoly corners", [
        ("FREEPARKING", "T"),
        ("GOTOJAIL", "R"),
        ("GO", "B"),
        ("JAILJUSTVISITING", "L")
    ]),

    "⚾": ("Baseball diamond", [
        ("SECOND", "T"),
        ("FIRST", "R"),
        ("HOME", "B"),
        ("THIRD", "L")
    ]),

    "💻": ("Diamond Model of Intrusion Analysis", [
        ("ADVERSARY", "T"),
        ("CAPABILITY", "R"),
        ("VICTIM", "B"),
        ("INFRASTRUCTURE", "L")
    ]),

    "🐉": ("Beijing's four imperial altars", [
        ("EARTH", "T"),
        ("SUN", "R"),
        ("HEAVEN", "B"),
        ("MOON", "L")
    ]),

    "🕹️": ("Joystick / D-pad", [
        ("UP", "T"),
        ("RIGHT", "R"),
        ("DOWN", "B"),
        ("LEFT", "L")
    ]),

    "🏛️": ("Washington, D.C.'s diamond", [
        ("NORTHPORTALESTATES", "T"),
        ("NORTHEASTBOUNDARY", "R"),
        ("BLUEPLAINS", "B"),
        ("PALISADES", "L")
    ]),

    "🎶": ("Orchestra seating", [
        ("PERCUSSION", "T"),
        ("DOUBLEBASSES", "R"),
        ("CONDUCTOR", "B"),
        ("VIOLINS", "L")
    ]),

    "⭐": ("Southern Cross (Crux)", [
        ("GACRUX", "T"),
        ("IMAI", "R"),
        ("ACRUX", "B"),
        ("MIMOSA", "L")
    ]),

    "🕓": ("Clock face", [
        ("TWELVE", "T"),
        ("THREE", "R"),
        ("SIX", "B"),
        ("NINE", "L")
    ]),

    "⛵": ("Ship", [
        ("BOW", "T"),
        ("STARBOARD", "R"),
        ("STERN", "B"),
        ("PORT", "L")
    ]),

    "🏜️": ("Colorado's neighbours", [
        ("WYOMING", "T"),
        ("KANSAS", "R"),
        ("NEWMEXICO", "B"),
        ("UTAH", "L")
    ]),

    "🪷": ("India", [
        ("HIMACHALPRADESH", "T"),
        ("WESTBENGAL", "R"),
        ("TAMILNADU", "B"),
        ("GUJARAT", "L")
    ]),

    "⚠️": ("NFPA 704 fire diamond", [
        ("FIRE", "T"),
        ("INSTABILITY", "R"),
        ("SPECIAL", "B"),
        ("HEALTH", "L")
    ])
}


# --------------------------------------------------
# 2. COMPARE A WORD WITH A SEQUENCE
# --------------------------------------------------

def compare_letters(word, sequence):
    """
    Compare the letters in a word and a sequence.

    The order of letters does not matter.

    Returns:
        ("=", "")       If both contain exactly the same letters.
        ("+", letter)   If the sequence has one extra letter.
        ("-", letter)   If the word has one extra letter.
        None            If they do not satisfy the rule.
    """

    word_letters = Counter(word)
    sequence_letters = Counter(sequence)

    difference = sequence_letters - word_letters

    if sum(difference.values()) == 0:
        reverse_difference = word_letters - sequence_letters

        if sum(reverse_difference.values()) == 0:
            return ("=", "")

        if sum(reverse_difference.values()) == 1:
            extra_letter = next(iter(reverse_difference))
            return ("-", extra_letter)

    elif sum(difference.values()) == 1:
        extra_letter = next(iter(difference))
        return ("+", extra_letter)

    return None


# --------------------------------------------------
# 3. FIND POSSIBLE SEQUENCES FOR EACH WORD
# --------------------------------------------------

def find_candidates(word, available_sequences):
    """
    Find all available sequences that can correspond
    to a given word.

    Each candidate includes:
        - The sequence
        - The operation (+, -, or =)
        - The relevant extra or missing letter
    """

    candidates = []

    for sequence, quantity in available_sequences.items():

        if quantity == 0:
            continue

        comparison = compare_letters(word, sequence)

        if comparison is not None:
            operation, letter = comparison

            candidates.append(
                (sequence, operation, letter)
            )

    return candidates


# --------------------------------------------------
# 4. SOLVE THE THEMES
# --------------------------------------------------

def solve_themes():

    # Count how many times each sequence appears.
    remaining_sequences = Counter(SEQUENCES)

    # Store the letters extracted from each theme.
    gained_letters = {}
    lost_letters = {}

    # Store the complete solution for each theme.
    theme_solutions = {}

    # Process themes in the specified emoji order.
    for emoji, (theme_name, words) in THEMES.items():

        print(f"\nSolving theme: {emoji} {theme_name}")

        # Find possible sequences for each of the four words.
        word_candidates = []

        for word, position in words:

            candidates = find_candidates(
                word,
                remaining_sequences
            )

            word_candidates.append(candidates)

        # Generate every possible combination of candidates.
        valid_solutions = []

        for combination in product(*word_candidates):

            selected_sequences = [
                candidate[0]
                for candidate in combination
            ]

            # A sequence cannot be used more times than it appears.
            selected_counts = Counter(selected_sequences)

            if any(
                selected_counts[sequence] >
                remaining_sequences[sequence]
                for sequence in selected_counts
            ):
                continue

            operations = [
                candidate[1]
                for candidate in combination
            ]

            # Every theme must contain:
            # One extra letter (+)
            # One missing letter (-)
            # Two exact matches (=)
            if sorted(operations) != ["+", "-", "=", "="]:
                continue

            valid_solutions.append(combination)

        # Require exactly one valid solution.
        if len(valid_solutions) != 1:
            raise ValueError(
                f"{theme_name}: Expected one solution, "
                f"but found {len(valid_solutions)}."
            )

        solution = valid_solutions[0]

        # Record the solution and consume its sequences.
        theme_solutions[emoji] = solution

        selected_counts = Counter(
            candidate[0] for candidate in solution
        )

        remaining_sequences.subtract(selected_counts)

        # Extract the gained and lost letters.
        gained = ""
        lost = ""

        for word, position in words:

            for sequence, operation, letter in solution:

                comparison = compare_letters(word, sequence)

                if comparison is None:
                    continue

                # Match this candidate to its corresponding word.
                if operation == "+" and comparison[1] == letter:
                    pass

            # The solution is in the same order as the words.
            word_index = words.index((word, position))
            sequence, operation, letter = solution[word_index]

            if operation == "+":
                gained += letter

            elif operation == "-":
                lost += letter

            print(
                f"  {word:20} -> {sequence:25} "
                f"{operation} {letter}"
            )

        gained_letters[emoji] = gained
        lost_letters[emoji] = lost

        print(f"  Gained letter: {gained}")
        print(f"  Lost letter:   {lost}")

    return (
        theme_solutions,
        gained_letters,
        lost_letters,
        remaining_sequences
    )


# --------------------------------------------------
# 5. DISPLAY THE FINAL EXTRACTION
# --------------------------------------------------

def main():

    print("Total sequences:", len(SEQUENCES))
    print("Total themes:", len(THEMES))

    if len(SEQUENCES) != 76:
        raise ValueError("Expected exactly 76 sequences.")

    if len(THEMES) != 19:
        raise ValueError("Expected exactly 19 themes.")

    (
        theme_solutions,
        gained_letters,
        lost_letters,
        remaining_sequences
    ) = solve_themes()

    print("\n" + "=" * 50)
    print("FINAL RESULTS")
    print("=" * 50)

    gained_message = "".join(
        gained_letters[emoji]
        for emoji in THEMES
    )

    lost_message = "".join(
        lost_letters[emoji]
        for emoji in THEMES
    )

    print("\nGained letters:", gained_message)
    print("Lost letters:  ", lost_message)

    print("\nRemaining sequences:")

    unused_sequences = {
        sequence: quantity
        for sequence, quantity in remaining_sequences.items()
        if quantity > 0
    }

    print(unused_sequences)

    if sum(remaining_sequences.values()) != 0:
        raise ValueError(
            "Not all sequences were used."
        )

    print("\nAll sequences successfully accounted for.")


if __name__ == "__main__":
    main()

