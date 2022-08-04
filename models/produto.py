from utils.helper import float_to_str

class Produto:
    
    contador: int = 1
    
    def __init__(self: object, name: str, price: float ) -> None:
        self.__codigo = Produto.contador
        self.__name = name
        self.__price = price
        Produto.contador += 1

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def price(self: object) -> float:
        return self.__price

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    def __str__(self: object) -> str:
        return f'Código: {self.codigo} \nName: {self.name} \nPrice: {float_to_str(self.price)}'