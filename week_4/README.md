Programming Help Sessions (PHS): Week 4
=======================================

Welcome back!

If you were here last week and you have already cloned the github repository,
you can update the phs directory with all of my new updates by navigating to
the `phs` directory (`cd phs`), and then running `git pull`.  If this doesn't
work, run `git reset --hard HEAD~`, after which you can run `git pull` (which
forces you to forget any changes you have made).  Now, if you list the files
(`ls`) in this directory you should see a new `week_4` folder. Move into this
directory.

Last time, we installed LaTeX. We need to install a few other packages for this
time, too. In a separate terminal, run the commands:

On Windows (in Windows Subsystem for Linux) or Ubuntu:
+ `sudo apt-get install texlive-latex-recommended texlive-latex-extra
  texlive-font-utils pandoc evince`

On Mac:
+ First install `homebrew`, a package manager for Mac OSX
  (details at `http://brew.sh`), with `/usr/bin/ruby -e "$(curl -fsSL
  https://raw.githubusercontent.com/Homebrew/install/master/install)"`
+ Install `mactex`, a package containing LaTeX and many of its commonly used
  modules, with `brew cask install mactex`
+ Install `pandoc` with `brew install pandoc`. 
+ Restart your terminal

Notice the new piece of software `pandoc`, which is capable of converting files
between various markup formats.  We will use it today to convert Markdown files
directly into PDF files.
Once this download is complete, ensure you have `latex` and `pdflatex`
installed with:
```
    % which latex
    /usr/bin/latex
    % which pdflatex
    /usr/bin/pdflatex
```

