# Data Structures and Algorithms in Python
```python
school = 'Code Fellows'
cohort = 'seattle-py-401d9'
person = 'Jason Burns'
```
---
<a id="contents"></a>

### Contents <br>

##### Data Structures <br>

1. [single_linked_list](#single_linked_list)
2. [stack](#stack)
3. [queue](#queue)
4. [binary_tree](#binary_tree)
5. [binary_search_tree](#binary_search_tree)
6. [graph](#graph)

##### Algorithms <br>

1. [reverse_arr](#reverse_arr)
2. [insert_shift_arr](#insert_shift_arr)
3. [array_binary_search](#array_binary_search)
4. [matrix_rotate](#matrix_rotate)
5. [nth_fibonacci](#nth_fibonacci)
6. [merge_lists](#merge_lists)
7. [queue_with_stacks](#queue_with_stacks)
8. [fifo_animal_shelter](#fifo_animal_shelter)
9. [multi_bracket_validation](#multi_bracket_validation)
10. [repeated_word](#repeated_word)


---

## DATA STRUCTURES


<a id="single_linked_list"></a>
### 1. single_linked_list <br>

Single direction linked list class.<br>

[link: code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/linked_lists)<br>

Methods;<br>
prepend: create and attach a node with a passed value to the head of the list.<br>
append: create and attach a node with a passed value to the tail of the list.<br>
includes: check the list for a given value. returns a bool.<br>
read_off: prints a list of the values of the linked list in order from the head.<br>
insert_before: create and attach a node with a passed value before a given value.<br>
insert_after: create and attach a node with a passed value after a given value.<br>
kth_from_end: print and return the value of a node a given number from the end.<br>


kth_from_end:
![kth_from_end](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/kth_from_end.jpg) <br>
append:
![ll_append](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/ll_append.jpg) <br>
insert_before:
![ll_insert_before](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/ll_insert_before.jpg) <br>
insert_after:
![ll_insert_after](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/ll_insert_after.jpg) <br>

[:top: Contents](#contents)

---

<a id="stack"></a>
### 2. stack <br>

Single direction linked list class for use as a stack.<br>

[link: code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/stack)<br>

In stack.py:
Create a Class for a Stack which creates an empty Stack when instantiated
This class should be aware of a default None value assigned to top when the isntance is created
This class should be aware of the len of the stack, which represents the count of Nodes in the stack at any time
This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the stack for each value in the iterable
Define any further magic methods such as len and str to support user functionality and informative responses
Define a method called push which takes any value as an argument and adds that value to the top of the stack with an O(1) Time performance
Define a method called pop which takes no arguments and removes / returns the Node at the top of the stack
Define a method called peek which takes no arguments and returns the Node at the top of the stack

[:top: Contents](#contents)

---


<a id="queue"></a>
### 3. queue <br>

Double linked list class for use as a queue.<br>

[link: code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/queue)<br>

In queue.py:
Create a Class for a Queue which creates an empty Queue when instantiated
This class should be aware of a default None value assigned to front when the isntance is created
This class should be aware of a default None value assigned to back when the isntance is created
This class should be aware of the len of the queue, which represents the count of Nodes in the queue at any time
This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the queue for each value in the iterable
Define any further magic methods such as len and str to support user functionality and informative responses
Define a method called enqueue which takes any value as an argument and adds that value to the back of the queue with an O(1) Time performance
Define a method called dequeue which takes no arguments and removes / returns the Node at the front of the queue

[:top: Contents](#contents)

---

<a id="binary_tree"></a>
### 4. binary_tree <br>

Nodes with up to two children each stemming from a root.<br>

[link: code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/binary_tree)<br>

Insert a node of the value given above a node with a target val.
Parent maintains branch side.
```python
def insert_above(self, val, target):
```
Insert a node of a val below to the L or R of a node with a target val
Children maintain branch side.
```python
def insert_below(self, val, target, side='L'):
```
![insert_before_after](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/insert_before_after.jpg) <br>

Search the tree for the maximm node value:
![find_max_value](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/find_max_value.jpg) <br>

[:top: Contents](#contents)

---

<a id="binary_search_tree"></a>
### 5. binary_search_tree <br>

Brinary search tree.<br>

[link: code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/binary_tree)<br>

This section is a binary search tree.
It organizes nodes in a binary structure from the root out.
Instantiation of a tree:
```python
acorn = BinaryTree()
```
Nodes are instantiated in val:data pairs.
Instantiation of a tree can be done with a list of iterables:
```python
oak = BinaryTree([(3, 'a'), (1, 'b'), (5, 'c')])
```
Or with a single, which is an iterable of one:
```python
sapling = BinaryTree([(8888, 'port')])
```
Additional inserts take one node at a time,
and are placed with binary logic by the integer val:
```python
def insert(self, val=None, data=None)

sapling.insert(315, 'new leaf')
```

Breadth first traversal:
![breadth_first_traversal](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/breadth_first_traversal.jpg) <br>

[:top: Contents](#contents)

---

<a id="graph"></a>
### 6. graph <br>

Non leanear vertex relationships.<br>
This graph class containes methods for:
Adding a vertex
Checking for a vertex
Adding an edge between verts
Aquiring the neighbors of a vertex
Breadth first traversal
Path (sequential edges) check

[link: code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/graph)<br>

In graph.py:
Create a Class for a Graph which creates an empty Graph when instantiated
Define any further magic methods such as len and str to support user functionality and informative responses
Define methods to add, create, count, and connect node in the graph

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/graph.jpg) <br>

breadth first traversal:
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/graph_breadth_first.jpg) <br>
depth first traversal:
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/depth_first.jpg) <br>
path weight accumulation:
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/get_edges.jpg) <br>




[:top: Contents](#contents)

---

## ALGORITHIMS


<a id="reverse_arr"></a>
### 1. reverse_arr <br>

Write a function called reverse_arr that takes an array as an argument and returns it in reverse.

[link: coded solution](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/reverse_array)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/reverse_array.jpg) <br>

[:top: Contents](#contents)

---

<a id="insert_shift_arr"></a>
### 2. insert_shift_arr <br>

Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.<br>
IN [4,8,15,23,42], 16<br>
OUT [4,8,15,16,23,42]<br>

[link: coded solution](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/array_shift)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/01_insert_shift_arr.jpg) <br>

[:top: Contents](#contents)

---

<a id="array_binary_search"></a>
### 3. array_binary_search <br>

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

[link: coded solution](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/array_binary_search)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/02_array_binary_search.jpg) <br>

[:top: Contents](#contents)

---

<a id="matrix_rotate"></a>
### 4. matrix_rotate <br>

Ask the candidate to write a function to rotate a 3x3 matrix (an array of integers), by 90 degrees clockwise.

[link: coded solution](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/matrix_rotate)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/matrix_rotate.jpg) <br>

[:top: Contents](#contents)

---

<a id="nth_fibonacci"></a>
### 5. nth_fibonacci <br>

Ask the candidate to write a function to accepts an integer, and returns the nth number in the Fibonacci sequence.

[link: coded solution](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/nth_fibonacci)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/nth%20fibonacci.jpg) <br>

[:top: Contents](#contents)

---

<a id="merge_lists"></a>
### 6. merge_lists <br>

Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

[link: coded solution](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/ll_merge)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/ll_merge.jpg) <br>

[:top: Contents](#contents)

---

<a id="queue_with_stacks"></a>
### 7. queue_with_stacks <br>

Implement the following methods for the Queue class:

enqueue(value) which inserts value into the Queue using a first-in, first-out approach.
dequeue() which extracts a value from the Queue using a first-in, first-out approach.
You have access to 2 Stack instances with push and pop methods.

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/queue_with_stacks.jpg) <br>

[:top: Contents](#contents)

---

<a id="fifo_animal_shelter"></a>
### 8. fifo_animal_shelter <br>

Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
dequeue(pref): returns either a dog or a cat. If pref, a string, is ‘cat’ return the longest-waiting cat. If pref is ‘dog’, return the longest-waiting dog. For anything else, return either a cat or a dog.

[link: coded solution](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/fifo_animal_shelter)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/fifo_animal_shelter.jpg) <br>

[:top: Contents](#contents)

---

<a id="multi_bracket_validation"></a>
### 9. multi_bracket_validation <br>

Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

[link: coded solution](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/multi_bracket_validation)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/multi_bracket_validation.jpg) <br>

[:top: Contents](#contents)

---

<a id="repeated_word"></a>
### 10. repeated_word <br>

Write a function that accepts a lengthy string parameter.
Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/repeated_word.jpg) <br>

[:top: Contents](#contents)

---

<!--
<a id="NAME"></a>
### X. NAME <br>

>des of problem

![title](https://github.com/jasonb315/data-structures-and-algorithms/blob/master/assets/NAME.jpg) <br>

[:top: Contents](#contents)

---
-->


<!--
Links:
http://github.com - automatic!
[GitHub](http://github.com)
-->

<!--
  * [1. NAME](#NAME)
-->
