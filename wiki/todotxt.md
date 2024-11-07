```todotxt
#  _            _       _        _
# | |_ ___   __| | ___ | |___  _| |_
# | __/ _ \ / _` |/ _ \| __\ \/ / __|
# | || (_) | (_| | (_) | |_ >  <| |_
#  \__\___/ \__,_|\___(_)__/_/\_\\__|
#
```

todo.txt
--------

Todo.txt is a simple task management system created by some Italian female programmer. Her name is not nearly as important as
her genius at developing a rather simple system to use an ordinary txt file to manage tasks. Below is an example.

```todo.txt
[ ] (A) 2024-10-19 extremely high priority task +example @wiki due:2024-10-19
[ ] (B) 2024-10-20 high priority task +example +another @terminal
[ ] (C) 2024-10-23 moderate priority task +moderate @office
[ ] (D) 2024-10-31 low priority task +low @home
```

(In a drab and monotone voice) And now it is once again time for one of our syntax tables... (unenthusiastic)
Hooray...

| Markup       | Description     | Required    |
| --------     | -------------   | ----------  |
| `[ ]`        | State Marker    | Recommended |
| `(A)`        | Priority Marker | Recommended |
| 1. `{DATE}`  | Completion date | Recommended |
| 2. `{DATE}`  | Creation Date   | Recommended |
| Text Content | Task Content    | Yes         |
| `+Text`      | Project Tag     | Yes         |
| `@Text`      | Contextual Tag  | Yes         |
| `due:{DATE}` | Due Date        | Recommended |

- https://github.com/todotxt/todo.txt

### Rules for Tasks awaiting completion

1. If priority exists, it ALWAYS comes first
2. Creation date follows the priority, separated by a space.
3. Context and Project tags can appear anywhere after priority and creation date

### Rules for Tasks which have been completed

1. Completed tasks begin with a lowercase "x".
2. The date the task was completed immediately follows the "x".

