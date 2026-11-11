def factorial(n): 
    if n == 0: 
        return 1 
    else: 
        return n * factorial(n - 1)

def fibonacci(n): 
    if n <= 1: 
        return n 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

def is_palindrome(s): 
    if len(s) <= 1: 
        return True 
    else: 
        return s == s[-1] and is_palindrome(s[1:-1])

def power(a, n): 
    if n == 0: 
        return 1 
    elif n % 2 == 1: 
        return power(a, n - 1) * a 
    else: 
        return power(a, n // 2) ** 2

def make_multiplier(factor): 
    def multiply(x): 
        return x * factor 
    return multiply

def process_data(data): 
    def clean(text): 
        return text.strip().lower() 
    return [clean(item) for item in data]

def make_counter(): 
    count = 0 
    def counter(): 
        nonlocal count 
        count += 1 
        return count 
    return counter
 
def my_decorator(func): 
    def wrapper(): 
        print("Начало") 
        func() 
        print("Конец") 
        return wrapper @my_decorator 
    def my_function(): 
        print("Выполнение") 
        my_function()

def show_args(*args): 
    print(f"Количество: {len(args)}") 
    print(f"Аргументы: {args}")
def concat(*words): 
    return ''.join(words)
 

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b