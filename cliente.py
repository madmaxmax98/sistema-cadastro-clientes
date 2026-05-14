class Cliente:
    def __init__(self, nome, email, telefone, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"