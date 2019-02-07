Programming Help Sessions (PHS): Week 1
=================================

Welcome to programming help sessions! The files in here were originally created
for the Colorado School of Mines "Physics help sessions," a group founded by
Everett Hildenbrandt, Alli Nilles, and David Grisham and, our own local Linux guru, 
Eric Jones. My name is Dillon Cislo - a Physics graduate and Linux user. The primary joy and utility of open-source programming,
though, is that none of our names matter-- only the content does. So long
as you act in this open-source manner, you and anyone you know may use,
modify, and distribute this code.

Generally speaking, the program that takes commands from the user and feeds them to the operating system, which then performs those commands, is called the **shell**.  Technically, it's possible to interact with the shell using a *graphical user interface (GUI)*.  Odds are this is the method you are currently familiar with.  However, as we'll soon discover, using such an interface with Linux negates much of the usefulness of using Linux at all!  In order to maximize your returns from this course, you will need to have access to a *command line interface (CLI)*, which allows you to talk to the shell via keyboard commands, as opposed to pointing and clicking.  In Linux and MacOS, the CLI is more commonly referred to as the *Terminal*.  Instructions for accessing the terminal are given below:
- Windows 10: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows,
  then open the program Ubuntu
- Mac: Cmd + Spacebar, type Terminal
- Ubuntu: Ctrl + Alt + T

Once installed, let's open up a second shell and update everything:
- Windows 10: In the shell run `sudo apt update` (which updates the
  Ubuntu repositories all shell programs are stored in) and then `sudo apt
  upgrade` (which upgrades all of your out-of-date software), and wait for
  everything to download and install
- Mac: In the shell run `xcode-select --install` to download most of the
  command line utilities you will ever need. If you are running mac and want to
  download more command line programs, in your free time look up `homebrew`

If you want to skip this introduction, feel free to reference the command line
cheatsheet (shell_cheatsheet.md) in this directory instead.

Basic shell commands
--------------------

With the command line installed, we can now start to work with the shell.  This interface might seem intimidating, but in reality it's simply a different way of performing the same interactions with your computer that are already second nature to you in the GUI paradigm.  First off, lets try to get our bearings.   You can look to see what is contained in your current directory
by **l**i**s**ting the files in this directory by typing ```ls``` (then Enter).
Then, look to see where you were located in your file system by **p**rinting
your **w**orking **d**irectory with ```pwd```. You can think of `pwd` as your
'compass', since it will always tell you where you are in your file system. In
this guide and elsewhere, shell commands will be formatted as:

```bash
    % ls 
    my_python_file.py   my_file_1.txt   my_image_1.pdf  my_webpage_1.html
    % pwd
    /home/eric
```
Is the output of your ```ls``` command ugly? (Only black and white text that is
all the same font?) If running Mac: run the command ```alias ls='ls -G'```. If
not running Mac: run the command ```alias ls='ls --color=auto'``` to make your
```ls``` command more colorful/intuitive. Currently you will need to run this
command every time you open bash manually, but next week we will modify your
bash configuration settings in a file called ```.bashrc``` that will run this
command automatically every time you open bash.


Let's make a new directory to practice moving around in the file system. We
will **m**a**k**e a **dir**ectory called my_dir with ```mkdir my_dir```. Now,
when we list the contents of our current directory, we see something like:
```
    % ls 
    my_dir  my_python_file.py   my_file_1.txt   my_image_1.pdf  my_webpage_1.html
```
Let's **c**hange **d**irectories to this new folder with ```cd my_dir```. Now, when
we look at where we are located we see:
```
    % pwd
    /home/eric/my_dir
```

If we wanted, we can go up a directory with ```cd ..```. then return back
to the my_dir directory again with ```cd my_dir```. Notice that you could have
also written ```cd my_d``` + Tab, and the rest of 'my_dir' will automatically
fill in! This is called tab-completion, and you should abuse this feature.

Now let's **r**e**m**ove (= delete) this temporary **dir**ectory by navigating
to the parent directory of ``my_dir`` and then running ``rmdir my_dir``.

```ls``` and ```cd``` are the bread-and-butter of navigating the command
line-- they are the equivalent of clicking on folders in a graphical file
directory.

