class Person:
    def get_name(self):
        if not hasattr(self, 'se_name'):
            son_name = self.__class__.__name__
            raise AttributeError(f"'{son_name}' object has no attribute 'se_name'")

        name1 = self.__getattribute__('se_name')
        name2 = self.__class__.__getattribute__(self, 'se_name')
        print(name1, name2)
        # return name
        # else:
        #     print(hasattr(self, 'se_name'))


class Student(Person):
    se_name = "张三"
    i = 1


if __name__ == '__main__':
    stu = Student()
    stu.get_name()
