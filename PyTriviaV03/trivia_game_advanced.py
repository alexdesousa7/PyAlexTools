import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import html, random
from trivia_client import TriviaClient


CATEGORIES = {
    "General Knowledge": 9,
    "Books": 10,
    "Film": 11,
    "Music": 12,
    "Television": 14,
    "Video Games": 15,
    "Science & Nature": 17,
    "Computers": 18,
    "Mathematics": 19,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Animals": 27
}


class TriviaAdvancedGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("PyTrivia V03 - Configuración")
        self.client = TriviaClient()

        self.build_config_window()

    def build_config_window(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        # Número de preguntas a realizar
        tk.Label(frame, text="Número de preguntas:").grid(row=0, column=0, sticky="w")
        self.num_questions = tk.Spinbox(frame, from_=1, to=20, width=5)
        self.num_questions.grid(row=0, column=1, pady=5)

        # Categoría a seleccionar
        tk.Label(frame, text="Categoría:").grid(row=1, column=0, sticky="w")
        self.category_box = ttk.Combobox(frame, values=list(CATEGORIES.keys()), state="readonly", width=25)
        self.category_box.grid(row=1, column=1, pady=5)
        self.category_box.set("Sports")  # Valor por defecto

        # Botón para iniciar el juego
        tk.Button(frame, text="Jugar", command=self.start_game, width=20).grid(row=2, column=0, columnspan=2, pady=15)

    def start_game(self):
        try:
            n = int(self.num_questions.get())
        except:
            messagebox.showerror("Error", "Número de preguntas inválido")
            return

        category_name = self.category_box.get()
        category_id = CATEGORIES[category_name]

        questions = self.client.get_questions(amount=n, category=category_id)

        if not questions:
            messagebox.showerror("Error", "No se pudieron obtener preguntas.")
            return

        GameWindow(self.root, questions)


class GameWindow:

    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.index = 0
        self.score = 0

        self.window = Toplevel(self.root)
        self.window.title("PyTrivia V03 - Juego")
        self.window.geometry("500x350")
        self.window.resizable(False, False)

        self.show_question()

    def show_question(self):
        q = self.questions[self.index]

        question_text = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        options = [html.unescape(a) for a in q["incorrect_answers"]] + [correct]
        random.shuffle(options)

        self.correct_answer = correct

        for widget in self.window.winfo_children():
            widget.destroy()

        tk.Label(self.window, text=f"Pregunta {self.index + 1}/{len(self.questions)}",
                 font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(self.window, text=question_text, wraplength=450,
                 font=("Arial", 11)).pack(pady=10)

        for opt in options:
            tk.Button(self.window, text=opt, width=40,
                      command=lambda o=opt: self.check_answer(o)).pack(pady=5)

    def check_answer(self, selected):
        if selected == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        else:
            messagebox.showwarning("Incorrecto", f"La respuesta correcta era: {self.correct_answer}")

        self.index += 1

        if self.index < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Resultado final", f"Has acertado {self.score}/{len(self.questions)}")
            self.window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaAdvancedGUI(root)
    root.mainloop()
