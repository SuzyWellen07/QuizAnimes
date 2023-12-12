<<<<<<< HEAD:routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from quiz_utils import load_questions_from_json, RandomQuestionStrategy, DifficultyQuestionStrategy, points_manager, calculate_score

# Criar um Blueprint em vez de usar diretamente o objeto Flask
bp = Blueprint('routes', __name__)

# Carregar as perguntas ao iniciar o aplicativo Flask
questions = load_questions_from_json('anime.json')
question_selection_strategy = RandomQuestionStrategy()  # Estratégia padrão: seleção aleatória
current_question = None  # Pergunta atual

# Função auxiliar para obter uma nova pergunta com base na estratégia de seleção
def get_new_question(difficulty=None):
    global current_question
    if difficulty:
        question_selection_strategy = DifficultyQuestionStrategy(difficulty)
    else:
        question_selection_strategy = RandomQuestionStrategy()
    current_question = question_selection_strategy.select_question(questions)
    return current_question

# Rota para a página inicial
@bp.route('/')
def index():
    return render_template('index.html')

# Rota para começar o quiz
@bp.route('/start')
def start():
    global current_question
    current_question = get_new_question()
    return render_template('quiz.html', question=current_question, feedback=None)

# Rota para processar as respostas do quiz
@bp.route('/quiz', methods=['POST'])
def quiz():
    global current_question
    user_response = int(request.form['user_response'])
    correct = current_question.check_resposta(user_response)
    
    feedback = "Resposta correta!" if correct else "Resposta incorreta. A resposta correta é: {}".format(
        current_question.response[user_response - 1]["correct"]
    )
    
    # Adicione pontos ao singleton
    points_manager.add_points(5) if correct else points_manager.add_points(0)
    
    current_question = get_new_question()  # Obtenha a próxima pergunta
    return render_template('quiz.html', question=current_question, feedback=feedback)

# Rota para exibir o resultado do quiz
@bp.route('/result')
def result():
    total_points = points_manager.get_total_points()
    return render_template('quiz_result.html', total_points=total_points)
=======
from flask import Blueprint, render_template, request, redirect, url_for
from quiz_utils import load_questions_from_json, RandomQuestionStrategy, DifficultyQuestionStrategy, points_manager, calculate_score

# Criar um Blueprint em vez de usar diretamente o objeto Flask
bp = Blueprint('routes', __name__)

# Carregar as perguntas ao iniciar o aplicativo Flask
questions = load_questions_from_json('anime.json')
question_selection_strategy = RandomQuestionStrategy()  # Estratégia padrão: seleção aleatória
current_question = None  # Pergunta atual

# Função auxiliar para obter uma nova pergunta com base na estratégia de seleção
def get_new_question(difficulty=None):
    global current_question
    if difficulty:
        question_selection_strategy = DifficultyQuestionStrategy(difficulty)
    else:
        question_selection_strategy = RandomQuestionStrategy()
    current_question = question_selection_strategy.select_question(questions)
    return current_question

# Rota para a página inicial
@bp.route('/')
def index():
    return render_template('index.html')

# Rota para começar o quiz
@bp.route('/start')
def start():
    global current_question
    current_question = get_new_question()
    return render_template('quiz.html', question=current_question, feedback=None)

# Rota para processar as respostas do quiz
# Rota para processar as respostas do quiz
@bp.route('/quiz', methods=['POST'])
def quiz():
    global current_question
    if 'user_response' not in request.form:
        return render_template('quiz.html', question=current_question, feedback="Por favor, selecione uma resposta.")
    user_response = request.form['user_response']
    
    if user_response is None or user_response == '':
        return render_template('quiz.html', question=current_question, feedback="Por favor, selecione uma resposta. 2")
    user_response = int(user_response)
    correct = current_question.check_resposta(user_response)
    
    feedback = "Resposta correta!" if correct else "Resposta incorreta. A resposta correta é: {}".format(
        current_question.response[user_response - 1]["correct"]
    )
    points_manager.add_points(5) if correct else points_manager.add_points(0)
    
    current_question = get_new_question()  # Obtenha a próxima pergunta
    return render_template('quiz.html', question=current_question, feedback=feedback)

# Rota para exibir o resultado do quiz
@bp.route('/result')
def result():
    total_points = points_manager.get_total_points()
    return render_template('quiz_result.html', total_points=total_points)
>>>>>>> 78d9105157d3f4a6edade77023ead9244fc7fea6:routes/routes.py
