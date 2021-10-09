class Student(object):
    def __init__(self, name, gender, tel):
        # 姓名、性别、手机号
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}  {self.gender}  {self.tel}'


if __name__ == '__main__':
    xiaoming = Student('小明', 'M', '18342219148')
    print(xiaoming)
