Programming Help Sessions (PHS): Week 5
=======================================

Welcome back!

If you were here last week and you have already cloned the github repository,
you can update the phs directory with all of my new updates by navigating to
the `phs` directory (`cd phs`), and then running `git pull`.  If this doesn't
work, run `git reset --hard HEAD~`, after which you can run `git pull` (which
forces you to forget any changes you have made).  Now, if you list the files
(`ls`) in this directory you should see a new `week_5` folder. Move into this
directory.

We will be viewing graphics in this session, so if you are running
  Windows, start your X graphics server, and then restart your terminals:
  + If you followed the guide last week and installed an X server, launch the
    program VcXsrv (assuming you have the line `export DISPLAY=localhost:0.0`
    in your `.bashrc` already)
  + If you are on a lab computer, launch the program XLaunch and accept the
    default settings (press Next three times + Finish)

Installing Python
-----------------
Today we are going to be learning some basics about Python - a ubiquitous and
syntactically pleasing programming language.  Of course, in order to use Python,
we first need to have it installed! You may already have it installed on your computer.
To check this run the command `python3 --version`.
If not, Python can be conveniently installed using the various package managers for your system:
+ Windows Subsystem for Linux/Linux:
```bash
sudo apt-get update
sudo apt-get install python3
```
+ MacOS:
```bash
brew install python3
```
The most crucial third-party Python package is `pip`, a tool for installing and managing other
Python packages, such as those found in the Python Package Index (PPI).
  A version was probably installed on your computer by default during the `python3` installation.
Check this by running the command `pip3 --version`.  If not try the commands
+ Windows Subsystem for Linux/Linux:
```bash
sudo apt-get -y install python3-pip
```
+ MacOS: 
```bash
brew install python3-pip
```

`pip` can now be used to easily mange powerful code packages. 
Let's see how this works.  Go ahead and enter the following command
```pip3 install numpy matplotlib``
NumPy is the most important package for scientific computing with Python.  Among other features,
it containts N-dimensional array objects, linear algebra tools, Fourier transforms etc.  Matplotlib is a plotting library that can produce publication quality figures in a variety of formats.


Convenient Shell Utilities
--------------------------
`ranger` is a vim-influenced file manager that makes it easier to interactively
navigate your file directory system from the terminal.  In fact, `ranger` is actually
a Python package and can therefore be installed using `pip`! To install 
the latest version of `ranger`, use the command:
```bash
python3 -m pip install ranger-fm
```
(This is simply another syntax for using `pip3`). Make sure the version of `ranger` installed
is v1.9.0 or later by using `ranger --version`. 
We can increase the functionality of the software by making a few simple modifications.
In particular, we can modify the configuration of ranger to allow us to preview PDF
files from the terminal. Run the command:
```bash
ranger --copy-config=all
```
to create/overwrite your configuration files for `ranger`. Use `vim` to open up the file
`~/.config/ranger/rc.conf`.  Find the line `set preview_images false` and change it to
`set preview_images true`. Now use `vim` to open up the file
`~/.config/ranger/scope.sh` and uncomment the following text
```bash
        # application/pdf)
        #     pdftoppm -f 1 -l 1 \
        #              -scale-to-x 1920 \
        #              -scale-to-y -1 \
        #              -singlefile \
        #              -jpeg -tiffcompression jpeg \
        #              -- "${FILE_PATH}" "${IMAGE_CACHE_PATH%.*}" \
        #         && exit 6 || exit 1;;
```

Open `ranger` from the command line. 
Use `hjkl` to move within and between directories. Use `Enter` to open
files (ranger will guess the default program), and use `q` to quit ranger.

Running Python Files in the Python Interpreter
----------------------------------------------
Open two command line windows and place one
above the other (splitscreen). In both windows, navigate to the
```~/phs/week_5``` directory. 

In one of the windows execute ```python3```, which will open up the python
interpreter-- this is a useful space in which to test basic syntax and how to
use functions, entering text one line at a time (like in the command line). We
can create python scripts in vim that run many lines at once.  In general, the
interpreter is good for testing out small snippets of code or ideas, while
scripts are good for larger more extensive programs that you will revisit and
modify. You should use python3 instead of python2 whenever possible, since it
is morally proper to use up-to-date software. (A large part of the following
text is taken from ```phs/python/intro/index.md```)

Once in the interpreter (```python3``` on the command line), you can use any
commands you would use in python:

```python
% python3
>>> print("Hello World!")
Hello World!
>>> 8*2
16
>>> 8**2
64
```
Exit the interpreter with ```Ctrl + d```, or with ```quit()```, or
with ```exit()```.  Other common python commands are listed at the end of this
guide--- on your own time, try out these commands in the python shell
(interpreter), and verify the outputs shown.

Creating Python Scripts in vim
------------------------------

A python script is a text file consisting of python commands on each line. When
the script is executed, each line of the script is sequentially executed in the
interpreter. Blank lines are ignored, and on any line the text that follows a
`#` is a comment and will be ignored.

