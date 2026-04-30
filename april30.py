import tkinter as tk
from tkinter import ttk
import tokenize
from io import BytesIO


def tokenizer_app():
    def run_tokenizer():
        for row in table.get_children():
            table.delete(row)

        text = input_box.get("1.0", tk.END)
       

        try:
            for tok in tokenize.tokenize(BytesIO(text.encode("utf-8")).readline):
                token_type = tokenize.tok_name.get(tok.type, str(tok.type))
                specific_token = tok.string

                if token_type in ["ENCODING", "ENDMARKER", "NL"]:
                    continue

                if token_type == "NAME":
                    if specific_token in [
                        "if", "else", "for", "while", "def", "return",
                        "class", "import", "from", "in", "and", "or", "not"
                    ]:
                        classification = "Keyword"
                    else:
                        classification = "Identifier"
                elif token_type == "NUMBER":
                    classification = "Number Literal"
                elif token_type == "STRING":
                    classification = "String Literal"
                elif token_type == "OP":
                    classification = "Operator / Symbol"
                elif token_type == "NEWLINE":
                    classification = "New Line"
                elif token_type == "INDENT":
                    classification = "Indentation"
                elif token_type == "DEDENT":
                    classification = "Dedentation"
                else:
                    classification = "Other"

                table.insert("", tk.END, values=(token_type,classification, specific_token))

        except tokenize.TokenError:
            table.insert("", tk.END, values=("ERROR", "Invalid Syntax", ""))

    root = tk.Tk()
    root.title("Python Tokenizer")
    root.geometry("850x500")

    tk.Label(root, text="Python Tokenizer", font=("Arial", 16, "bold")).pack(pady=10)

    input_box = tk.Text(root, height=10, width=90)
    input_box.pack(pady=10)

    tk.Button(root, text="TOKENIZER", command=run_tokenizer, font=("Arial", 12, "bold")).pack(pady=10)

    table = ttk.Treeview(
        root,
        columns=("Token Type", "Token Name Classification", "Specific Token"),
        show="headings"
    )

    table.heading("Token Type", text="Token Type")
    table.heading("Token Name Classification", text="Token Name Classification")
    table.heading("Specific Token", text="Token symbol")

    table.column("Token Type", width=150, anchor="center")
    table.column("Token Name Classification", width=300, anchor="center")
    table.column("Specific Token", width=300, anchor="center")

    table.pack(fill="both", expand=True, pady=10)

    root.mainloop()


tokenizer_app()