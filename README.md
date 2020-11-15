# sql_formatter
> A SQL formatter


## Install

`pip install sql_formatter`

## How to use

Let's say you have a SQL query like this

```python
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
print(example_sql)
```

    
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
    


Then you can use this package to format it so that it is better readable

```python
from sql_formatter.core import format_sql
print(format_sql(example_sql))
```

    CREATE OR REPLACE TABLE mytable AS -- mytable example
    SELECT a.asdf,
           b.qwer, -- some comment here
           c.asdf, -- some comment there
           b.asdf2
    FROM   table1 AS a
        LEFT JOIN table2 AS b -- and here a comment
            ON a.asdf = b.asdf -- join this way
        INNER JOIN table3 AS c
            ON a.asdf = c.asdf
    WHERE  a.asdf = 1 -- comment this
       and b.qwer = 2
       and a.asdf <= 1 --comment that
        or b.qwer >= 5
    GROUP BY a.asdf;

