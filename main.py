import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import csv
from scrapper import *
from config import *
from format_data import *

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.title(f"Data Insight {versao}")
        self.iconbitmap(f"{caminho_assetUI}DATA_INSIGHT.ico")
        self.geometry(resolucao)
        self.configure(bg=cor_fundo)
        self.resizable(0, 0)
        
        # Variáveis dos caminhos
        self.caminho_arquivo = tk.StringVar()  # CSV
        self.caminho_diretorio = tk.StringVar()  # Caminho para salvar o arquivo
        self.caminho_diretorio.set('saida')  # Caminho de saída padrão
        
        # Variável para o formato de saída
        self.tipo_arquivo_saida = tk.StringVar(value="XLSM")  # Valor inicial XLSM
        
        # Menu suspenso
        self.menu_suspenso()

        # Logo
        logo_img = tk.PhotoImage(file=f"{caminho_assetUI}Title2.png")
        self.rotulo = tk.Label(self, image=logo_img, bg=cor_fundo, 
                               border="0", activebackground=cor_fundo, highlightthickness=0, bd=0, relief="flat")
        self.rotulo.image = logo_img  
        self.rotulo.place(x=300, y=100, anchor="center")

        # Botão CSV
        cont_img = tk.PhotoImage(file=f"{caminho_assetUI}inserir.png")
        self.botao_conteudo = tk.Button(self, image=cont_img, command=self.selecao_arquivo,
                                       bg=cor_fundo, activebackground=cor_fundo, border="0", bd=0, relief="flat")
        self.botao_conteudo.image = cont_img 
        self.botao_conteudo.place(x=230, y=250, anchor="center")
        
        # Botão Coletar
        b_coletar_img = tk.PhotoImage(file=f"{caminho_assetUI}coletar_cont.png")
        self.botao_coletar = tk.Button(self, image=b_coletar_img, command=self.coletar_dados, 
                               bg=cor_fundo, activebackground=cor_fundo, border="0", 
                               highlightthickness=0, bd=0, relief="flat")
        self.botao_coletar.image = b_coletar_img  
        self.botao_coletar.place(x=370, y=250, anchor="center")


    def menu_suspenso(self):
        menu_bar = tk.Menu(self)
        
        # Menu de configuração dos arquivos
        config_menu = tk.Menu(menu_bar, bg=cor_fundo, activebackground=cor_ativo)
        config_menu.add_command(label="Saída de arquivo", command=self.selec_dir)
        config_menu.add_command(label="Formato de Saída", command=self.selec_formato_arquivo)
        
        # Adiciona o menu a barra no topo da janela
        menu_bar.add_cascade(label="Arquivo", menu=config_menu)
        menu_bar.add_cascade(label="Sobre", command=self.abrir_sobre)
        
        # Define o menu na janela
        self.config(menu=menu_bar)

    # Função para selecionar o diretório
    def selec_dir(self):
        self.diretorio_saida = filedialog.askdirectory(title="Selecione a pasta de saída dos dados")
        if self.diretorio_saida:
            self.caminho_diretorio.set(f"{self.diretorio_saida}")
            global dir_saida
            dir_saida = self.diretorio_saida
            messagebox.showinfo("Pasta de Saída", f"Pasta selecionada: {self.diretorio_saida}")
           

    # Função para selecionar o arquivo CSV
    def selecao_arquivo(self):
        caminho_selec_arquivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if caminho_selec_arquivo:
            self.caminho_arquivo.set(caminho_selec_arquivo)
            messagebox.showinfo("Seleção de Arquivo", f"Arquivo selecionado: {caminho_selec_arquivo}")

    # Função para selecionar o formato de saída
    def selec_formato_arquivo(self):
        # Janela de seleção de formato
        janela_format = tk.Toplevel(self)
        janela_format.title("Formato de Saída")
        janela_format.geometry("300x150")
        
        ttk.Label(janela_format, text="Formato de Arquivo:").grid(row=0, column=0, padx=10, pady=10)
        tipo_arquivo_saida = ttk.Combobox(janela_format, values=["JSON", "XLSM"], state="readonly")
        tipo_arquivo_saida.grid(row=0, column=1, padx=10, pady=10)
        tipo_arquivo_saida.set(self.tipo_arquivo_saida.get()) 

        def set_arq_form():
            self.tipo_arquivo_saida.set(tipo_arquivo_saida.get()) 
            janela_format.destroy()
            messagebox.showinfo("Formato de Arquivo", f"Formato selecionado: {self.tipo_arquivo_saida.get()}")

        botao_ok = ttk.Button(janela_format, text="OK", command=set_arq_form)
        botao_ok.grid(row=1, column=1, padx=10, pady=10, sticky="e")

    # Função para abrir "Sobre"
    def abrir_sobre(self):
        janela_sobre = tk.Toplevel(self)
        janela_sobre.title("Sobre")
        janela_sobre.geometry("400x400")
        janela_sobre.iconbitmap(f"{caminho_assetUI}DATA_INSIGHT.ico")
        janela_sobre.configure(bg=cor_fundo)
        janela_sobre.resizable(0, 0)
        janela_sobre.bind('<Escape>', lambda e: janela_sobre.destroy())
        
        logo_img = tk.PhotoImage(file=f"{caminho_assetUI}DI_logo(150).png")
        rotulo = tk.Label(janela_sobre, image=logo_img, bg=cor_fundo, 
                        border="0", relief="flat")
        rotulo.image = logo_img  
        rotulo.place(x=200, y=90, anchor="center")
        
        texto_sobre = tk.Label(janela_sobre, text=sobre_texto, bg=cor_fundo, 
                            wraplength=350, justify="center")
        texto_sobre.place(x=183, y=270, anchor="center")

    def coletar_dados(self):
        try:
            caminho_arquivo_csv = self.caminho_arquivo.get()  
            if caminho_arquivo_csv:
                with open(caminho_arquivo_csv, newline='') as arquivo_csv:
                    lattesIDs = list(csv.reader(arquivo_csv))
                    
                    for index, linha in enumerate(lattesIDs):
                        if len(linha) > 0:
                            id = linha[0].strip()
                            LattesURL = f"{LattesBaseURL}{id}"
                            
                            coletor = ScrapLattes(LattesURL)
                            conteudo = coletor.coletar_conteudo()

                            if conteudo:
                                lattes_formatar_conteudo(conteudo)

                            coletor.sair()
                        else:
                            print(f"Linha {index+1} está vazia e foi ignorada.")
                            
                messagebox.showinfo("Completo", "Coleta de dados finalizada com sucesso!")
                if self.tipo_arquivo_saida.get() == "XLSM":
                    converter_xlsm(dir_json, dir_saida)
                else:
                    salvar_dados_json(dados_classificados, dir_saida)
                
            else:
                messagebox.showwarning("Atenção", "Nenhum arquivo CSV selecionado")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a execução: {e}")

if __name__ == "__main__":
    app = AppGUI()
    app.mainloop()
