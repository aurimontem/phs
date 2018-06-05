Programming Help Sessions (PHS): Week 3
=======================================

Welcome back!

If you were here last week and you have already cloned the github repository,
you can update the phs directory with all of my new updates by navigating to
the `phs` directory (`cd phs`), and then running `git pull`. Now, if you list
the files (`ls`) in this directory you should see a new `week_3` folder. Move
into this directory.

Installing LaTeX
----------------
LaTeX ("lay-tek" or "la-tek", not "lay-tex") is a typesetting program that
generates pretty files. Most physics textbooks and typed notes from your
classes, for example, will have been created in LaTeX. However, this program is
fairly hefty is size (.5 GB or so) and is typically not included by default.
Let's install it.

On Windows or Ubuntu (in Windows Subsystem for Linux):
+ `sudo apt-get install texlive-latex-recommended`

On Mac:
+ First install `homebrew`, a package manager for Mac OSX
  (details at `http://brew.sh`), with `/usr/bin/ruby -e "$(curl -fsSL
  https://raw.githubusercontent.com/Homebrew/install/master/install)"`
+ Install `mactex`, a package containing LaTeX and many of its commonly used
  modules, with `brew cask install mactex`
+ Restart your terminal

Ensure you have `latex` and `pdflatex` installed with:
```
    % which latex
    /usr/bin/latex
    % which pdflatex
    /usr/bin/pdflatex
```

Compiling a simple skeleton document
------------------------------------
LaTeX turns a plaintext .tex document into a beautifully typeset and
vector graphic .pdf document. (It can also create .dvi and .ps documents, but in
the modern era .pdf is all you will need). In LaTeX, though, there is a learning
curve-- unlike Microsoft Word, where "what you see is what you get", you do not
simply type on a screen and print out the document.

Briefly look at the LaTeX syntax with `less skeleton_document.tex`. We will
compile this document into a pdf using `pdflatex MY_FILE.tex`:
```
    % pdflatex skeleton_document.tex
    This is pdfTeX, Version 3.14159265-2.6-1.40.18 (TeX Live 2017/Arch Linux) (preloaded format=pdflatex)
     restricted \write18 enabled.
    entering extended mode
    (./skeleton_document.tex
    LaTeX2e <2017-04-15>
    <--- MANY MORE LINES --->
    Output written on skeleton_document.pdf (1 page, 124382 bytes).
    Transcript written on skeleton_document.log.
```

If you `ls`, you should now see additional files, including
`skeleton_document.pdf`. Let's open this file with a pdf viewer:
+ Mac OSX: run `open skeleton_document.pdf`. `open` in Mac will automatically
  map to the proper program for whatever file type you are opening
+ Ubuntu: run `evince skeleton_document.pdf`, or some other pdf viewer (I use
  `mupdf skeleton_document`). If you want to make this feel more fluid, you can
  add the line `alias pdf='evince'` to your `.bashrc`, and then use the command
  `pdf skeleton_document.pdf`.
