# sql_formatter
> A SQL formatter


## Install

`pip install sql_formatter`

## How to use

Let's say you have a SQL query like this

```
ex_sql = """
seLecT a.asdf, b.qwer,
b.asdf2 frOm table1 as a leFt join 
table2 as b
    on a.asdf = b.asdf  inner join table3 as c
on a.asdf=c.asdf
whEre a.asdf= 1
anD b.qwer =2
and a.asdf<=1
or b.qwer>=5
groUp by a.asdf
"""
print(ex_sql)
```

    
    seLecT a.asdf, b.qwer,
    b.asdf2 frOm table1 as a leFt join 
    table2 as b
        on a.asdf = b.asdf  inner join table3 as c
    on a.asdf=c.asdf
    whEre a.asdf= 1
    anD b.qwer =2
    and a.asdf<=1
    or b.qwer>=5
    groUp by a.asdf
    


Then you can use this package to format it so that it is better readable

```
print(format_sql(ex_sql))
```

    
    SELECT a.asdf,
           b.qwer,
           b.asdf2
    FROM   table1 AS a
        LEFT JOIN table2 AS b
            ON a.asdf = b.asdf
        INNER JOIN table3 AS c
            ON a.asdf = c.asdf
    WHERE  a.asdf = 1
       and b.qwer = 2
       and a.asdf <= 1
        or b.qwer >= 5
    GROUP BY a.asdf

