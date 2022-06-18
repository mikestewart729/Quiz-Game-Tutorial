# quiz.py

import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "Which GAIA subfunction is responsible for cleaning polluted waters": [
        "POSEIDON",
        "ARTEMIS",
        "DEMETER",
        "HADES",
    ],
    "What is the name of a facility where HEPHAESTUS builds new machines": [
        "Cauldron",
        "Factory",
        "Shop",
        "Beastworks",
    ],
    "What is the name of the crystalline resource of high value found in sunken caves":
    [
        "Greenshine",
        "Redgleam",
        "Blueglow",
        "Silverglint",
    ],
    "Dreadwings are flying combat machines based on which real-world animal": [
        "Bats",
        "Vultures",
        "Crows",
        "Pterodactyls",
    ],
    "What does Aloy recover from Thebes, Ted Faro's bunker under old San Francisco": [
        "Omega Clearance",
        "AETHER",
        "DEMETER",
        "POSEIDON",
    ],
    "What is the name of the capital settlement of the Tenakth Sky Clan": [
        "The Bulwark",
        "Thornmarsh",
        "Scalding Spear",
        "The Memorial Grove",
    ]
}

def prepare_questions(questions, num_questions):
    """
    Preprocess questions from the QUESTIONS data structure
    """
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def get_answer(question, alternatives):
    """
    Displays question and answer choices to user, and gets valid user answer choice
    """
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

def ask_question(question, alternatives):
    """
    Ask questions of the user and determine if the answer is correct
    """
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

def run_quiz():
    """
    Run the main quiz loop
    """
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nYou got {num_correct} correct out of {num} questions")

if __name__ == "__main__":
    run_quiz()
