from typing import Dict


class LSystem:
    def __init__(self, axiom: str, theorems: Dict[str, str]):
        self.axiom = axiom
        self.theorems = theorems

    def get_l_string(self, index: int):
        if index < 0:
            raise ValueError("Negative index")
        if index == 0:
            return self.axiom
        result = ""
        for char in self.get_l_string(index - 1):
            result += self.theorems.get(char, char)
        return result


if __name__ == '__main__':
    axiom_ = "X"
    theorems_ = {
        "X": "X+YF+",
        "Y": "-FX-Y"
    }
    l_system = LSystem(axiom_, theorems_)
    for i in range(10):
        print(l_system.get_l_string(i))