Let's make our first python "Hello, world" script. To do this, open up a new
file with ```vim my_script.py```. You should now be looking at the vim editor
in all its glory. Let's quickly save and quit with ```:wq + Enter```, and
investigate our new file in the shell with ```ls -lah```:
```
    % ls -lah
    total 288K
    drwxr-xr-x  2 eric users 4.0K Oct 18 12:40 .
    drwxr-xr-x 10 eric users 4.0K Oct 18 12:02 ..
    -rw-r--r--  1 eric users 190K Oct 18 11:59 command_line_appendix.pdf
    -rw-r--r--  1 eric users  951 Oct 18 11:59 jabberwocky
    -rw-r--r--  1 eric users 1016 Oct 18 11:59 my_fancy_script.py
    -rw-r--r--  1 eric users    0 Oct 18 12:40 my_script.py
    -rw-r--r--  1 eric users  28K Oct 18 12:33 README.md
    -rw-r--r--  1 eric users 2.7K Oct 18 11:59 shell_cheatsheet.md
    -rw-r--r--  1 eric users 1.6K Oct 18 11:59 vim_cheatsheet.md
    -rw-r--r--  1 eric users 5.6K Oct 18 12:24 vim_exercise_1.md

```
Notice our new script ```my_script.py``` is present, with size 0. This makes
sense-- we didn't type anything! Open the script again with ```my_script.py```.
Go into insert mode (```i```), and type the lines:
```python
#!/usr/bin/env python3
# This comment is the second line of the file
print("Hello, world!")
```
Then escape from insert mode (```Esc```) and write and quit (```:wq```). You
should now be at the shell once again. In the first line in the file, we placed the 'sh-bang'
`#!/usr/bin/env  python3`. This tells the shell to execute the file using
python3, and the ```/usr/bin/env``` is a program that knows and tells bash where
python3 is located on your computer. 

You would like to execute this file, but it is currently just a text file:
```
    % ls -lah my_script.py
    -rw-r--r-- 1 eric users 46 Oct 18 12:44 my_script.py
```

To make this file executable, you need to **ch**ange the **mod**ifications and
take the **u**ser class and add (**+**) e**x**ecute permissions, with `chmod
u+x my_script.py`. Now, the file has execute permissions:
```
    % chmod u+x my_script.py
    % ls -lah my_script.py
    -rwxr--r-- 1 eric users 46 Oct 18 12:44 my_script.py
```
Notice the '-' is now an 'x'. Execute this file with `./my_script.py`: 
```
    % ./my_script.py
    Hello, world!
```

(As a caveat, you could have originally executed the file without changing the
file permissions with `python3 my_script.py`, but making files you want to
execute executable with `chmod` is the proper way to do things in the command
line)

Executing premade python files
------------------------------

Now let's read through the fancier python file `my_fancy_script.py` in vim.
Part A demonstrates a simple for loop, using the `range` command which
effectively constructs a list of numbers that you can iterate through. Part B
uses a for loop to perform the derivative of some (time, position) coordinates.
Part C constructs and calls a simple function that adds numbers within a
certain range. Part D is optional, and integrates a function for those in
Physics 134 that needed to know this (see below for more details).

If you try to execute it right now, it won't work:
```
    % ./my_fancy_script.py
    bash: ./my_fancy_script.py: Permission denied
```

