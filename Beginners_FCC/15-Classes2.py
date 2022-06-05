from Questions import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) orange\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:               #question ahora reemplaza al self. de la Class
        answer = input(question.promt)       #en este momento question.promt = Questions - Muestra la primera pregunta, luego la segunda...
        if answer == question.answer:        #en este momento question.answer = Questions
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)