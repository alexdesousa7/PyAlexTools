import html
import random
from trivia_client import TriviaClient

CATEGORIES = {
    9: "General Knowledge",
    10: "Books",
    11: "Film",
    12: "Music",
    14: "Television",
    15: "Video Games",
    17: "Science & Nature",
    18: "Computers",
    19: "Mathematics",
    21: "Sports",
    22: "Geography",
    23: "History",
    24: "Politics",
    27: "Animals"
}


class TriviaGameConsole:

    def __init__(self):
        self.client = TriviaClient()

    def choose_category(self):
        print("\n=== Categorías disponibles ===")
        for cid, name in CATEGORIES.items():
            print(f"{cid}. {name}")

        while True:
            choice = input("\nElige el ID de la categoría: ").strip()
            if choice.isdigit() and int(choice) in CATEGORIES:
                return int(choice)
            print("Categoría inválida. Inténtalo de nuevo.")

    def choose_amount(self):
        while True:
            n = input("¿Cuántas preguntas quieres jugar? (1-20): ").strip()
            if n.isdigit() and 1 <= int(n) <= 20:
                return int(n)
            print("Número inválido. Intenta de nuevo.")

    def play(self):
        print("\n=== PyTrivia V03 - Versión Consola ===")

        amount = self.choose_amount()
        category = self.choose_category()

        questions = self.client.get_questions(amount=amount, category=category)

        if not questions:
            print("No se pudieron obtener preguntas. Inténtalo más tarde.")
            return

        score = 0

        for i, q in enumerate(questions, start=1):
            question_text = html.unescape(q["question"])
            correct = html.unescape(q["correct_answer"])
            options = [html.unescape(a) for a in q["incorrect_answers"]] + [correct]
            random.shuffle(options)

            print(f"\n--- Pregunta {i}/{amount} ---")
            print(question_text)

            for idx, opt in enumerate(options, start=1):
                print(f"  {idx}. {opt}")

            answer = input("Tu respuesta (número): ").strip()

            if not answer.isdigit() or not (1 <= int(answer) <= len(options)):
                print(f"Respuesta inválida. La correcta era: {correct}")
                continue

            chosen = options[int(answer) - 1]

            if chosen == correct:
                print("¡Correcto!")
                score += 1
            else:
                print(f"Incorrecto. La respuesta correcta era: {correct}")

        print(f"\n=== Resultado final: {score}/{amount} ===")


if __name__ == "__main__":
    game = TriviaGameConsole()
    game.play()