This is because you don't have the right permissions! Allow **u**sers to
e**x**ecute with ```chmod```:
```
    % ls -lah my_fancy_script.py
    -rw-r--r-- 1 eric users 837 Oct 18 13:58 my_fancy_script.py
    % chmod u+x my_fancy_script.py
    -rwxr--r-- 1 eric users 837 Oct 18 13:58 my_fancy_script.py
    % ./my_fancy_script.py
    PART A
    <<< ETC. >>>
```
[ An aside:

If you want to run part D: change ```run_part_d = False``` to ```run_part_d =
True``` and try running it. You may need to install the python packages
```numpy``` (for numerical integration) and ```matplotlib``` (for plotting)
with ```pip3 install numpy``` and ```pip3 install matplotlib```). If you don't
have ```pip3```, you may need to install it with ```sudo apt install
python3-pip```. Then, the code in Part D solves the differential equation dx/dt
= 5*x - x^2 for time 0 to 10. Replace your dx/dt and your t_max in the
integrand function. Currently Part D saves a figure of x(t) to
```my_first_figure.pdf```. To view this pdf file:
+ In Windows, navigate to the file following
  https://www.howtogeek.com/261383/how-to-access-your-ubuntu-bash-files-in-windows-and-your-windows-system-drive-in-bash/
+ In Mac: run ```file my_first_figure.pdf``` and the default pdf viewer will
  open the file
+ In Linux: run ```evince my_first_figure.pdf``` (if you don't have evince
  installed, run ```sudo apt install evince```)

]

In general, the procedure for creating and running python files from the
command line is:
+ make your own python file `my_first_script.py` with `vim my_first_script.py`
  that includes the sh-bang ```#!/usr/bin/env python3```
+ make it executable with `chmod` and run it:
```bash
% chmod u+x my_first_script.py     # Do once to make executable
% ./my_first_script.py             # Can be run like this every time
```
+ or run your file with python
```bash
% python3 my_first_script.py
```
If you chose to make your script executable by running `chmod u+x my_first_script.py` and called it
using the `./` syntax, the 'sh-bang' described above is **required**.

Food for thought: What was the difference between running our short "Hello,
world!" program in the interpreter versus running it in a script? In what
instances are scripts useful, and when is the interpreter useful?

Python Commands
---------------

### Assignment and Arithmetic

Assignment uses the `=` operator. The standard arithmetic operators are
supported (`+`, `*`, `-`, `/`) on number types.

```python
>>> a = 5
>>> print(a)
5
>>> a = 15 + 30
>>> print(a)
45
>>> b = 22
>>> print(a, b)
45 22
>>> print(a*b + (b-a))
967
>>> b = a / b
>>> print(b)
2.0454545454545
>>> b = a / b
>>> print(b)
22.0
```

What if we want to perform a `sqrt` or `sin`? We have to import a module which
has that function defined - the `math` module. Modules consist of prebuilt
commands that are constructed and peer-reviewed by a few open-source
contributors. Once you learn to use these modules (especially `numpy`, `scipy`,
`itertools`, and `matplotlib`), your code can worry more about implementing
ideas rather than the implementation itself.


```python
>>> import math             # Somewhere before we use `math`
>>> print(math.sqrt(4))
2.0
>>> print(math.sqrt(15))
3.872983346207417
>>> print(math.sin(math.pi / 2))
1.0
```
We often use exponentials, or other complex math functions, when trying to solve
problems with programming. Find e^10, where e is the base of the natural log.
Then, take log(16), then (log(16) base 2). What function do you use, and how do
you call it?  Google will have all the answers.  (google "python exponential",
for example)

Eventually, you can also write your own modules that contain your own specific
functions for your own specific task-- to do this, you can create a python file
called `my_module.py`, and then import it in a python script with `import
my_module`.


### Lists

In python, lists are one of the fundamental datatypes. Even strings (`'apple'`)
are stored as lists of single characters (`['a', 'p', 'p', 'l', 'e']`) in
python.  To construct a list, we can define it manually using `[element1, ...,
elementn]` syntax. The elements can be of any type, and of heterogeneous types.

```python
>>> test_list = [1,2,3,4,5]
>>> print(test_list)
[1, 2, 3, 4, 5]
>>> names = ["Bob", "Rob", "Robert", "Bobert"]
>>> print(names)
['Bob', 'Rob', 'Robert', 'Bobert']
>>> things = ["Car", 4, 2.23, "Denver"]
>>> print(things)
['Car', 4, 2.23, 'Denver']
```

