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
all the same font?) Fear not!  The hallmark of a Linux operating system is its customizability.
If running Mac: run the command ```alias ls='ls -G'```. If
not running Mac: run the command ```alias ls='ls --color=auto'``` to make your
```ls``` command more colorful/intuitive. Currently you will need to run this
command every time you open bash manually, but next week we will modify your
bash configuration settings in a file called ```.bashrc``` that will run this
command automatically every time you open bash.


Let's make a new directory to practice moving around in the file system. We
will **m**a**k**e a **dir**ectory called my_dir with ```mkdir my_dir```. Now,
when we list the contents of our current directory, we see something like:
```bash
    % ls 
    my_dir  my_python_file.py   my_file_1.txt   my_image_1.pdf  my_webpage_1.html
```
Let's **c**hange **d**irectories to this new folder with ```cd my_dir```. Now, when
we look at where we are located we see:
```bash
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
```bash
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
```bash
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
```bash
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
```bash
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
```bash
    % file README.md
    README.md: ASCII text
```

You should now feel comfortable navigating up and down directories (```cd```,
```ls```) as well as displaying the text in files (```cat```, ```head```,
```tail```). These tools are hardly scratching the surface of command line
tools: wait for future weeks to learn more advanced tools, or check out the
command line cheatsheet shell_cheatsheet.md in this directory if you are
impatient. Alternatively, read through Alex Dorsett's thorough shell guide
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
```bash
    % pwd
    /home/eric/phs/week_1
    % ls
    jabberwocky  my_script.py  README.md  shell_cheatsheet.md  vim_cheatsheet.md  vim_exercise_1.md
    % vim vim_exercise_1.md
```

(remember to tab complete after ```vim vim_e```) (as before, if you need to
install vim use ```sudo apt install vim``` command)

This vim exercise is self-contained, so work through the examples. vim has
different "modes": normal mode, insert mode, and visual mode. You start out in
normal mode (use 'h,j,k,l' to move), and you enter insert mode with 'i'. Escape
insert mode back into normal mode with 'Esc'. When in normal model, undo your
last command with 'u', and **w**rite and **q**uit (= save and close) the file
with ':wq'. I know reaching for the Esc key all the time is annoying-- in
future classes we will remap CapsLock to Esc, which is much better in my
opinion. See you after you've completed ```vim_exercise_1.md```!

