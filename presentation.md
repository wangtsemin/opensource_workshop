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
    * publish it in a way that is easily accessible

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

    * stop calling files "paper_v1_2016_a_March.tex"
    * never lose work by overwriting a previous version
	* easily see what you (or your co-author) changed in the last version
	* this you can do locally (no github needed)


github
------

* Github offers two extras:

    * backup your files "in the cloud"
    * Github pages (`gh-pages`): special branch that allows you to publish html files
	* difference between [this page](https://github.com/janboone/opensource_workshop/blob/gh-pages/presentation.html) and [this one](http://janboone.github.io/opensource_workshop/presentation)

* additional extras: students put homework on github and you can edit/grade
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



Python
========

programming
-----------

* what is programming?
* advantage python: write readable code!
* What do we use python for?

    * solving models
    * data manipulation
    * making interactive graphs (plotly)


-----------

<iframe src="https://plot.ly/~janboone/204.embed"
        height="800" width="100%"
        scrolling="no" seamless="seamless"
        frameBorder="0">
</iframe>

-----------


	* sending (lots of) emails
	* scraping websites





easy to read
------------

* python has a number of 'tricks' that make it easy to read:

    * spacing to indicate commands that belong together
    * iterate over 'anything'; `for firm in ['google', 'apple', 'facebook']`
    * `output['apple'] = 5000`
    * `[5*x for x in [0,1,2,3]]` creates vector `[0, 5, 10, 15]`


Jupyter
==========

notebook
--------

* notebook is useful ..



<!--

How to turn this markdown file into a presentation:

pandoc -s --mathjax --slide-level 2  -t revealjs presentation.md -V theme=solarized -o presentation.html

pandoc --slide-level 2 --toc --toc-depth=1 -t beamer presentation.md -V theme:Montpellier -o presentation.pdf




new slide:

------------


-->