You can access a specific element of a list using the `my_list[index]` syntax.
The `index`'th element of the list `my_list` will be returned (the first element
is accessed with `index = 0`). A negative `index` will start from the back of
the list.

```python
>>> test_list = ["a", "b", "c", "d"]
>>> print(test_list[0])
a
>>> print(test_list[2])
c
>>> print(test_list[-1])
d
>>> print(test_list[-2])
c
```

### Operators and Functions

The `+` operator on two lists extends the first list with the second list.

```python
>>> list1 = [1,2,3]
>>> list2 = [4,5,6]
>>> print(list1, list2, list1 + list2)
[1, 2, 3] [4, 5, 6] [1, 2, 3, 4, 5, 6]
```

The `append` function on a list adds an element to the end of the list:

```python
>>> test_list = [1,2,3]
>>> print(test_list)
[1, 2, 3]
>>> test_list.append(4)
>>> print(test_list)
[1, 2, 3, 4]
```
The `len` function on a list tells you how long it is.

```python
>>> print(len ([1,2,3,4,5]))
5
```

In your shell, create some test lists and compare the behavior of `append` and
`extend`. What happens when you `append` lists to lists?


### Strings

Strings are a special case of a python `list` where the elements are `char`'s.
You can create a `string` in python using quotes (single or double). You can
concatenate strings using the `+` operator.

```python
>>> my_string = "hello"
>>> print(my_string)
hello
>>> string_two = " world"
>>> print(my_string + string_two)
hello world
>>> print(len (my_string))
5
```

In the python shell, create a test string. How would you access the first
letter of that string, with list syntax?

### List Slices

List slices can be used to select a certain subset of another list. They use the
`my_list[start:end:inc]` syntax. The new list starts at the `start` index, goes
until the `end` index (but does not include it), making jumps of `inc`. By
default, `start` is `0`, `end` is `len(my_list)`, and `inc` is `1`.

```python
>>> test_list = [1,2,23,2,38,48,54,90]
>>> print(test_list[3:5])
[2, 38]
>>> print(test_list[:7])       # Everything up to element 7
[1, 2, 23, 2, 38, 48, 54]
>>> print(test_list[2:7:2])    # Every second element from 2-7
[23, 38, 54]
>>> print(test_list[::-1])     # Reverse a list
[90, 54, 48, 38, 2, 23, 2, 1]
```

In the python shell, try the following:

- reverse elements 1 through 4 in a test list
- use list slices to extract the first 4 letters in a string

### Loops

To build lists and perform other calculations, we use loops. A python `for` loop
iterates through a `list` provided by the user. This `list` could be a range of
numbers, or lines in a file, or any list.

```python
>>> for x in [1,2,8,4,19]:
...     print(x, x+i)          # Notice extra space before print
...
1 2
2 4
hello hellohello
4 8
19 38
```
Notice in this example you are not printing the iterator (i=1,2,3), but rather
are printing the constituent elements of the list themselves.

Quite often we need to add up numbers in a loop. If we wanted to sum the numbers
from 3 to 5, we need to create a range. The `range(start,end,inc)` function will
produce all numbers up to, but not including, `end` and will increment by `inc`
(1 by default). Also note that we need to initialize the `tot` variable before
the loop. The `tot += elem` operation is shorthand for `tot = tot + elem`.

```python
>>> print(range(3,6))
range(3, 6)                     # Most useless output ever
>>> for i in range(3,6):
...     print(i)               # Don't forget extra space before print
...
3
4
5
>>> tot = 0                         # Let's calculate a total
>>> for elem in range(302,6000):
...     tot += elem
...
>>> print(tot)
17951549
```

Notice that the statements which are "inside" the loop must be indented. There
is no rule saying you have to use spaces or tabs, but you have to be
**consistent**. This enforces easier-to-read code.

### Building lists with append

This method is useful when you don't know how long your list will be, but you
think it will be short. The function `append` is not as efficient as some of the
later methods.

```python
>>> app_list = []
>>> data_to_app = [1,3,5,8,1000]
>>> for elem in data_to_app:
...     app_list.append(elem)
>>> print(app_list)
[1, 3, 5, 8, 1000]
```

