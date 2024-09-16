from selenium.webdriver.common.by import By
from browser import iniciar_browser
from config import *


# Classe para coletar dados dos perfis Lattes
class ScrapLattes:
    def __init__(self, url):
        self.url = url
        self.browser = iniciar_browser()
        
    def sair(self):
        self.browser.quit()
        
    def coletar_conteudo(self):
        try:
            self.browser.get(self.url)
            # Utilizar apenas com interface gráfica para resolução de captcha
            self.browser.implicitly_wait(25) 
            
            try:
                pesq_id = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[1]/ul/li[2]/span")
                conteudo_projeto["id"] = pesq_id.text
                print(conteudo_projeto["id"])                                                                               # Debug
                nome_pesq_element = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[1]/h2")
                conteudo_projeto["nome"] = nome_pesq_element.text if nome_pesq_element else "Nome não encontrado"
                
                if self.browser.find_elements(By.XPATH, '//a[@name="ProjetosPesquisa"]'):
                    print(f"Projetos de Pesquisa encontrados de {conteudo_projeto['nome']} {conteudo_projeto['id']}")       # Debug
                    pesquisa = self.browser.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div/div/div/div[9]/div')
                    conteudo_projeto["pesq"] = [element.text for element in pesquisa]
                else:
                    print("Projetos de Pesquisa não encontrados")

                if self.browser.find_elements(By.XPATH, '//a[@name="ProjetosExtensao"]'):
                    print(f"Projetos de Extensão encontrados de {conteudo_projeto['nome']} {conteudo_projeto['id']}")       # Debug
                    extensao = self.browser.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[10]/div")
                    conteudo_projeto["ext"] = [element.text for element in extensao]
                else:
                    print("Projetos de Extensão não encontrados")

                if self.browser.find_elements(By.XPATH, '//a[@name="ProjetosDesenvolvimento"]'):
                    print(f"Projetos de Desenvolvimento encontrados de {conteudo_projeto['nome']} {conteudo_projeto['id']}")  # Debug
                    desenvolvimento = self.browser.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/div/div[11]/div")
                    conteudo_projeto["dev"] = [element.text for element in desenvolvimento]
                else:
                    print("Projetos de Desenvolvimento não encontrados")
                
                return conteudo_projeto

            except Exception as e:
                print(f"Erro ao acessar perfil: {e}")

        except Exception as e:
            print(f"Erro ao acessar o browser: {e}")
            return None