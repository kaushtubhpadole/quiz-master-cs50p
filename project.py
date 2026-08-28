import json
import random


def main():
    while True:
        print("==============================")
        print("         QUIZ MASTER")
        print("==============================")
        print("1. Start Quiz")
        print("2. View Previous Scores")
        print("3. Add Questions")
        print("4. Exit")
        print("==============================")

        choice = input("Choose an option: ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            previous_score()

        elif choice == "3":
            new_question()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

def start_quiz():
    with open("questions.json", "r") as file:
        questions = json.load(file)

    if len(questions) < 5:
        print("There are not enough questions.")
        return

    selected_questions = random.sample(questions, 5)

    score = 0

    for question in selected_questions:
        print()
        print(question["question"])

        answer = input("Answer: ")

        if answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The answer is {question['answer']}.")

    print()
    print(f"Your score: {score}/5")

    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []

    scores.append({
        "score": score,
        "total": 5
    })

    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)


def previous_score():
    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []

    if len(scores) == 0:
        print("No previous scores.")
        return

    print()
    print("Previous Scores")
    print("----------------")

    for i, result in enumerate(scores, start=1):
        print(f"Quiz {i}: {result['score']}/{result['total']}")


def new_question():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")

    new_question = {
        "question": question,
        "answer": answer
    }

    with open("questions.json", "r") as file:
        questions = json.load(file)

    questions.append(new_question)

    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)

    print("Question added successfully!")


if __name__ == "__main__":
    main()
