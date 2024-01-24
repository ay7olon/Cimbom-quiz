from string import ascii_lowercase
QUESTIONS= {
    "When did Galatasaray founded ": [
        "1905","1771","1903","1881"
    ],
    "When did Galatasaray won the UEFA Cup Final": [
        "2000","2001","1999","2002"
    ],
    "Who is the founder of Galatasaray": [
        "Ali Sami Yen","Ataturk","Fatih Terim","Ismet Inonu"
    ],
    "How many Turkish Super League championships does Galatasaray have ":[
        "23","33","13","20"
    ],
    "Who is Fatih  for Galatasaray": [
        "Legend","Coach","Founder","Sponsor"
    ],
    "Which team is the top rival of Galatasaray":[
        "Fenerbahce","Besiktas","Trabzonspor","Bursaspor"
    ],
}
    
    
num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        
print(f"\nYou got {num_correct} correct out of {num} questions")