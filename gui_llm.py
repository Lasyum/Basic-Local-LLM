import tkinter as tk
from tkinter import scrolledtext
from local_llm import load_model, generate_text

class LLMGUI:
    def __init__(self, master):
        self.master = master
        master.title("Local LLM")

        self.model, self.tokenizer = load_model()

        self.prompt_label = tk.Label(master, text="Enter your prompt:")
        self.prompt_label.pack()

        self.prompt_entry = tk.Entry(master, width=50)
        self.prompt_entry.pack()

        self.generate_button = tk.Button(master, text="Generate", command=self.generate)
        self.generate_button.pack()

        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=20)
        self.output_text.pack()

    def generate(self):
        prompt = self.prompt_entry.get()
        generated_text = generate_text(prompt, self.model, self.tokenizer)
        self.output_text.insert(tk.END, f"Prompt: {prompt}\nGenerated text: {generated_text}\n\n")

root = tk.Tk()
gui = LLMGUI(root)
root.mainloop()
