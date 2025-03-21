import random

def uniform_distribution(a, b, size=1):
    """
    Generuje liczby z rozkładu jednostajnego w przedziale [a, b].
    
    :param a: Dolna granica przedziału.
    :param b: Górna granica przedziału.
    :param size: Liczba liczb do wygenerowania.
    :return: Lista wygenerowanych liczb.
    """
    return [random.uniform(a, b) for _ in range(size)]

def normal_distribution(mean, std_dev, size=1):
    """
    Generuje liczby z rozkładu normalnego (Gaussa).
    
    :param mean: Średnia rozkładu.
    :param std_dev: Odchylenie standardowe.
    :param size: Liczba liczb do wygenerowania.
    :return: Lista wygenerowanych liczb.
    """
    return [random.gauss(mean, std_dev) for _ in range(size)]

def exponential_distribution(lambda_, size=1):
    """
    Generuje liczby z rozkładu wykładniczego.
    
    :param lambda_: Parametr lambda (intensywność).
    :param size: Liczba liczb do wygenerowania.
    :return: Lista wygenerowanych liczb.
    """
    return [random.expovariate(lambda_) for _ in range(size)]