Programming Help Sessions (PHS): Week 5
=======================================

Welcome back!

If you were here last week and you have already cloned the github repository,
you can update the phs directory with all of my new updates by navigating to
the `phs` directory (`cd phs`), and then running `git pull`.  If this doesn't
work, run `git reset --hard HEAD~`, after which you can run `git pull` (which
forces you to forget any changes you have made).  Now, if you list the files
(`ls`) in this directory you should see a new `week_5` folder. Move into this
directory.

Convenient shell utilities
--------------------------
Install `ranger`:
+ Windows Subsystem for Linux/Linux: `sudo apt install ranger`
+ Mac: `brew install ranger`

Open `ranger` from the command line. The result is a vim-influenced file
manager. Use `hjkl` to move within and between directories. Use `Enter` to open
files (ranger will guess the default program), and use `q` to quit ranger.

Install `zsh` (similar to above). Execute it by typing the command `zsh` in the
shell. You are now in `zsh` instead of `bash`. The original shell (from the old
days) is `sh`, which you can open by executing `sh` on the command line. To
exit any of these shells, use the command `exit`.

As Unix systems have evolved, shells have evolved as well. In my mind, this
evolution goes `sh` (the 'Bourne shell') -> `bash` (bourne-again shell) -> some
newer variant such as `zsh` ('Z shell'), though others exist (e.g. `fish`, the
'friendly interactive shell').

In the `zsh` shell, check out the new autocomplete options. Type the command
`head -` and then tab-complete after typing the hyphen, and you will see some
of the most commonly used hyphens (such as `-n`). This tab-completion works for
most commands (e.g. try `git ` then tab-complete after the space).

Using `ssh` (secure shell)
--------------------------
`ssh` is a protocol that allows you to securely login to a remote server. Once
logged in, you can use the remote server in the same way that you have been
using the shell in this course.  The security of ssh is ensured through
cryptography, which is an entire field of study.  The idea is to encrypt
the communication between you and the server, so that even if the communication
is intercepted, it will be entirely indecipherable.

It is common practice to use `ssh` to remotely access a different system. In
the old days, Windows users would use the program Putty in order to `ssh` into
Unix machines. I used to `ssh` into my college computers in order to have
access to pay-walled research articles, or to use proprietary software (e.g.
Mathematica) that I didn't have personal access to. My friend would `ssh` into
his parent's computers, which allowed him to keep them updated and in good
shape without being there in person.  Most commonly, I `ssh` into
supercomputers, which are much faster (typically they have many more CPU or GPU
cores) than my personal machine.

I can't share my login to supercomputers that I have access to (liability,
etc., etc.), and so we will be using a publicly available server at SDF
(sdf.org). We will use a free account I made earlier, with username `eric2` and
password `my_pass`. To login to the server, we use the command
```
    % ssh eric2@sdf.org
```
When prompted that "The authenticity of host 'sdf.org (205.166.94.16)' can't be
established", type `yes` and continue. Then enter in the password `my_pass`
when prompted, and press `Enter` a few times until you see the prompt
```
    sdf:/sdf/udd/e/eric2>
```
This is the same type of shell that we have been using all along! Try some
familiar commands:
```
    % ls
    .          ..         .history   .hushlogin .lesshst   .signature my_acct    my_file
    % cat my_file
    Hello
    hello there
    % pwd
    /sdf/udd/e/eric2
    % whoami
    eric2
```

However, if you try to use different commands (like `head` or `tail`), they
don't work. Even using `vim` doesn't work-- `vim` becomes `nano`, a different
(equally ubiquitous) text editor. Try making a file with `vim my_name` where
you replace my_name with your actual name. This will make the files unique--
since everyone is logged in as the same user, if people open the same file at
the same time, those files will be overwritten. In this text editor (which is
not vim), you use the arrow keys to move around, and enter text normally (i.e.
not like in vim). To save, use `Ctrl+O`, and to quit use `Ctrl+X`. In general,
the caret `^` means `Ctrl`.

