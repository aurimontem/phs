Programming Help Sessions (PHS): Week 2
=======================================

Welcome back!

If you were here last week and you have already cloned the github repository,
you can update the phs directory with all of my new updates by navigating to
the `phs` directory (by **c**hanging **d**irectories with `cd phs`), and then
running `git pull`. This command 'pulls' any updated files from the github
repo into your own personal computer. Now, if you list the files (`ls`) in this
directory you should see a new `week_2` folder. Move into this directory.

Before we get too involved, let's take a moment to recap what we learned last
week. Move up to the parent directory and then into the `week_1` in one
command, with `cd ../week_1`. Be sure to tab complete! In the `week_1`
directory there are cheatsheets for the shell and for vim. Let's open and read
through the shell cheatsheet with `vim shell_cheatsheet.md`. Close the file in
vim with `:q` or `:q!`. Now open and read through the vim cheatsheet file. Now
move back to the week_2 directory with `cd ../week_2`.

Rearranging files in the shell
------------------------------
Now that we're in week_2 (check with `pwd`), we're going to make a fake
directory that holds our classwork with `mkdir classes`. Now move into this
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
```
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
use the wildcard operator `*`, which returns all matching entries. For example,
`ls *` will list all of the files, `ls e*` will only return entries that begin
with e (this will return em), and `ls *m` will only return entries that end
with m (this will return em and quantum). Try out these commands.

We can use this wildcard operator anywhere in the command line that would
typically except a filename. For example, to list all of the contents of all of
our files, we can use `cat *` (con**cat**enation). Even further, we can take
all of our class information and turn it into one big file by **redirecting**
the output of `cat *` to a new file with `>`:
```
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
all_my_classes class_notes_winter_2018`.

Let's say that you really didn't like quantum and didn't learn anything (hence
why it is empty!). To **r**e**m**ove the file, we use `rm quantum`. Ensure we
have removed it with `ls`. WARNING: This is not your childproofed delete from
Windows or Mac-- when you remove something, it is gone for good. There is no
recycle bin (unless you choose to make one). `rm` can be dangerous, especially
when combined with the wildcard (be very careful before running `rm *`!).

Now it is springtime, and we need to do some spring cleaning to make our
classes directory relevant for this quarter. Let's make a separate directory in
the parent directory for classes from winter 2018:
```
    % mkdir ../winter_2018
    % ls ..
    classes     README.md   winter_2018
    % pwd
    /home/eric/phs/week_2/classes
```

Note that here we executed commands that 'remotely' by using them with the
parent directory variable `..`. Now, we wish to move all of our files to this
`winter_2018` directory, which we can do with `mv * ../winter_2018`. Here the
wildcard selects all files, and moves them to our recently created directory.
Ensure this is the case with `ls` and `ls ../winter_2018`. Finally move to the
week_2 directory with `cd ..`. If you want, you can delete the two
directories you created with `rm -r winter_2018 classes`, but you can also keep
them if you want. Again, be careful! `rm -r` will delete without asking for
your approval, and there is no 'undo'.


Next we will work through more shell exercises that were originally located in
`phs/shell/exercise_1`.

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
can find Othello's lines using `grep` (the syntax for grep is `grep PATTERN
FILE`, where PATTERN is what you are searching for, and FILE is the file you're
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
program into the input of another. Here we use the 'word count' program `wc`,
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

If we wanted to navigate this in an easier way, we can pipe the output of this
command into `less` with `grep -A 2 'OTHELLO' othello.txt | less`, in which you
can use vim-style navigation key bindings.


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
    % grep -c -v ':' data_file.csv | wc -w
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

As always, first get a feel for the file by displaying it with `less` (or
`vim`). Knowing that NWChem outputs a `@` at the beginning of a line with
energy information on it, search for `^@`. The `^` is a regular expression that
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
'-A' option for `grep` to print out the lines following our matches. At first,
we may not know how many lines to print out, so we'll try something excessive,
perhaps 40? Then narrow it down (or expand it) to make sure you get all the
atoms. Once we're satisfied that we're getting the results we want, we can
redirect the output to a file for saving.

```bash
    % grep -A 40 'Geometry "geometry"' dextran_qm_dft.out
```

                                 Geometry "geometry" -> ""
                                 -------------------------

     Output coordinates in angstroms (scale by  1.889725989 to convert to a.u.)

      No.       Tag          Charge          X              Y              Z
     ---- ---------------- ---------- -------------- -------------- --------------
        1 C                    6.0000    -1.46614374     1.14413858     0.20689570
        2 C                    6.0000    -0.06510930     1.71491488     0.52712986
        3 C                    6.0000     1.01933089     0.89126609    -0.19986268
        #### More lines here ####
       20 H                    1.0000    -0.60963072    -2.48793956     1.59468758
       21 H                    1.0000    -1.82931112    -2.81641725     0.34650697
       22 H                    1.0000     1.71835792    -2.27555426    -0.39890742
       23 H                    1.0000     2.96714682     0.88238211    -0.22383765
       24 H                    1.0000    -0.14249451    -3.77623236    -0.91338242

          Atomic Mass
          -----------

          C                 12.000000
          O                 15.994910
          H                  1.007825


     Effective nuclear repulsion energy (a.u.)     827.3774954752

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
        #### More lines here ####
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
a bash function which runs all these commands on the file automatically, but we
will save this for another time. If you're curious, check out the relevant
sections of `index.md` in `phs/shell/exercise_1`. **HERE**

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
    % file presentation_plots.zipA
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

Customize your text editing user experience with a `.vimrc`
-----------------------------------------------------------
In the same way that we were able to modify our `bash` user experience with a
`.bashrc`, we can modify our `vim` experience with a `.vimrc`. It is also a
hidden file, stored in the home directory. At the start of every `vim` session,
every line in your `vimrc` is executed sequentially. As we did with the
`.bashrc`, open your `vimrc` in vim with `vim ~/.vimrc`, then open my sample
vimrc alongside with `vsplit my_vimrc`. Switch between sides with `Ctrl-W
Ctrl-W` or with `Ctrl-W Ctrl-H` or `Ctrl-W Ctrl-L` (you will notice 'h' and 'l'
are the left and right navigation keys in vim). If you want, copy and paste the
entire file by going to the top of the file with `gg`, enter visual block mode
with `V`, go to the end of the file with `G`, yank all of the text with `y`,
change to the other window with `Ctrl-W Ctrl-W`, and paste with `P`.


If you are looking for more commands to put in your `.vimrc`, google it (or
[this link](https://dougblack.io/words/a-good-vimrc.html) is pretty good too).

