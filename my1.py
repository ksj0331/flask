class woman:
    name = ""
    weight = 50
    id = 20
    iq = 120
    height = 170

    def __init__(self, str):
         self.name = str

    def eat(self):
        self.weight+=1
        print(self.name + "가 먹었습니다.")

    def study(self):
        self.iq+=1
        print(self.name + "가 싸웠습니다.")

    def sleep(self):
        self.height+=1
        print(self.name + "가 잠을 잤습니다.")

    def show(self):
        print(self.name, "의 상태는", self.weight, "kg, ",self.height, "cm, ", self.iq, "iq 입니다.")

