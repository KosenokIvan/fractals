from typing import Dict


class LSystem:
    def __init__(self, axiom: str, theorems: Dict[str, str], cash_size: int = 16):
        self.axiom = axiom
        self.theorems = theorems
        self.cash = [""] * cash_size
        self.cash[0] = self.axiom

    def __getitem__(self, index: int):
        if index < 0:
            raise ValueError("Negative index")
        if index < len(self.cash) and self.cash[index] != "":
            return self.cash[index]
        result = ""
        for char in self[index - 1]:
            result += self.theorems.get(char, char)
        if index < len(self.cash):
            self.cash[index] = result
        return result

    def set_parameters(self, axiom: str, theorems: Dict[str, str], cash_size: int = 16):
        self.axiom = axiom
        self.theorems = theorems
        self.cash = [""] * cash_size
        self.cash[0] = self.axiom


if __name__ == '__main__':
    axiom_ = "X"
    theorems_ = {
        "X": "X+YF+",
        "Y": "-FX-Y"
    }
    l_system = LSystem(axiom_, theorems_)
    for i in range(10):
        print(l_system[i])
