
from bmi_calc.bmi import Bmi


def main():
    bmi = Bmi(input("이름을 입력하시오")
              ,int(input("키를 입력하세요"))
              ,int(input("몸무게를 입력하세요")))
    print("{}님에 BMI지수는 {}입니다 {}".format(bmi.name, bmi.bmi()))


if __name__ == '__main__':
    main()
