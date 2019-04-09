class Contact2:
    # 이름 , 전화번호, 이메일, 주소를 입력받아서 자료구조에 저장하는 예제
    def __init__(self, name,phone,email,addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):

        print("이름 {} \n"
              "전화번호 {} \n"
              "이메일 {} \n"
              "주소 {} \n".format(
             self.name
            ,self.phone
            ,self.email
            ,self.addr))

    @staticmethod
    def set_contact():
        name = input("이름")
        phone = input("핸드폰번호")
        email = input("이메일")
        addr = input("주소")
        contact2 = Contact2(name,phone,email,addr)

        return contact2

    @staticmethod
    def get_contact(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def del_contact(ls, name):
        for i, t in enumerate(ls):
            if t.name == name:
                del ls[i]

    @staticmethod
    def print_menu():
        print("1. 연락처입력")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴 선택")

        return int(menu)

    @staticmethod
    def run():
        ls = []
        while 1:
            menu = Contact2.print_menu()

            if menu == 1:
                t = Contact2.set_contact()
                ls.append(t)

            elif menu == 2:
                Contact2.get_contact(ls)

            elif menu == 3:
                name = input("삭제할 이름")
                Contact2.del_contact(ls, name)

            elif menu == 4:
                break