Now let's explore the rest of this filesystem. With `ls -lah` we can see who
owns which files. We can also run this on the parent directory (`..`). A sample
of the output is:
```
    % pwd
    /sdf/udd/e/eric2
    % ls -lah
    total 35K
    drwx------     3 eric2  users  512B Nov 26 08:48 .
    drwxr-xr-x  1229 new    wheel   24K Nov 25 12:36 ..
    -rw-r--r--     1 eric2  users   10K Nov 26 09:01 .history
    -rw-------     1 eric2  users    8B Nov 22 23:14 .hushlogin
    -rw-------     1 eric2  users   44B Nov 26 08:14 .lesshst
    -rw-------     1 eric2  users   61B Nov 22 22:57 .signature
    drwxr-xr-x     2 eric2  users  512B Nov 22 22:58 my_acct
    -rw-r--r--     1 eric2  users   18B Nov 26 08:52 my_file
    % cd ..
    % pwd
    /sdf/udd/e
    % ls -lah
    <-- MANY OTHER DIRECTORIES -->
    drwx------     2 erezbeyi          new    512B Sep 13 18:51 erezbeyi
    drwx------     2 ergab             users  512B May 26  2010 ergab
    drwxr-xr-x     2 erhjzuztert       new    512B May 22  2018 erhjzuztert
    drwx------     2 eric13            users  512B Oct  1  2010 eric13
    drwx------     3 eric2             users  512B Nov 26 08:48 eric2
    drwx------     2 eric84            users  512B Aug 19  2010 eric84
    drwx------     2 erica.parker      users  512B Oct  8 15:41 erica.parker
    <-- MANY OTHER DIRECTORIES -->
```
Notice that our name and folder, `eric2`, is in this directory. We own this
folder, but other users have their own personal folders, too. However, we
aren't able to access most of these other people's folders:
```
    % cd eric84
    /usr/local/bin/psh[622]: cd: /sdf/udd/e/eric84 - Permission denied
```
This is because their permissions forbid others from reading their data.
However, some people have relaxed their permissions. `erhjzuztert`, for
example, has a folder that others (such as us) are able to read:
```
    drwxr-xr-x     2 erhjzuztert       new    512B May 22  2018 erhjzuztert
```
Let's check out their directory with `cd erhjzuztert`. Explore with `ls`. This
is a boring directory (only dotfiles), but you can read them with `cat` if you
wish. If you try to make a file (e.g. with `touch my_file`), you won't be able
to-- this is because you don't have 'write' permissions.

This is the extent to which we will explore this remote server. Exit with the
command `exit`, and press `Enter` and `Ctrl+C` a few times until you are back
to your normal shell.

Creating a Github repository
----------------------------
Next we will learn how to use git in the command line, which you will use to
make a personal Github repository. I am largely following the github help page
at https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/

First, make an account at github.com. You will need to verify your email in
order for an account to be created. In this guide, I will assume that your
username is **uname**.

Create a new repository (the "New repository" button once you are logged in on
github), and name it something (I named it `my_first_repo`). You don't need to
add a description. Keep it public (private requires you pay money), and keep
all the other options as they are by default.

Make a sample directory in your computer that will become your first github
repository, and add some files to it. I called mine `my_first_repo`:
```
    % cd ~
    % mkdir my_first_repo
    % cd my_first_repo
    % touch file_1
    % echo This is some text > file_2
    % ls
    file_1  file_2  README.md
```

Note that at this point, this is just a sample repository.
We want to initialize this directory as a git repository, which we do with
the command `git init` (interested in details? `man git init`):
```
    % git init
    Initialized empty Git repository in /home/eric/my_first_repo/.git/
    % ls -lah
    drwxr-xr-x  3 eric users 4.0K Nov 28 15:45 .
    drwxr-xr-x 14 eric users 4.0K Nov 28 15:30 ..
    -rw-r--r--  1 eric users    0 Nov 28 15:31 file_1
    -rw-r--r--  1 eric users   10 Nov 28 15:31 file_2
    drwxr-xr-x  7 eric users 4.0K Nov 28 15:45 .git
    % cd .git
    % ls
    branches  config  description  HEAD  hooks  info  objects  refs
```
This `.git` subdirectory contains all of the information needed for git to
function.

Now we need to link our directory `my_first_repo` with the github repository we
just made. We do this with the command `git remote`:
```
    % git remote add origin https://github.com/uname/my_first_repo.git
    % git remote -v
```
The above URL is also available in the "Quick setup" box of your my_first_repo page
on github.

Here, the first command creates a "remote" called **origin** that is
https://github.com/uname/my_first_repo.git. This means, anytime you use the
parameter `origin` in a git command, git will know that you really mean
https://github.com/uname/my_first_repo.git. This knowledge (and much more) is
stored in the .git directory (try `cat .git/config` to see). It turns out that
`origin` is the default git parameter for many git commands-- that means, once
you set this remote, any future git commands will automatically be applied to
your github repository `my_first_repo`.

