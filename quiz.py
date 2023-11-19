class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define your questions and answers
questions = [
    Question("What is the capital of France? ", "Paris"),
    Question("Which planet is known as the Red Planet? ", "Mars"),
    Question("What is the largest mammal in the world? ", "Blue whale"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer.lower() == question.answer.lower():
            score += 1
    print("You got", score, "out of", len(questions), "questions correct.")

# Run the quiz
run_quiz(questions)
