# How to contribute

You can contribute to this project:

* writing issues
* contributing to the code basis

## Writing issues

If you find some bug or you think some new feature could improve the package, please write an issue going to [New Issue](https://github.com/PabloRMira/sql_formatter/issues/new/choose) and follow the instructions under the corresponding template

## Contributing to the code basis

We follow the [nbdev](https://github.com/fastai/nbdev) framework for the literate programming development of this project. So if you want to contribute, please familiarize first with this framework. Specially, we write our code, tests and documentation at the same time in jupyter notebooks.

If you have not heard about `nbdev` yet and / or find the idea weird to develop in notebooks as it was the case for me, please watch the following youtube video first: [I like notebooks](https://www.youtube.com/watch?v=9Q6sLbz37gk) by Jeremy Howard, the creator of this wonderful framework. 

### Setup the development environment
Prerequisites to setup the development environment:
* conda

To setup the development environment:
1. Fork this project repository, i.e., click on the "Fork" button on the right of the top of the repo page. This creates a copy of the project code on your GitHub user account.
2. Clone your forked project from your GitHub account to your local disk and navigate into it:

```bash
git clone git@github.com:YourLogin/sql_formatter.git
cd sql_formatter
```

3. Setup the `upstream` remote to be the original project repository (this one and not your forked one):

```bash
git remote add upstream https://github.com/PabloRMira/sql_formatter.git
```

4. Synchronize your master branch with the upstream branch:

```bash
git checkout master
git pull upstream master
```

5. Create a new branch to hold your development changes:

```bash
git checkout -b my_feature_branch
```

6. Install our conda development environment running `conda env create -f environment.yml`
7. Activate the python environment using `conda activate sql-formatter-dev`
8. Run `nbdev_install_git_hooks`
9. Run `pip install -e .` to install the package in editable mode. This way the command line interface (CLI) `sql-formatter` will incorporate your changes in the python code
10. When your change is ready commit it, and push it to your fork

```
git add modified_files
git commit -m "some message"
git push -u origin my_feature_brach
```

11. Follow [these instructions](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork) to create a pull request from your fork.

### Development Workflow

For development we follow these steps:
1. Pick an existing issue and write in the comments you would like to fix it
  * If your idea is not documented in an issue yet, please write first an issue
2. Create a branch from `master` and implement your idea
3. Before pushing your solution run first `make prepush` to make sure everything is allright to merge, specially our tests
4. Make a pull request for your solution
  * The pull request title should be meaningful, something like "[PREFIX] Title of the issue you fixed". Please try to use some of the following prefixes: 
    * [FIX] for bugfixes
    * [FEA] for new features
    * [DOC] for documentation
    * [MNT] for maintenance

> Only pull requests / commits using the aforementioned prefixes will be added to the changelog / release notes