In the shell, take the following list of lists and create one flattened list
using a for loop and the `+` operator:

```python
>>> to_flatten = [[1,2,3],["wat"],[0.2,1000]]
```

### Building a pre-allocated list

In this example, we allocate all the memory for the list ahead of time and
update values after. This is more efficient than appending to an existing list
every time (the lists memory only needs to be allocated once). This technique
is especially useful in conjunction with the `linspace` function of the `numpy`
module, and is the standard way to crunch large list calculations (solving
ODEs, analyzing large data sets, etc.).  The syntax `[0]*num` creates a list of
`0`'s that is `num` long.

```python
>>> xs = [1,3,5,10,15]
>>> vs = [0]*(len(xs)-1)            # Allocate memory for velocities
>>> dt = 1
>>> for t in range(len(vs)):
...     dx = xs[t+1] - xs[t]
...     vs[t] = dx/dt
...
>>> print(vs)
```

The loop above took a list of positions and, assuming constant time intervals,
created a list of velocities. On your own, take that list of velocities and make
a loop to calculate a list of accelerations, including allocating memory before
the loop. Your resulting list should be `[0.0, 3.0, 0.0]`.


### Building lists with list comprehensions

This is the most compact and "pythonic" way to build lists. It is also usually
the fastest. List comprehensions need to be used with an existing list to build
from, which can be a built-in like the `range(start, stop, inc)` function.

Here are some examples of list comprehensions. Notice that you can evaluate
general expressions (even calling functions) in the list comprehension.

```python
>>> simple_range = [x for x in range(5)]
>>> print(simple_range)
[0, 1, 2, 3, 4]
>>> squared = [i*i for i in simple_range]
>>> print(squared)
[0, 1, 4, 9, 16]
>>> import math
>>> sqrts = [math.sqrt(element) for element in range(12, 15)]
>>> print(sqrts)
[3.4641016151377544, 3.605551275463989, 3.7416573867739413]
```

We can also add conditional statements, for example to grab all multiples of
five. The `%` operator - called `modulus` - calculates the remainder after
division (eg. `5 % 3 == 2`, `17 % 7 == 3`, `10 % 2 == 0`). The `==` operator
calculates if the terms on either side are equal, and returns a boolean `True`
or `False`.

```python
>>> simple_range = [x for x in range(44) if x % 5 == 0]
>>> print(simple_range)
[0, 5, 10, 15, 20, 25, 30, 35, 40]
>>> squares_under_fifty = [n*n for n in range(51) if n*n <= 50]
>>> print(squares_under_fifty)
[0, 1, 4, 9, 16, 25, 36, 49]
```
We can do mathematical operations within the list comprehension. In the shell,
write your own list comprehension which returns the squares of all of the
integers from 10 to 20.

As a final example, let's write a quick `flatten` function which takes a list of
lists and creates a list with one less level of nesting:

```python
>>> list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
>>> flattened = [x for sublist in list_of_lists for x in sublist]
>>> print(flattened)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

This is some crazy syntax, so take a while to think about how this works. It
might help to see the equivalent `for` + `append` loop expression:

```python
>>> list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
>>> flattened = []
>>> for sublist in list_of_lists:   # Appears first in nested comprehension
...     for x in sublist:           # Appears second
...         flattened.append(x)
...
>>> print(flattened)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

List comprehensions are much faster than for loops + append, especially for
larger lists!


Computing Collatz sequences in python
-------------------------------------
There is a suspiciously simple conjecture in mathematics that has never been
proven, called the Collatz conjecture. Start
with a positive integer, and if it is even divide by two, and if it is odd
multiply by three and add 1. The conjecture states that no matter what number
you start with, you will end up with 1. (e.g.: 3 -> 10 -> 5 -> 16 -> 8 -> 4 ->
2 -> 1)

We are going to build these Collatz chains using python. Open a new python file
in vim with `vim my_collatz.py`, and in the first line enter the sh-bang
`#!/bin/python3`. In the first couple of lines, place a simple `print('hey
there')`. Open another shell and navigate to the same folder. Make the python
file executable with `chmod u+x my_collatz.py`, and execute it with
`./my_collatz`. Ensure that your shell prints the expected statement.

