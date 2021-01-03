# sql_formatter
> A Python based SQL formatter


![CI](https://github.com/PabloRMira/sql_formatter/workflows/CI/badge.svg) [![PyPI](https://img.shields.io/pypi/v/sql-formatter?color=blue&label=pypi%20version)](https://pypi.org/project/sql-formatter/#description)

## How to install

`pip install sql-formatter`

## How to use

Format your SQL files via the command line

`sql-formatter sql_file.sql sql_file2.sql`

You can also format all your SQL-files via

`sql-formatter *.sql` in Unix

or via

`sql-formatter "*.sql"` in Windows

To format all your SQL files recursively use

`sql-formatter --recursive "*.sql"` in Unix and Windows

### Usage with `pre-commit`

[pre-commit](https://pre-commit.com) is a nice development tool to automatize the binding of pre-commit hooks. After installation and configuration `pre-commit` will run your hooks before you commit any change. 

To add `sql-formatter` as a hook to your `pre-commit` configuration to format your SQL files before commit, just add the following lines to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
    - id: sql_formatter
      name: SQL formatter
      language: system
      entry: sql-formatter
      files: \.sql$

```

### Usage in Python

To exemplify the formatting let's say you have a SQL query like this

```
example_sql = """
create or replace table mytable as -- mytable example
seLecT a.asdf, b.qwer, -- some comment here
c.asdf, -- some comment there
b.asdf2 frOm table1 as a leFt join 
table2 as b -- and here a comment
    on a.asdf = b.asdf  -- join this way
    inner join table3 as c
on a.asdf=c.asdf
whEre a.asdf= 1 -- comment this
anD b.qwer =2 and a.asdf<=1 --comment that
or b.qwer>=5
groUp by a.asdf
"""
```

Then you can use this package to format it so that it is better readable

```
from sql_formatter.core import format_sql
print(format_sql(example_sql))
```

    CREATE OR REPLACE TABLE mytable AS -- mytable example
    SELECT a.asdf,
           b.qwer, -- some comment here
           c.asdf, -- some comment there
           b.asdf2
    FROM   table1 as a
        LEFT JOIN table2 as b -- and here a comment
            ON a.asdf = b.asdf -- join this way
        INNER JOIN table3 as c
            ON a.asdf = c.asdf
    WHERE  a.asdf = 1 -- comment this
       and b.qwer = 2
       and a.asdf <= 1 --comment that
        or b.qwer >= 5
    GROUP BY a.asdf


It can even deal with subqueries and it will correct my favourite simple careless mistake (comma at the end of SELECT statement before of FROM) for you on the flow :-)

```
print(format_sql("""
select asdf, cast(qwer as numeric), -- some comment
qwer1
from 
(select asdf, qwer, from table1 where asdf = 1) as a
left 
join (select asdf, qwer2 from table2 where qwer2 = 1) as b
on a.asdf = b.asdf
where qwer1 >= 0
"""))
```

    SELECT asdf,
           cast(qwer as numeric), -- some comment
           qwer1
    FROM   (SELECT asdf,
                   qwer
            FROM   table1
            WHERE  asdf = 1) as a
        LEFT JOIN (SELECT asdf,
                          qwer2
                   FROM   table2
                   WHERE  qwer2 = 1) as b
            ON a.asdf = b.asdf
    WHERE  qwer1 >= 0


The formatter is also robust against nested subqueries

```
print(format_sql("""
select field1, field2 from (select field1, 
field2 from (select field1, field2, 
field3 from table1 where a=1 and b>=100))
"""))
```

    SELECT field1,
           field2
    FROM   (SELECT field1,
                   field2
            FROM   (SELECT field1,
                           field2,
                           field3
                    FROM   table1
                    WHERE  a = 1
                       and b >= 100))


If you do not want to get some query formatted in your SQL file then you can use the marker `/*skip-formatter*/` in your query to disable formatting for just the corresponding query

```
from sql_formatter.format_file import format_sql_commands
print(format_sql_commands(
"""
use database my_database;

-- My first view --
create or repLace view my_view as
select asdf, qwer from table1
where asdf <= 10;


/*skip-formatter*/
create oR rePlace tabLe my_table as
select asdf
From my_view;
"""
))
```

    use database my_database;
    
    
    -- My first view --
    CREATE OR REPLACE VIEW my_view AS
    SELECT asdf,
           qwer
    FROM   table1
    WHERE  asdf <= 10;
    
    
    /*skip-formatter*/
    create oR rePlace tabLe my_table as
    select asdf
    From my_view;
    


### A note of caution

For the SQL-formatter to work properly you should meticulously end each of your SQL statements with semicolon (;)

However, we have equiped the `sql-formatter` with some basic validations:

* *Forgotten semicolon validation*: The validator will check if the `CREATE` keyword appears more than twice, indicating the user that he / she may have forgotten a semicolon
* *Unbalanced parenthesis*: The validator will check if there are unbalanced parenthesis in the query
* *Unbalanced `case when ... end`*: The validator will check if there are `case when` statements without `end` or vice versa

### What `sql_formatter` does not do

This package is just a SQL formatter and therefore

* cannot parse your SQL queries into e.g. dictionaries
* cannot validate your SQL queries to be valid for the corresponding database system / provider

Up to now it only formats queries of the form

* `CREATE TABLE / VIEW ...`
* `SELECT ...`

Every other SQL commands will remain unformatted, e.g. `INSERT INTO` ...

## Formatting Logic

The main goal of the `sql_formatter` is to enhance readability and quick understanding of SQL queries via proper formatting. We use **indentation** and **lowercasing / uppercasing** as means to arrange statements / clauses and parameters into context. By **programmatically standardizing** the way to write SQL queries we help the user understand its queries faster.

As a by-product of using the `sql_formatter`, developer teams can focus on the query logic itself and save time by not incurring into styling decisions, this then begin accomplished by the `sql_formatter`. This is similar to the goal accomplished by the [black package](https://github.com/psf/black) for the Python language, which was also an inspiration for the development of this package for SQL. 

We can summarize the main steps of the formatter as follows:

1. Each query is separated from above by two newlines.
2. Everything but **main statements\* / clauses** is lowercased

\* Main statements:

* CREATE ... TABLE / VIEW table_name AS
* SELECT (DISTINCT)
* FROM
* (LEFT / INNER / RIGHT / OUTER) JOIN
* UNION
* ON
* WHERE
* GROUP BY
* ORDER BY
* OVER
* PARTITION BY

3. Indentation is used to put parameters into context. Here an easy example:

```sql
SELECT field1,
       case when field2 > 1 and
                 field2 <= 10 and
                 field1 = 'a' then 1
            else 0 end as case_field,
       ...
FROM   table1
WHERE  field1 = 1
   and field2 <= 2
    or field3 = 5
ORDER BY field1;
```

> This is a very nice, easy example but things can become more complicated if comments come into play

4. Subqueries are also properly indented, e.g.

```sql
SELECT a.field1,
       a.field2,
       b.field3
FROM   (SELECT field1,
               field2
        FROM   table1
        WHERE  field1 = 1) as a
    LEFT JOIN (SELECT field1,
                      field3
               FROM   table2) as b
        ON a.field1 = b.field1;
```

5. Everything not being a query of the form `CREATE ... TABLE / VIEW` or `SELECT ...` is left unchanged

## Versioning

We version our package via [semantic versioning](https://semver.org), i.e., 

* We use three digits separated by points x1.x2.x3, e.g. 0.5.1
* We increase x1 (the major version) if we introduce breaking changes
  * Exception: Versions with 0 at the beginning (e.g. 0.5.1) mean that the package is not stable yet and therefore every new feature could be a breaking change
* We increase x2 (the minor version) if we introduce a new feature
* We increase x3 (the patch version) if we fix a bug

New documentation, refactoring / maintenance of code and admin tasks do not change the versions.

You can follow the changes introduced by each version in our [CHANGELOG](https://github.com/PabloRMira/sql_formatter/blob/master/CHANGELOG.md)

## How to contribute

You can contribute to this project:

* writing issues
* contributing to the code basis

### Writing issues

If you find some bug or you think some new feature could improve the package, please write an issue going to [New Issue](https://github.com/PabloRMira/sql_formatter/issues/new/choose) and follow the instructions under the corresponding template

### Contributing to the code basis

We follow the [nbdev](https://github.com/fastai/nbdev) framework for the literate programming development of this project. So if you want to contribute, please familiarize first with this framework. Specially, we write our code, tests and documentation at the same time in jupyter notebooks.

If you have not heard about `nbdev` yet and / or find the idea weird to develop in notebooks as it was the case for me, please watch the following youtube video first: [I like notebooks](https://www.youtube.com/watch?v=9Q6sLbz37gk) by Jeremy Howard, the creator of this wonderful framework. 

#### Setup the development environment
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

#### Development Workflow

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

## Acknowledgements

Thank you very much to Jeremy Howard and all the [nbdev](https://github.com/fastai/nbdev) team for enabling the *fast* and delightful development of this library via the `nbdev` framework.

For more details on `nbdev`, see its official [tutorial](https://nbdev.fast.ai/tutorial.html)

Thank you very much for the developers of the [black](https://github.com/psf/black) package, which was also an inspiration for the development of this package
