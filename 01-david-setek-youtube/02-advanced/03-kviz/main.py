from data import question_data
from questions import Questions
from quiz_brain import QuizBrain

# vytvorim prazdny list, kde budem ukladat objekty (otazka a odpoved) vytvorene
# v class Questions (questions.py)
obj_question_list = []

# cyklus pre nacitanie jednotlivych poloziek v liste question_data
for one_item in question_data:
    # ulozim si z question_data listu, ktory je tvoreny dictionary
    # jednotlive polozky dictionary (text a answer)
    text_dic = one_item["text"]
    answer_dic = one_item["answer"]
    # vytvorim objekt obj_question podla class Questions
    # objekt obsahuje parametre (text a answer)
    obj_question = Questions(text_dic, answer_dic)
    # ulozim vytvorene objekty obj_question do noveho listu
    obj_question_list.append(obj_question)

# vytvorim objekt quiz
# do class QuizBrain poslem udaje vytvoreneho obj_question_list
quiz = QuizBrain(obj_question_list)
# cyklus na zadavanie otazok, pokial otazky su :)
while quiz.has_question() == True:  # nie je nutne pisat == True.
    quiz.next_question()

# finalny vypis
print("Gratulujem! Dokoncil si kviz :)")
print(f"Tvoje celkove dosiahnute skore je: {quiz.score} zo {quiz.question_number}")
