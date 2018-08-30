from a_queue import Queue


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
        return self.length

    def enqueue(self, animal):

        if animal == 'cat' or 'dog':
            self.animal.enqueue(animal, self.tags)
            self.tags += 1
            self.count += 1
        else:
            print('cat or dog only')
            return False

    def dequeue(self, pref):
        if pref == 'cat' or 'dog':
            self.pref.dequeue()
        else:
            cat_head = self.cats._front.tag
            dog_head = self.dogs._front.tag
            if cat_head > dog_head:
                self.cats.dequeue()
            else:
                self.dogs.dequeue()
        self.count -= 1
