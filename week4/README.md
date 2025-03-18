Класс для работы с денежными суммами.
    
    Атрибуты:
        amount (float): Сумма денег.
        currency (str): Валюта.
        
    Методы:
        __init__(self, amount: float, currency: str = "RUB")
            Инициализирует объект с заданной суммой и валютой (по умолчанию RUB).
            
        __str__(self) -> str
            Возвращает строку, представляющую объект в человекочитаемом формате.
            
        __add__(self, other: 'Money') -> 'Money'
            Осуществляет сложение двух денежных единиц одной валюты.
            
        __sub__(self, other: 'Money') -> 'Money'
            Осуществляет вычитание двух денежных единиц одной валюты.
            
        __mul__(self, multiplier: Union[int, float]) -> 'Money'
            Умножает сумму на числовой множитель.
            
        __eq__(self, other: 'Money') -> bool
            Проверяет равенство двух денежных единиц.
            
        from_string(cls, str_value: str) -> 'Money'
            Создает объект на основе строки вида '1000 RUB'.
            
        save(self, filename: str) -> None
            Сохраняет объект в файл в формате JSON.
            
        load(cls, filename: str) -> 'Money'
            Загружает объект из файла в формате JSON.
            
        to_rub(self) -> 'Money'
            Конвертирует сумму в рубли.
            
        to_usd(self) -> 'Money'
            Конвертирует сумму в доллары.
            
        to_eur(self) -> 'Money'
            Конвертирует сумму в евро.