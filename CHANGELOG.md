# Release notes

## 0.4.0

### New features:
* [FEA] Add validator for case when ... end (#102)

### Bugfixes:
* [FIX] case when wrongly formatted if comment after condition (#106)
* [FIX] Formatting of comment after semicolon (#104)

### Refactoring / Maintenance:
* [MNT] Refactor code basis (#105)

## 0.3.2

### Bugfixes:
* [FIX] comment marker [CI] failing sometimes (#97)
* [FIX] SELECT DISTINCT fields not being formatted properly (#96)

## 0.3.1

### New features:
* [FEA] Add CLI to handle git release and changelog creation programmatically via commit messages (#87)
* [FEA] Add formatting for multiline comments (#86)
* [FEA] Separate each ON join by newline (#80)

### Bugfixes:
* [FIX] Semicolon / CREATE validation fails (#85)
* [FIX] Fields in ORDER BY in PARTITION BY with wrong indentation (#84)
* [FIX] View name is wrongly written uppercase in CREATE OR REPLACE VIEW my_view AS (#79)

### Documentation:
* [DOC] Add docs for maintenance / refactoring (#89)
* [DOC] Update README (#82)
* [DOC] Add hint for contributors to install the package in editable mode for the CLI to incorporate changes in code basis (#81)

### Refactoring / Maintenance:
* [MNT] Refactor / Simplify code basis, remove deprecated functions, adjust docs (#90)

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