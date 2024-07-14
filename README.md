This is for MACOS, as I work there :) An Llama2, which is very basic AI model..

Set up the environment:

Install Homebrew if not already installed (Goto homebrew and copy their link) If your path is not correct use -echo- to correct it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python

# Create a new directory for your project
mkdir local_llm
cd local_llm

# Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

Install dependencies:

pip install torch torchvision torchaudio
pip install transformers
pip install accelerate

Create a Python script:

Create a file named local_llm.py and add the following code:
pythonCopyfrom transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model():
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return model, tokenizer

def generate_text(prompt, model, tokenizer, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens=True)

if __name__ == "__main__":
    model, tokenizer = load_model()
    
    while True:
        prompt = input("Enter your prompt (or 'quit' to exit): ")
        if prompt.lower() == 'quit':
            break
        
        generated_text = generate_text(prompt, model, tokenizer)
        print("Generated text:", generated_text)

Run the script:

python local_llm.py
This will start an interactive session where you can enter prompts and get generated text.
Creating a simple GUI (optional):

Install tkinter if not already installed:
brew install python-tk
Create a new file named gui_llm.py:
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
**** Run the GUI:
gui_llm.py
