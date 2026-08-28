import json

from project import start_quiz, previous_score, new_question


def test_start_quiz(monkeypatch, tmp_path):
    questions = [
        {
            "question": "What is the capital of India?",
            "answer": "New Delhi"
        },
        {
            "question": "Which country is largest in world?",
            "answer": "Russia"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "answer": "Jupiter"
        },
        {
            "question": "How many days are there in leap year?",
            "answer": "366"
        },
        {
            "question": "How many days are there in a week?",
            "answer": "7"
        }
    ]

    scores = []

    questions_file = tmp_path / "questions.json"
    scores_file = tmp_path / "scores.json"

    questions_file.write_text(json.dumps(questions))
    scores_file.write_text(json.dumps(scores))

    monkeypatch.chdir(tmp_path)

    answers = iter([
        "New Delhi",
        "Russia",
        "Jupiter",
        "366",
        "7"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    monkeypatch.setattr(
        "project.random.sample",
        lambda questions, n: questions
    )

    start_quiz()

    saved_scores = json.loads(scores_file.read_text())

    assert saved_scores[0]["score"] == 5
    assert saved_scores[0]["total"] == 5


def test_previous_score(monkeypatch, tmp_path, capsys):
    scores = [
        {
            "score": 4,
            "total": 5
        },
        {
            "score": 5,
            "total": 5
        }
    ]

    scores_file = tmp_path / "scores.json"
    scores_file.write_text(json.dumps(scores))

    monkeypatch.chdir(tmp_path)

    previous_score()

    output = capsys.readouterr().out

    assert "Quiz 1: 4/5" in output
    assert "Quiz 2: 5/5" in output


def test_new_question(monkeypatch, tmp_path):
    questions = [
        {
            "question": "What is the capital of India?",
            "answer": "New Delhi"
        },
        {
            "question": "Which country is largest in world?",
            "answer": "Russia"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "answer": "Jupiter"
        },
        {
            "question": "How many days are there in leap year?",
            "answer": "366"
        },
        {
            "question": "How many days are there in a week?",
            "answer": "7"
        }
    ]

    questions_file = tmp_path / "questions.json"
    questions_file.write_text(json.dumps(questions))

    monkeypatch.chdir(tmp_path)

    answers = iter([
        "What is the capital of Japan?",
        "Tokyo"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    new_question()

    updated_questions = json.loads(questions_file.read_text())

    assert len(updated_questions) == 6
    assert updated_questions[5]["question"] == "What is the capital of Japan?"
    assert updated_questions[5]["answer"] == "Tokyo"
