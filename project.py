from string import ascii_lowercase

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.num_correct = 0

    def display_question(self, num, question, alternatives):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")
        return correct_answer, labeled_alternatives

    def get_user_answer(self):
        return input("\nChoice? ")

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.num_correct += 1
            print("⭐ Correct! ⭐")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")

    def run_quiz(self):
        for num, (question, alternatives) in enumerate(self.questions.items(), start=1):
            correct_answer, labeled_alternatives = self.display_question(num, question, alternatives)
            answer_label = self.get_user_answer()
            answer = labeled_alternatives.get(answer_label)
            self.check_answer(answer, correct_answer)

        print(f"\nYou got {self.num_correct} correct out of {len(self.questions)} questions")


def main():
    QUESTIONS = {
        "When did Galatasaray founded ": ["1905", "1771", "1903", "1881"],
        "When did Galatasaray won the UEFA Cup Final": ["2000", "2001", "1999", "2002"],
        "Who is the founder of Galatasaray": ["Ali Sami Yen", "Ataturk", "Fatih Terim", "Ismet Inonu"],
        "How many Turkish Super League championships does Galatasaray have ": ["23", "33", "13", "20"],
        "Who is Fatih for Galatasaray": ["Legend", "Coach", "Founder", "Sponsor"],
        "Which team is the top rival of Galatasaray": ["Fenerbahce", "Besiktas", "Trabzonspor", "Bursaspor"],
    }

    quiz = Quiz(QUESTIONS)
    quiz.run_quiz()


if __name__ == "__main__":
    main()
