
class Bmi:
    def __init__(self,name,hei,wei):
        self.wei = wei
        self.hei = hei
        self.name = name

    def bmi(self):
        bmi = (self.wei / (self.hei * self.hei)) * 10000

        if bmi >= 40:
            return "고도비만, {}".format(bmi)

        elif bmi >= 35:
            return "중등도 비만, {}".format(bmi)

        elif bmi >= 30:
            return "경도비만, {}".format(bmi)

        elif bmi >= 25:
            return "과체중, {}".format(bmi)

        elif bmi >= 18:
            return "정상, {}".format(bmi)

        else:
            return "저체중{}".format(bmi)

