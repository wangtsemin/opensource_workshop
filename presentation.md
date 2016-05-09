% Open Source Workshop
% Ties and Jan
% May 18th, 2016


Introduction
================

what's the plan?
----------------


* We give short introductions to

    * Git
    * Github
	* Python
	* Jupyter notebook

* and then we will have fun with a notebook

underlying idea
---------------

* reproducible research:

    * write code that is understandable (also to yourself)
    * markdown for typesetting, latex for equations etc.
    * publish it in a way that is easily accessible

* at this [python conference](https://www.youtube.com/watch?v=oP9Qcjq8UVI), they use an AER paper to explain why this is important

* students can make assignments in this way:

    * combine their explanations and their code
    * post assignments so that you can easily grade them


Git and Github
===================

git
---


![Git](http://imgs.xkcd.com/comics/git.png)

----------


* git is a "versioning system"

    * stop calling your files "paper_v1_2016_a_March.tex"
    * never lose work by overwriting a previous version
	* easily see what you (or your co-author) changed in the last version
	* this you can do locally (no github needed)


github
------

* Github offers two extras:

    * backup your files "in the cloud"
    * Github pages (`gh-pages`): special branch that allows you to publish html files
	* difference between [this page](https://github.com/janboone/opensource_workshop/blob/gh-pages/presentation.html) and [this one](http://janboone.github.io/opensource_workshop/presentation)

* additional extras:

    * students put homework on github and you can edit/grade
    * issues page

        * team of teachers can respond to questions
        * same question needs to be answered only once

workflow
--------

* go to github and register
* then create a repository on-line; e.g. https://github.com/janboone/opensource_workshop
* there are lots of tutorials on how to do this
* then at the command line:

    * `git clone https://github.com/janboone/opensource_workshop`
    * `cd opensource_workshop`
	* create new files, change existing files etc.
	* when you are done
	* `git add .` adds all the files in the directory
	* `git commit -m "say something about what you added"`
	* `git push` changes files at github.com to the latest version
	* if you change something again, go through `git add`, `git commit` and `git push`

branches
--------

* git allows you to have different versions of your work (say, paper)
* useful for PhD students to have a branch `supervisor` that you can delete after your defense
* main branch is called `master`
* on github there is a special branch `gh-pages` that publishes html
* want to know more?

    * http://gitimmersion.com/
    * https://www.codecademy.com/learn/learn-git
    * https://git-scm.com/book/en/v2


Python
========

programming
-----------

* Programming? --> instruct a computer to do something
* How?
	- Formulate your instruction in a language that the computer can understand

Which language?
-----------

![Language](http://www.codingdojo.com/blog/wp-content/uploads/Programming-Languages-for-2016_graph.jpg)

Why Python?
-----------

* From the ground up build to be:
	* easy to learn
	* efficient to use ("programming time is more valuable than computer time")
	* readable for humans
* Very rich and constantly growing eco-system of tools for data science   
**But --> it is still a general purpose language with near-unlimited possibilities!**
* The origin of the Jupyter (IPython) Notebook

What can we use Python for?
-----------

* Solving models and performing numerical calculations
* Data processing (cleaning, wrangling, etc.) 
* Process (large amounts of) files (deal with "big data")
* Extract information from web-pages (web-crawling)
* Extract textual information (text mining)
* Machine learning applications
* Create (interactive) graphs
* **And many many other applications!**


Python is easy?!:
------------

```
numbers = [11, 5, 20, 6] 
response = 'The following number is too big:'

for i in numbers:
	if i > 10:
		print(response)
		print(i)
```

Can you read what the above code would do? 

How does Python execute code?
------------

Python executes code using what is called an interpreter --> `the Python interpreter`
![Illustration_1](https://dl.dropboxusercontent.com/u/1265025/python_tut/illustration_1.png)

The Python interpreter goes chronologically through the code and tells the computer line-by-line what to do. 

How can you run Python code?
------------

How do we send our code to the Python interpreter?   

1. Save the code in a `.py` file and execute it using the console with `python example.py`
	--> Prepare the code in a text-editor and send all the code to the interpreter at once
	
2. Use the interactive Python (IPython) console by typing in console: `ipython` or `python`
	--> Send Python code per line to the interpret and get an immediate response (hence *interactive*)
	
3. Use the Jupyter Notebook as an intermediary in your browser 
	--> Send Python code per line but use a web-application instead of the command line

Python 2 or Python 3?!
------------

**Python 2.7:** older version that only receives maintenance updates   
**Python 3.5:** newest version that receives all the new cool features


90% of the code will run fine regardless of the version, but Python 3 introduced some changes that are not backwards compatible. For example:
```
print 'Hello, world!'  #This only works in Python 2.7
print('Hello, world!') #This works in both Python 2.7 and Python 3
```

**Which version to use? --> hotly debated topic**

My personal advice:   

> Use Python 3.5 if you can unless you need to rely on prior code that is only available in Python 2.7
> It is relatively easy to install both Python 2.7 and Python 3.5 on one computer

The Python eco-system: modules and packages
------------

What is a module or package? --> essentially a `.py` file (*module*) or a collection of `.py` files (*package*)
Python modules/packages are pieces of Python code that you can `import` and use in your own code. 

**Two types of modules/packages:**

1. Build-in modules --> always included with any installation of Python
2. Third-party modules/packages --> made available on the internet by people like you and me!  
	--> The Python Package Index (PyPI) currently hosts around 80,000 packages! 

**Example:**
```
import os            # Standard library
import pandas as pd  # Third-party
```

The Python eco-system: modules and packages
------------

**How to install third-party modules/packages?**

Use `pip` to install packages that are hosted on the Python Package Index

Distributions like `Anaconda` and `Enthought Canopy` are awesome because they automatically install Python bundled with the most used packages for data science. 

Using a distribution saves you from having to install all the main-stream packages manually! 

Want to know more?
------------

 * [Automate the boring stuff](https://automatetheboringstuff.com/)
 * [Quant-econ.net](http://quant-econ.net/)
 * [other links](http://www.cs.colostate.edu/~anderson/cs545/index.html/doku.php?id=useful_links)


Jupyter
==========

What is the Jupyter Notebook?
--------

An open-source web application that allows people to create and share documents that contain live code, equations, visualizations, and explanatory text. 

In other words, the Jupyter Notebook provides a programming environment that makes it easy to document your reasoning and explain your code in a human-readable and shareable fashion.

Example
--------
![](https://dl.dropboxusercontent.com/u/1265025/python_tut/illustration_2.png)

Combine programs and programming languages
--------

The Jupyter Notebook is aimed to be language agnostic so it supports a wide variety of programs and programming languages. But there is more: you can also combine programs/languages within one notebook! 

Python is supported by default (as it was originally developed for Python)

* **R:**  rpy2  ([link](http://rpy2.bitbucket.org/))
* **Stata:** IPystata ([link](https://github.com/TiesdeKok/ipystata))
* **SAS:** SAS kernel ([link](https://github.com/sassoftware/sas_kernel))
* **Matlab:** matlab_kernel ([link](https://github.com/calysto/matlab_kernel))

How does it work?
--------
Only Python:

![](https://dl.dropboxusercontent.com/u/1265025/python_tut/illustration_3a.png)

Python + R (for example):

![](https://dl.dropboxusercontent.com/u/1265025/python_tut/illustration_3.png)


Start a Notebook server:
--------

From the command line   
(if you use Anaconda I would recommend using the `Anaconda Command Prompt`)

1. `cd` to the desired starting directory   
   --> e.g. `cd "C:\Stack\Work\Project_1"`
2. Start the Jupyter Notebook server:  
   --> `jupyter notebook`

Use a third-party tool to store directories and start the Jupyter Notebook server ([Notebook Opener](https://github.com/TiesdeKok/NotebookOpener)):

![](https://raw.githubusercontent.com/TiesdeKok/NotebookOpener/master/Images/example.png)

Use the Jupyter Notebook:
--------
Two modes: 

`command mode` --> enable by pressing `esc`   
 `edit mode` --> enable by pressing `enter`   

Useful shortcuts:




`command mode` |`edit mode` 	
---	| ---	
`Y` : cell to code	|  `Tab` : code completion or indent
`M` : cell to markdown  |   `Shift-Tab` : tooltip
`A` : insert cell above  	|   	`Ctrl-A` : select all
`B` : insert cell below  	|   `Ctrl-Z` : undo
`X`: cut selected cell | .


-----------



* In `both modes`

    * `Shift-Enter` : run cell, select below
    * `Ctrl-Enter` : run cell 

<!--


How to turn this markdown file into a presentation:

pandoc -s --mathjax --slide-level 2  -t revealjs --highlight-style=zenburn presentation.md -V theme=solarized -o presentation.html 

pandoc --slide-level 2 --toc --toc-depth=1 -t beamer presentation.md -V theme:Montpellier -o presentation.pdf




new slide:

------------


-->
