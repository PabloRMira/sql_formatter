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
    GROUP BY a.asdf;


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
    WHERE  qwer1 >= 0;


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
                       and b >= 100));


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

### What `sql_formatter` does not do

This package is just a SQL formatter and therefore

* cannot parse your SQL queries into e.g. dictionaries
* cannot validate your SQL queries to be valid for the corresponding database system / provider

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
1. Clone the project and navigate into the project with your terminal
2. Install our conda development environment running `conda env create -f environment.yml`
3. Activate the python environment using `conda activate sql-formatter-dev`
4. Run `nbdev_install_git_hooks`
5. Run `pip install -e .` to install the package in editable mode. This way the command line interface (CLI) `sql-formatter` will incorporate your changes in the python code

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
