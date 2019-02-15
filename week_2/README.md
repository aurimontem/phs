Programming Help Sessions (PHS): Week 2
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

Is the output of your ```ls``` command ugly? (Only black and white text that is
all the same font?) If running Mac: run the command ```alias ls='ls -G'```. If
not running Mac: run the command ```alias ls='ls --color=auto'``` to make your
```ls``` command more colorful/intuitive. Currently you will need to run this
command every time you open bash manually, but next week we will modify your
bash configuration settings in a file called ```.bashrc``` that will run this
command automatically every time you open bash.

Now, if you list the files (`ls`) in this directory you should see a new
`week_2` folder. Move into this directory.

Before we get too involved, let's take a moment to recap what we learned last
week. Move up to the parent directory and then into the `week_1` in one
command, with `cd ../week_1`. Be sure to tab complete! In the `week_1`
directory there are cheatsheets for the shell and for vim. Let's open and read
through the shell cheatsheet with `vim shell_cheatsheet.md`. Close the file in
vim with `:q` or `:q!`. Now open and read through the vim cheatsheet file. Now
move back to the week_2 directory with `cd ../week_2`.

A Side Project: Installing LaTeX
--------------------------------
LaTeX ("lay-tek" or "la-tek", not "lay-tex") is a typesetting program that
generates pretty files. Most physics textbooks and typed notes from your
classes, for example, will have been created in LaTeX. However, this program is
fairly hefty is size (.5 GB or so) and is typically not included by default.
We will not use it this week, but we will next week, and it takes a while to
install. So let's prepare, and install it now.

Open up a separate terminal and run the following commands:

On Windows or Ubuntu (in Windows Subsystem for Linux):
+ `sudo apt-get install texlive-latex-recommended`

On Mac:
+ First install `homebrew`, a package manager for Mac OSX
  (details at `http://brew.sh`), with `/usr/bin/ruby -e "$(curl -fsSL
  https://raw.githubusercontent.com/Homebrew/install/master/install)"`
+ Install `mactex`, a package containing LaTeX and many of its commonly used
  modules, with `brew cask install mactex`
+ Restart your terminal

Once these downloads are completed, ensure you have `latex` and `pdflatex`
installed with:
```
    % which latex
    /usr/bin/latex
    % which pdflatex
    /usr/bin/pdflatex
```


Rearranging files in the shell
------------------------------
Now that we are a little more familiar with the command line,
and also with using ```vim```, we can start to be a little more adventurous.
We're going to make a fake directory that holds our classwork with `mkdir classes`.
 Now move into this
directory, using tab complete. Let's make a new empty file for quantum with
`touch quantum` (check to see that it is empty using `cat`, `head`, `tail`, or
`ls -lah`). Print text in the shell using `echo` (try `echo "Hello, world"`).
Make a new file using this text with the redirection command `>`. Therefore, to
store some text about E&M we can use `echo "Maxwell's equations" > em`. To
append things to this file we use `>>`, while using `>`
overwrites. Therefore we can remind ourselves about more E&M things with `echo
"everything is a multipole expansion" >> em`. Lastly let's make a file in vim
for classical mechanics with `vim classical`, write your favorite equation in
insert mode (press `i` in regular mode), escape insert mode with Esc, and write
and quit (= save and close) the file with `:wq` in regular mode.
```bash
    % pwd
    /home/eric/phs/week_2/classes
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
all_my_classes class_notes_winter_2019`.

Let's say that you really didn't like quantum and didn't learn anything (hence
why it is empty!). To **r**e**m**ove the file, we use `rm quantum`. Ensure we
have removed it with `ls`. WARNING: This is not your childproofed delete from
Windows or Mac-- when you remove something, it is gone for good. There is no
recycle bin (unless you choose to make one). `rm` can be dangerous, especially
when combined with the wildcard (be very careful before running ```rm *``` !).

