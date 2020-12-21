# Changelog

## 0.2.0

### New features:
* [FEA] Add validation for balanced parenthesis (#73)
* [FEA] Add validation for missing semicolon ; (#72)
* [FEA] Add CLI funcitonality to format files recursively in subfolders (#68)
* [FEA] Add CLI functionality for wildcards * (#59)

### Bugfixes:
* [FIX] SELECT .. FROM split if some of they keywords in quotes (#71)
* [FIX] case when in function does not get proper indentation (#65)
* [FIX] ORDER BY formatting within PARTITION BY (#63)
* [FIX] Text in quotes is wrongly lowercased (#62)
* [FIX] Do not split if ; is in comments (#61)
* [FIX] Formatting for CREATE ... TABLE / VIEW should be more general (#60)
* [FIX] Ambiguous report message (#58)
* [FIX] UNION (join) has no formatting (#57)

### Documentation:
* [DOC] Add docs for how to contribute (#74)

## 0.1.2

### Bugfixes:
* [FIX] CREATE TASK wrongly identified as query (#42)
* [FIX] PARTITION BY, SELECT DISTINCT and tests for ORDER BY and PARTITION BY (#39)

### Documentation:
* [DOC] Write docs for how to install and add CI and Pypi images (#40)

## 0.1.1

### Bugfixes:
* [FIX] SELECT adds newline for function arguments and outsource auxiliary functions to utils (#35)
* [FIX] PARTITION BY not properly formatted and No formatting for ORDER BY (#33)
* [FIX] ON formatting does not work properly (#31)