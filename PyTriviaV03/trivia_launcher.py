import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os


class TriviaLauncher:

    def __init__(self, root):
        self.root = root
        self.root.title("PyTriviaV03 - Launcher")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="Selecciona una versión del juego",
                 font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(frame, text="Versión Consola",
                  width=25, command=self.run_console).pack(pady=5)

        tk.Button(frame, text="GUI Básica",
                  width=25, command=self.run_gui_basic).pack(pady=5)

        tk.Button(frame, text="GUI Avanzada",
                  width=25, command=self.run_gui_advanced).pack(pady=5)

    def run_console(self):
        self.run_script("trivia_game_console.py")

    def run_gui_basic(self):
        self.run_script("trivia_game_gui.py")

    def run_gui_advanced(self):
        self.run_script("trivia_game_advanced.py")

    def run_script(self, script_name):
        script_path = os.path.join(os.path.dirname(__file__), script_name)

        if not os.path.exists(script_path):
            messagebox.showerror("Error", f"No se encontró el archivo:\n{script_name}")
            return

        try:
            subprocess.Popen([sys.executable, script_path])
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo ejecutar el archivo:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaLauncher(root)
    root.mainloop()