Make sure you have a good workflow here! I like to have two terminal windows
side by side, one in the shell ready to execute the python file (use the up
arrow to access the last command you used), and the other in vim editing the
python file.  Switch between these windows with Windows+Tab or Alt+Tab.

We will make the Collatz sequence together in class. One key aspect of python
is that you need your spacing to be correct. If you are indented where you
shouldn't be, or not indented where you should be, python will throw an error
(`IndentationError: unexpected indent`). When errors occur, read the error
message-- it even says what line the error occured on, and tells you the class
of what was wrong.

To make the Collatz sequence, we will use: function definitions (`def`),
`while` loops, list `append`ing, casting numbers as `int`s, `if` and `else`
statements, and eventually accept user input from the command line with
`sys.argv`. To see a completed version of this file, refer to
`my_collatz_solution.py`.

Simulating Random Walkers in 2D
-------------------------------

Documentation to come! Sorry for the delay!
You might need `sudo apt-get install python3-tk` for this one.

Using `ssh` (secure shell)
--------------------------
`ssh` is a protocol that allows you to securely login to a remote server. Once
logged in, you can use the remote server in the same way that you have been
using the shell in this course.  The security of ssh is ensured through
cryptography, which is an entire field of study.  The idea is to encrypt
the communication between you and the server, so that even if the communication
is intercepted, it will be entirely indecipherable.

It is common practice to use `ssh` to remotely access a different system. In
the old days, Windows users would use the program Putty in order to `ssh` into
Unix machines. I used to `ssh` into my college computers in order to have
access to pay-walled research articles, or to use proprietary software (e.g.
Mathematica) that I didn't have personal access to. My friend would `ssh` into
his parent's computers, which allowed him to keep them updated and in good
shape without being there in person.  Most commonly, I `ssh` into
supercomputers, which are much faster (typically they have many more CPU or GPU
cores) than my personal machine.

I can't share my login to supercomputers that I have access to (liability,
etc., etc.), and so we will be using a publicly available server at SDF
(sdf.org). We will use a free account I made earlier, with username `eric2` and
password `my_pass`. To login to the server, we use the command
```
    % ssh eric2@sdf.org
```
When prompted that "The authenticity of host 'sdf.org (205.166.94.16)' can't be
established", type `yes` and continue. Then enter in the password `my_pass`
when prompted, and press `Enter` a few times until you see the prompt
```
    sdf:/sdf/udd/e/eric2>
```
This is the same type of shell that we have been using all along! Try some
familiar commands:
```
    % ls
    .          ..         .history   .hushlogin .lesshst   .signature my_acct    my_file
    % cat my_file
    Hello
    hello there
    % pwd
    /sdf/udd/e/eric2
    % whoami
    eric2
```

However, if you try to use different commands (like `head` or `tail`), they
don't work. Even using `vim` doesn't work-- `vim` becomes `nano`, a different
(equally ubiquitous) text editor. Try making a file with `vim my_name` where
you replace my_name with your actual name. This will make the files unique--
since everyone is logged in as the same user, if people open the same file at
the same time, those files will be overwritten. In this text editor (which is
not vim), you use the arrow keys to move around, and enter text normally (i.e.
not like in vim). To save, use `Ctrl+O`, and to quit use `Ctrl+X`. In general,
the caret `^` means `Ctrl`.

