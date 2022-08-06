# Kakapo

## Dashboard

```bash
dashboard fitness

┌─ Steps by month ────────────┐
│                ╷            │
│   Month        │ Steps      │
│ ╶──────────────┼──────────╴ │
│   2022-08      │ 10321      │
│   2022-07      │ 550139     │
│   2022-06      │ 556459     │
│   2022-05      │ 465849     │
│   2022-04      │ 510721     │
│   2022-03      │ 501969     │
│                ╵            │
└─────────────────────────────┘
```

## Journal

```bash
# Append "Today I went to the zoo!" to todays journal
$ journal Today I went to the zoo!

# List all of todays entries 
$ journal

# Append "Today I walked up a big hill" to last mondays journal
$ journal -d "last monday" Today I walked up a big hill

# List all entries from 1st July 2022
$ journal -d 2022-07-01
```

## Directory Structure

The journal entries are written to directories structured as below. The default root directory is `~/kakapo` can be overridden by setting $KAKAPO_HOME.

```
📁 ~/
  📁 kakapo/
    📁 dashboards/
      📔 fitness.yaml
    📁 data/
      📔 steps.csv
      📔 caffeine.csv
    📁 journal/
      📁 2022/
        📁 06/
          📔 2022-06-01.md
          📔 2022-06-02.md
          📔 ...
        📁 07/
          📔 2022-07-01.md
```