import customtkinter as ctk

# Configuração do tema
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

# Criando a janela principal
janela = ctk.CTk()
janela.title("Calculadora")
janela.geometry("285x425")  

# Criando o display
texto_display = ctk.StringVar()
campo_display = ctk.CTkEntry(
    janela, textvariable=texto_display, font=("Arial", 28), 
    justify="right", width=320, height=50, corner_radius=10
)
campo_display.pack(pady=15, padx=10)

# Função para lidar com cliques nos botões
def clique_botao(valor):
    texto_atual = texto_display.get()
    if valor == "=":
        try:
            resultado = eval(texto_atual)  # Calcula a expressão
            texto_display.set(resultado)
        except Exception:
            texto_display.set("Erro")
    elif valor == "C":
        texto_display.set("")  #Limpa o display
    else:
        texto_display.set(texto_atual + valor)  # Adiciona o número/símbolo ao display

layout_botoes = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
]


frame_botoes = ctk.CTkFrame(janela)
frame_botoes.pack(pady=10)

for linha in layout_botoes:
    linha_frame = ctk.CTkFrame(frame_botoes)
    linha_frame.pack()
    for rotulo in linha:
        if rotulo in ["C", "=", "+", "-", "*", "/"]:
            cor_botao = "#FF8C00"  
            cor_hover = "#D47600"  
        else:
            cor_botao = "#808080"  
            cor_hover = "#6E6E6E"  

        botao = ctk.CTkButton(
            linha_frame, text=rotulo, width=70, height=70, 
            font=("Arial", 20), corner_radius=10, 
            fg_color=cor_botao, 
            hover_color=cor_hover,
            text_color="white", 
            command=lambda v=rotulo: clique_botao(v)
        )
        botao.pack(side="left", padx=5, pady=5)

# Iniciar a interface
janela.mainloop()