Now let's explore the rest of this filesystem. With `ls -lah` we can see who
owns which files. We can also run this on the parent directory (`..`). A sample
of the output is:
```
    % pwd
    /sdf/udd/e/eric2
    % ls -lah
    total 35K
    drwx------     3 eric2  users  512B Nov 26 08:48 .
    drwxr-xr-x  1229 new    wheel   24K Nov 25 12:36 ..
    -rw-r--r--     1 eric2  users   10K Nov 26 09:01 .history
    -rw-------     1 eric2  users    8B Nov 22 23:14 .hushlogin
    -rw-------     1 eric2  users   44B Nov 26 08:14 .lesshst
    -rw-------     1 eric2  users   61B Nov 22 22:57 .signature
    drwxr-xr-x     2 eric2  users  512B Nov 22 22:58 my_acct
    -rw-r--r--     1 eric2  users   18B Nov 26 08:52 my_file
    % cd ..
    % pwd
    /sdf/udd/e
    % ls -lah
    <-- MANY OTHER DIRECTORIES -->
    drwx------     2 erezbeyi          new    512B Sep 13 18:51 erezbeyi
    drwx------     2 ergab             users  512B May 26  2010 ergab
    drwxr-xr-x     2 erhjzuztert       new    512B May 22  2018 erhjzuztert
    drwx------     2 eric13            users  512B Oct  1  2010 eric13
    drwx------     3 eric2             users  512B Nov 26 08:48 eric2
    drwx------     2 eric84            users  512B Aug 19  2010 eric84
    drwx------     2 erica.parker      users  512B Oct  8 15:41 erica.parker
    <-- MANY OTHER DIRECTORIES -->
```
Notice that our name and folder, `eric2`, is in this directory. We own this
folder, but other users have their own personal folders, too. However, we
aren't able to access most of these other people's folders:
```
    % cd eric84
    /usr/local/bin/psh[622]: cd: /sdf/udd/e/eric84 - Permission denied
```
This is because their permissions forbid others from reading their data.
However, some people have relaxed their permissions. `erhjzuztert`, for
example, has a folder that others (such as us) are able to read:
```
    drwxr-xr-x     2 erhjzuztert       new    512B May 22  2018 erhjzuztert
```
Let's check out their directory with `cd erhjzuztert`. Explore with `ls`. This
is a boring directory (only dotfiles), but you can read them with `cat` if you
wish. If you try to make a file (e.g. with `touch my_file`), you won't be able
to-- this is because you don't have 'write' permissions.

This is the extent to which we will explore this remote server. Exit with the
command `exit`, and press `Enter` and `Ctrl+C` a few times until you are back
to your normal shell.

Some practice with vim and LaTeX
--------------------------------
Let's get some practice modifying documents in vim. Open
`skeleton_document.tex` in vim, and scroll down to line 24. Autocompile it
regularly (use `@w` and `@o` in vim, like we defined last week in our
`.vimrc`), and each time you recompile the .tex file refresh the pdf to see how you
changed it. Perform the following tasks (autocompiling each time):

+ Modify some of the math on lines 16 and 18
+ Follow the instructions and fix the typos on lines 24-33
+ Add an item to the itemize environment (line 49-ish) with your favorite type
  of ice cream
+ Make a sub-sub-list by making a new enumerate environment within the existing
  ones on line 58
+ Break the Pythagorean theorem by adding an extra constant (line 65-ish)
+ Add a new row to the matrix (line 75-ish)

If you have already performed this practice, execute the program `vimtutor`
instead from the shell:
```
    % vimtutor
```
More vim practice
-----------------
Make your own CV! Open the file `cv_simple.tex` in vim, and find all of the
fake names (Ann Ersha) with `/Ann Ersha`, then `Enter`, and scroll between
instances with `n` (forwards) or `N` (backwards). For each one, replace the
name with your name. Compile and open the file.

Or: You can change all of the names at once using the regular expression:
```
    :%s/Ann Ersha/My Name Here/gc
```
This will look for every instance of Ann Ersha, and ask if you want to change
it-- type `y` for yes, or `n` for no. 

Then:
+ update your email
+ update your research experience (what labs have you been in)
+ update your affiliations

This is basically identical to my CV format (the format is given is `res.cls`),
and in my opinion looks very professional. People will be able to tell it is
made in latex, too, and they will be impressed!

Other useful shell programs
---------------------------
See what programs are running (task manager) with `top`. If you want it to be
fancy and have colorful graphics, use `htop` (install it if you need). See the
low-level hardware commands your system is running with `dmesg`. View the
background daemon commands your system is running with `journalctl`. Examine
your cpu with `lspcu`. See your filesystem with `lsblk` and `df`. See your
wireless/wired connection hardware profiles with `ip link`. Remember your
wireless name (mine is 'wlp4s0'). Use `iftop -i wlp4s0` (replace 'wlp4s0' with
your wireless device name) to see the internet traffic you are uploading and
downloading. Use `ps` to see currently running processes. Use `pkill
PROCESS_NAME` to force kill a given process (I sometimes need to use `pkill
chromium` when my internet bugs out).



