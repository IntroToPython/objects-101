objects-101
===========

Let's make some simple objects!


Example
===========

```python
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance
```
        

Blog Post
===========
http://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/


Book
===========

Think Python: How to Think Like a Computer Scientist

http://www.greenteapress.com/thinkpython/thinkpython.pdf


Sharing Your Work
===========
1) Once in Cloud9, create a new file named (yourname).py.
![Create a new file.](http://cl.ly/image/0q161Z3f2K3h/Screen%20Shot%202014-10-01%20at%208.26.18%20PM.png)

2) Use the terminal to add your file to the repository.
- `git add (yourname.py)`
- `git commit -m "(Commit Message)"`
- `git push origin master`
- ![Add, Commit, Push](http://cl.ly/image/0m2H373m1j2h/Screen%20Shot%202014-10-01%20at%208.28.01%20PM.png)

3) Create a pull request from your fork to the IntroToPython/objects-101 repo.
- At the main screen for your fork, click the large green button with arrows on it next to the branch name.
- Click the large Create Pull Request button and name your pull request.
- Click Create Pull Request one more time.
![Creating a PR](http://cl.ly/image/1i232B3L1R0c/Screen%20Shot%202014-10-01%20at%208.29.14%20PM.png)

This process will allow peer review on any incoming work, along with the ability to discuss specific lines on the same page.


Questions?
==========

Email: anthony@blar.do
