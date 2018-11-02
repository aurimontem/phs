Programming Help Sessions (PHS): Week 3
=======================================

Welcome back!

If you were here last week and you have already cloned the github repository,
you can update the phs directory with all of my new updates by navigating to
the `phs` directory (by **c**hanging **d**irectories with `cd phs`), and then
running `git pull`. This command 'pulls' any updated files from the github
repo into your own personal computer. Sometimes, `git` is worried about
overwriting changes you've made to files, and so you won't be able to `pull`
until you run `git reset --hard HEAD~`, after which you can run `git pull`.
This deletes any changes you've made to your `phs/` directory since the last
time you `git clone`d or `git pull`ed, after which point you are free to `pull`
the new version.

Customize your Linux environment
--------------------------------
This week we are going to learn how to "customize" your shell environment. The
way to do this in the shell is with `rc` files, such as a `.bashrc` or a
`.vimrc`. These are configuration files that customize a program-- in this case
, the files configure bash or vim respectively. However, `rc` files exist for
many programs (if you use matplotlib for plotting in python you can use a
`.matplotlibrc` to customize default fontsizes or colors, or Linux users have
an `.xinitrc` that configures their graphics). These files are called
"dotfiles", since they begin with a `.`. These files are "hidden files", which
means you need to use `ls -a` to see them (`-a` is the parameter for "all
files").

I think of `rc` files as an abbreviation for "runtime configuration" (even though this
is technically not what it stands for). The way a `.bashrc` file works, is that
when you open a bash shell, the commands in your `.bashrc` file are executed
immediately, line by line. How do you check that your shell (terminal) is
running bash? Check with:
```
    % echo $SHELL
    bash
    % echo $0
    bash
```
Here, `$SHELL` is a saved variable, that you can output. We will learn about
`$0` later this session. Other examples of saved variables that you can echo
are `$USER` (your username) and `$HOME` (your home directory). You can change
directories to your home directory with `cd $HOME` (check with `pwd`), or you
can use the shorthand `cd ~`. That's right-- `~` and `$HOME` store the same
value:
```
    % echo ~
    /home/eric
    % echo $HOME
    /home/eric
```

Anyways, we are getting off track. You are using a `bash` shell, so your
`.bashrc` file is executed line by line in bash every time you start up bash or
open a terminal. Let's test this. Move to your home directory with `cd ~`. Do
you have a `.bashrc` file already? If you `ls`, you will not see any dotfiles--
use `ls -a` or `ls -lah` instead. Do you see a `.bashrc` file? In either case,
let's open it in vim: `vim .bashrc`.

I'm going to add a few nonsense bash commands to demonstrate how the `.bashrc`
works. If you have a `.bashrc` file that contains text, leave the existing text
alone, but elsewhere add the lines (in vim use `hjkl` to move, `i` for insert
mode, and `Esc` to escape, and `:wq` to write and quit):
```
    echo "hey there"
    cd phs
    pwd
```

Now open and close your `bash` shell. What happened? To me, I see:
```
    hey there
    /home/eric/phs
    % 
```
When you opened bash, the `.bashrc` was automatically executed. Let's replace
its current contents with something useful. Delete the lines we just added in
vim with `Shift + v` to sweep out the selection, then `d` to delete. Instead,
assuming the line is not already present in your `.bashrc`, add the line
+ `alias ls='ls --color=auto'` if using Windows or Linux
+ `alias ls='ls -G'` if using Mac

Once you `:wq` in vim, now every time you open `bash`, the colors should
automatically look nice. This is a simple customization, but hopefully it gets
the message (and potential customizability) across.  I include an example
`.bashrc` file in this directory, which I called `my_bashrc`-- if we have time,
we will revisit this at the end of the session.

Creating simple bash scripts
----------------------------
Now move back to the `week_3` directory with `cd phs/week_3`.  We learned last
week how to make python scripts executable, with the sh-bang `#!/bin/env
python3`. We can make `bash` scripts executable, by making a file in vim and
adding the sh-bang `#!/bin/env bash`, and executing it. Let's make a file
`my_bash_script` in vim with `vim my_bash_script`, that contains
```bash
    #!/bin/env bash
    echo My name
    echo is
    echo INSERT YOUR NAME HERE
```
Then, exit insert mode with `Esc` and write and quit vim with `:wq`.  As
before, we need to make this file executable (`chmod`), and then execute it
(`./file_to_be_executed`). In the shell, run
```
    % chmod u+x my_bash_script
    % ./my_bash_script
    My name
    is
    Eric
```

Let's be a little more creative: edit this file again with `vim
my_bash_script`, but this time make it read:
```bash
    #!/bin/env bash
    echo This file has parameters 
    echo $0
    echo $1
    echo $2
```

We can run the file immediately (without `chmod`) since it already has
executable permissions. We find that by running it, it outputs:
```
    % ./my_bash_script
    This file has parameters
    ./my_bash_script


```
Interesting-- `$0` returns the name of the function that we are running. What
do `$1` and `$2` do? Let's try running the file again, but pass parameters:
```
    % ./my_bash_script physics rules
    This file has parameters
    ./my_bash_script
    physics
    rules
```
Therefore, `$1` and `$2` are parameters passed to the function `$0`. (For those
curious, google "positional parameters" to learn more). Earlier, when we ran
`echo $0`, the output was `bash`-- this is because in the shell, bash is the
name of the executed function.

Finally, we want to learn how to use this bash script from anywhere in our
filesystem. If we changed directories and wanted to run `my_bash_script`, we
would need to do something like `../../my_work/phs/week_3/my_bash_script
physics rules`. This is inconvenient-- when we run the command `vim`, or
`less`, or `head`, or `cat`, these functions all work without needing to
explicitly state where they are located. Hey-- where are they located? Use the
command `which` to figure it out:
```
    % which vim
    /usr/bin/vim
    % which cat
    /usr/bin/cat
    % which less
    /usr/bin/less
```

All of these files are stored in the `bin` directory, which is short for
"binary files". This directory `/usr/bin` is where all of the commands you use
in the shell are located (try out `ls /usr/bin` and scroll through the list).
Why is it that these programs can be executed from anywhere? The answer is in
the shell variable `$PATH`, which is a list of directories that your shell
searches through whenever you run a command. Look at what is in your path with
```
    % echo $PATH
    /usr/local/sbin:/usr/local/bin:/usr/bin
```
You'll notice that the place where `vim` and `cat` were located is one of the
directories in the `$PATH` variable.  In general people will have different
`$PATH` variables.  When you execute a program `foo` in the command line, the
shell will look through every directory in `$PATH` looking for an executable
program that is named `foo`, and once it finds one, it executes it. We want to
make a **personal** `bin` directory in our home directory, in which we can
place scripts that we have made. In my `bin` folder (located at `~/bin`, aka
`/home/eric/bin`), I have 17 scripts that my friends and I have made and shared
with each other.

To make a personal bin folder, we need to add it to the $PATH. Find where your
home directory is with `echo $HOME`-- I am assuming this returns
`/home/your_username`. Then, to add a new personal `bin` folder to your
`$PATH`, in bash run the command
```
    % PATH=$PATH:/home/your_username/bin
```
(for me I run `PATH=$PATH:/home/eric/bin`). If this `/home/your_username/bin`
is already in your `$PATH`, you don't need to do this.

By redefining the `$PATH` variable, we can now create a new `bin` folder in our
home directory, and move our script to that directory. First check if a `bin`
folder exists in the home directory with `ls ~`. If it does not, make it with
`mkdir ~/bin`. Then move our script to the new `bin` directory with `mv
my_bash_script ~/bin`. `ls .` to ensure it is gone, and `ls ~/bin` to ensure it
was moved.

Now, we can run the command `my_bash_script` even without the `./` part, just
like we would run `less` or `cat`! Try it out:
```
    % my_bash_script physics rules
    This file has parameters
    /home/eric/bin/my_bash_script
    physics
    rules
```

We have made a program that is executable from anywhere on our machine.
However, the crux was updating the `$PATH` variable. If we restarted bash,
`$PATH` would revert to its previous value. That means, every time we start
`bash`, we want the `$PATH` variable to update to include our personalized
`bin`. To do this, naturally, we will add to our `.bashrc`. We can do this
either with `vim ~/.bashrc`, and add the line
`PATH=$PATH:/home/your_username/bin`, or we can use the redirect command `>>`
and do it in one bash command
```
    % echo PATH=$PATH:/home/your_username/bin >> ~/.bashrc
```
which will append the command to the `.bashrc`. Now you can restart bash, and
still use your script `my_bash_script` anywhere you wish.

Compiling a simple skeleton document
------------------------------------
Next, we turn to the typesetting language LaTeX. LaTeX turns a plaintext .tex
document into a beautifully typeset and vector graphic .pdf document. (It can
also create .dvi and .ps documents, but in the modern era .pdf is all you will
need). In LaTeX, though, there is a learning curve-- unlike Microsoft Word,
where "what you see is what you get", you do not simply type on a screen and
print out the document.

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
  convenient graphic interfacing. If you have configured an X server (following
  the instructions under "Graphical Applications" at
  https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/),
  then you can launch the program VcXsrv, update the bash variable `$DISPLAY`
  with `export DISPLAY=localhost:0.0`, and run a graphical application. (You
  will need to run this `export` command every time you have a new bash
  session-- alternatively, add this line to your `.bashrc` with `echo "export
  DISPLAY=localhost:0.0" >> ~/.bashrc`.

+ Windows on Broida 5223 lab computers: Open the X server on the desktop of
  these computers, and accept the default settings (press Next) until you can't
  anymore. You should now be able top open graphical applications on these
  machines.

+ Windows, don't use graphics server method: If you don't configure an X
  server, you will need to navigate to your Linux files through your standard
  Windows file explorer. For details see
  [here](https://github.com/Microsoft/WSL/issues/2578). In your Windows file
  explorer, navigate to
  `C:\Users\%USERNAME%\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\`,
  but DO NOT modify any of the files. If you do, you may break the Windows
  Subsystem for Linux. Treat every file as 'read-only'. Once you are here,
  navigate to the `phs/week_3` folder, and double-click `skeleton_document.pdf`
  like you did in the old days. This incompatibility, which doesn't allow you
  to natively use graphics from the shell, is a surface defect of a deeper
  problem, is why I still urge you to dual-boot Ubuntu: you are not truly using
  Linux, and so there will always be things like this that break your user
  experience/immersion in Linux.


In an adjacent window now, in vim open `skeleton_document.tex` to see the basic
syntax, and to learn how to use the (very useful!) `f` key. We will flip
between `vim` and the `.pdf` to see what syntax produces what output.

You will notice that this generates a lot of extra files (`*.log`, `*.aux`)
that we don't need. We can remove these files with the script
`clean_up_files`-- look at its contents with vim, ensure it is executable with
`ls -lah`, and run it with `./clean_up_files`. Note what your workspace looks
like before and after. Let's add this script to our bin, so that we can use it
anywhere:
```
    % cp clean_up_files ~/bin
```

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

These scripts are useful in many different contexts. Therefore, we should make
them accessible from anywhere! To do this we will copy the `compile_article` to
our bin, where `clean_up_files` is already located:
```
    % cp compile_article ~/bin
```

Now, you can check to see that you can call these scripts from anywhere:
```
    % which clean_up_files
    /home/eric/bin/clean_up_files
    % which compile_article
    /home/eric/bin/compile_article
```

Isn't having a personal `bin` wonderful!?

Open both the `.tex` and the `.bib` file in vim, using `vim bibtex_file.tex`
and then `:tabe bibtex_file.bib` in vim. Switch between these two files with
`gt`, which stands for **g**oto **t**ab. Note the format of the `.bib` file.
This citation is typically available for any scientific journal, look for the
'download citation' link on the article website.


Make presentations in Beamer, and formal research reports in LaTeX
------------------------------------------------------------------
Beamer is an open-source presentation software, which allows for LaTeX to be
used as a presentation tool. An example presentation is `beamer_template.tex`,
which can be compiled by executing `compile_article` in the same manner as
above.

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


Customize your shell user experience with a `.bashrc`
-----------------------------------------------------
Files in your home directory that start with a `.` (they are 'hidden') and end
in `rc` are configuration files for given program. Today we will modify a
`.bashrc`, which gives options for bash (which is probably the shell you are
using). You can ensure this with `echo $0` (every line you enter into the shell
is literally passed to the `bash` function (or whatever this command returned),
and the shell organizes the input and output in a user-friendly command line).
Your `.bashrc` file is executed line by line in bash every time you start up
bash or open a terminal, which effectively personalizes your shell.

Ensure you are in the `week_2` directory with `pwd`. A sample bashrc is already
in this `week_2` directory as `my_bashrc`.  Investigate it with
`head`/`tail`/`cat`.  See if you have a `.bashrc` already located in your home
directory. Since it is a dotfile, you need to specify the `-a` (all) command to
ls: `ls -a ~`. Whether or not you already have one, open one in vim with `vim
~/.bashrc`. Once open in vim, open my sample file in the same vim screen with
`:vsplit my_bashrc`.

Now we will use `vim` to copy and paste select lines from one bashrc to the
other. You can tell which file is which on the bottom, where it will say
`my_bashrc` or `~/.bashrc`. Switch between the two sides of your screen with
`Ctrl-W Ctrl-W` in normal mode. Select some text in `my_bashrc` with visual
block mode `V`, then sweeping text with `j` or `k`, and they yanking (=copying)
with `y`. Change screens with `Ctrl-W Ctrl-W`, navigate to where you want it
with `j` and `k`, and paste it with `p` or `P`.

We will work through the lines in the bashrc together. Briefly, an `alias` is a
keybinding, so `alias v='vim'` means that anytime I type `v`, it literally gets
turned into the command `vim`. Think of these as 'keyboard shortcuts'.
Functions in bash execute a series of commands that act on the function
parameters. `$@` means 'all of the parameters you pass', `$1` means 'the first
parameter you pass', and so on. `PS1` is what your shell prompt says (for me it says
eric@eric-arch ~). If you wanted, you could put `echo "Hi there"` in your
`.bashrc`, and every time bash opened it would greet you with "Hi there".


If you want more examples of what experienced users put in their `.bashrc`, try
[this
thread](https://serverfault.com/questions/3743/what-useful-things-can-one-add-to-ones-bashrc)
for some ideas

Convert .ris bibliography citations into .bib citations
-------------------------------------------------------
Often, journals only have a `.ris` (RIS) type of citations (like
`pmcid-PMC5080291.ris` in this directory; `cat` this file to see what it looks
like compared to the `.bib` file). Using shell commands, we can convert these
RIS citations into BIB citations. We will need some commands in the `bibutils`
package. Download it with `sudo apt install bibutils` (Windows/Ubuntu)  or
`brew install bibutils` (Mac).

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



