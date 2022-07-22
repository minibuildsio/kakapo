# Kakapo

## Features

```bash
journal Today I went to the zoo!
#   Append "Today I went to the zoo!" to todays journal
```

```bash
journal
#   List all of todays entries 
```

```bash
journal -d "last monday" Today I walked up a big hill
#  Append "Today I walked up a big hill" to last mondays journal
```

```bash
journal -d 2022-07-01
#  List all entries from 1st July 2022
```

## Directory Structure

The journal entries are written to directories structured as below. The default root directory is `~/kakapo` can be overridden by setting $KAKAPO_HOME.

```
📁 ~/
  📁 kakapo/
    📁 journal/
      📁 2022/
        📁 06/
          📔 2022-06-01.md
          📔 2022-06-02.md
          📔 ...
        📁 07/
          📔 2022-07-01.md
```