import random
from quiz_utils import filter_questions_by_anime, filter_questions_by_difficulty, get_unique_anime_options, load_questions_from_json, RandomQuestionStrategy, DifficultyQuestionStrategy, calculate_score, points_manager

# Função principal
def main():
    questions = load_questions_from_json('anime.json')
    question_selection_strategy = RandomQuestionStrategy()  # Estratégia padrão: seleção aleatória

    print("Bem-vindo ao Quiz de Anime!\n")

    total_points = 0  # Pontuação total do usuário
    correct_count = 0  # Contador de respostas corretas
    difficulty = 1  # Inicializa a dificuldade com um valor padrão

    while True:
        print("Escolha uma opção:")
        print("1 - Filtrar por dificuldade")
        print("2 - Filtrar por anime")
        print("3 - Filtrar todas")
        print("4 - Sair")
        choice = input("Digite o número da opção: ")

        if choice == "1":
            difficulty = int(input("\nEscolha a dificuldade (1-Fácil, 2-Moderado, 3-Difícil): "))
            filtered_questions = filter_questions_by_difficulty(questions, difficulty)

            if filtered_questions:
                for question in filtered_questions:
                    question.display()
                    answer = input("Pressione Enter para continuar ou 'Q' para retornar ao menu: ").strip().lower()
                    if answer == 'q':
                        break
                    else:
                        user_resposta = int(answer)
                        correct = question.check_resposta(user_resposta)
                        if correct:
                            correct_count += 1
                            total_points += 5  # Adiciona 5 pontos por cada resposta correta
                        print("\n")  # Adiciona uma linha em branco após exibir a resposta
            else:
                print("Nenhuma pergunta correspondente encontrada.")
                
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
                    question_selection_strategy = DifficultyQuestionStrategy()  # Redefinir para seleção aleatória
                else:
                    print("\nNenhuma pergunta correspondente encontrada.")
                    continue
            else:
                print("\nOpção de anime inválida.")
                continue
        elif choice == "3":
            try:
                num_questions = int(input("\nQuantas perguntas você gostaria de responder? "))
                all_questions = questions.copy()
                random.shuffle(all_questions)
                for question in all_questions[:num_questions]:
                    question.display()
                    answer = input("Sua resposta: ")
                    answer_int = int(answer)
                    correct = question.check_resposta(answer_int)
                    if correct:
                        print("Resposta correta!")
                        correct_count += 1
                        total_points += 5  # Adiciona 5 pontos por cada resposta correta
                    else:
                        print("Resposta incorreta. A resposta correta é:", question.response[answer_int - 1]["correct"])
                    print("\n")  # Adiciona uma linha em branco após exibir a resposta
            except ValueError:
                print("\nPor favor, insira um número válido.")
                continue
        elif choice == "4":
            print("\nSaindo do Quiz. Até a próxima!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")
            continue

    # Exibição da pontuação ao final do quiz
    total_points = calculate_score(correct_count)
    print(f"\nQuiz finalizado!\nPerguntas corretas: {correct_count}\nPontuação total: {total_points}")

#if __name__ == "__main__":
#    main()
