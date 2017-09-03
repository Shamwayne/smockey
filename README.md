# Soshy-Mock (now on v0.2.2)
A barebones User and Comments Mock Object Generator for use in testing or automated database generation.
Still a work in progress but basic functionality of generating MockUsers and MockComments is already functional.

## Usage

To use the library, just import the relevant object from soshy

```python
from soshy import MkBasicUser, MockComment

```

Importing a generator is just as simple

```python
from soshy import genBasicUsers, genMockComments
```

## Basic Examples

To create a single user with data you specify, Just create a MockUser object with custom attribute values. e.g:
```python
from soshy import MkBasicUser

john = MkBasicUser("John", "john@somemail.com", "Male", "password123")

john.username # returns "John"
john.email    # returns "john@somemail.com"
john.gender   # returns "Male"
john.password # returns a hashed value of "password123" by default. To remove this,  add False as the last attribute
```

But mostly this library was intented for creating a large amount of MockUser objects.
Soshy was mainly intended for internal user for quickly populating an database with test data and for automated web testing
To automate generating a list of MockUsers Objects, simple use the **genBasicUsers()** command

```python
from soshy import MkBasicUser, genBasicUsers

users_list = genBasicUsers()

type(users_list) # returns <list object>
len(users_list) # returns 10. the default number of MockUsers generated is 10

users_list[0] 
#<MockUser => username=rjuszczak0, email=kbaudinet0@surveymonkey.com, gender=Male,     password=803dc4a1c83e747a7dbfbccbf8d26b11ec7f7c598070e49d543e8190b866091b816ebfa261ef5082c0bfbc142441b16b2b0ce14131ece77718c4db2a282293ac >

users_list[0].username # returns "rjuszczak0"
users_list[0].gender # "Male"
```

For Examples of how to use Soshy for generating database, check the test files. Basic implementation details are outlined both for SqlAlchemy as well as mongoengine.


## Coming soon
- Comments Documentation
- additional classes
- how to extend the base classes



