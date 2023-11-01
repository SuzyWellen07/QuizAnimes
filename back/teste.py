import json
import random

# Função para mapear o nível de dificuldade em palavras
def difficulty_to_word(difficulty):
    if difficulty == 1:
        return "Fácil"
    elif difficulty == 2:
        return "Moderado"
    elif difficulty == 3:
        return "Difícil"
    else:
        return "Desconhecido"

# Classe que representa uma pergunta
class Question:
    def __init__(self, id, question, response, difficulty, anime):
        self.id = id
        self.question = question
        self.response = response
        self.difficulty = difficulty
        self.anime = anime

    def display(self):
        print(f"Questão (Nível: {difficulty_to_word(self.difficulty)}) - {self.anime}:")
        print(self.question)
        for i, resposta in enumerate(self.response, start=1):
            print(f"{i}. {resposta['option']}")

    def check_resposta(self, user_resposta):
        try:
            user_resposta = int(user_resposta)
            if 1 <= user_resposta <= len(self.response):
                resposta_selecionada = self.response[user_resposta - 1]
                if resposta_selecionada["correct"]:
                    points_manager.add_points(10)
                    return True
        except (ValueError, IndexError):
            pass
        return False

# Classe Singleton para gerenciar os pontos
class PointsSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PointsSingleton, cls).__new__(cls)
            cls._instance.total_points = 0
        return cls._instance

    def add_points(self, points):
        self.total_points += points

    def get_total_points(self):
        return self.total_points

points_manager = PointsSingleton()

# Função para filtrar perguntas por dificuldade
def filter_questions_by_difficulty(questions, difficulty):
    return [question for question in questions if question.difficulty == difficulty]

# Função para filtrar perguntas por anime
def filter_questions_by_anime(questions, anime):
    return [question for question in questions if question.anime == anime]

# Função para obter opções de animes únicos do conjunto de perguntas
def get_unique_anime_options(questions):
    return list(set(question.anime for question in questions))

# Função para carregar perguntas de um arquivo JSON
def load_questions_from_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions_data = data["quiz"]
    questions = []

    for question_data in questions_data:
        id = question_data["id"]
        question = question_data["question"]
        response = question_data["response"]
        difficulty = question_data["difficulty"]
        anime = question_data["anime"]
        questions.append(Question(id, question, response, difficulty, anime))

    return questions

# Interface para as estratégias de seleção de perguntas
class QuestionSelectionStrategy:
    def select_question(self, questions):
        pass

# Estratégia de seleção aleatória
class RandomQuestionStrategy(QuestionSelectionStrategy):
    def select_question(self, questions):
        return random.choice(questions)

# Estratégia de seleção por dificuldade
class DifficultyQuestionStrategy(QuestionSelectionStrategy):
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def select_question(self, questions):
        filtered_questions = filter_questions_by_difficulty(questions, self.difficulty)
        if filtered_questions:
            return random.choice(filtered_questions)
        else:
            return None

def main():
    questions = load_questions_from_json('anime.json')
    question_selection_strategy = RandomQuestionStrategy()  # Estratégia padrão: seleção aleatória

    print("Bem-vindo ao Quiz de Anime!\n")

    while True:
        print("Escolha uma opção:")
        print("1 - Filtrar por dificuldade")
        print("2 - Filtrar por anime")
        print("3 - Sair")
        choice = input("Digite o número da opção: ")

        if choice == "1":
            difficulty = int(input("\nEscolha a dificuldade (1-Fácil, 2-Moderado, 3-Difícil): "))
            question_selection_strategy = DifficultyQuestionStrategy(difficulty)
        elif choice == "2":
            anime_options = get_unique_anime_options(questions)
            print("\nAnimes disponíveis:")
            for i, anime_option in enumerate(anime_options, start=1):
                print(f"{i}. {anime_option}")
            anime_choice = int(input("Escolha o número do anime: "))
            if 1 <= anime_choice <= len(anime_options):
                anime = anime_options[anime_choice - 1]
                filtered_questions = filter_questions_by_anime(questions, anime)
                if filtered_questions:
                    question_selection_strategy = RandomQuestionStrategy()  # Redefinir para seleção aleatória
                else:
                    print("\nNenhuma pergunta correspondente encontrada.")
                    continue
            else:
                print("\nOpção de anime inválida.")
                continue
        elif choice == "3":
            print("\nSaindo do Quiz. Até a próxima!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")
            continue

if __name__ == "__main__":
    main()
