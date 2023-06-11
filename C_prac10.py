# C_prac10.ipynb
# Chapter 10 Exercises

# Problem: Stack
class Stack:
    def __init__(self):
        '''
        Create a new Stack
        '''
        self.__stack__ = []
    
    def __str__(self):
        '''
        Print the stack in the following format: S<item1, item2, item3, ...>S
        '''
        t = str(self.__stack__)[1:-1]
        return 'S<' + t + '>S'

    def push(self, item):
        '''
        Put item into stack
        '''
        self.__stack__.append(item)
    
    def isEmpty(self):
        '''
        Return whether stack is empty
        '''
        return not(bool(self.__stack__))

    def pop(self):
        '''
        Pop impending item in stack. Print 'Stack is empty' if so.
        '''
        if self.isEmpty():
            print('Stack is empty')
        else:
            return self.__stack__.pop()

    def size(self):
        '''
        Return size of stack
        '''
        return len(self.__stack__)


# Problem: Queue
class Queue:
    def __init__(self):
        '''
        Create a Queue
        '''
        self.__queue__ = []

    def __str__(self):
        '''
        Set the printed form
        '''
        t = str(self.__queue__)[1:-1]
        return 'Q<' + t + '>Q'
    
    def isEmpty(self):
        '''
        Return whether Queue is empty
        '''
        return not(bool(self.__queue__))
    
    def enqueue(self, item):
        '''
        Enlist item to queue
        '''
        self.__queue__.append(item)
    
    def dequeue(self):
        '''
        Remove foremost item from queue
        '''
        if not(self.isEmpty()):
            return self.__queue__.pop(0)
        else:
            print('Queue is empty')
    
    def size(self):
        '''
        Return size of queue
        '''
        return len(self.__queue__)
    
    def peek(self):
        '''
        Only view foremost item in Queue
        '''
        return self.__queue__[0]
    

# Problem: Palindrome Check
def ispalindrome(txt):
    '''
    Checks if given string is a palindrome.
    '''
    def stripper(txt):
        '''
        Strips the string to a favorable string w/ only lowercase letters.
        '''
        t_list = list(txt)
        t_list = filter(lambda x: x.isalpha(), t_list)
        t_list = list(map(lambda x: x.lower(), t_list))
        return ''.join(t_list)
    
    txt = stripper(txt)
    txt_stack = Stack()
    t_list = list(txt)
    for letter in t_list:
        txt_stack.push(letter)
    rev_list = []
    while not txt_stack.isEmpty():
        rev_list.append(txt_stack.pop())
    if t_list == rev_list:
        return True
    else:
        return False


# Problem: Parentheses Matching
def bracket(txt):
    t_list = list(txt)
    t_list = filter(lambda x: not(x.isalpha()), t_list)

    bracket_stack = Stack()
    bracket_dic = {'}':'{', ')':'(', ']':'['}
    for i in t_list:
        if i not in bracket_dic.keys():
            bracket_stack.push(i)
        if i in bracket_dic.keys():
            if bracket_stack.isEmpty():
                return False
            elif bracket_dic[i] != bracket_stack.pop():
                return False
    if not bracket_stack.isEmpty():
        return False
    else:
        return True
    

# Problem: Fibonacci
def Fibonacci(n):
    '''
    Calculates fibonacci number using Queue
    '''
    fib_queue = Queue()
    fib_queue.enqueue(0)
    fib_queue.enqueue(1)
    for i in range(2, n+1):
        fib_queue.enqueue(fib_queue.dequeue() + fib_queue.peek())
    _ = fib_queue.dequeue()
    return fib_queue.dequeue()


# Problem: Double-ended Queue

class DoubleQueue:
    '''
    Class description of Double-ended Queue
    '''
    def __init__(self):
        '''
        Initialization of dQ
        '''
        self.__dQ__ = []
    
    def __str__(self):
        '''
        Set printing form of dQ
        '''
        t = str(self.__dQ__)[1:-1]
        return 'dQ<' + t + '>dQ'
    
    def addFront(self, e):
        '''
        Add e to Front of dQ
        '''
        self.__dQ__.insert(0, e)
    
    def addRear(self, e):
        '''
        Add e to Rear of dQ
        '''
        self.__dQ__.append(e)
    
    def deleteFront(self):
        '''
        Delete Front Element
        '''
        return self.__dQ__.pop(0)
    
    def deleteRear(self):
        '''
        Delete Last Element
        '''
        return self.__dQ__.pop(-1)
    
    def getFront(self):
        '''
        Get Front Element
        '''
        return self.__dQ__[0]
    
    def getRear(self):
        '''
        Get Rear Element
        '''
        return self.__dQ__[-1]
    
    def isEmpty(self):
        '''
        Return if dQ is Empty
        '''
        return not(bool(self.__dQ__))
    
    def size(self):
        '''
        Return size of dQ
        '''
        return len(self.__dQ__)
    

# Problem: Card Game
def cardGame(n = int(input('Input: '))):
    '''
    Get last card of card game
    '''
    card_dQ = DoubleQueue()
    for i in range(1, n+1):
        card_dQ.addRear(i)
    while card_dQ.size() != 1:
        card_dQ.deleteFront()
        card_dQ.addRear(card_dQ.deleteFront())
    return card_dQ.getFront()


# Problem: Calculator