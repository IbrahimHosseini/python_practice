from decorators import do_twice, timer


@do_twice
def say_greet():
    return 'Hi Ebrahim'


@do_twice
def say_greet_again(name):
    return f'Hi {name} again'



@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])



waste_some_time(999)