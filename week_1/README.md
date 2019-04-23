Programming Help Sessions (PHS): Week 1
=================================

Welcome to the programming help sessions! The files in here were originally
created for the Colorado School of Mines "Physics help sessions," a group
founded by Everett Hildenbrandt, Alli Nilles, David Grisham, and myself (Eric
Jones).  The primary joy and utility of open-source programming, though, is
that none of our names matter-- only the content does. So long as you act in
this open-source manner, you and anyone you know may use, modify, and
distribute this code.

To participate in the PHS, you will need to have access to a **shell**. The
shell is the program that takes commands from the user and feeds them to the
operating system, which then performs those commands. We will be using a
**command line** (also called a **terminal**) to interface with this shell. You
are probably used to using a graphical user interface or GUI (e.g. clicking and
dragging your mouse) to interact with your computer; in this course we will
instead use text commands that are entered in the terminal to interact with
your computer. I will use shell, terminal, and command line interchangably in
this course (though, strictly speaking, I should probably be more careful!).

So, first we need to ensure everyone has access to a shell.
In Linux and MacOS you will have a shell by default. Windows 10 users will need
to install one via the "Windows Subsystem for Linux" (WSL). To access a
terminal:
- Windows 10: install WSL by following
  https://docs.microsoft.com/en-us/windows/wsl/install-win10 or
  https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/,
  then open the program Ubuntu 
- Mac: Cmd + Spacebar, type Terminal
- Ubuntu: Ctrl + Alt + T

Once installed, let's open up a second shell and update everything:
- Windows 10: In the shell run `sudo apt update` (which updates the Ubuntu
  repositories all shell programs are stored in) and then `sudo apt upgrade`
  (which upgrades all of your out-of-date software), and wait for everything to
  download and install
- Mac: In the shell run `xcode-select --install` to download most of the
  command line utilities you will ever need. If you are running mac and want to
  download more command line programs, in your free time look up `homebrew`

If you want to skip this introduction, feel free to reference the command line
cheatsheet (shell_cheatsheet.md) in this directory instead.

Now that everything is installed, split-screen your computer so that the
terminal is on the left-hand side, and so that the Week 1 PHS guide is on the
right-hand side.


Basic shell commands
--------------------

With the command line installed, we can now start to work with the shell.  This
interface might seem intimidating, but in reality it's simply a different way
of performing the same interactions with your computer that are already second
nature to you in the GUI paradigm.

First, let's try to get our bearings.  You can look to see what is contained in
your current directory by **l**i**s**ting the files in this directory by typing
`ls` (then Enter). Does nothing show up? If so, that is because the directory
you are in is empty. Create an empty file called my_file by running the command `touch
my_file`, and then try to **l**i**s**t your files again with `ls`. Do you see
something now?

Then, look to see where you were located in your file
system by **p**rinting your **w**orking **d**irectory with ```pwd```. You can
think of `pwd` as your 'compass', since it will always tell you where you are
in your file system. The output of these commands should resemble the
following, where `%` indicates an input command, and lines without `%` indicate
the terminal's output:

```bash
    % ls 
    % touch my_file
    % ls
    my_file
    % pwd
    /home/eric
```

Let's make a new directory to practice moving around in the file system. We
will **m**a**k**e a **dir**ectory called my_dir with ```mkdir my_dir```. Now,
when we list the contents of our current directory, we see something like:
```bash
    % mkdir my_dir
    % ls 
    my_dir  my_file
```
Is the output of your ```ls``` command ugly? (Only black and white text that is
all the same font?) Fear not!  The hallmark of a Linux operating system is its
customizability.  If running Mac: run the command ```alias ls='ls -G'```. If
not running Mac: run the command ```alias ls='ls --color=auto'``` to make your
```ls``` command more colorful/intuitive. For now, you will need to run this
command every time you open bash manually, but next week we will modify your
bash configuration settings in a file called ```.bashrc``` that will run this
command automatically every time you open bash.

Let's **c**hange **d**irectories to this new folder with ```cd my_dir```. Now, when
we look at where we are located we see:
```bash
    % pwd
    /home/eric
    % cd my_dir
    % pwd
    /home/eric/my_dir
```

If we wanted, we can go up a directory with ```cd ..```. then return back
to the my_dir directory again with ```cd my_dir```. Notice that you could have
also written ```cd my_d``` + Tab, and the rest of 'my_dir' will automatically
fill in! This is called tab-completion, and you should abuse this feature.

Now let's **r**e**m**ove (= delete) this temporary **dir**ectory by navigating
to the parent directory of ``my_dir`` and then running ``rmdir my_dir``.

```bash
    % pwd
    /home/eric/my_dir
    % cd ..
    % pwd
    /home/eric
    % ls
    my_dir  my_file
    % rmdir my_dir
    % ls
    my_file

```

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
If you're not there already, navigate to the `phs` directory:
```bash
    % cd
    % pwd
    /home/eric
    % cd phs
    % pwd
    /home/eric/phs
```


