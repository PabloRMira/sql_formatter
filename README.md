# sql_formatter (WIP)
> A SQL formatter


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
```

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


It can even deal with subqueries

```python
example_with_subqueries = """
select asdf, cast(qwer as numeric), -- some comment
qwer1
from 
(select asdf, qwer, from table1 where asdf = 1) as a
left 
join (select asdf, qwer2 from table2 where qwer2 = 1) as b
on a.asdf = b.asdf
where qwer1 >= 0
"""
print(example_with_subqueries)
```

    
    select asdf, cast(qwer as numeric), -- some comment
    qwer1
    from 
    (select asdf, qwer, from table1 where asdf = 1) as a
    left 
    join (select asdf, qwer2 from table2 where qwer2 = 1) as b
    on a.asdf = b.asdf
    where qwer1 >= 0
    


and it will correct simple careless mistakes (like my favourite one: comma at the end of SELECT statement before of FROM) for you on the flow :-)

```python
print(format_sql(example_with_subqueries))
```

    SELECT asdf,
           cast(qwer AS numeric), -- some comment
           qwer1
    FROM   (SELECT asdf,
                   qwer
            FROM   table1
            WHERE  asdf = 1) AS a
        LEFT JOIN (SELECT asdf,
                          qwer2
                   FROM   table2
                   WHERE  qwer2 = 1) AS b
            ON a.asdf = b.asdf
    WHERE  qwer1 >= 0;


## Acknowledgements

Thank you very much to Jeremy Howard and all the [nbdev](https://github.com/fastai/nbdev) team for enabling the *fast* and delightful development of this library via the `nbdev` framework.

For more details on `nbdev`, see its official [tutorial](https://nbdev.fast.ai/tutorial.html)
