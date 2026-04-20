import tkinter as tk
from tkinter import Toplevel, Label, Button, messagebox
import html, random
from trivia_client import TriviaClient


class TriviaGameGUI:

    DEFAULT_CATEGORY = 9   # General Knowledge
    DEFAULT_AMOUNT = 5     # Número de preguntas por defecto

    def __init__(self, root):
        self.root = root
        self.client = TriviaClient()

        self.questions = []
        self.index = 0
        self.score = 0
        self.correct_answer = None

    def start(self):
        """Inicia el juego y abre la ventana."""
        self.questions = self.client.get_questions(
            amount=self.DEFAULT_AMOUNT,
            category=self.DEFAULT_CATEGORY
        )

        if not self.questions:
            messagebox.showerror("Error", "No se pudieron obtener preguntas.")
            return

        self.window = Toplevel(self.root)
        self.window.title("PyTrivia V03 - GUI Básica")
        self.window.geometry("500x350")
        self.window.resizable(False, False)

        self.show_question()

    def show_question(self):
        """Muestra la pregunta actual y sus opciones."""
        q = self.questions[self.index]

        question_text = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        options = [html.unescape(a) for a in q["incorrect_answers"]] + [correct]
        random.shuffle(options)

        self.correct_answer = correct

        # Limpiar ventana
        for widget in self.window.winfo_children():
            widget.destroy()

        Label(self.window, text=f"Pregunta {self.index + 1}/{self.DEFAULT_AMOUNT}",
              font=("Arial", 12, "bold")).pack(pady=10)

        Label(self.window, text=question_text, wraplength=450,
              font=("Arial", 11)).pack(pady=10)

        for opt in options:
            Button(
                self.window,
                text=opt,
                width=40,
                command=lambda o=opt: self.check_answer(o)
            ).pack(pady=5)

    def check_answer(self, selected):
        """Comprueba si la respuesta es correcta y avanza."""
        if selected == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        else:
            messagebox.showwarning("Incorrecto", f"La respuesta correcta era: {self.correct_answer}")

        self.index += 1

        if self.index < self.DEFAULT_AMOUNT:
            self.show_question()
        else:
            messagebox.showinfo("Resultado final", f"Has acertado {self.score}/{self.DEFAULT_AMOUNT}")
            self.window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    game = TriviaGameGUI(root)
    game.start()
    root.mainloop()
