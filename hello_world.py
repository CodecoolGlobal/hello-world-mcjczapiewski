i = 1


def hello_world():
    return "Hello, World!"


def hello(name):
    if name:
        say_what = "Hello, " + name + "!"
    else:
        say_what = "Hellow, World!"
    return say_what


def print_hello(name):
    say_what = name.say_what
    if say_what:
        print(say_what)

# def print_cmd_line():

# def print_mltp_args():


def task():
    global i
    print("\nTASK NO", i)
    i += 1


task()
hi_you = hello_world()
print(hi_you)

task()
name = input("Hi! What's your name?: ")
hi_you = hello(name)
print(hi_you)

task()
hi_you = print_hello(name)
print(hi_you)