+ Windows: This is a little tricky. Windows Subsystem for Linux allows you to
  reproduce the command line aspects of Linux, but it doesn't allow for
  convenient graphic interfacing. Instead, you will need to navigate to your
  Linux files through your standard Windows file explorer. For details see
  [here](https://github.com/Microsoft/WSL/issues/2578). In your Windows file
  explorer, navigate to
  `C:\Users\%USERNAME%\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\`,
  but DO NOT modify any of the files. If you do, you may break the Windows
  Subsystem for Linux. Treat every file as 'read-only'. Once you are here,
  navigate to the `phs/week_3` folder, and double-click `skeleton_document.pdf`
  like you did in the old days. This incompatibility, which doesn't allow you
  to natively use graphics from the shell, is a surface
  defect of a deeper problem, is why I still urge you to dual-boot Ubuntu: you
  are not truly using Linux, and so there will always be things like this that
  break your user experience/immersion in Linux.


In an adjacent window now, in vim open `skeleton_document.tex` to see the basic
syntax, and to learn how to use the (very useful!) `f` key. We will flip
between `vim` and the `.pdf` to see what syntax produces what output.

You will notice that this generates a lot of extra files (`*.log`, `*.aux`)
that we don't need. We can remove these files with the script
`clean_up_files`-- look at its contents with vim, ensure it is executable with
`ls -lah`, and run it with `./clean_up_files`. Note what your workspace looks
like before and after.

LaTeX with BiBTeX + adding scripts to your `bin`
------------------------------------------------

LaTeX is widely used, and accordingly has extensive documentation for nearly
every need. In general, (as with most things) the fastest way to learn how to
use LaTeX is google: en.wikibooks.org/wiki/LaTeX/ is an excellent resource for
basic issues, and StackExchange typically has solutions to any more advanced or
specific questions.

Let's now look at a simple LaTeX report template that uses BibTeX, a
bibliography manager.  A simple report file is in `bibtex_file.tex`, which uses
the BibTex file `bibtex_file.bib`. Each of these files are comprised of text,
and are compiled with LaTeX. The commands necessary to compile this article are
in `compile_article`; you can either run this bash script (`./compile_article
bibtex_file.tex`) or you can type out each command in the bash script, replacing
the `$filename` by `bibtex_file`. The commands of this script are `pdflatex`--
which we used earlier-- and `bibtex`, which is a command used to get your
references right. When using `bibtex`, you need to compile the article multiple
times (as in the script) in order for the program to learn what references go
where correctly. Also, this script runs `clean_up_files` at the end, which
removes any unnecessary files that are made during the compilation process.

It would be nice to be able to call this script from anywhere, so we are going to
place it in our `bin`, which is where user-made scripts go. To do this, ensure
you have a `bin` in your home directory (if not, make one with `mkdir ~/bin`),
and run `cp clean_up_files ~/bin` and `cp compile_article ~/bin`. To tell your
computer to look in this directory when you run a command in the shell, we add
it to the `$PATH` variable. See what your PATH looks like with `echo $PATH`. If
it doesn't include the directory we just made (in `/home/your_username/bin`),
add it to the path with `PATH=$PATH:/home/your_username/bin`. We want this
`bin` to be accessible every time you are in the shell, so add the line
`PATH=$PATH:/home/your_username/bin` to your `.bashrc` if it wasn't in your
default path. Now you should be able to call the `clean_up_files` script and
`compile_article` script from anywhere. Make sure this worked with `which
clean_up_files` and `which compile_article`, which should return the location
of the function. Try it!

Open both the `.tex` and the `.bib` file in vim, using `vim bibtex_file.tex`
and then `:tabe bibtex_file.bib` in vim. Switch between these two files with
`gt`, which stands for **g**oto **t**ab. Note the format of the `.bib` file.
This citation is typically available for any scientific journal, look for the
'download citation' link on the article website. Often, though, these journals
only have a `.ris` (RIS) type of citations (like `pmcid-PMC5080291.ris` in this
directory; `cat` this file to see what it looks like compared to the `.bib`
file). Using shell commands, we can convert these RIS citations into BIB
citations. We will need some commands in the `bibutils` package. Download it
with `sudo apt install bibutils` (Windows/Ubuntu)  or `brew install bibutils`
(Mac).

Now we can take a RIS citation and convert it to `.xml`, then take the `.xml`
citation and convert it to `.bib`. To do this, run
```
    % cat pmcid-PMC5080291.ris | ris2xml | xml2bib
    @Article{Edwards2016,
    author="Edwards, Adrianne N.
    and Karim, Samiha T.
    and Pascual, Ricardo A.
    and Jowhar, Lina M.
    and Anderson, Sarah E.
    and McBride, Shonna M.",
    title="Chemical and Stress Resistances of Clostridium difficile Spores and Vegetative Cells",
    journal="Front Microbiol",
    year="2016",
    month="Oct",
    day="26",
    publisher="Frontiers Media S.A.",
    volume="7",
    pages="1698",
    <--- MANY MORE LINES --->
    url="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC5080291/"
    }
```
Now we can take this output and pipe it into your `.bib` entry, with `cat
pmcid-PMC5080291.ris | ris2xml | xml2bib >> bibtex_file.bib`. Make sure you use
the redirect `>>` instead of the overwrite `>`! Once you do this your `.bib`
file may have a weird \<feff\> character before your BiBTeX entry, but you can
delete it in the usual way in vim with `x`. I often delete the `abstract` field of the
BiBTeX entry with `dd`, but it is up to you. (An alternative to redirecting
this output is to copy it into the `bibtex_file.bib` file-- for me, I do this by
highlighting the text in the shell with a mouse, then middle-clicking in insert
mode in vim)

Now we have a new `.bib` entry, so let's use it. Write a line in the
`bibtex_file.tex` that includes the command `\cite{Edwards2016}`, then
recompile this file with `compile_article bibtex_file.tex`, and view the
resulting pdf to ensure your citation worked properly. With this method, you
will never need to make your own citations ever again for scientific articles!

I find myself converting citation styles quite often, since lots of medical
journals don't support `.bib` export. Therefore, I have a command `makebib`
defined in my `.bashrc`-- you can have it too! Add the following lines to your
`.bashrc`:
```
    # convert .ris to .bib
    function makebib() {
        cat $1 | ris2xml | xml2bib
    }
```
Then restart your shell, and test the output `makebib
pmcid-PMC5080291.ris`-- it should act the same as before, and if you desire,
you can redirect it to your bibtex file.

In this script, as in the `compile_article` command before, the `$1` is
whatever the first parameter you pass to your function is; `$2` is the second
variable; and `$@` is all of the variables you pass.


Humanities paper example + adding scripts to your `.vimrc`
----------------------------------------------------------

LaTeX is not only for scientific writing! `lais_example.tex` is an example of
how to format some common elements of papers for your liberal arts classes.
Using BibTex, as in the previous example, is useful for LAIS as well! You can
usually export citations in the correct format (as `.bib`) from most academic
journals, or otherwise export them as `.ris` and convert them to into `.bib`
style citations as we did earlier.  Open `lais_example.tex` in vim, explore it,
and compile it with `compile_article lais_example.tex`.


Wouldn't it be nice to be able to compile LaTeX documents without leaving vim?
We'll record a [Vim macro](vim.wikia.com/wiki/Macros) which does this
compilation for us. I like to use the macro `@w`, because to me this is like a
'deep' write - not only am I writing the document, I'm compiling it to produce
the output.

Place these lines in your `.vimrc`:

```vim
autocmd BufRead,BufNewFile *.tex let @w=':wa:!compile_article %'
```

To copy these lines, you should open `README.md` in vim and search for
`/autocmd`, and yank this line with visual block mode `Vy`. Open your `.vimrc`
in the same window with `:split ~/.vimrc`, navigate to where you want to paste
this line, and paste with `p` or `P`. You cannot just copy and paste these
lines from your internet browser, because we are using a special character (in
vim it looks like `^M` but actually it is the literal Enter key, ``, which we
can't see on github but which we can see in vim. To make this character, press
(in insert mode) `Ctrl-V` followed by `Enter` (try it yourself!). `Ctrl-V`
allows for any non-standard key to be 'printed' in this way, including
Backspace, Ctrl+keys, and others.  This is why the above formatting of the
README on github looks kind of weird.

In this command, we are telling Vim to run the command in quotes (`:wa...%^M`)
every time we press the key `@` then `w` (not together). The command calls
`compile_article`, the script we currently placed in our `bin`, in order to
build a document. The `autocmd BufRead,BufNewFile *.tex` tells Vim to use this
definition for `@w` whenever a `tex` file is opened.

Notice the `^M ` in the command string - that is not just a `Shift+6+M`, it's
actually a special character which means `newline` - get that character by
pressing `Ctrl+v` in insert mode, then pressing `Enter`. You can get similar
special characters which mean `Escape` or other special keys using the same
process.

This command will literally be fed into Vim character-by-character. When you
press `@w`, first a `:` will be passed to Vim, putting it in command mode, then
a `wa` will be fed to it, typing the command `wa` for you (and writing=saving
all of the files you have open). When it reaches the
`^M `, the `Enter` key is fed to Vim, running that command for you. So we are
writing out all open files with the first `:wa`.

The second bit of the command opens up command mode again, `:`, then uses the
`!` to tell Vim that the rest of the command is a shell command, not a Vim
command (try running `:!ls`, for example). The `%` will be replaced by the
filename of the document you are currently editing.

If you have some other command or script that you want to use from LaTeX, put
that in quotes after the exclamation point instead. For example, if you have a
script `my_script` that accepts the file you are currently editing (`%`) and does
some task, put `:wa:!my_script %`.

Wouldn't it be nice to open the resulting PDF from vim, too? This will not work
for Windows users, as your Linux subsystem is not compatible with running
graphics. This process is similar to compiling the document to PDF: we will
define some macro that does it for us. I use `@o`.

```vim
autocmd BufRead,BufNewFile *.tex let @o=':!EDITOR %:r.pdf &>/dev/null &'
```
You should replace the word EDITOR by the pdf viewer of your choice-- I like
`mupdf`, but `evince` is another good choice. For Mac, I would recommend
replacing it by `open`. For me, this command reads
```vim
autocmd BufRead,BufNewFile *.tex let @o=':!mupdf %:r.pdf &>/dev/null &'
```

Again, the formatting is weird due to the special character `^M`-- view this
file in vim in order to copy and paste.  Here, we've simply added another macro
for Vim to use when we open `.tex` files.  This macro calls the command `mupdf
%:r.pdf &>/dev/null &`. `mupdf` is a pdf viewer (you may have `okular` or
`evince` - check by running those commands in your terminal).  The `%:r` will
be replaced with the filename minus the extension (`report.tex` -> `report`),
so that `%:r.pdf` will be replaced by the filename minus the initial extension
plus `.pdf` (`report.tex` -> `report.pdf`).  The `&>/dev/null` tells the shell
to throw away output (any minor errors that `mupdf` has, etc), and the final
`&` tells `mupdf` to run in the background, so that Vim will stay open and
visible.


Make presentations in Beamer, and formal research reports in LaTeX
------------------------------------------------------------------
Beamer is an open-source presentation software, which allows for LaTeX to be
used as a presentation tool. An example presentation is `beamer_template.tex`,
which can be compiled by executing `compile_beamer` in the same manner as
above, or by running `@w` when you have `beamer_template.tex` open in vim.

Also in this document, you will see how to include graphics, how to draw in
LaTeX using tikz, how to include sets of equations, and how to cite references
without using BiBTeX.

To see an example research report (my final from Parallel Computing, where I
parallelized matrix multiplication), look in the `example_tex_report`
directory. Compile and view the document as usual.

Build a resume in LaTeX
-----------------------
Finally look at a sample LaTeX resume/CV `cv_simple.tex`. Compile this in the
usual way with `compile_article cv_simple.tex`, and take a look at how it
looks. This uses the `res.cls` document style, which basically modifies a bunch
of the default commands to make them look like a resume. Based on the pdf
output, it should be self-explanatory to modify the appropriate sections of
this CV with your own achievements, but hopefully this gives you a good
framework to start from!

In sum, you should have enough LaTeX resources that you can modify in order to
fit any of your needs: view the basic `.tex` file structure in
`skeleton_document.tex`, view a document with BiBTeX citations with
`bibtex_file.tex` and `bibtex_file.bib`, view a humanities-style document with
`writing_example.tex`, view a Beamer presentation with `beamer_template.tex`,
and view a fully fleshed out report that includes figures in the
`example_tex_report` directory.


More python syntax
------------------
Now for something entirely different. We are going to create an intuitive
programming workflow with python, vim, and the shell. Open the python
interpreter in your shell with `python`, and follow along by entering the
following python functions in the interpreter. If you would like, practice
stringing these functions together in a script (`vim my_script.py`), and then
run the script (`python my_script`, or make it executable with `#!/bin/python`
on the first line, `chmod u+x my_script.py`, and `./my_script`) to ensure it
outputs what you expect.

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
>>> print(len([1,2,3,4,5]))
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



