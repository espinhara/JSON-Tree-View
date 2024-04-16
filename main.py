import tkinter as tk
from tkinter import ttk
import json

def process_json():
    json_str = input_text.get("1.0", tk.END)
    try:
        data = json.loads(json_str)
        populate_tree(data)
    except json.JSONDecodeError as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Erro ao carregar o JSON: {e}")

def populate_tree(data):
    tree.delete(*tree.get_children())
    add_node(tree, "", data)

def add_node(tree, parent, node):
    if isinstance(node, dict):
        for key, value in node.items():
            item_id = tree.insert(parent, "end", text=str(key))
            add_node(tree, item_id, value)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            item_id = tree.insert(parent, "end", text=str(i))
            add_node(tree, item_id, item)
    else:
        tree.insert(parent, "end", text=str(node))

# Cria a janela principal
root = tk.Tk()
root.title("JSON Tree Viewer")

# Define um estilo para o Treeview
style = ttk.Style()
style.configure("Treeview", background="#f0f0f0", fieldbackground="#f0f0f0", font=("Arial", 10))

# Cria uma caixa de texto para inserir o JSON
input_text = tk.Text(root, width=80, height=10)
input_text.pack(pady=10)

# Cria um botão para processar o JSON
process_button = tk.Button(root, text="Processar JSON", command=process_json, bg="#4CAF50", fg="white")
process_button.pack()

# Cria o Treeview
tree = ttk.Treeview(root)
tree.pack(expand=True, fill="both", padx=10, pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
