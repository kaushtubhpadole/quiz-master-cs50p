# Quiz Master

#### Video Demo: <URL HERE>

#### Description:

Quiz Master is a Python-based quiz application developed as my final project for CS50's Introduction to Programming with Python (CS50P). The purpose of this project is to provide a simple and interactive way for users to answer general knowledge questions, receive an immediate score, view their previous results, and add new questions to the quiz.

When the program starts, the user is presented with a menu containing four options: Start Quiz, View Previous Scores, Add Questions, and Exit. The menu continues to appear until the user chooses to exit the program.

The main functionality of the project is the Start Quiz option. The program stores all quiz questions and answers in a separate JSON file called `questions.json`. When a quiz is started, the program loads the questions from this file and randomly selects five questions using Python's `random` module. The user is then asked each question and enters an answer. The program compares the user's answer with the correct answer without considering differences in uppercase and lowercase letters. If the answer is correct, the user's score is increased. If the answer is incorrect, the program displays the correct answer.

After all five questions have been answered, the final score is displayed. The result is then stored in another JSON file called `scores.json`. This allows the program to keep previous results even after the program has been closed.

The View Previous Scores option reads the information from `scores.json` and displays the user's previous quiz results. Each result shows the quiz number and the score obtained out of five questions. If there are no previous scores, the program informs the user that no scores are available.

The Add Questions option allows the user to expand the quiz without modifying the Python source code. The user enters a new question and its correct answer. The program then adds the new question to `questions.json`. This means that questions added by the user can be selected in future quizzes.

The project contains four main files. `project.py` contains the main program and its functions. `questions.json` stores the quiz questions and their corresponding answers. `scores.json` stores the results of completed quizzes. `test_project.py` contains automated tests written using `pytest` to test the main functionality of the project.

I chose JSON files for storing questions and scores because JSON is simple to read and write using Python's built-in `json` module. It also allows the data to remain available between different executions of the program without requiring a database. I used the `random` module so that the quiz is different each time the user plays.

The project also includes automated tests for `start_quiz`, `previous_score`, and `new_question`. The tests use pytest features such as `monkeypatch` and temporary directories so that the tests can simulate user input and file operations without modifying the actual project data.

This project helped me apply several concepts learned throughout CS50P, including functions, loops, conditionals, exception-free file handling, JSON data, lists and dictionaries, modules, randomization, user input, and automated testing with pytest.