Suppose now that we want to due some file pruning to clean up for the new year
and to make our
classes directory relevant for this quarter. Let's make a separate directory in
the parent directory for classes from winter 2019:
```bash
    % mkdir ../winter_2019
    % ls ..
    classes     README.md   winter_2019
    % pwd
    /home/eric/phs/week_2/classes
```

Note that here we executed commands 'remotely' by using them with the
parent directory variable `..`. Now, we wish to move all of our files to this
`winter_2019` directory, which we can do with `mv * ../winter_2019`. Here the
wildcard selects all files, and moves them to our recently created directory.
Ensure this is the case with `ls` and `ls ../winter_2019`. Finally move to the
week_1 directory with `cd ..`. If you want, you can delete the two
directories you created with `rm -r winter_2019 classes`, but you can also keep
them if you want. Again, be careful! `rm -r` will delete without asking for
your approval, and there is no 'undo'.



Open source Othello
-------------------

Ensure you are in the `week_2` directory with `pwd`. Now we're going to examine
the contents of the file `othello.txt` with command-line tools. Spoiler alert
for anyone who hasn't read Othello... We will:
+ Estimate how many lines Othello has, and how many Lodovico has
+ Print out the first sentence of each of Othello's lines
+ See how many times Othello's name is called in the play

First, print out the file (using `cat` or `head`) to get an idea of the structure:

```bash
    % cat othello.txt
               Othello, the Moore of Venice
    [1]Shakespeare homepage | [2]Othello | Entire play
    #### Many more lines here ####
       LODOVICO

    [To IAGO] O Spartan dog,
    More fell than anguish, hunger, or the sea!
    Look on the tragic loading of this bed;
    This is thy work: the object poisons sight;
    Let it be hid. Gratiano, keep the house,
    And seize upon the fortunes of the Moor,
    For they succeed on you. To you, lord governor,
    Remains the censure of this hellish villain;
    The time, the place, the torture: O, enforce it!
    Myself will straight aboard: and to the state
    This heavy act with heavy heart relate.

    Exeunt
```
Now use `less` to view the document with `less othello.txt`. In `less` you can
navigate using the same key bindings as in vim, so 'j' and 'k' scroll up or
down, and 'f' and 'b' page through forwards and back.  Notice that everytime
Othello speaks, the document first prints OTHELLO. Based on this pattern, we
can find Othello's lines using `grep` (the syntax for grep is `grep [OPTIONS] PATTERN
FILE`, where [OPTIONS] are any additional flags you wish to specify that modify the default
output, PATTERN is what you are searching for, and FILE is the file you're
searching; for details check out `man grep`):

```bash
    % grep 'OTHELLO' othello.txt
    OTHELLO
    OTHELLO
    #### Many more lines here ####
    OTHELLO
```
To **c**ount the number of entries that grep found, we can use the '-c' option.
We apply this to count Othello's lines:

```bash
    % grep -c 'OTHELLO' othello.txt
    296
```
Another alternative is to PASS all of the lines of grep's output into another
command line program. This is called 'piping', and uses the character `|`. This
is similar to redirection (`<` or `<<`), but it pipes the output from one
program into the input of another. Here we use the '**w**ord **c**ount' program `wc`,
with the option `-l` which counts the number of lines. Notice that there are
usually many ways to solve a problem, and there are lots of powerful and small
command line programs that can be combined with pipes.
```bash
    % grep -c 'LODOVICO' othello.txt
    39
    % grep 'LODOVICO' othello.txt | wc -l
    39
```
Print out the first line of each of Othello's lines using the '-A' option
for `grep`. Unsure what `-A` does? Use `man grep`, then search (`/`) for -A with
    `/-A` + Enter. Use `q` to quit the man page. In this case, `grep -A 2
    'OTHELLO' othello.txt` will print the line containing 'OTHELLO' as well as
    the following two lines (`-A` for **A**fter).

```bash
    % grep -A 2 'OTHELLO' othello.txt
    OTHELLO
    #### Many more lines here ###
    OTHELLO

    O fool! fool! fool!
    --
    OTHELLO

    Soft you; a word or two before you go.
    --
    OTHELLO

    I kiss'd thee ere I kill'd thee: no way but this;
