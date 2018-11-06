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
1. [stack](#stack)
1. [queue](#queue)
1. [binary_tree](#binary_tree)
1. [binary_search_tree](#binary_search_tree)
1. [graph](#graph)

##### Sorts <br>

1. [selection_sort](#selection_sort)
1. [merge_sort](#merge_sort)
1. [quick_sort](#quick_sort)
1. [radix_sort](#radix_sort)

##### Algorithms <br>

1. [reverse_arr](#reverse_arr)
1. [insert_shift_arr](#insert_shift_arr)
1. [array_binary_search](#array_binary_search)
1. [matrix_rotate](#matrix_rotate)
1. [nth_fibonacci](#nth_fibonacci)
1. [merge_lists](#merge_lists)
1. [queue_with_stacks](#queue_with_stacks)
1. [fifo_animal_shelter](#fifo_animal_shelter)
1. [multi_bracket_validation](#multi_bracket_validation)
1. [repeated_word](#repeated_word)
1. [tree_intersection](#tree_intersection)
<!-- TODO map filter reduce -->

---

## DATA STRUCTURES


<a id="single_linked_list"></a>
### 1. single_linked_list <br>

Single direction linked list class.<br>

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/linked_lists)<br>

In computer science, a linked list is a linear collection of data elements, whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which together represent a sequence.<br>


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

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/stack)<br>

A stack is an abstract data type that serves as a collection of elements, with two principal operations:<br>

push, which adds an element to the collection, and
pop, which removes the most recently added element that was not yet removed.<br>
The order in which elements come off a stack gives rise to its alternative name, LIFO (last in, first out). Additionally, a peek operation may give access to the top without modifying the stack.<br>

[:top: Contents](#contents)

---


<a id="queue"></a>
### 3. queue <br>

Double linked list class for use as a queue.<br>

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/queue)<br>

A queue is a particular kind of abstract data type (ADT) or collection in which the entities in the collection are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue. This makes the queue a First-In-First-Out (FIFO) data structure.<br>

[:top: Contents](#contents)

---

<a id="binary_tree"></a>
### 4. binary_tree <br>

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.<br>

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/binary_tree)<br>

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

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/binary_tree)<br>

Binary search trees (BST), sometimes called ordered or sorted binary trees, are a particular type of container: data structures that store "items" (such as numbers, names etc.) in memory. They allow fast lookup, addition and removal of items, and can be used to implement either dynamic sets of items, or lookup tables that allow finding an item by its key (e.g., finding the phone number of a person by name).<br>

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

A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph.<br>

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/graph)<br>

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/graph.jpg) <br>

breadth first traversal:
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/graph_breadth_first.jpg) <br>
depth first traversal:
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/depth_first.jpg) <br>
path weight accumulation:
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/get_edges.jpg) <br>


[:top: Contents](#contents)

---

<a id="hash_table"></a>
### 5. hash_table <br>

Hash Table.<br>

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/data_structures/hash_table)<br>

A hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.<br>

* `.put(key, value)` - store a value with the given key
* `.get(key)` - get the value associated with the given key
* `.update(key, value)` - modify the value associated with the given key
* `.remove(key)` - delete a value associated with a key
* `.keys()` - return a collection of all the keys

[:top: Contents](#contents)

Left join:

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/left_join.png) <br>
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/hash_join.jpg) <br>

---

## SORTS

<a id="selection_sort"></a>
### 1. selection_sort <br>

Selection sort.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/sorting_algos/selection)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/selection_sort.jpg) <br>

[:top: Contents](#contents)

---

<a id="merge_sort"></a>
### 2. merge_sort <br>

Write a function that accepts an array of integers, and returns an array sorted by a recursive mergesort algorithm.


[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/sorting_algos/merge)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/merge_sort.jpg) <br>
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/merge_sort_2.jpg) <br>

[:top: Contents](#contents)

---


<a id="merge_sort"></a>
### 2. merge_sort <br>

Write a function that accepts an array of integers, and returns an array sorted by a recursive quicksort algorithm.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/sorting_algos/merge)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/merge_sort.jpg) <br>
![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/merge_sort_2.jpg) <br>

[:top: Contents](#contents)

---

<a id="radix_sort"></a>
### 2. radix_sort <br>

Write a function that accepts an array of integers, and returns an array sorted by a radix algorithm.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/sorting_algos/radix)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/radix.jpg) <br>

[:top: Contents](#contents)

---

## ALGORITHIMS


<a id="reverse_arr"></a>
### 1. reverse_arr <br>

Write a function called reverse_arr that takes an array as an argument and returns it in reverse.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/sorting_algos/quicksort)

[:top: Contents](#contents)

---

<a id="insert_shift_arr"></a>
### 2. insert_shift_arr <br>

Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.<br>
IN [4,8,15,23,42], 16<br>
OUT [4,8,15,16,23,42]<br>

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/array_shift)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/01_insert_shift_arr.jpg) <br>

[:top: Contents](#contents)

---

<a id="array_binary_search"></a>
### 3. array_binary_search <br>

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/array_binary_search)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/02_array_binary_search.jpg) <br>

[:top: Contents](#contents)

---

<a id="matrix_rotate"></a>
### 4. matrix_rotate <br>

Ask the candidate to write a function to rotate a 3x3 matrix (an array of integers), by 90 degrees clockwise.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/matrix_rotate)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/matrix_rotate.jpg) <br>

[:top: Contents](#contents)

---

<a id="nth_fibonacci"></a>
### 5. nth_fibonacci <br>

Ask the candidate to write a function to accepts an integer, and returns the nth number in the Fibonacci sequence.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/nth_fibonacci)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/nth%20fibonacci.jpg) <br>

[:top: Contents](#contents)

---

<a id="merge_lists"></a>
### 6. merge_lists <br>

Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/ll_merge)

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

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/fifo_animal_shelter)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/fifo_animal_shelter.jpg) <br>

[:top: Contents](#contents)

---

<a id="multi_bracket_validation"></a>
### 9. multi_bracket_validation <br>

Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/multi_bracket_validation)

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

<a id="tree_intersection"></a>
### 10. tree_intersection <br>

Write a function that accepts a lengthy string parameter.
Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

[code](https://github.com/jasonb315/data_structures_and_algorithms/tree/master/challenges/tree_intersection)

![title](https://github.com/jasonb315/data_structures_and_algorithms/blob/master/assets/tree_intersection.jpg) <br>

[:top: Contents](#contents)

---




tree_intersection
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