Downloading PHS files with git
------------------------------
Now let's copy the entirety of the 'programming help sessions' files
onto your computer from github, using the command ```git```. First, check if
your computer has it installed by typing ```git``` (+ Enter) on the command
line. If it is not found, you need to install it. This is the second joy and
utility of Linux: super easy installation of programs. You will install
```git```  with your machine's package manager:
- Windows w/ Ubuntu: ```sudo apt install git``` (if this doesn't work you may need
  to first run ```sudo apt update``` then ```sudo apt upgrade```)
- Mac: ```xcode-select --install``` (this will install most of the command line
  tools you will ever need)
- Linux: ```sudo apt-get install git```

Notice the command ```sudo``` in these commands. ```sudo``` stands for
'superuser do', and it executes whatever command follows with root (basically
'admin') privileges. ```sudo``` is often needed for 'system level' commands
(installation of software, for example) but it is also powerful-- with it, you
can irreparably delete your entire operating system! Be careful.

Now we will change to our home directory with ```cd ~```-- here '~' represents
your home directory (to see what this is, try ```echo $HOME```. '$HOME' is a
stored variable that simply contains the path to your 'home' directory, and you
can modify it if you'd like. With git, we will download the files used by PHS
onto your computer with the command ```git clone``` + the github address:
```
    % cd ~
    % git clone https://github.com/erijones/phs.git
    Cloning into 'phs'...
    remote: Counting objects: 354, done.
    remote: Compressing objects: 100% (22/22), done.
    remote: Total 354 (delta 12), reused 29 (delta 9), pack-reused 317
    Receiving objects: 100% (354/354), 4.67 MiB | 2.63 MiB/s, done.
    Resolving deltas: 100% (135/135), done.
```

What is new? Check with ```ls```, and move into the new directory with ```cd
phs```. Explore the new folders here using ```cd```, ```ls```, and ```cd ..```.
Eventually, come back to the base phs folder with ```cd ~/phs```. Some command
lines have access to the `tree` command which is a neat way to visualize the
file structure; see if your system can do this with ``tree .``, once you are
located in the `phs` directory. (Here `.` means 'in my current directory'.
Therefore, `cd .` will leave you in the same directory)

What would you do if you didn't have these handy PHS guides to help you
program? The answer is the `man` pages. `man` is short for 'manual', and it
will tell you everything you need to know about a shell command. Try running
`man ls`. Use `j` and `k` to scroll up and down, and use `q` to quit. Notice
all the `-a`, `-A`, etc. type commands? These are called 'flags', and they
modify the base command. 

Reading from and manipulating files
-----------------------------------
With ```ls``` we can see the files in this home directory, but by adding *flags*
onto the  'ls' command, we can modify its behavior. For example, if we want to
list things in **l**ong form, **a**ll files including hidden files, and in a
**h**uman readable format, we can use ```ls -lah```: (use `man ls` to figure
out what `-l`, `-a`, and `-h` mean!)
```
    % ls
    latex  misc  python  README.md  shell  vim  week_1
    % ls -lah
    total 44K
    drwxr-xr-x  9 eric users 4.0K May  5 22:08 .
    drwxr-xr-x 24 eric users 4.0K May  5 22:08 ..
    drwxr-xr-x  8 eric users 4.0K May  5 22:08 .git
    -rw-r--r--  1 eric users   25 May  5 22:08 .gitignore
    drwxr-xr-x  2 eric users 4.0K May  5 22:08 latex
    drwxr-xr-x  2 eric users 4.0K May  5 22:08 misc
    drwxr-xr-x  6 eric users 4.0K May  5 22:08 python
    -rw-r--r--  1 eric users  749 May  5 22:08 README.md
    drwxr-xr-x  4 eric users 4.0K May  5 22:08 shell
    drwxr-xr-x  2 eric users 4.0K May  5 22:08 vim
    drwxr-xr-x  2 eric users 4.0K May  5 22:08 week_1
```

On the left side, you can see the *permissions* of various files (e.g.
drwxr-xr-x). Here, the leftmost 'd' means the file is a directory-- i.e. you
can ```cd``` into it. The other letters refer to **r**eading, **w**riting, and
e**x**ecuting permissions for different user groups (google 'user permissions
linux'). Also shown is the size of the file in bytes (K = 1024) and their last
date of modification (just now, when you ```git clone```d them).

You may notice that only two files are not directories: .gitignore and
README.md. We can output their contents to the screen with ```cat``` (for
con**cat**enate):
```
    % cat .gitignore
    *.html
    *.pyc
    *.pdf
    *.swp
    % cat README.md
    Programming Help Sessions
    =========================

    Here are some guides (and other useful things) for programming and Linux,
    << OTHER TEXT >>
    -   [Linux program configurations (dotfiles)](dotfiles/)
```

The careful reader will notice that the contents of README.md are precisely the
contents visible at ```github.com/erijones/phs```-- this is because the github
website exactly consists of the text in the README.md file. ```*.md``` is the
format for markdown files (google markdown), which are basically fancy .txt or
basic .tex files. Indeed, if you are reading this document on github, you can
see the exact same document in the ~/phs/week_1 directory. We will read the
first few lines of it with ```head```:
```
    % pwd
    /home/eric/phs
    % cd week_1
    % ls
    README.md  shell_cheatsheet.md  vim_cheatsheet.md
    % head README.md
    Programming Help Sessions: Week 1
    =================================

    Welcome to programming help sessions! The files in here were originally created
    for the Colorado School of Mines ``Physics help sessions,'' a group founded by
    my friends (Everett Hildenbrandt, Alli Nilles, and David Grisham) and me (Eric
    Jones). The primary joy and utility of open-source programming, though, is that
    none of our names matter-- only the content does. So long as you act in this
    open-source manner, you and anyone you know may use, modify, and distribute
    this code.
```

We could also use ```cat README.md``` but that would display some 300 lines of
text, which is a little too much. We can also use ```tail README.md``` to see
the last 10 lines of the document. To see the first 30 lines, for example, use
```head -n 30 README.md```.

The third joy and utility of the command line is that everything is either a
file or a directory. Therefore, for any item ```foo``` you can either ```cd
foo``` or ```cat foo```, and something will be displayed. (However, if you try
to ```cat``` a .jpg file, expect to get nonsense!) To determine what type of a
file something is, use the ```file``` command (this is especially useful when
figuring out how .tar and .zip files were compressed!):
```
    % file README.md
    README.md: ASCII text
```

You should now feel comfortable navigating up and down directories (```cd```,
```ls```) as well as displaying the text in files (```cat```, ```head```,
```tail```). These tools are hardly scratching the surface of command line
tools: wait for future weeks to learn more advanced tools, or check out the
command line cheatsheet shell_cheatsheet.md in this directory if you are
impatient. Alternatively, read through Alex Dorsett's thorough shell sguide
```command_line_appendix.pdf```.

Since everything is just a file or a directory, we will now learn how to
manipulate text using the text-editor ```vim```.

Text editing in ```vim```
-------------------------
```vim``` is not your standard text editor-- your mouse will not work! It is
entirely keyboard based. You may exclaim "this is terrible!" at first, but once
you overcome the barrier, you will be **significantly** faster at typing with
vim than with a point-and-click text editor (e.g. the built in python editor,
MATLAB, Microsoft Word). The main reason for this is that your mouse has two
buttons, while your keyboard has around 100 (vim is case sensitive). Further,
if you use ```vim```, it will become the ONLY text editor you will need-- it
can write your LaTeX code, your python, your C++, your Julia, and whatever
else. (A caveat: you don't *always* need to use vim. I use the built-in
text editors for Gmail and Mathematica and iPython, but I often find myself
wishing they had vim key bindings!). 

One "teaser" video that demonstrates how an experienced vim user works is:
https://www.youtube.com/watch?v=FcpQ7koECgk. Can you do these types of edits
as quickly in your GUI text editor?

Let's get started by by opening the file ```vim_exercise_1.md``` in vim:
```
    % pwd
    /home/eric/phs/week_1
    % ls
    jabberwocky  my_script.py  README.md  shell_cheatsheet.md  vim_cheatsheet.md  vim_exercise_1.md
    % vim vim_exercise_1.md
```

(remember to tab complete after ```vim vim_e```) (as before, if you need to
install vim use ```sudo apt install vim``` command)

This vim exercise is self-contained, so work through the examples. vim has
different "modes": normal model, insert mode, and visual mode. You start out in
normal mode (use 'h,j,k,l' to move), and you enter insert mode with 'i'. Escape
insert mode back into normal mode with 'Esc'. When in normal model, undo your
last command with 'u', and **w**rite and **q**uit (= save and close) the file
with ':wq'. I know reaching for the Esc key all the time is annoying-- in
future classes we will remap CapsLock to Esc, which is much better in my
opinion. See you after you've completed ```vim_exercise_1.md```!

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