```

If we wanted to navigate this output in an easier way, we can pipe the output
of this command into `less` with `grep -A 2 'OTHELLO' othello.txt | less`, in
which you can use vim-style navigation key bindings.


Extracting useful content from a toy data file in the command line
--------------------------------------------------------------
Next we are going to extract information with the a toy data file containing random
data, `data_file.csv`. Using command line tools, we will:
+ Display the 'Reduced Chai Values' and 'Final Energy Values'
+ Show only the last two 'Reduced Chai Values'
+ Find out how many data lines are in the file
+ Find out how many data points are in the file

First get an idea of what the file looks like with `less`. Use the search
function of less (press '/' followed by your search string, for example
'Values') to probe the file's contents.  Use the 'n' key to jump to the next
match, 'N' to go to previous. Use the keys 'k' and 'j' to scroll.

```bash
    % less data_file.csv
    Reduced Chai Values:
    6575839, 7151022, 7334710, 4978808
    #### Many more lines ####
    Final Energy Values:
    3880766, 14001684, 13718481, 8132653
    #### Many more lines ####
```

Find the 'Reduced Chai Values' and 'Final Energy Values' by calling grep with
the '-A' option. Pipe the second into `less` to be able to scroll through and
search the output.

```bash
    % grep -A 1 'Reduced Chai Values' data_file.csv
    Reduced Chai Values:
    6575839, 7151022, 7334710, 4978808
    --
    #### More lines here ####
    Reduced Chai Values:
    9074041, 6222272, 14989142, 5701998

    % grep -A 1 'Final Energy Values' data_file.csv | less
    Final Energy Values:
    3880766, 14001684, 13718481, 8132653
    --
    #### More lines here ####
    --
    Final Energy Values:
    10340226, 8981179, 12774173, 8236417
lines 1-65
```

To show only the last two 'Reduced Chai Values', pipe the output of `grep` into
`tail`, and tell `tail` to only output the last 6 lines with the '-n' option.

```bash
  % grep -A 1 'Reduced Chai Values' data_file.csv | tail -n 6
    --
    Reduced Chai Values:
    1056171, 5042308, 4669985, 10144310
    --
    Reduced Chai Values:
    9074041, 6222272, 14989142, 5701998

```

Use the '-c' option for `grep` to count the data lines, coupled with the '-v'
option to invert the selection (only showing lines that DO NOT match the
search; in the following case we show any line not containing a colon). As
before, you can also use the `wc` (word count) command to count the number of lines grep
outputs.

```bash
    % grep -c -v ':' data_file.csv
    5000
    % grep -v ':' data_file.csv | wc -l
    5000
```

To verify there are four data entries on each line, we will count the total
number of data points using the word (`-w`) option of `wc` instead of the line
(`-l`) option.
Again, we grep for all of the lines containing data with the '-v' option for
`grep`, and then pipe the output into `wc`.

```bash
    % grep -v ':' data_file.csv | wc -w
    20000
