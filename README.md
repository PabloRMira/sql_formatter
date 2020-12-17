# sql_formatter
> A Python based SQL formatter


![CI](https://github.com/PabloRMira/sql_formatter/workflows/CI/badge.svg) [![PyPI](https://img.shields.io/pypi/v/sql-formatter?color=blue&label=pypi%20version)](https://pypi.org/project/sql-formatter/#description)

## How to install

`pip install sql-formatter`

## How to use

Format your SQL files via the command line

`sql-formatter sql_file.sql sql_file2.sql`

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

### What `sql_formatter` does not do

This package is just a SQL formatter and therefore

* cannot parse your SQL queries into e.g. dictionaries
* cannot validate your SQL queries before formatting

## Acknowledgements

Thank you very much to Jeremy Howard and all the [nbdev](https://github.com/fastai/nbdev) team for enabling the *fast* and delightful development of this library via the `nbdev` framework.

For more details on `nbdev`, see its official [tutorial](https://nbdev.fast.ai/tutorial.html)
