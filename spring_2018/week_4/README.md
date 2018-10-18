Programming Help Sessions (PHS): Week 4
=======================================

Welcome back!

If you were here last week and you have already cloned the github repository,
you can update the phs directory with all of my new updates by navigating to
the `phs` directory (`cd phs`), and then running `git pull`. Now, if you list
the files (`ls`) in this directory you should see a new `week_4` folder. Move
into this directory.

Last time, we installed LaTeX. If you were not here last week, install it using
the following commands:

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

A sidenote for Mac users, and bash syntax for everyone:
-------------------------------------------------------
In the past we have modified a `.bashrc` file that modifies our preferences
when we work in bash. However, when opening Terminal in Mac OS, bash looks for
the file `.bash_profile` instead of `.bashrc` (as it does in Linux/WSL).
Therefore, Mac users should ensure that their `.bash_profile` is 'linked' to
their `.bashrc`, which is accomplished by opening your `.bash_profile` in vim
with `vim ~/.bash_profile`, and adding the following lines of text (from
[Stack Exchange](https://apple.stackexchange.com/questions/51036/what-is-the-difference-between-bash-profile-and-bashrc)):
```
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

The first line is your standard if statement, where the conditional `[ -f ~f
~/.bashrc ]` is a little funky. The single brackets `[]` literally invoke the
`test` command (see `man test`), which returns True or False depending on the
expression. Here we are asking if a file exists (`-f`) called `~/.bashrc`.

The second line executes the `.bashrc` file-- remember, it is just a bash
script, full of bash commands, and is therefore executable! The third line is
the bash syntax for ending an if statement (`fi` is if backwards). In all,
whenever a login shell is entered (such as when Terminal is opened in Mac OS),
`.bash_profile` will be called, and the above code will call the text in
`.bashrc`. Therefore, you can now enter text into the `.bashrc` and it will
customize your bash session as you would expect.

Scripts and LaTeX compilation revisited
---------------------------------------
Last time we used some script files, but didn't go into the guts of how they
work. Let's explore these scripts in more detail today.

First recall that you can make a `.tex` file into a `.pdf` file by running the
command `pdflatex`. For example,
```
    % pdflatex lais_example.tex
```
Run `lt` to list your files in time-reversed order (which should be in your
`.bashrc` from Week 2) to see the output of the `pdflatex` command
```
    % lt
    < SOME OTHER FILES >
    -rw-r--r-- 1 eric users  70K Jun  4 00:00 lais_example.pdf
    -rw-r--r-- 1 eric users   75 Jun  4 00:00 lais_example.aux
    -rw-r--r-- 1 eric users 4.9K Jun  4 00:00 lais_example.log
```
Now you can open `lais_example.pdf` using your favorite pdf viewer (`open` in
Mac, `evince` or `mupdf` in Ubuntu, and the complicated way of viewing files
from your Windows side discussed in Week 3 in WSL). However, there are extra
files-- the `*.aux` and `*.log` files are generated in the pdf compilation
process. These can be cumbersome, so we remove them with a `clean_up_files`
command.  Ensure it is executable with `chmod u+x clean_up_files` and `ls
-lah`. Let's view its contents.
```
    % cat clean_up_files
    #!/usr/bin/bash
    rm *.blg *.bbl *.aux *.log *.nav *.out *.snm *.toc &> /dev/null
```
The first line is the 'shebang', which tells the Linux kernel which program to
use to interpret this file and where that program is located; in this case, it
is using bash, which is in `/usr/bin/bash`. Notice that if we were making a
`python` script, we would replace this with `#!/usr/bin/python` instead (since
we want the shell to use `python` to interpret the file). HOWEVER: This may be
different on your computer! To find where **your** bash command is located,
type
```
    % which bash
    /your/path/here/bash
```
And replace the shebang with `#!/your/path/here/bash`. If your bash path is
different then mine, then you will have to make this replacement for all of the
bash scripts I've provided you!  The second line is a bash command that is
executed every time you run the function `clean_up_files`; it is a simple `rm`
command that will remove all the files that have the extensions listed. The end
`&> /dev/null` takes the output generated by the file (errors that are created
when some extension filetypes don't exist) and throws it away.

Run the command with `./clean_up_files`. Here, `.` selects the current
directory (try `cd .`), and you are calling the function `clean_up_files`
located in the current directory.

Presumably, you will want to run this command from anywhere in your computer,
and not just when the script is in your same directory. To make it so you can
always reach this file, put it somewhere in your path. Your path is all of the
places your computer will look for commands to call, when you type in commands
in the shell. See the extent of your path with:
```
    % echo $PATH
    /home/eric/bin:/usr/local/sbin:/usr/local/bin:/usr/bin
```
For me, I could place my script in any of these directories, and then I will be
able to call the command from anywhere. Alternatively, I could make a new bin
in my home directory. Here I am going to call it `my_bin`, but you should
probably just call it `bin` if its not already there!
```
    % cd ~
    % mkdir my_bin
    % cd my_bin
    % pwd
    /home/eric/my_bin
```
and then add a line to my `.bashrc` stating that I want this new bin to be in
my path
```
    PATH=$PATH:/home/eric/my_bin
```
Here, `my_bin` will be automatically added to my path every time I open a bash
session. Restart your shell in order for this change to take effect.

Now you can use this command anywhere:
```
    % mkdir temp
    % cp lais_example.tex temp
    % cd temp
    % pdflatex lais_example.tex
    <-- COMPILING PDF -->
    % ls
    lais_example.aux  lais_example.pdf  lais_example.log  lais_example.tex
    % clean_up_files
    % ls
    lais_example.pdf  lais_example.tex
```

You may recall that compiling a LaTeX file that references an external
bibliography file, `*.bib`, requires some extra work. If you don't want to
worry about this work, then just use the script `compile_article`:
```
    % ./compile_article bibtex_file.tex
    <-- SOME TEXT -->
    ... Compiled LaTeX file w/ BiBTeX citations to bibtex_file.pdf
```
How does this script work?

Once again, the shebang states that this is a bash function. Modify it so that
it fits your `which bash` directory. The parameter you pass to the function is
saved as `$1`, and it is slightly modified to get the base file name and a
bibtex file name. `1%.*` is a regular expression that selects all of the
variable `$1` that is before a `.`. In bash, all variables begin with `$`:
```
    % myvar="test string"
    % echo myvar
    myvar
    % echo $myvar
    test string
```
Next, the script checks to see if the bibtex filename exists (`-e`), using the
test command. This is the same test command that was used earlier in the
`.bash_profile` stuff! It is checking if bibtex files exist. If they do, it
performs the four-step process to reference and cite the bibliography; if it
doesn't, it performs the one-step command `pdflatex $filename`.

At the end, the file runs `clean_up_files` and passes the output of this
command (any error messages or warnings) to the trash `/dev/null`. This
suppresses any output (normal output or error messages) in the command line,
which can be nice from a minimalist perspective, but can be bad if things break
and you don't know why (since all the error messages are being suppressed).
For example, notice the following:
```
    % echo 4
    4
    % echo 4 &> /dev/null
    % echo 5
    5
```

Presumably, you wish to be able to run this command from anywhere as well.
Therefore, put it in your bin as before; for me, I am using the
`/home/eric/bin` bin so I perform
```
    % cp compile_article /home/eric/bin
```
(and I can ensure this bin is in my path with `echo $PATH`). Once I open a new
terminal, I can check that my two scripts can be called from anywhere with the
`which` command:
```
    % which clean_up_files
    /home/eric/bin/clean_up_files
    % which compile_article
    /home/eric/bin/compile_article
```
This `which` command will always tell you where your executables are stored
(try `which bash` or `which vim` or `which firefox`). Typically 'official'
programs (installed by your package manager) go in `/usr/bin`, while scripts
and functions you make go in `/home/YOUR_NAME/bin`.

If you would like, you can now call these commands from anywhere-- including
from inside vim. If you want to do this, look at the week_3 README.md in vim,
search for the `autocmd` lines with `/autocmd` + Enter in vim, and copy the
relevant lines (with `yy`), open your .vimrc (`split ~/.vimrc`), change tabs
(`Ctrl+W Ctrl+W`), and paste (`p` or `P`) for each relevant line. Now compiling
articles and viewing them are hotkeyed as `@w` and `@o`, respectively.

Making LaTeX-quality documents simply with Markdown
---------------------------------------------------
One alternative to LaTeX is Markdown. Markdown is like fancy .txt-- it has
basic formatting. However, there is a powerful tool called `pandoc` that can
convert markdown into any other format: it can convert it into LaTeX, or html,
or Word, and it will still format the document nicely.

As an example, look at the text in `basic_markdown.md`. We will convert it into
a `.tex` document, and then into a `.pdf` like we did before. First we need to
download `pandoc`:
+ Ubuntu/Windows: `sudo apt install pandoc`
+ Mac: `brew install pandoc`

Now we will convert a standalone file (`-s`) from (`-f`) markdown to (`-t`)
latex to a particular output file (`-o`) with the command
```
    % pandoc -s -f markdown -t latex -o basic_markdown.tex basic_markdown.md
```
Now you have the converted LaTeX file basic_markdown.tex-- take a look at it
with `less` or `tail`, and you will see that markdown inserts a huge preamble,
but then cuts and pastes the markdown text between the `\begin{document}` and
`\end{document}` tags. Now we can convert this `.tex` file into a `.pdf` with
our earlier `compile_article` command:
```
    % compile_article basic_markdown.tex
```
Take a look at the output pdf.

Pandoc will also convert markdown files into, for example, word documents
(.docx). Try
the following:
```
    % pandoc -s -f markdown -t docx -o basic_markdown.docx basic_markdown.md
```
Now open `basic_markdown.docx` in Word or Libreoffice, and you will see that it
is your standard Word editor. Therefore, you can use `vim` to make a first
draft (create and edit text), and then convert it to Word and format it there
(or share it with your groupmates or advisor who may be LaTeX-illiterate). The
`-t` option has many formats-- even `.html`! Try
```
    % pandoc -s -f markdown -t html -o basic_markdown.html basic_markdown.md
```
and open the html file in your web browser with `chromium basic_markdown.html`
or `firefox basic_markdown.html` (as before, Windows users will need to
navigate to this file with Windows explorer).

Alternatively, we can compile our markdown file into a pdf in one step with the
`build_pdf` command:
```
    % ./build_pdf basic_markdown
```
Note here that we don't include the file extension for this program. Open
`build_pdf` in vim and look through its contents-- every line is just a bash
command, and the commands are spun together in a script.  As before, we can
make a macro in `vim` to run this `build_pdf` program automatically.  First
copy this program into your bin with `cp build_pdf ~/bin` (or wherever your bin
is). Then add the following lines into your `~/.vimrc`:
```
autocmd BufRead,BufNewFile *.md let @w=':wa:!build_pdf %:r'
autocmd BufRead,BufNewFile *.md let @o=':!mupdf %:r.pdf &> /dev/null &'
```
As before, copy and paste from the `vim` file rather from the website because
`^M` messes with the formatting. As before, `autocmd BufRead,BufNewFile *.md`
says to only use this macro if the file ends in `.md`, and the rest says to
write with `@w` or open in `mupdf` with `@o`; if you want, replace mupdf by the
pdf viewer of your choice.

Now open `basic_markdown.md` in vim, and try using `@w` to compile and `@o` to
open the pdf file. This is an easy way to turn standard text that even includes
LaTeX formatting into a nice output pdf, without the need to remember the
often-confusing LaTeX syntax.

I use markdown as my go-to for casual note taking. For example, I annotate
papers that I read in a `papers.md` document with headers and bullet points; I
make notes for skype meetings with a collaborator using `pandoc` to turn my
markdown into a beamer document (it turns different headings into new slides);
and right now I am writing a PHS `README.md` file in markdown.

How to read python code
-----------------------
Now we're going to change gears. We are going to read a python program that
solves the [Travelling Salesman
Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), which is a
path-finding algorithm that is 'NP-hard'. The idea is that you pass a set of
(x,y) points, which are the 'cities', and the algorithm tries to find the
shortest path that goes through every city. There are N! (N factorial) possible
paths, making searching through the entire space computationally difficult as N
gets high (even 8 or 9 cities becomes tough). My computer science friend
Everett (who contributed substantially to this github) made the file `tsp.py`,
which solves this problem. We are going to learn how to read another person's
(very well-written!) code.

We can call this program from the command line with no
arguments:
```
    % ./tsp.py
    num_cities solver mean_path_length soln_time
    1 ex 0.0 1.3709068298339844e-05
    1 gn 0.0 3.2949447631835935e-05
    1 gn|rr 0.0 3.77655029296875e-05
    2 ex 16132.644668497474 4.096031188964844e-05
    2 gn 16132.644668497474 3.9696693420410156e-05
    2 gn|rr 16132.644668497474 0.00011475086212158203
    3 ex 7495.262777507686 6.508827209472656e-05
    3 gn 7495.262777507686 5.121231079101563e-05
    3 gn|rr 7495.262777507686 0.00018041133880615235
    <-- MORE TEXT -->
    8 ex 22931.936861565802 0.1611496925354004
    8 gn 23941.350371085395 0.0001177072525024414
    8 gn|rr 23123.333516324063 0.0011884927749633788
    9 ex 25193.072798235462 1.511652660369873
    9 gn 31351.462117922387 0.00013170242309570312
    9 gn|rr 25810.48689333421 0.0014333009719848632
    5 gn 21076.07626519443 7.588863372802735e-05
    5 gn|rr 21076.07626519443 0.000551915168762207
    55 gn 69928.73564822332 0.001180124282836914
    55 gn|rr 67162.96990070955 0.05030813217163086
    105 gn 93065.38118132828 0.0032633304595947265
    105 gn|rr 91389.26112079193 0.18043625354766846
    155 gn 112451.85217660034 0.006205296516418457
    155 gn|rr 110414.06614910407 0.3990992546081543
```
This tells the program to run a set of N randomly-generated cities, where N is
given in the first column of the output. A set of solvers-- ex='exact',
gn='greedy', rr='relax random'-- are used to solve the set of cities. For a low
number of cities (num_cities = 3, for example) the exact solver (`ex`) and the
greedy solver (`gn`) agree; for higher numbers of cities (e.g. 8), the exact
solver finds a path-distance that is shorter than the greedy solver-- hence the
greedy solver does not find the optimal solution! Also plotted is the
soln_time, the time required to run each solver.

Alternatively, we can run the program on a sample input, such as in
`test_tsp_data`-- take a look at it with `cat test_tsp_data`. Run it with this
input file as a parameters:
```
    % ./tsp.py test_tsp_data
    num_cities solver mean_path_length soln_time
    51 gn 78052.83943359695 0.001081826686859131
    51 gc 81486.2765634988 0.0018710017204284668
    51 rr 72749.15233533758 0.04166923522949219
    51 rs 72749.15233533758 0.0372262978553772
    51 gn|rr 73700.41364973532 0.04255806922912598
```
Here the solver tried 5 different solvers, and we can see that `rr` and `rs`
did the best (but took the longest!).

With this input/output knowledge, the python program is still a fancy black
box. How do we decipher what is going on inside, so that we can
understand/modify/improve/extend it? Open the file in vim, and we will work
through deciphering what's going on inside.

Parallelizing code on the supercomputer
---------------------------------------
Let's pretend that you had access to a supercomputer cluster. If you had an
algorithm that was computationally intensive-- such as this one-- you may want
to run a set of simulations at once. For example, consider the 5 different input
files in `inputs`; (in theory) running these sequentially on your computer
could take a while, so instead we will run them on a fake supercomputer using
the supercomputer submission script `submit_template` (this is for SLURM
job-manager, but the moral contents of the file will be the same for any
supercomputer scheduler). Examine the contents of this file
```
    % cat submit_template
    #!/bin/bash

    #SBATCH -D /u/as/jp/ehildenb/tsp/job.%j.%N.out
    #SBATCH -D /u/as/jp/ehildenb/tsp/
    #SBATCH -J {JOB_NAME}
    #SBATCH --get-user-env
    #SBATCH --clusters=mpp1
    #SBATCH --ntasks=1
    #SBATCH --export=NONE
    #SBATCH --time=48:00:00

    /home/YOURNAME/phs/week_4/tsp.py {INPUT_FILE}
```
To make this file work, replace YOURNAME with your proper address (check `pwd`
in the directory that holds `tsp.py`). This has two 'placeholder' fields that
are INPUT_FILE and JOB_NAME that will be automatically replaced by their proper
contents with the `submit_multi` script-- check out the `sed` commands in
`submit_multi`:
```
    % cat submit_multi
    <-- MORE TEXT -->
     # Modify our submission file with the correct info
    sed -i 's/{JOB_NAME}/'"$input"'/' "$sub_file"
    sed -i 's!{INPUT_FILE}!'"$dir_name/$input"'!' "$sub_file"
    <-- MORE TEXT -->
```
These lines replace JOB_NAME by the variable `$input`, and replace INPUT_FILE
by one of the input files in the `inputs` directory. Once you modify
`submit_template` and ensure the path to `tsp.py` is correct, you can run the
`submit_multi` script with `./submit_multi`. In the resultant `tsp_*.in`
folders, there are output files `*.out` that will give the shortest paths for
each input file `*.in`. Therefore, you have successfully parallelized this
code! The only difference on a supercomputer is that instead of `bash
submission_script.sh`, you will run `sbatch submission_script.sh` which will
run the program on the supercomputer on some explicitly specified way
(described in the `submit_template`).

The end
-------
Thanks for attending! If there is any extra time, we can discuss any lingering
questions you might have.

I hope you learned a bit of Linux and are comfortable working in the command
line. I am planning on running these sessions again in the future-- would
any of you be interested in attending and working as a helper in the future?
What improvements would you like to see for the sessions? Are there topics you
would like for me to cover in more detail? What were the most useful, and least
useful things I did? Thanks for your time!