With ```ls``` we can see the files in this home directory, but by adding *flags*
onto the  'ls' command, we can modify its behavior. For example, if we want to
list things in **l**ong form, **a**ll files including hidden files, and in a
**h**uman readable format, we can use ```ls -lah```: (use `man ls` to figure
out what `-l`, `-a`, and `-h` mean!)
```bash
    % pwd
    /home/eric/phs
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
    % pwd
    /home/eric/phs/week_1
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

Let's try to investigate the poem `jabberwocky`, which is in this directory
(check with `ls`), by using `head` and `tail`. We will also use the command
`less`, which allows us to scroll up and down with `j` and `k`, and quit with
`q`.

```bash
    % pwd
    /home/eric/phs/week_1
    % ls
    command_line_appendix.pdf  jabberwocky  README.md  shell_cheatsheet.md
    vim_cheatsheet.md  vim_exercise_1.md

    % head jabberwocky
    "Jabberwocky"

    'Twas brillig, and the slithy toves
    Did gyre and gimble in the wabe;
    All mimsy were the borogoves,
    And the mome raths outgrabe.

    "Beware the Jabberwock, my son!
    The jaws that bite, the claws that catch!
    Beware the Jubjub bird, and shun

    % tail jabberwocky

    "And hast thou slain the Jabberwock?
    Come to my arms, my beamish boy!
    O frabjous day! Callooh! Callay!"
    He chortled in his joy.

    'Twas brillig, and the slithy toves
    Did gyre and gimble in the wabe;
    All mimsy were the borogoves,
    And the mome raths outgrabe.

    % echo "use q to quit in the program 'less'"
    use q to quit in the program less
    % less jabberwocky
    


```

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

Extra credit reading about vim:
+ run the command `vimtutor` to learn more about vim
+ https://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim#answer-1220118

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

Rearranging files in the shell
------------------------------
If you're not there already, navigate to the `phs/week_1` directory:
```bash
    % cd
    % pwd
    /home/eric
    % cd phs/week_1
    % pwd
    /home/eric/phs/week_1
```

Now that we are a little more familiar with the command line, and also with
using ```vim```, we can start to be a little more adventurous.  We're going to
make a fake directory that holds our classwork with `mkdir classes`.  Now move
into this directory, using tab complete. Let's make a new empty file for
quantum with `touch quantum` (check to see that it is empty using `cat`,
`head`, `tail`, or `ls -lah`). Print text in the shell using `echo` (try `echo
"Hello, world"`).  Make a new file using this text with the redirection command
`>`. Therefore, to store some text about E&M we can use `echo "Maxwell's
equations" > em`. To append things to this file we use `>>`, while using `>`
overwrites. Therefore we can remind ourselves about more E&M things with `echo
"everything is a multipole expansion" >> em`. Lastly let's make a file in vim
for classical mechanics with `vim classical`, write your favorite equation in
insert mode (press `i` in regular mode), escape insert mode with Esc, and write
and quit (= save and close) the file with `:wq` in regular mode.

```bash
    % pwd
    /home/eric/phs/week_1/classes
    % touch quantum
    % echo "Maxwell's equations" > em
    % echo "everything is a multipole expansion" >> em
    % vim classical
    % ls
    classical   em  quantum
    % ls -lah
    total 36K
    drwxr-xr-x 2 eric users 4.0K May 10 15:30 .
    drwxr-xr-x 3 eric users 4.0K May 10 15:31 ..
    -rw-r--r-- 1 eric users    7 May 10 15:30 classical
    -rw-r--r-- 1 eric users   56 May 10 15:27 em
    -rw-r--r-- 1 eric users    0 May 10 15:20 quantum
```

What if we want to learn information from all of these files at once? We can
use the wildcard operator ```*```, which returns all matching entries. For example,
`ls *` will list all of the files, `ls e*` will only return entries that begin
with e (this will return em), and `ls *m` will only return entries that end
with m (this will return em and quantum). Try out these commands.

We can use this wildcard operator anywhere in the command line that would
typically except a filename. For example, to list all of the contents of all of
our files, we can use `cat *` (con**cat**enation). Even further, we can take
all of our class information and turn it into one big file by **redirecting**
the output of `cat *` to a new file with `>`:
```bash
    % cat * > all_my_classes
    % ls
    all_my_classes  classical  em  quantum
    % cat all_my_classes
    F = ma
    Maxwell's equations
    everything is a multipole expansion
```

Let's say that `classical` is a well-made file, and we want to use it as a
template for some other file. **C**o**p**y it to a new file with `cp classical
new_classical`. Let's additionally say that we want our ``all_my_classes`` file
to be more specific, so we can **m**o**v**e it to have a new name with `mv
all_my_classes class_notes_spring_2019`.

Let's say that you really didn't like quantum and didn't learn anything (hence
why it is empty!). To **r**e**m**ove the file, we use `rm quantum`. Ensure we
have removed it with `ls`. WARNING: This is not your childproofed delete from
Windows or Mac-- when you remove something, it is gone for good. There is no
recycle bin (unless you choose to make one). `rm` can be dangerous, especially
when combined with the wildcard (be very careful before running ```rm *``` !).

Suppose now that we want to due some file pruning to clean up for the new year
and to make our
classes directory relevant for this quarter. Let's make a separate directory in
the parent directory for classes from spring 2019:
```bash
    % mkdir ../spring_2019
    % ls ..
    classes     README.md   spring_2019
    % pwd
    /home/eric/phs/week_1/classes
```

Note that here we executed commands 'remotely' by using them with the
parent directory variable `..`. Now, we wish to move all of our files to this
`spring_2019` directory, which we can do with `mv * ../spring_2019`. Here the
wildcard selects all files, and moves them to our recently created directory.
Ensure this is the case with `ls` and `ls ../spring_2019`. Finally move to the
week_1 directory with `cd ..`. If you want, you can delete the two
directories you created with `rm -r spring_2019 classes`, but you can also keep
them if you want. Again, be careful! `rm -r` will delete without asking for
your approval, and there is no 'undo'.




