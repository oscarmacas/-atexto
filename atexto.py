class MoneyToTextConverter:
    def __init__(self):
        self.units = [
            "cero", "un", "dos", "tres", "cuatro", "cinco",
            "seis", "siete", "ocho", "nueve", "diez", "once",
            "doce", "trece", "catorce", "quince", "dieciséis",
            "diecisiete", "dieciocho", "diecinueve"
        ]
        
        self.tens = [
            "", "", "veinte", "treinta", "cuarenta", "cincuenta",
            "sesenta", "setenta", "ochenta", "noventa"
        ]
        
        self.hundreds = [
            "", "ciento", "doscientos", "trescientos", "cuatrocientos",
            "quinientos", "seiscientos", "setecientos", "ochocientos",
            "novecientos"
        ]
        
    def convert(self, amount):
        if amount == 0:
            return "cero"
        
        words = ""
        
        # Procesar millones
        millions = amount // 1000000
        if millions > 0:
            words += self._convert_less_than_thousand(millions) + " millón "
            amount %= 1000000
        
        # Procesar miles
        thousands = amount // 1000
        if thousands > 0:
            words += self._convert_less_than_thousand(thousands) + " mil "
            amount %= 1000
        
        # Procesar cientos
        if amount > 0:
            words += self._convert_less_than_thousand(amount)
        
        return words.strip()
    
    def _convert_less_than_thousand(self, num):
        if num >= 100:
            return self.hundreds[num // 100] + " " + self._convert_less_than_thousand(num % 100)
        elif num >= 20:
            return self.tens[num // 10] + " " + self.units[num % 10]
        else:
            return self.units[num]

def main():
    converter = MoneyToTextConverter()
    
    while True:
        try:
            amount = float(input("Introduce la cantidad de dinero: "))
            break
        except ValueError:
            print("Cantidad no válida. Introduce un número válido.")

    dollars = int(amount)
    cents = int((amount - dollars) * 100)

    text_representation = converter.convert(dollars) + " dólares"
    if cents > 0:
        text_representation += f" con {converter.convert(cents)} centavos"

    print(f"{amount:.2f} en palabras: {text_representation}")

if __name__ == "__main__":
    main()
