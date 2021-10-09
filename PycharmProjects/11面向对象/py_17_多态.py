class Dog:
    def work(self):
        pass

class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DrugDog(Dog):
    def work(self):
        print('追查毒品')

# 定义人类
class Person:
    def work_with_dog(self, dog):
        dog.work()


zhangsan = Person()

xiaoliu = ArmyDog()
zhangsan.work_with_dog(xiaoliu)

xiaoqi = DrugDog()
zhangsan.work_with_dog(xiaoqi)
