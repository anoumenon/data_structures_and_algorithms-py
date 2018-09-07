class Cat(object):
    '''
    Node in a stack.
    '''

    def __init__(self, tag, _next=None):
        self.tag = tag
        self._next = _next

    def __data__(self):
        return f'{self}'

    def __repr__(self):
        return(
            f'<Cat | tag: {self.tag} | Next: {self._next}>'
            )


class Dog(object):
    '''
    Node in a stack.
    '''

    def __init__(self, tag, _next=None):
        self.tag = tag
        self._next = _next

    def __data__(self):
        return f'{self}'

    def __repr__(self):
        return(
            f'<Dog | tag: {self.tag} | Next: {self._next}>'
            )


class Queue(object):
    '''
    Singly linked list class as queue.
    '''
    def __init__(self):
        '''
        Instantiation
        O(1) time.
        '''
        self._front = None
        self._back = None
        self.length = 0

    def __str__(self):
        return(
             f'Front: {self._front}'
             )

    def __repr__(self):
        return(
            f'<Queue | Front: {self._front}')

    def enq(self, animal):
        """
        String
        """
        if self._front is None:
            self._front = animal
            self._back = animal
        else:
            self._back._next = animal
            self._back = animal

    def deq(self):
        """
        String
        """
        if self._front:
            adopt = self._front
            if self._front._next:
                self._front = self._front._next
            else:
                self._front = None
            adopt._next = None
            return adopt
        else:
            return False


class Shelter(object):
    """string
    """
    def __init__(self):
        """string
        """
        self.cats = Queue()
        self.dogs = Queue()
        self.tags = 0
        self.count = 0

    def __str__(self):
        return(
            f'tags: {self.tags} | count: {self.count}'
        )

    def __repr__(self):
        return(
            f'tags: {self.tags} | count: {self.count}'
        )

    def __len__(self):
        return self.count

    def enqueue(self, animal):
        if animal is 'dog':
            pupper = Dog(self.tags)
            self.tags += 1
            self.count += 1
            self.dogs.enq(pupper)

        if animal is 'cat':
            kitty = Cat(self.tags)
            self.tags += 1
            self.count += 1
            self.cats.enq(kitty)
        elif animal:
            pass

    def dequeue(self, animal):
        if animal is 'dog' and self.dogs._front:
            self.count -= 1
            self.dogs.deq()

        if animal is 'cat' and self.cats._front:
            self.count -= 1
            self.cats.deq()

        elif animal and (self.dogs._front or self.cats._front):
            if self.dogs._front and self.cats._front:
                if self.dogs._front.tag < self.cats._front.tag:
                    self.dogs.deq()
                    return
                else:
                    self.cats.deq()
                    return
            elif self.dogs._front:
                self.dogs.deq()
                return
            elif self.cats._front:
                self.cats.deq()
                return
            else:
                pass
        else:
            return False
