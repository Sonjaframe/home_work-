class math:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self) -> None:
        sum = self.a + self.b
        return print(f"Сложение: {sum}")
    def multiplication(self) -> None:
        mult = self.a * self.b
        return print(f"Умножение: {mult}")
    def division(self) -> float:
        div = self.a/self.b
        if self.b ==0:
            return print(f"Деление ноль невозможно")
        else:
            return print(f"Деление: {div}")
    def subtraction(self) -> None:
        subt = self.a - self.b
        return print(f"Вычетание: {subt}")
math_obj = math(80, 5)
math_obj.addition()
math_obj.multiplication()
math_obj.division()
math_obj.subtraction()
      # print( self.a / self.b)
   # def subtraction(self):
        #print(self.a - self.b)