```
Therefore, since there are 5000 lines and 20000 'words', there are four data
entries per line (unless the file isn't uniform).

Parsing content from real supercomputer output
----------------------------------------------

Next we will perform similar exercises, but this time use the supercomputer
output file `dextran_qm_dft.out`. We will:
+ See the steps and energies for each relaxation of the dextran molecule
+ Save the energies for each relaxation step
+ Save the geometries along each relaxation step
+ Combine the energies and geometries into one file

Dextran is a complex branched polysaccharide derived from the condensation of
glucose.  It was originally discovered by Louis Pasteur as a microbial product
in wine.  The file output we are about to explore was produced by NWChem.
NWChem is an ab initio computational chemistry package designed to run on 
high performance parallel supercomputing clusters.  Alongside some other information,
this file contains a numerical estimate of the equilibrium geometry of the dextran molecule,
 calulated using *density functional theory (DFT)*.  DFT is a quantum mechanical
modelling method that allows for the computation of different properties of
many-electron systems by expressing the ground state of such a system as a unique 
functional of the electron density (a significant simplification!).  The theoretical
formalization of DFT was done in large part by Walter Kohn, here at UCSB, for which
he received the 1998 Nobel Prize in Chemistry!

As always, first get a feel for the file by displaying it with `less` (or
`vim`). Notice that NWChem outputs a ```@``` at the beginning of each line containing
energy information.  Knowing this, we can learn about the energies outputted by the
program by searching for `^@`. The `^` is a regular expression that
matches the beginning of a line, so this search only returns lines that begin
with a `@`. If we wanted to only search for `@`, we need to use `/\@`, where
the `\` is an escape character-- these are needed when the character we are
searching for has other uses in the program.  Also search for 'Geometry' to get
an idea of what those parts of the file look like.

```bash
    % less dextran_qm_dft.out
```

    Please copy the file /lrz/sys/applications/nwchem/6.3/impi/.nwchemrc to your
    home directory.
    This file is necessary for NWChem to find the standard libraries.
     argument  1 = optimize.nw
        #### More lines here ####

    Northwest Computational Chemistry Package (NWChem) 6.3
    ------------------------------------------------------


    Environmental Molecular Sciences Laboratory
    dextran_qm_dft.out lines 1-65/24471 0%

Now that we are familiar with the output format, let's use `grep` to grab only
the lines we need from the file. Once again, the '^' tells `grep` to only match
'@' symbols at the beginning of a line. Note that the syntax of regular
experessions (e.g. how we are using `^`) is preserved across programs. We can
save these energies and deltas by redirecting the stdout of grep to another
file, 'dextran_energies.out'.

```bash
    % grep '^@' dextran_qm_dft.out
```

    @ Step       Energy      Delta E   Gmax     Grms     Xrms     Xmax   Walltime
    @ ---- ---------------- -------- -------- -------- -------- -------- --------
    @    0    -686.92664205  0.0D+00  0.02562  0.00530  0.00000  0.00000    124.6
    @    1    -686.93572937 -9.1D-03  0.00495  0.00123  0.05800  0.21419    230.6
    @    2    -686.93688173 -1.2D-03  0.00371  0.00079  0.03159  0.12217    377.7
    @    3    -686.93728094 -4.0D-04  0.00183  0.00045  0.02043  0.06471    536.9
    @    4    -686.93765371 -3.7D-04  0.00231  0.00055  0.02664  0.09902    685.2
    @    5    -686.93795400 -3.0D-04  0.00218  0.00046  0.02601  0.08722    834.3
    @    6    -686.93815263 -2.0D-04  0.00214  0.00036  0.02147  0.06602    982.6
    @    7    -686.93820464 -5.2D-05  0.00078  0.00014  0.00714  0.01937   1114.2
    @    8    -686.93823383 -2.9D-05  0.00089  0.00015  0.00618  0.01997   1236.3
    @    9    -686.93825965 -2.6D-05  0.00063  0.00014  0.00684  0.02057   1365.8
    @   10    -686.93828289 -2.3D-05  0.00065  0.00012  0.00676  0.02784   1504.9
    @   11    -686.93829701 -1.4D-05  0.00049  0.00010  0.00514  0.02142   1618.2
    @   12    -686.93830468 -7.7D-06  0.00046  0.00008  0.00443  0.01556   1748.7
    @   13    -686.93830745 -2.8D-06  0.00013  0.00003  0.00102  0.00292   1827.3
    @   14    -686.93830891 -1.5D-06  0.00006  0.00001  0.00100  0.00300   1906.5
    @   15    -686.93830931 -4.1D-07  0.00005  0.00001  0.00041  0.00128   1978.5
    @   15    -686.93830931 -4.1D-07  0.00005  0.00001  0.00041  0.00128   1978.5

```bash
    % grep '^@' dextran_qm_dft.out > dextran_energies.out
    % cat dextran_energies.out