If you refresh your github repo page (`github.com/uname/my_first_repo`), you
won't see the `file_1` or `file_2` that you created earlier. So far, you have
only modified git on *your* side-- you haven't yet communicated with github.

The fundamental git workflow is:
1. Modify files in your directory as normal. These changes are not yet
   reflected in the github repository.
2. Once you have gotten to a point that you would like to merge with your
   github repository, use the command `git add .` to add or "stage" files you
   have been working on to *index* or *staging area*. To check this staging
   area, use `git status`.
3. Consolidate all of the changes you have made into one package, called a
   "commit", with `git commit -m "commit message"`. You must add a commit
   message, which details what you did in this commit (e.g. "added files" or
   "added function my_func") These commits are the building blocks of git-- you
   can watch the evolution of a program through git commits that incrementally
   add and delete lines of code. (Want to see the evolution of Linux? Check out
   https://github.com/torvalds/linux/commits)
4. Push your changes to the github repository with `git push`. This takes any
   commits you have made and adds them to the github repository. The first time
   you run this command you must run `git push -u origin master` instead, which
   specifies the `origin` remote (defined earlier) as the `master` "upstream"
   repository that we wish to push to. After this, we can just use `git push`

All together, let's follow these steps to push our new files (`file_1` and
`file_2` to our github repository `my_first_repo`:
```
    % ls
    file_1  file_2
    % git add *
    % git status
    On branch master

    No commits yet

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

        new file:   file_1
        new file:   file_2
    % git commit -m "my commit message"
    [master (root-commit) 90a8e6a] my commit message
     2 files changed, 1 insertion(+)
     create mode 100644 file_1
     create mode 100644 file_2
    % git push -u origin master
    Username for 'https://github.com': eric-alt
    Password for 'https://eric-alt@github.com': 
    Enumerating objects: 4, done.
    Counting objects: 100% (4/4), done.
    Delta compression using up to 4 threads
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (4/4), 256 bytes | 256.00 KiB/s, done.
    Total 4 (delta 0), reused 0 (delta 0)
    remote: 
    remote: Create a pull request for 'master' on GitHub by visiting:
    remote:      https://github.com/eric-alt/my_first_repo/pull/new/master
    remote: 
    To https://github.com/eric-alt/my_first_repo.git
     * [new branch]      master -> master
    Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Now, refresh and your github repository should include these new files!

Let's try this one more time, to get the hang of it better.
1. Modify file_1 in vim (`vim file_1`) and add some lines. Then save and quit
   (`:wq`)
2. Add a new file called `README.md` with the command
   `echo "This is a readme" > README.md`
3. `git add .`
4. `git commit -m "modified files and added README"`
5. `git push` and enter your username and password (note we don't need to add
   `-u origin master` here-- it knows by default)

Now, refresh the github repository and you should see new files, as well as a
`README.md` file that displays on the "homepage" of your repository. 

Are you getting tired of entering your username and password each time you run
`git push`? Luckily enough, you can use SSH (the same SSH we used earlier) to
connect with github, and you can setup "passwordless" logins. In this way, you
can `git push` without entering a username and password, but you will also be
able to SSH into remote machines (with the `ssh` command) and automatically
login as well.  We won't do this in class, but I would recommend following the
tutorial at https://help.github.com/articles/connecting-to-github-with-ssh/ on
your own time.

Next up, we will use our github accounts to improve the Programming Help
Sessions

Modifying the PHS repository
----------------------------
Next, you will improve the programming help sessions by contributing to it with
git.

1. Go to the original PHS directory (github.com/erijones/phs) and click the
   "Fork" button on the top-right of the page. 



Some practice with vim and LaTeX
--------------------------------
Let's get some practice modifying documents in vim. Open
`skeleton_document.tex` in vim, and scroll down to line 24. Autocompile it
regularly (use `@w` and `@o` in vim, like we defined last week in our
`.vimrc`), and each time you recompile the .tex file refresh the pdf to see how you
changed it. Perform the following tasks (autocompiling each time):

+ Modify some of the math on lines 16 and 18
+ Follow the instructions and fix the typos on lines 24-33
+ Add an item to the itemize environment (line 49-ish) with your favorite type
  of ice cream
+ Make a sub-sub-list by making a new enumerate environment within the existing
  ones on line 58
+ Break the Pythagorean theorem by adding an extra constant (line 65-ish)
+ Add a new row to the matrix (line 75-ish)

If you have already performed this practice, execute the program `vimtutor`
instead from the shell:
```
    % vimtutor
```
More vim practice
-----------------
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

Other useful shell programs
---------------------------
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



