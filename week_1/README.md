Programming Help Sessions: Week 1
=================================

Welcome to programming help sessions! The files in here were originally created
for the Colorado School of Mines ``Physics help sessions,'' a group founded by
my friends Everett Hildenbrandt, Alli Nilles, David Grisham, and myself (Eric
Jones). The primary joy and utility of open-source programming, though, is that
none of our names matter-- only the content does. So long as you act in this
open-source manner, you and anyone you know may use, modify, and distribute
this code.

If you are already at this point, you probably already have access to a command
line, also known as a *shell*:
- Windows 10: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows,
  then open the program Ubuntu
- Mac: Cmd + Spacebar, type Terminal
- Ubuntu: Ctrl + Alt + T

If you want to skip this introduction, feel free to reference this
[command line cheatsheet](shell_cheatsheet.md) instead.

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



