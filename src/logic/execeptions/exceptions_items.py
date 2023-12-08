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

class EmptyListProjects(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class FileNameBlank(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class DirectoryBlank(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class InvalidFileFormat(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class InvalidFileEstucture(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class FileNotFoundError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)