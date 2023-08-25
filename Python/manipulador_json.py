from os import system
import json

class json_back:
    def __init__(self) -> None:
        self.dados={}
        
    def novo_item(self, Nome, endereco_exe, endereco_icon):
        """o arquivo de imagem precisa ter no minimo 168x269 e no maximo 350x500"""
        self.dados[Nome]={"Exe": endereco_exe, "Ico": endereco_icon}
    
    def carregar(self):
        with open("Python/paths.json", "r") as arq:
            self.dados=json.load(arq)
        return self.dados

    def salvar(self):
        """
        Escreve novas alterações no paths.json
        """
        with open('Python/paths.json', 'w') as arq:
            json.dump(self.dados, arq, indent=4, sort_keys=True)

if __name__=="__main__":
    home=json_back()
    print(home.carregar())

#system(f"start {dados[game]}")