```

    @ Step       Energy      Delta E   Gmax     Grms     Xrms     Xmax   Walltime
    @ ---- ---------------- -------- -------- -------- -------- -------- --------
    @    0    -686.92664205  0.0D+00  0.02562  0.00530  0.00000  0.00000    124.6
    @    1    -686.93572937 -9.1D-03  0.00495  0.00123  0.05800  0.21419    230.6
    @    2    -686.93688173 -1.2D-03  0.00371  0.00079  0.03159  0.12217    377.7
    @    3    -686.93728094 -4.0D-04  0.00183  0.00045  0.02043  0.06471    536.9
    @    4    -686.93765371 -3.7D-04  0.00231  0.00055  0.02664  0.09902    685.2
    @    5    -686.93795400 -3.0D-04  0.00218  0.00046  0.02601  0.08722    834.3
    @    6    -686.93815263 -2.0D-04  0.00214  0.00036  0.02147  0.06602    982.6
    @    7    -686.93820464 -5.2D-05  0.00078  0.00014  0.00714  0.01937   1114.2
    @    8    -686.93823383 -2.9D-05  0.00089  0.00015  0.00618  0.01997   1236.3
    @    9    -686.93825965 -2.6D-05  0.00063  0.00014  0.00684  0.02057   1365.8
    @   10    -686.93828289 -2.3D-05  0.00065  0.00012  0.00676  0.02784   1504.9
    @   11    -686.93829701 -1.4D-05  0.00049  0.00010  0.00514  0.02142   1618.2
    @   12    -686.93830468 -7.7D-06  0.00046  0.00008  0.00443  0.01556   1748.7
    @   13    -686.93830745 -2.8D-06  0.00013  0.00003  0.00102  0.00292   1827.3
    @   14    -686.93830891 -1.5D-06  0.00006  0.00001  0.00100  0.00300   1906.5
    @   15    -686.93830931 -4.1D-07  0.00005  0.00001  0.00041  0.00128   1978.5
    @   15    -686.93830931 -4.1D-07  0.00005  0.00001  0.00041  0.00128   1978.5

Now we have the electronic energies at each relaxation step (as well as position
deltas between steps) saved to a file.

Now we need to get the geometry at each relaxation step. Here, we'll use the
`-A` option for `grep` to print out the lines following our matches. At first,
we may not know how many lines to print out, so we'll try something excessive,
perhaps 40? Then narrow it down (or expand it) to make sure you get all the
atoms. Counting lines by hand is silly so instead use the ```-n``` flag to have
```grep``` output the line number on which each search result is printed. 
Once we're satisfied that we're getting the results we want, we can
redirect the output to a file for saving.

```bash
    % grep -A 40 'Geometry "geometry"' dextran_qm_dft.out
```
```bash

24166:                         Geometry "geometry" -> "geometry"
24167-                         ---------------------------------
24168- 
24169- Output coordinates in angstroms (scale by  1.889725989 to convert to a.u.)
24170- 
24171-  No.       Tag          Charge          X              Y              Z
24172- ---- ---------------- ---------- -------------- -------------- --------------
24173-    1 C                    6.0000    -1.47281583     1.16321379     0.18283825
24174-    2 C                    6.0000    -0.08182585     1.70439523     0.50320778
24175-    3 C                    6.0000     0.97487226     0.87553614    -0.21761849

			### MORE LINES HERE ###

