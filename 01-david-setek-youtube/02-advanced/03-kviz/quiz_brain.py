class QuizBrain:
    # constructor - funkcia, ktora sa automaticky vyvola pri volani tejto triedy (class)
    # nacitam question_list (tvoreny objektmi) z main.py
    def __init__(self, cl_list):
        self.question_list = cl_list
        self.question_number = 0
        self.score = 0

    # funkcia na priradenie otazky
    def next_question(self):
        # vytvorim premennu current_question, kde ulozim "text" otazky z listu
        # ques_list (co je vlastne list tvoreny objektmi) a index zacina od 0
        # (ten definujem v constructore - ques_number)
        current_question = self.question_list[self.question_number]
        # pripocitam 1
        self.question_number += 1
        # vlozim odpoved uzivatela do premennej user_answer, pricom mu
        # vypisem text otazky (current_question.text), kedze je to objekt,
        # ma atribut "text", ktory bol definovany v class Questions (questions.py)
        user_answer = input(
            f"Otazka c. {self.question_number}: {current_question.text} (True/False): "
        )
        # overenie spravnosti odpovede skrz funkciu answer_check
        self.answer_check(user_answer, current_question.answer)

    # funkcia na zistenie ci mame este otazku
    def has_question(self):
        # ak je cislo otazky menej ako pocet objektov(otazok) v liste
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def answer_check(self, cl_user_ans, cl_correct_ans):
        self.user_ans = cl_user_ans
        self.correct_ans = cl_correct_ans
        # podmienka ci sa user_answer = correct_answer
        if self.user_ans.lower() == self.correct_ans.lower():
            # pripocitam jedn bod
            self.score += 1
            print("Tvoja odpoved je spravna")
        else:
            print("Tvoja odpoved je nespravna")
            print(f"Spravna odpoved je {self.correct_ans}")
        print(f"Tvoje skore je: {self.score} / {self.question_number}")
