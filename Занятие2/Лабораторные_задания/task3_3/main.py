def header_footer(decorate):  # TODO написать декоратор
    def wrapper():
        print("========")
        decorate()
        print("========")
    return wrapper

@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
