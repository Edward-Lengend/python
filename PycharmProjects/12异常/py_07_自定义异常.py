"""
在Python中，抛出自定义异常的语法为raise异常类对象。
用raise抛出自定义异常类对象

需求：密码长度不足，则报异常（用户输入密码，如果输入的长度不足3位，
    则报错，即抛出自定义异常，并捕获该异常）。

"""
# 1.自定义异常类
# 2.抛出异常
# 3.捕获该异常


class ShortInputError(Exception):  # 自定义异常类要继承Exception类
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 设置异常类描述信息
    def __str__(self):
        return f'您输入的密码长度是{self.length}， 最小密码长度为{self.min_len}'


def main():
    try:
        passwd = input('请输入你的密码')
        if len(passwd) < 3:
            raise ShortInputError(len(passwd), 3)
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')

main()