24192-   20 H                    1.0000    -0.60963072    -2.48793956     1.59468758
24193-   21 H                    1.0000    -1.82931112    -2.81641725     0.34650697
24194-   22 H                    1.0000     1.71835792    -2.27555426    -0.39890742
24195-   23 H                    1.0000     2.96714682     0.88238211    -0.22383765
24196-   24 H                    1.0000    -0.14249451    -3.77623236    -0.91338242
24197- 
24198-      Atomic Mass 
24199-      ----------- 
24200- 
24201-      C                 12.000000
24202-      O                 15.994910
24203-      H                  1.007825
24204- 
24205-
24206- Effective nuclear repulsion energy (a.u.)     827.3774954752
```

Looks like we overshot by 10 lines

```bash
    % grep -A 30 'Geometry "geometry"' dextran_qm_dft.out
```

                                 Geometry "geometry" -> ""
                                 -------------------------

     Output coordinates in angstroms (scale by  1.889725989 to convert to a.u.)

      No.       Tag          Charge          X              Y              Z
     ---- ---------------- ---------- -------------- -------------- --------------
        1 C                    6.0000    -1.46614374     1.14413858     0.20689570
        2 C                    6.0000    -0.06510930     1.71491488     0.52712986
        3 C                    6.0000     1.01933089     0.89126609    -0.19986268

			### MORE LINES HERE ###

       20 H                    1.0000    -0.60963072    -2.48793956     1.59468758
       21 H                    1.0000    -1.82931112    -2.81641725     0.34650697
       22 H                    1.0000     1.71835792    -2.27555426    -0.39890742
       23 H                    1.0000     2.96714682     0.88238211    -0.22383765
       24 H                    1.0000    -0.14249451    -3.77623236    -0.91338242

```bash
    % grep -A 30 'Geometry "geometry"' dextran_qm_dft.out > dextran_geometries.out
```

Finally, let's combine our energies and geometries files into one total file with by
redirecting the output of `cat` into a new file `dextran_full_output`:

```
    % cat dextran_energies.out dextran_geometries.out > dextran_full_output
```

If we wanted to, we could define
a bash script which runs all these commands on the file automatically, but we
will save this for another time. If you're curious, check out the relevant
sections of `index.md` in `phs/shell/exercise_1`.

Manipulating multiple files with globbing
-----------------------------------------

Next we will practice using the wildcard operator `*` to select and move
consistently named files. We will be using the the files in directory 'plots'.
We will:
+ Select only the 'CCFreq' and 'CCTime' plots
+ Select only the 'tmax-140' plots
+ Select only the 'CCFreq' and 'tmax-140' plots, then zip them up so that they
  can be easily emailed

First move into the plots directory. We will select all the 'CCFreq' files or
'CCTime' files using 'globbing', or 'wildcards'. A wildcard is a `*` on the
command line, which tells Bash to try to match anything there. Let's try it.
Examine the output of these commands:

```bash
    % ls CCFreq*
    % ls CCFreq_*
    % ls CCFreq_* CCTime_*
```

Now create a directory and copy the selected files into that directory:

```bash
    % mkdir final_plots
    % cp  CCFreq_* CCTime_* final_plots
    % ls final_plots/
```

    CCFreq_L-8_tmax-10_dt-0.1.png   CCFreq_L-8_tmax-30_dt-0.2.png
    CCTime_L-8_tmax-140_dt-0.5.png  CCFreq_L-8_tmax-10_dt-0.2.png
    CCFreq_L-8_tmax-50_dt-1.png     CCTime_L-8_tmax-140_dt-1.png
    CCFreq_L-8_tmax-120_dt-1.png    CCTime_L-8_tmax-10_dt-0.1.png
    CCTime_L-8_tmax-30_dt-0.2.png   CCFreq_L-8_tmax-140_dt-0.2.png
    CCTime_L-8_tmax-10_dt-0.2.png   CCTime_L-8_tmax-50_dt-1.png
    CCFreq_L-8_tmax-140_dt-0.5.png  CCTime_L-8_tmax-120_dt-1.png
    CCFreq_L-8_tmax-140_dt-1.png    CCTime_L-8_tmax-140_dt-0.2.png

Now, try selecting for only the 'tmax-140' plots, including all three of
'CCFreq', 'CCTime', and 'Board'

```bash
    % ls *_tmax-140_*