A sidenote for Mac users, and bash syntax for everyone:
-------------------------------------------------------
Last week, we learned how to modify our `.bashrc` file that configures our bash
experience. However, when opening Terminal in Mac OS, bash
looks for the file `.bash_profile` instead of `.bashrc` (as it does in
Linux/WSL).  Therefore, Mac users should ensure that their `.bash_profile` is
'linked' to their `.bashrc`, which is accomplished by opening your
`.bash_profile` in vim with `vim ~/.bash_profile`, and adding the following
lines of text (from
[Stack Exchange](https://apple.stackexchange.com/questions/51036/what-is-the-difference-between-bash-profile-and-bashrc)):
```
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

For those of you who are unfamiliar,
this type of logical structre is called an `if` statement.
 In the first line, the single brackets `[]` literally invoke the
`test` command (see `man test`), which returns `true` or `false` depending on the
expression. If the conditional `[ -f 
~/.bashrc ]` is determined to be true, then the contents of the `if` statement are
subsequently evaluated. 
   Here we are asking if a file exists (`-f`) called `~/.bashrc`.

The content of the `if` statement  executes the `.bashrc` file-- remember, it is just a bash
script, full of bash commands, and is therefore executable! The final line is
the bash syntax for ending an if statement (`fi` is if backwards). 
Whenever a login shell is entered (such as when Terminal is opened in Mac OS),
`.bash_profile` will be called, and the above code will call the text in
`.bashrc`. Therefore, you can now enter text into the `.bashrc` and it will
customize your bash session as you would expect.

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

A sample `.bashrc` with some useful commands can be found in this `week_4`
directory under the file name `my_bashrc`.
 Open up my example file `my_bashrc` in this directory with `vim
my_bashrc`. Once open, open your actual `.bashrc` file with `:vsplit ~/.bashrc`
in vim. Switch between the two sides of vim with `Ctrl+w Ctrl+w` or by using
`Ctrl-h` and `Ctrl-l`.
Yank entire lines with `yy`; or sweep out whole lines with `V`, then sweep with `jk`, then
yank with `y`. Then switch windows with `Ctrl+w Ctrl+w`, then paste with `p`.
Or, if you want, you can go into insert mode (`i`) and write the commands by
hand.

I recommend copying and pasting the first block of functions into your
`.bashrc` (lines 3 through 26). After you are done editing, write and quit all
files with `:wqa` in vim. To use the new `.bashrc`, either run `source
~/.bashrc`, or restart your terminal.

Let's take a closer look at one of these functions, `vv`. When you call it, it
makes a new variable called `temp` that is the output of a series of piped
commands. Piece by piece, `ls -tr` lists files in time-reversed order, so
that the most recently modified files are at the end. `*.+(tex|md|py)` only
lists the files that end in `.tex`, `.md`, or `.py` files (these are just suggestions
for type of text
files people generally work with-- you can change this as needed). We pipe this
output into tail, and take the final entry (i.e. the name of the file that was
more recently modified). We store this file as the variable `temp`, and then
state it in the terminal, and open it in vim. Try out the different pieces of
this command in the command line.

This function, `vv`, is the sort of time-saving macro or function you can
already write that can improve your efficiency.

To test this, make a new file with `echo SOME TEXT >> my_file.tex`, and run the
command `vv` in the command line.

I also include some other files in this `my_bashrc` that you can add. The `S`
and `s` are functions that allow you to 'bookmark' a directory and teleport
there. `vmd` will make a template file for markdown, which we will get to
later.


Scripts and LaTeX compilation revisited
---------------------------------------
Last time we used some script files, which we made executable from anywhere in
our computer. Let's review what we did last time, and you can check and ensure
that your machine is up to date:

+ We created a `bin` folder in our home directory, in which we placed
  executable scripts. Do you have this directory? Check with `ls ~/bin`-- if
  this gives an error, then you do not have it.
+ We added this bin to the `$PATH` bash local variable, but including a line in
  our `.bashrc` that says `PATH=$PATH:/home/dillon/bin`, where `/home/dillon` on
  your machine should be your home directory (check `echo $HOME` if you're not
  sure what that is)
  + Check that this worked by looking at your `$PATH` variable with the
    command `echo $PATH`. At the end of it, you should see `<other
    text>:/home/dillon/bin`.
  + Remind yourself that the `.bashrc` is the configuration file that is
    executed every time you open bash. Therefore, this reassignment of the
    `$PATH` variable occurs every time you open your computer.
+ We have some files in the `bin` from last week. They are included in this
  week's directory as well. Ensure they are in your path with `which
  compile_article` and `which clean_up_files`.
+ Lastly, we will be viewing graphics in this session, so if you are running
  Windows, start your X graphics server, and then restart your terminals:
  + If you followed the guide last week and installed an X server, launch the
    program VcXsrv (assuming you have the line `export DISPLAY=localhost:0.0`
    in your `.bashrc` already)
  + If you are on a lab computer, launch the program XLaunch and accept the
    default settings (press Next three times + Finish)

Now, recall that you can make a `.tex` file into a `.pdf` file by running the
command `pdflatex`. For example,
```
    % pdflatex skeleton_document.tex
```
This generated unnecessary output files (.aux, .log) that we can delete with
`clean_up_files`.

Some files are more complicated to compile (such as those that use bibTeX, a
way to easily store references and cite articles. You can compile **any** latex
file with the `compile_article` command, too:
```
    % compile_article skeleton_document.tex
```

Run `lt` to list your files in time-reversed order (the `.pdf` file should be
the newest file). Now you can open `lais_example.pdf` using your favorite pdf
viewer (`open` in Mac, `evince` or `mupdf` in Ubuntu or Windows (assuming your
X server is configured)).


LaTeX with BiBTeX
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

Open both the `.tex` and the `.bib` file in vim, using `vim bibtex_file.tex`
and then `:tabe bibtex_file.bib` in vim. Switch between these two files with
`gt`, which stands for **g**oto **t**ab. Note the format of the `.bib` file.
This citation is typically available for any scientific journal, look for the
'download citation' link on the article website.

Easy latex compilation with your `.vimrc`
-----------------------------------------
As we have seen, it is rather formulaic to compile and display latex files. But
it would be annoying if every time we made a modification to our latex file, we
had to exit vim, display the pdf, and enter vim again. We can make the
compilation and display of these files very streamlined by modifying your
`~/.vimrc`.

Just like your `.bashrc` file is run every time bash opens, your `.vimrc` file
runs every time vim opens. In vim you use commands all the time-- even `:wq` is
a command. Just like we coded useful macros into our `.bashrc` file to save
time, we can code useful macros into our `.vimrc` to save time. Open up the
`my_vimrc` file in the `week_4` directory with `vim my_vimrc`. As before, open
up your actual `.vimrc` file in the same window with `:vsplit ~/.vimrc`. Your
`.vimrc` may be empty, if you have never used it before. Switch windows with
`Ctrl+w Ctrl+w`.

I recommend copying and pasting the first 8 lines into your `.vimrc`. Do this
with block visual mode `V`, sweeping out the desired section (`j` and `k`),
yanking with `y`, changing windows with `Ctrl+w Ctrl+w`, and pasting with `p`.

Let's explore one of these commands:

```vim
autocmd BufRead,BufNewFile *.tex let @w=':wa:!compile_article %'
```

Notice that this looks different on the github than it does in vim. This is
because we are using a special character (in vim it looks like `^M` but
actually it is the literal Enter key, ``, which we can't see on github but
which we can see in vim. To make this character, press (in insert mode)
`Ctrl-V` followed by `Enter` (try it yourself!). `Ctrl-V` allows for any
non-standard key to be 'printed' in this way, including Backspace, Ctrl+keys,
and others.  This is why the above formatting of the README on github looks
kind of weird.

In this command, we are telling Vim to run the command in quotes (`:wa...%^M`)
every time we press the key `@` then `w` (not together). The command calls
`compile_article`, the script we currently placed in our `bin`, in order to
build a document. The `autocmd BufRead,BufNewFile *.tex` tells Vim to use this
definition for `@w` whenever a `.tex` file is opened.

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

Lines 7 and 8 of `my_vimrc` allow us top open the file through vim. In the same
way as before, it uses the editor `evince` to open the proper `pdf` file. In
Mac, you should replace `evince` by `open` (which is the default Mac graphics
viewer). For all users, fee free to replace this command with whichever PDF viewer
you prefer (`mupdf` for instance).

Again, the formatting is weird due to the special character `^M`-- view this
file in vim in order to copy and paste.  Here, we've simply added another macro
for Vim to use when we open `.tex` files.  This macro calls the command `evince
%:r.pdf &>/dev/null &`. The `%:r` will
be replaced with the filename minus the extension (`report.tex` -> `report`),
so that `%:r.pdf` will be replaced by the filename minus the initial extension
plus `.pdf` (`report.tex` -> `report.pdf`).  The `&>/dev/null` tells the shell
to throw away output (any minor errors that `evince` has, etc), and the final
`&` tells `evince` to run in the background, so that Vim will stay open and
visible.

Now compiling articles and viewing them are hotkeyed in vim as `@w` and `@o`.
Try it out by opening `skeleton_document.tex` in vim, and running `@w`, and
then `@o`.

BEWARE: If you have a compilation error, you won't return from vim until you
ignore it (press `X` three times-- you need to press it three times since we
are using pdflatex three times so that bibliographies are properly compiled).


Making LaTeX-quality documents simply with Markdown
---------------------------------------------------
One alternative to LaTeX is Markdown. Markdown is like fancy .txt-- it has
basic formatting. However, there is a powerful tool called `pandoc` that can
convert markdown into any other format: it can convert it into LaTeX, or html,
or Word, and it will still format the document nicely.

As an example, look at the text in `basic_markdown.md`. We will convert it into
a `.tex` document, and then into a `.pdf` like we did before. We will use
`pandoc`, which should be already installed. If it isn't, run:
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
command, and the commands are spun together in a script.

As before, we can
make a macro in `vim` to run this `build_pdf` program automatically. The
careful reader will know that we already did this, when we earlier altered our
`.vimrc`! All that is left to be done is to move this file to your
bin with `cp build_pdf ~/bin` (or wherever your bin
is).

Now open `basic_markdown.md` in vim, and try using `@w` to compile and `@o` to
open the pdf file. This is an easy way to turn standard text that even includes
LaTeX formatting into a nice output pdf, without the need to remember the
often-confusing LaTeX syntax.

Finally, open the file `beamer_in_markdown.md`. Compile it with `@w` and open
it with `@o`. This is a beamer (latex-style) file, useful for presentations,
made in markdown! This workflow makes it easy to produce high-quality slides for
presentations with only a few lines of text.

This workflow also makes markdown extremely useful
 for casual note taking. For example, You can annotate
papers that you read in a `papers.md` document with headers and bullet points.
Alternatively, you can 
make notes for skype meetings with a collaborator using `pandoc` to turn your
markdown into a beamer document (it turns different headings into new slides).
In fact, the document you are reading right now is actually a `README.md` file
created in markdown!


Some vim practice
-----------------
Let's get some practice modifying documents in vim. Open
`skeleton_document.tex` in vim, and scroll down to line 24. Autocompile it
regularly, open it as a pdf, and then every time you compile it refresh the pdf
to see how you changed it. This is how latex is meant to be done. Get practice
by doing the following tasks (autocompiling each time):

+ Modify some of the math on lines 16 and 18
+ Follow the instructions and fix the typos on lines 24-33
+ Add an item to the itemize environment (line 49-ish) with your favorite type
  of ice cream
+ Make a sub-sub-list by making a new enumerate environment within the existing
  ones on line 58
+ Break the Pythagorean theorem by adding an extra constant (line 65-ish)
+ Add a new row to the matrix (line 75-ish)

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

Other various shell utilities
-----------------------------
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



