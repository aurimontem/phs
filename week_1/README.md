Programming Help Sessions: Week 1
=================================

Welcome to programming help sessions! The files in here were originally created
for the Colorado School of Mines ``Physics help sessions,'' a group founded by
my friends (Everett Hildenbrandt, Alli Nilles, and David Grisham) and me
(Eric Jones). The primary joy and utility of open-source programming,
though, is that none of our names matter-- only the content does. So long
as you act in this open-source manner, you and anyone you know may use,
modify, and distribute this code.

If you are already at this point, you probably already have access to a command
line, also known as a *shell*:
- Windows 10: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows,
  then open the program Ubuntu
- Mac: Cmd + Spacebar, type Terminal
- Ubuntu: Ctrl + Alt + T

If you want to skip this introduction, feel free to reference the command line
cheatsheet (cheatsheet.md) in the [shell](../shell) directory instead.

Basic shell commands + downloading PHS files with git
-----------------------------------------------------

With the command line installed, you looked to see what is in your current
directory by *listing* files in this directory by typing ```ls``` (then Enter).
Then, you looked to see where you were located in your file system by *printing
[your] working directory* with ```pwd```. It is common for shell commands to
be formatted as:

```
    % ls 
    my_python_file.py   my_file_1.txt   my_image_1.pdf  my_webpage_1.html
    % pwd
    /home/eric
```

We want to make a new directory that we will use for PHS. We will *make a
directory* called my_dir with ```mkdir my_dir```. Now, when we list the contents
of this directory, we see:
```
    % ls 
    my_dir  my_python_file.py   my_file_1.txt   my_image_1.pdf  my_webpage_1.html
```

Let's *change directories* to this new folder with ```cd my_dir```. Now, when
we look at where we are located we see:
```
    % pwd
    /home/eric/my_dir
```

If we wanted, we can go up a directory with ```cd ..```. then return back
to the my_dir directory again with ```cd my_dir```. Notice that you could have
also written ```cd my_d``` + Tab, and the rest of 'my_dir' will automatically
fill in! This is called tab-completion, and you should use it constantly.

```ls``` and ```cd``` are the bread-and-butter of navigating the command
line-- they are the equivalent of clicking on folders in a graphical file
directory.

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
Eventually, come back to the base phs folder with ```cd ~/phs```.

Reading from and manipulating files
-----------------------------------
With ```ls``` we can see the files in this home directory, but by adding *flags*
onto the  'ls' command, we can modify its behavior. For example, if we want to
list things in **l**ong form, **a**ll files including hidden files, and in a
**h**uman readable format, we can use ```ls -lah```:
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
tools: wait for future weeks to learn, or check out the command line cheatsheet
(cheatsheet.md) in the [shell](../shell) directory if you are impatient. 

Since everything is just a file or a directory, we will now learn how to
manipulate text using the text-editor ```vim```.

Text editing in ```vim```
-------------------------