```

    Board_L-8_tmax-140_dt-0.2.png  CCFreq_L-8_tmax-140_dt-0.2.png
    CCTime_L-8_tmax-140_dt-0.2.png Board_L-8_tmax-140_dt-0.5.png
    CCFreq_L-8_tmax-140_dt-0.5.png CCTime_L-8_tmax-140_dt-0.5.png
    Board_L-8_tmax-140_dt-1.png    CCFreq_L-8_tmax-140_dt-1.png
    CCTime_L-8_tmax-140_dt-1.png

Now select all files that are both 'CCFreq' and also 'tmax-140' plots, copy
them into a new directory called 'presentation_plots', then zip it up using the
`zip` command so that you can email it. Make sure to pass the '-r' option
(recursive) to the `zip` command so that it zips the entire
'presentation_plots' directory.

```bash
    % mkdir presentation_plots
    % cp CCFreq_*_tmax-140* presentation_plots
    % zip -r presentation_plots.zip presentation_plots/
```

To examine this newly created zip file we can first learn its filetype with
`file`, and then **l**ist the file contents using `unzip`, which is the inverse
to `zip`. Then we will extract the files to a new folder (with the `-d` flag)
with `unzip`:
```
    % file presentation_plots.zip
    presentation_plots.zip: Zip archive data, at least v1.0 to extract
    % unzip -l presentation_plots.zip
    Archive:  presentation_plots.zip
      Length      Date    Time    Name
    ---------  ---------- -----   ----
            0  2018-05-13 21:54   presentation_plots/
        13434  2018-05-13 21:54   presentation_plots/CCFreq_L-8_tmax-140_dt-1.png
        21676  2018-05-13 21:54   presentation_plots/CCFreq_L-8_tmax-140_dt-0.2.png
        16966  2018-05-13 21:54   presentation_plots/CCFreq_L-8_tmax-140_dt-0.5.png
    ---------                     -------
        52076                     4 files
    % mkdir unzipped_folder
    % unzip presentation_plots.zip -d unzipped_folder
    Archive:  presentation_plots.zip
       creating: unzipped_folder/presentation_plots/
      inflating: unzipped_folder/presentation_plots/CCFreq_L-8_tmax-140_dt-1.png
      inflating: unzipped_folder/presentation_plots/CCFreq_L-8_tmax-140_dt-0.2.png
      inflating: unzipped_folder/presentation_plots/CCFreq_L-8_tmax-140_dt-0.5.png

```

Another common (though oddly confusing to use) file compression tool is `tar`.
Here the syntax is `tar -cvf MY_TARFILE.tar FILES_TO_COMPRESS` (`-c`=create a
tar archive, `-v`=verbose output, `-f`=use the files I am about to pass). To extract, use
`tar -xvf MY_TARFILE.tar` (`-x`=extract).

```
    % tar -cvf presentation_plots.tar presentation_plots/*
    presentation_plots/CCFreq_L-8_tmax-140_dt-0.2.png
    presentation_plots/CCFreq_L-8_tmax-140_dt-0.5.png
    presentation_plots/CCFreq_L-8_tmax-140_dt-1.png
    % file presentation_plots.tar
    presentation_plots.tar: POSIX tar archive (GNU)
    % file presentation_plots.zip
    presentation_plots.zip: Zip archive data, at least v1.0 to extract
    % tar -xvf presentation_plots.tar                     
    presentation_plots/CCFreq_L-8_tmax-140_dt-0.2.png
    presentation_plots/CCFreq_L-8_tmax-140_dt-0.5.png
    presentation_plots/CCFreq_L-8_tmax-140_dt-1.png
```

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

Running python files in the python interpreter
----------------------------------------------
Now we're going to learn how to use python, a syntactically-pleasing and
readable programming language. Open two command line windows and place one
above the other (splitscreen). In both windows, navigate to the
```~/phs/week_1``` directory. 

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

Creating python scripts in vim
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
