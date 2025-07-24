import tkinter as tk 
from tkinter import messagebox, simpledialog
import json
import os

NOME_ARQUIVO = "tarefas.json"


def carregar_tarefas():
    
    if not os.path.exists(NOME_ARQUIVO):
        return []
    with open(NOME_ARQUIVO, "r") as f:
        return json.load(f)
    


def salvar_tarefas():
    with open(NOME_ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)
        
        

def atualizar_lista():
    listbox_tarefas.delete(0, tk.END)
    for tarefa in tarefas:
        status = "✔" if tarefa["conluída"] else " "
        listbox_tarefas.insert(tk.END, f'[{status}] {tarefa["descricao"]}')
        if tarefa["Conclúida"]:
            listbox_tarefas.itemconfig(tk.END, {'bg': '#d9ead3'})

def adicionar_tarefa():
    descricao = simpledialog.askstring("Adicionar tarefa", "Digite a descrição da tarefa:")
    if descricao:
        tarefas.append({"descricao": descricao, "concluída": False})
        salvar_tarefas(tarefas)
        atualizar_lista()
        

def remover_tarefa():
    try:
        indice_selecionado = listbox_tarefas.curselection()[0]
        tarefas.pop(indice_selecionado)
        salvar_tarefas(tarefas)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")

def marcar_concluida():
    try:
        indice_selecionado = listbox_tarefas.curselection()[0]
        tarefas[indice_selecionado]["Concluída"] = True
        salvar_tarefas(tarefas)
        atualizar_lista() 
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para marcar como concluída")
        

# Janela (Interface Gráfica)

janela = tk.Tk()
janela.title("Organizador de tarefas")
janela.geometry("500x400")


tarefas = carregar_tarefas

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_adicionar = tk.Button(frame_botoes, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(side=tk.LEFT, padx=5)

btn_remover = tk.Button(frame_botoes, text="Remover Tarefa", command=remover_tarefa)
btn_remover.pack(side=tk.LEFT, padx=5)

btn_concluir = tk.Button(frame_botoes, text="Marcar como Concluída", command=marcar_concluida)
btn_concluir.pack(side=tk.LEFT, padx=5)


listbox_tarefas = tk.Listbox(janela, width=50, height=15, font=("Arial, 12"))
listbox_tarefas.pack(pady=10)

atualizar_lista()


janela.mainloop()





