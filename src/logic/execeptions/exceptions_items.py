class ItemNameAlreadyExists(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class ItemNameBlank(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)       

class UnknownItem(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class NonChangeableProperty(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        
class ItemDontHaveThisAttribute(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
