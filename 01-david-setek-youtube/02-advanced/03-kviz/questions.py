# vytvorim triedu Questions, kde poslem udaje z data_question
# tie premenim na objekt s atributmi "text" a "answer"
class Questions:
    def __init__(self, cl_text, cl_answer):
        self.text = cl_text
        self.answer = cl_answer
