# Release notes

## 0.5.2

### Bugfixes:
* [FIX] case when wrongly formatted if case when at least in second argument and preceded by text in quotes ([#133](https://github.com/PabloRMira/sql_formatter/pull/133))
* [FIX] comment assignment fails sometimes ([#130](https://github.com/PabloRMira/sql_formatter/pull/130))

### Documentation:
* [DOC] Fix wrong formatting in README ([#127](https://github.com/PabloRMira/sql_formatter/pull/127))

## 0.5.1

### Bugfixes:
* [FIX] Formatter adds whitespaces between symbols inside of quotes ([#121](https://github.com/PabloRMira/sql_formatter/pull/121))

### Documentation:
* [DOC] Add docs for versioning and changelog ([#125](https://github.com/PabloRMira/sql_formatter/pull/125))
* [DOC] Add docs for formatting logic ([#123](https://github.com/PabloRMira/sql_formatter/pull/123))
* [DOC] Correct docs for contributing: fork instead of branch ([#122](https://github.com/PabloRMira/sql_formatter/pull/122))

## 0.5.0

### New features:
* [FEA] Add newline for each case when ... end condition and make functions robust against keywords in comments ([#112](https://github.com/PabloRMira/sql_formatter/pull/112))

### Refactoring / Maintenance:
* [MNT] Add link to pull request in changelog ([#114](https://github.com/PabloRMira/sql_formatter/pull/114))

## 0.4.0

### New features:
* [FEA] Add validator for case when ... end ([#102](https://github.com/PabloRMira/sql_formatter/pull/102))

### Bugfixes:
* [FIX] case when wrongly formatted if comment after condition ([#106](https://github.com/PabloRMira/sql_formatter/pull/106))
* [FIX] Formatting of comment after semicolon ([#104](https://github.com/PabloRMira/sql_formatter/pull/104))

### Refactoring / Maintenance:
* [MNT] Refactor code basis ([#105](https://github.com/PabloRMira/sql_formatter/pull/105))

## 0.3.2

### Bugfixes:
* [FIX] comment marker [CI] failing sometimes ([#97](https://github.com/PabloRMira/sql_formatter/pull/97))
* [FIX] SELECT DISTINCT fields not being formatted properly ([#96](https://github.com/PabloRMira/sql_formatter/pull/96))

## 0.3.1

### New features:
* [FEA] Add CLI to handle git release and changelog creation programmatically via commit messages ([#87](https://github.com/PabloRMira/sql_formatter/pull/87))
* [FEA] Add formatting for multiline comments ([#86](https://github.com/PabloRMira/sql_formatter/pull/86))
* [FEA] Separate each ON join by newline ([#80](https://github.com/PabloRMira/sql_formatter/pull/80))

### Bugfixes:
* [FIX] Semicolon / CREATE validation fails ([#85](https://github.com/PabloRMira/sql_formatter/pull/85))
* [FIX] Fields in ORDER BY in PARTITION BY with wrong indentation ([#84](https://github.com/PabloRMira/sql_formatter/pull/84))
* [FIX] View name is wrongly written uppercase in CREATE OR REPLACE VIEW my_view AS ([#79](https://github.com/PabloRMira/sql_formatter/pull/79))

### Documentation:
* [DOC] Add docs for maintenance / refactoring ([#89](https://github.com/PabloRMira/sql_formatter/pull/89))
* [DOC] Update README ([#82](https://github.com/PabloRMira/sql_formatter/pull/82))
* [DOC] Add hint for contributors to install the package in editable mode for the CLI to incorporate changes in code basis ([#81](https://github.com/PabloRMira/sql_formatter/pull/81))

### Refactoring / Maintenance:
* [MNT] Refactor / Simplify code basis, remove deprecated functions, adjust docs ([#90](https://github.com/PabloRMira/sql_formatter/pull/90))

## 0.2.0

### New features:
* [FEA] Add validation for balanced parenthesis ([#73](https://github.com/PabloRMira/sql_formatter/pull/73))
* [FEA] Add validation for missing semicolon ; ([#72](https://github.com/PabloRMira/sql_formatter/pull/72))
* [FEA] Add CLI funcitonality to format files recursively in subfolders ([#68](https://github.com/PabloRMira/sql_formatter/pull/68))
* [FEA] Add CLI functionality for wildcards * ([#59](https://github.com/PabloRMira/sql_formatter/pull/59))

### Bugfixes:
* [FIX] SELECT .. FROM split if some of they keywords in quotes ([#71](https://github.com/PabloRMira/sql_formatter/pull/71))
* [FIX] case when in function does not get proper indentation ([#65](https://github.com/PabloRMira/sql_formatter/pull/65))
* [FIX] ORDER BY formatting within PARTITION BY ([#63](https://github.com/PabloRMira/sql_formatter/pull/63))
* [FIX] Text in quotes is wrongly lowercased ([#62](https://github.com/PabloRMira/sql_formatter/pull/62))
* [FIX] Do not split if ; is in comments ([#61](https://github.com/PabloRMira/sql_formatter/pull/61))
* [FIX] Formatting for CREATE ... TABLE / VIEW should be more general ([#60](https://github.com/PabloRMira/sql_formatter/pull/60))
* [FIX] Ambiguous report message ([#58](https://github.com/PabloRMira/sql_formatter/pull/58))
* [FIX] UNION (join) has no formatting ([#57](https://github.com/PabloRMira/sql_formatter/pull/57))

### Documentation:
* [DOC] Add docs for how to contribute ([#74](https://github.com/PabloRMira/sql_formatter/pull/74))

## 0.1.2

### Bugfixes:
* [FIX] CREATE TASK wrongly identified as query ([#42](https://github.com/PabloRMira/sql_formatter/pull/42))
* [FIX] PARTITION BY, SELECT DISTINCT and tests for ORDER BY and PARTITION BY ([#39](https://github.com/PabloRMira/sql_formatter/pull/39))

### Documentation:
* [DOC] Write docs for how to install and add CI and Pypi images ([#40](https://github.com/PabloRMira/sql_formatter/pull/40))

## 0.1.1

### Bugfixes:
* [FIX] SELECT adds newline for function arguments and outsource auxiliary functions to utils ([#35](https://github.com/PabloRMira/sql_formatter/pull/35))
* [FIX] PARTITION BY not properly formatted and No formatting for ORDER BY ([#33](https://github.com/PabloRMira/sql_formatter/pull/33))
* [FIX] ON formatting does not work properly ([#31](https://github.com/PabloRMira/sql_formatter/pull/31))