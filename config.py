# Arquivo para armazenar configurações gerais

# Diretórios padrão
dir_json = 'json'
dir_saida = 'saida'
dir_config = 'config_json'

# Define o tipo de arquivo a ser salvo:
        # True = XLSM
        # False = JSON
tipo_arquivo_saida = False

# URLs
LattesBaseURL = 'https://lattes.cnpq.br/'
palavras_chave_limpeza = ['Descrição:', 'Projeto certificado ']

# Armazenagem de dados
conteudo_projeto = {    "pesq": None, 
                        "ext" : None, 
                        "dev" : None, 
                        "nome": None,
                        "id"  : None
                        }

dados_classificados = { 
                    'pesquisador'     : " ",
                    'ano_inicio'      : " ",
                    'ano_fim'         : " ",
                    'titulo'          : " ",
                    'situacao'        : " ",
                    'natureza'        : " ",
                    'alunos'          : " ",
                    'integrantes'     : " ",
                    'financiador'     : " ",
                    'tipo_financiador': " ",
                    'num_orientacoes' : " ",
                    'num_producoes'   : " "   
                                                                                    
}

# Não implementado
conteudo_publicacao = {"nome": None,
                       "id"  : None} 

# Configurações de interface gráfica
resolucao       = "600x400"
versao          = "1.0.0"
cor_fundo       = "#F5F5F5" #1c1c1c
cor_letra       = "#ececec"
cor_ativo       = "#007aff"
fonte           =("Segoe UI", 9)
caminho_assetUI = "UI/assets/"

sobre_texto = f"""
            DATA INSIGHT: Coletor de Dados Acadêmicos
            Versão: {versao}
            
            Aluno: Bruno Moraes
            
            Coordenador: 
            Rafael Silva Guimarães
            Leandro Marochio Fernandes
            
            
            IFES Campus Cachoeiro de Itapemirim
        
        """
