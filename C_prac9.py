# C_prac9.ipynb
# Chapter 9 Exercises

# Problem: Counter

class Counter:
    def __init__(self, name):
        self.name = name
        self.count = 0
    def reset(self):
        self.count = 0
        print(f'{self.name}이 초기화 되었습니다.')
    def increment(self):
        self.count += 1
    def get(self):
        return self.count


a = Counter('counter1')
b = Counter('counter2')
for i in range(10):
    a.increment()
    b.increment()
print(a.get())
print(b.get())
a.reset()
print(a.get())


# Problem: Stadium Count

import random
crowdTicket = [random.randint(0,1) for i in range(10000)]

soccer = Counter('Soccer')
baseball = Counter('Baseball')

for i in crowdTicket:
    if i == 0:
        soccer.increment()
    elif i == 1:
        baseball.increment()

print(f'{soccer.name}: {soccer.get()}')
print(f'{baseball.name}: {baseball.get()}')

# Problem: Circle Class

from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius__ = radius
    def getRadius(self):
        return round(self.__radius__, 3)
    def calArea(self):
        return round(pi * (self.__radius__ ** 2), 3)
    def calCircum(self):
        return round(2 * pi * self.__radius__, 3)

radius = float(input('Input: '))
c = Circle(radius)
print('원의 반지름: ', c.getRadius())
print('원의 넓이: ', c.calArea())
print('원의 둘레: ', c.calCircum())


# Problem: Caesar Password

class Sender:
    '''
    Class for sending the password.
    '''

    def slider(self, n, m):
        '''
        Function to generate the moved password.
        '''
        def letter_slider(letter):
            '''
            Function to generate moved letter (individual basis).
            '''
            ind = ord(letter)
            if letter.islower():
                newind = (ind - 97 + n) % 26 + 97
                return chr(newind)
            elif letter.isupper():
                newind = (ind - 65 + n) % 26 + 65
                return chr(newind)
            else:
                return letter
            
        temp_list = list(m)
        new_list = []
        for i in temp_list:
            new_list.append(letter_slider(i))
        ans = ''.join(new_list)
        return ans
    
    def send(self, n, m, classReceiver):
        '''
        Sending the moved pw to Receiver class.
        '''
        print(self.slider(n, m))
        classReceiver.receive(self.slider(n, m))


class Receiver:
    def receive(self, txt):
        '''
        Receives the encoded password
        '''
        self.m = txt
    
    def reverse_slider(self, n):
        '''
        Function to generate the original password.
        '''
        def letter_slider(letter):
            '''
            Function to generate original letter (individual basis).
            '''
            ind = ord(letter)
            if letter.islower():
                newind = (ind - 97 - n) % 26 + 97
                return chr(newind)
            elif letter.isupper():
                newind = (ind - 65 - n) % 26 + 65
                return chr(newind)
            else:
                return letter
            
        temp_list = list(self.m)
        new_list = []
        for i in temp_list:
            new_list.append(letter_slider(i))
        ans = ''.join(new_list)
        return ans
    
    def decode(self, n):
        '''
        Decoding and returning the original pw.
        '''
        print(self.reverse_slider(n))
        return self.reverse_slider(n)
    

# Problem: BankAccount Class

class BankAccount:
    '''
    Bank Account Class for managing your precious funds
    '''
    def __init__(self, owner, alias = "자유입출금"):
        '''
        Set initial state
        '''
        self.__owner__ = owner
        self.__alias__ = alias
        self.__balance__ = 0
        print('안녕하세요. 컴핵은행입니다.')
        print(f'{self.__owner__}님 {self.__alias__} 계좌를 개설하였습니다.')
    
    def deposit(self, n):
        '''
        Deposit money in bank account
        '''
        self.__balance__ += n
        print(f'{self.__alias__} 계좌에 {n}원을 입금하였습니다.')
    
    def withdraw(self, n):
        '''
        Withdraw money from bank account
        '''
        if n > self.__balance__:
            print(f'{self.__alias__} 계좌의 잔액이 부족합니다.')
        else:
            self.__balance__ -= n
            print(f'{self.__alias__} 계좌에서 {n}원을 출금하였습니다.')
    
    def bankBalance(self):
        '''
        Show bank account balance
        '''
        print(f'{self.__alias__} 계좌의 잔액은 {self.__balance__}원입니다.')


# Problem: Box Class
