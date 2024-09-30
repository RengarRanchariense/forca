import customtkinter
import random


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #CONFIG APP
        self.title("FORCA")
        self.geometry("800x600")
        self.minsize(800,600)
        self.maxsize(800,600)
        self.config(background="white")
        self.lifes = 5
        
        #CONFIG COLUMN
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.tema_escolhido = ""
        self.palavra_secreta = ""
        self.letters_used = []
        self.word_sorted = []
        
        
        
        
        
        #LABELS
        self.label_game = customtkinter.CTkLabel(self,text="JOGO DA FORCA",
                                                 text_color="black",
                                                 font=("Helvetica", 80,"bold"),
                                                 justify="center", fg_color="white", pady=20)
        self.label_game.grid(pady=30, sticky="we", row=0, column=0, columnspan=3)
        
        self.label_tema = customtkinter.CTkLabel(self,text="A DICA É: " + self.tema_escolhido,
                                                 text_color="black",
                                                 font=("Helvetica", 30,"bold"),
                                                 justify="center", fg_color="white", pady=10)
        self.label_tema.grid(row=1, columnspan=3, sticky ="nesw")
        
        self.label_word = customtkinter.CTkLabel(self,text="",
                                                 text_color="black",
                                                 font=("Helvetica", 60,"bold"),
                                                 justify="center", fg_color="white", pady=10)
        self.label_word.grid(row=2, columnspan=3, sticky ="nesw")
        
        self.label_aux_used = customtkinter.CTkLabel(self, text="LETRAS UTILIZADAS", text_color="black",
                                                     font=("Helvetica", 20,"bold"),
                                                     justify="center", fg_color="white", pady=5)
        self.label_aux_used.grid(row=3,columnspan=3)
        
        
        self.label_letter_used = customtkinter.CTkLabel(self, text="", text_color="black",
                                                     font=("Helvetica", 10,"bold"),
                                                     justify="center", fg_color="white", pady=5)
        self.label_letter_used.grid(row=4,columnspan=3)
        
        self.lifes_label = customtkinter.CTkLabel(self, text=f"VOCÊ POSSUI: {self.lifes} VIDAS RESTANTES ", text_color="black",
                                                     font=("Helvetica", 10,"bold"),
                                                     justify="center", fg_color="white", pady=10)
        self.lifes_label.grid(row=5,columnspan=3)
        
        #entrada de dados
        
        self.letter_entry = customtkinter.CTkEntry(self,placeholder_text="DIGITE A SUA LETRA", width=60, height=40, justify="center")
        self.letter_entry.grid(row=6, column=1, sticky ="nesw")
        
        #BOTÃO
        self.btn = customtkinter.CTkButton(self, text="SORTEAR PALAVRA", width=100, height=40, command=self.sort)
        self.btn.grid(row=7, column=1,sticky ="nesw", pady=15)
        
    def play(self):
            letra = self.letter_entry.get().lower()
            self.letter_entry.delete(0, customtkinter.END)
            self.letters_used.append(letra.upper())
            
            self.label_letter_used.configure(text=" ".join(self.letters_used).upper())
            
            if letra in self.palavra_secreta:
                for idx, char in enumerate(self.palavra_secreta):
                    if char == letra:
                        self.word_sorted[idx] = letra
                        
                self.label_word.configure(text=" ".join(self.word_sorted).upper())
                
                if "_" not in self.word_sorted:
                    self.label_game.configure(text="VOCÊ VENCEU", text_color="green")
                    self.btn.configure(text="RECOMEÇAR", command=self.restart_game)
                    
            else:
                self.lifes -= 1
                self.lifes_label.configure(text=f"VOCÊ POSSUI: {self.lifes} VIDAS RESTANTES")
                
                if self.lifes == 0:
                    self.label_game.configure(text="GAME OVER", text_color="red")
                    self.label_word.configure(text=self.palavra_secreta.upper())
                    self.btn.configure(text="RECOMEÇAR", command=self.restart_game)
                    
    def restart_game(self):
        self.lifes=5
        self.letters_used = []
        self.word_sorted = []
        self.label_letter_used.configure(text="")
        self.lifes_label.configure(text=f"VOCÊ POSSUI: {self.lifes} VIDAS RESTANTES")
        self.label_game.configure(text="JOGO DA FORCA", text_color="black")
        self.sort()
        
            
    def sort(self):
            palavras = {
                "animais": ["cachorro", "gato", "elefante", "girafa", "tartaruga", "leao", "tigre", "zebra", "canguru", "urso"],
                "frutas": ["banana", "maca", "uva", "laranja", "abacaxi", "melancia", "morango", "kiwi", "pera", "manga"],
                "profissoes": ["medico", "engenheiro", "advogado", "professor", "padeiro", "carpinteiro", "bombeiro", "piloto", "dentista", "policial"],
                "cores": ["vermelho", "azul", "amarelo", "verde", "roxo", "laranja", "branco", "preto", "rosa", "cinza"],
                "países": ["brasil", "argentina", "canada", "japao", "alemanha", "franca", "australia", "india", "egito", "mexico"],
                "esportes": ["futebol", "basquete", "tenis", "volei", "natacao", "boxe", "ciclismo", "atletismo", "golfe", "surfe"],
                "instrumentos": ["violao", "piano", "bateria", "flauta", "saxofone", "guitarra", "trompete", "baixo", "violino", "harpa"],
                "comidas": ["pizza", "hamburguer", "lasanha", "sushi", "batata", "esfiha", "tacos", "cuscuz", "brigadeiro", "churrasco"],
                "veiculos": ["carro", "moto", "bicicleta", "caminhao", "onibus", "navio", "trem", "aviao", "helicoptero", "patinete"],
                "filmes": ["inception", "avatar", "titanic", "gladiador", "matrix", "jumanji", "interestelar", "coringa", "frozen", "rocky"]}
            
            self.tema_escolhido = random.choice(list(palavras.keys()))
            self.palavra_secreta = random.choice(palavras[self.tema_escolhido])
            
            self.label_tema.configure(text="A DICA É: " + self.tema_escolhido.upper())
            self.word_sorted = ["_" for _ in self.palavra_secreta]
            self.label_word.configure(text=" ".join(self.word_sorted))
            
            self.btn.configure(text="TENTAR LETRA", command=self.play)
                    
        
        
        
app = App()
app.mainloop()