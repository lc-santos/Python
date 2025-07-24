import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# Nome do arquivo para salvar as tarefas
NOME_ARQUIVO = "tarefas.json"

# --- Funções da Lógica do Aplicativo ---

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON. Se o arquivo não existir, retorna uma lista vazia."""
    if not os.path.exists(NOME_ARQUIVO):
        return []
    with open(NOME_ARQUIVO, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(NOME_ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def atualizar_lista():
    """Limpa a lista na tela e a recarrega com as tarefas atuais."""
    listbox_tarefas.delete(0, tk.END)
    for tarefa in tarefas:
        status = "✓" if tarefa["concluida"] else " "
        listbox_tarefas.insert(tk.END, f'[{status}] {tarefa["descricao"]}')
        # Adiciona uma cor de fundo diferente para tarefas concluídas
        if tarefa["concluida"]:
            listbox_tarefas.itemconfig(tk.END, {'bg':'#d9ead3'}) # Verde claro

def adicionar_tarefa():
    """Pede ao usuário uma nova tarefa e a adiciona à lista."""
    descricao = simpledialog.askstring("Nova Tarefa", "Digite a descrição da tarefa:")
    if descricao:
        tarefas.append({"descricao": descricao, "concluida": False})
        salvar_tarefas(tarefas)
        atualizar_lista()

def remover_tarefa():
    """Remove a tarefa selecionada."""
    try:
        indice_selecionado = listbox_tarefas.curselection()[0]
        tarefas.pop(indice_selecionado)
        salvar_tarefas(tarefas)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")

def marcar_como_concluida():
    """Marca a tarefa selecionada como concluída."""
    try:
        indice_selecionado = listbox_tarefas.curselection()[0]
        tarefas[indice_selecionado]["concluida"] = True
        salvar_tarefas(tarefas)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para marcar como concluída.")

# --- Interface Gráfica ---

# Cria a janela principal
janela = tk.Tk()
janela.title("Meu Organizador de Tarefas")
janela.geometry("500x400") # Define o tamanho da janela

# Carrega as tarefas
tarefas = carregar_tarefas()

# Frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10) # Adiciona um espaço vertical

# Botões
btn_adicionar = tk.Button(frame_botoes, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(side=tk.LEFT, padx=5)

btn_remover = tk.Button(frame_botoes, text="Remover Tarefa", command=remover_tarefa)
btn_remover.pack(side=tk.LEFT, padx=5)

btn_concluir = tk.Button(frame_botoes, text="Marcar como Concluída", command=marcar_como_concluida)
btn_concluir.pack(side=tk.LEFT, padx=5)

# Listbox para exibir as tarefas
listbox_tarefas = tk.Listbox(janela, width=50, height=15, font=("Arial", 12))
listbox_tarefas.pack(pady=10)

# Atualiza a lista na tela ao iniciar
atualizar_lista()

# Inicia o loop principal da aplicação
janela.mainloop()