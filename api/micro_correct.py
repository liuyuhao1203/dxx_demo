import os

class MicroCorrect:
    # 类变量，属于类，不属于单个实例
    class_variable = '我是一个类变量'
    current_file_path = os.path.abspath(__file__)
    current_directory_path = os.path.dirname(current_file_path)

    def __init__(self, name, age):
        # 实例变量，属于类的每个实例
        self.name = name
        self.age = age

    @classmethod
    def correct_logic(cls, user_input):
        """
        逻辑性文字修复功能
        """
        try:
            with open(cls.current_directory_path + '/pt/corrcet_pt/logic.pt', 'r', encoding='utf-8') as f:
                logic_pt = f.read()
                logic_pt = logic_pt.replace('${text}', user_input)
            return logic_pt
            # if user_input.lower() == 'exit':  # 检查用户是否想要退出
            #     print("Exiting the program.")
            #     break

        except KeyboardInterrupt:
            rint("Program was interrupted by user.")
    
    def greet(self):
        # 实例方法，使用实例变量
        print(f"Hello, {self.name}. You are {self.age} years old.")

    @classmethod
    def class_method(cls):
        # 类方法，使用类变量
        print(f"You are using the class method of {cls.__name__}.")
        print(f"The class variable is: {cls.class_variable}")

    @staticmethod
    def static_method():
        # 静态方法，不使用类或实例变量
        print("This is a static method. It does not have access to class or instance variables.")

if __name__ == '__main__':
    MicroCorrect.correct_logic()