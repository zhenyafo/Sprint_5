import random
import string
import time


class Generators:
    @staticmethod
    def generate_email():
        first_name = "testuser"
        last_name = "testov"
        cohort = "99"
        random_numbers = ''.join(random.choices(string.digits, k=3))
        timestamp = str(int(time.time()))[-3:]
        
        return f"{first_name}_{last_name}_{cohort}_{random_numbers}{timestamp}@yandex.ru"
    
    @staticmethod
    def generate_password(length=6):
        if length < 6:
            length = 6
        
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))
    
    @staticmethod
    def generate_name():
        names = ["Алексей", "Мария", "Иван", "Елена", "Сергей", "Ольга", "Дмитрий", "Анна"]
        return random.choice(names)
    
    @staticmethod
    def generate_invalid_password():
        return ''.join(random.choices(string.ascii_letters, k=5))
     