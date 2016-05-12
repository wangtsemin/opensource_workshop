# opensource_workshop
program of open source workshop at Tilburg University

On the 18th and 23rd of May we are organizing two open source workshops. The planning is as follows:

* May 18, 14:15-16:30 in room DZ 1: Ties and Jan give an introduction to GitHub, Python and the Jupyter notebook
* May 23, 12:45-15:30 in room GZ 104: Ties teaches Python hands-on. In this session we will tackle some common empirical use-cases with Python. Main topics to be covered include: data handling and cleaning, processing large amounts of files, extracting textual information (“text mining”), extracting information from web-pages (“web scraping”), and creating (interactive) data visualizations.

**Note that the rooms that were originally advertised have changed**

In June, we plan to organize a third workshop for R.

GitHub is a great way to put your research under version-control and optionally share it with the rest of the world. You can host your homepage at GitHub but also collaborate with other people in a more sophisticated way than sending emails with attachments. We have experimented with students putting their assignments on GitHub, so that we can give comments and grade the assignments. The first experience is very positive.


However, starting with GitHub may not be straightforward for everyone. Therefore, we will give a first introduction. Questions to be answered include: what is GitHub? When is it better than Dropbox? What is the point of version control? How do you create a repository with your research material on GitHub? How do you collaborate with others on GitHub?


Python is a great and fun programming language. For research purposes it is tremendously useful across all disciplines. It is fast outpacing proprietary tools like Matlab and Mathematica and it is free! We use it for our own research but are also introducing it into BSc and MSc courses and students tend to like it. There are numerous introductions to Python available on the web which can make it daunting to actually start using it. Our goal is to give an introduction to Python that provides you with the necessary tools to get started and to help you navigate all the great Python resources publicly available on the web.


The Jupyter notebook is a great way to create and share documents that contain live code, equations, visualizations and explanatory text. This is, again, very useful for both research and educational purposes. The Jupyter notebook is language agnostic and can be used for both for Python and R among many other languages.


Hope to see you at the workshops!


# Installing things

If you want to bring your laptop, it is useful to install the following software beforehand:

* As we will be working with GitHub, we need to install [Git](https://git-scm.com/downloads) . No need to install a fancy GUI, as we will be working with the command line.

    * if you need more help [this](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git) may be useful and
    * [this as well](http://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

The program language that we use, is python which we will use with the ipython or Jupyter notebook interface. You can install these things separately, but it is easier to install everything together. The best way to do this is to use the [anaconda distribution](https://www.continuum.io/downloads). Make sure to install python 2.7 (not 3.0). See the [quantitative economics website](http://quant-econ.net/py/getting_started.html) on how to install anaconda.

# getting the material

If you want to get the material (presentation and notebooks) that we use, you need to install git and then do the following:

* type at a terminal/shell/command prompt: `git clone https://github.com/janboone/opensource_workshop`
* `cd opensource_workshop`
* in the master branch you find the notebooks in the folder `example`
* in the `gh-pages` branch, you find the presentation
* to get to this branch, type (when you are in the `opensource_workshop` folder): `git checkout gh-pages`

