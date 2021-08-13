# First Program in Python 3
    
    print("Hello World!!")
    >>>Hello World!!   

# __Data Types in Python(Built-in)__
## __Single Data Points(Single Value)__
* __Number__ 
    * Integer
    * Float
    * Complex
* __String__
* __Boolean__
***
### **Example of single data point:**
### __Number:-__
Create a valid variable name and assign a value to it.Then print the value using *print()* function

    >>>my_age = 21
    >>>your_age = 22
    >>>my_weight = 50.5
    >>>print("I'm "+ my_age+ "years old")
    I'm 21years old
>__Check the data type using__ *type()* __function__

    # Integer data type
    >>>type(my_age)
    <class 'int'> 

    # Float data type
    >>>type(my_weight)
    <class 'float'>

#### *__Complex:__*
Complex number has two parts *real* and *imaginary* part.

> **Create a Complex Number**

    >>>z = complex(3, -4)
    >>>print(z)
    (3-4j)
    >>>type(z)
    <class 'complex'>
    >>>z = 4 - 5j
    >>>z
    (4-5j)


***
### __String:-__ 
"Strings in python are surrounded by either single quotation marks, or double quotation marks." - *w3schools*

    # Double Quote
    >>>my_name = "Sakib"
    >>>print(my_name)
    Sakib
    # Single Quote
    >>>his_name = 'John Doe'
    >>>print(his_name)
    John Doe 
> **Check the data type using *type()* function**
    >> Single and Double quote gives the same results

    >>>type(my_name)
    <class 'str'>
    >>>type(his_name)
    <class 'str'>
---
### __Boolean:-__
In python Boolean data types either `True` or `False`. Spell exactly `True` or `False` not `true`,`false` or any formats.


    >>>is_raining = True
    >>>print(is_raining)
    True
    >>>print(5 > 3)
    False

> **Check The Data Type Using *type()* Function:**

    >>>type(is_raining)
    <class 'bool'>
    >>>type(5>3)
    <class 'bool'>
    >>>type(False)
    <class 'bool'>
---
## **Many Data Points(Multiple Values)**
* **Lists**
* **Tuple**
* **Dictionary**
* **Set**
---
### **Examples of Multiple Data Point:**
## **Lists:-**
"Lists are used to store multiple items in a single variable." - *w3schools*
## Lists Characteristics:
* Ordered
* Mutable
* Allow Duplicates
> **Create a Lists:**


    >>>dept_list = ['EEE','CSE','ME','CE']
    >>>print(dept_list)
    ['EEE','CSE','ME','CE']

    # lists using list() constructor
    >>>new_dept_list = list(('Archi','ChE','ETE','ECE'))
    ['Archi','ChE','ETE','ECE']

> **Check Data Types:**

    >>>type(dept_list)
    <class 'list'>

> **Lists Operations**

`Indexing`

    # indexing starts from 0 
    >>>dept_list[0]
    'EEE'
    # negative indexing starts from last items
    >>>dept_list[-1]
    'CE'

`Slicing`

    # slicing starts from n1 to (n2-1)
    >>>dept_list[1:3]
    ['CSE','ME']