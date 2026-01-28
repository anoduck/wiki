```text
#  _____ ____ ___ ____
# | ____| __ )_ _| __ )
# |  _| |  _ \| ||  _ \
# | |___| |_) | || |_) |
# |_____|____/___|____/
#
```

# Ebib: A BibLaTeX database manager for references.

> [!hint] There is also a page specifically dedicated to BibLaTeX [here](biblatex).

An Emacs package that offers a kickass way to manage all of those damn references, in a well designed interface.

## What is Ebib?

Since the eighties individuals who work in the sciences have relied on a markup language called Bibtex, to manage
all of their research references inside of a "database". Bibtex is not a database in the formal sense of the
word, but rather, bibtex allows you to record all your reference information as a structured file. It has been
around a long time, and has grown into the defacto standard for managing research references in the sciences.
The markup language also has changed very little since it's inception, until a reimplementation came around in
LaTeX. This reimplementation is BibLaTeX, and it differs only minutely from Bibtex, making it compatible with
most programs that work with bibtex.

The kicker is the number of references used in research can quickly grow with time, and become difficult to
manage in raw markup form. Also, manual input of data, and correcting formatting errors is quite tedious,
making the use of an interface quite convenient. This is where Ebib enters the room. Emacs has long been
favored by the scientific community, and providing an easy to use interface to bibtex only seems like the
natural progression of things.

## KeyBinds

Unlike other topics in this wiki, which are organized by operational topic, this page will be organized as a
cheatsheet, and list keybinds first.

### Navigation Keys

|       Keys        |   Label    |         Description         | Alt Label |      Alt Desc.      |
| :---------------: | :--------: | :-------------------------: | :-------: | :-----------------: |
|    `M-x ebib`     |    Ebib    |   Open up the Ebib Index    |           |                     |
|        `q`        |    quit    |          Quit Ebib          |   quit    |    Quit Editing     |
|        `z`        | background | Drop Ebib to the background |           |                     |
|        `o`        |    Open    |   Open a new bibtex file.   |           |                     |
|        `c`        |   Close    |    Close the current DB     |           |                     |
|       `up`        |     Up     |      Move up one entry      |    Up     |  Move up one field  |
|        `p`        |     Up     |      Move up one entry      |    ""     |         ""          |
|       `C-p`       |     Up     |      Move up one entry      |    ""     |         ""          |
|      `down`       |    Down    |     Move down one entry     |   Down    | Move Down one field |
|        `n`        |    Down    |     Move down one entry     |    ""     |         ""          |
|       `C-n`       |    Down    |     Move down one entry     |    ""     |         ""          |
|        `b`        |   10x Up   |     Move ten strings up     |   Prev    |    Previous set     |
|      `PgUp`       |   10x Up   |     Move ten strings up     |    ""     |         ""          |
|      `Space`      |  10x Down  |    Move ten strings down    |   Next    |      Next Set       |
|      `PgDn`       |  10x Down  |    Move ten strings down    |    ""     |         ""          |
|        `g`        |    Head    |    Move to first string     |   First   |     First Field     |
|      `Home`       |    Head    |    Move to first string     |    ""     |         ""          |
|        `G`        |    Tail    |     Move to last string     |   Last    |     Last Field      |
|       `End`       |    Tail    |     Move to last string     |    ""     |         ""          |
|        `e`        |    edit    |    Edit a @String value     |           |                     |
|        `d`        |   Delete   |      Delete a @String       |           |                     |
|        `c`        |    Copy    |       Copy a @String        |           |                     |
|        `x`        |   Export   |      Export a @String       |           |                     |
|        `X`        | Export All |     Export all @Strings     |           |                     |
|      `[1-9]`      |  Jump DB   |       Jump between DB       |           |                     |
| `left` or `right` |  Next DB   |   Jump to Next or Prev DB   |           |                     |
|        `j`        | entry jump |       Jump to entry X       |           |                     |
|      `C-u j`      | entry jump |   Jump to X in Current DB   |           |                     |
|       `C-b`       | Hist Back  |  Move backwards in History  |           |                     |
|       `C-f`       | Hist Forw  |  Move forwards in History   |           |                     |
|        `=`        | Def. Sort  |      Def. Sort toggle       |           |                     |
|    `<` or `>`     | Sort Cols. |   Change Sorting on cols.   |           |                     |
|        `j`        |   Search   |  Search for Specific Entry  |           |                     |


### Modification Keys

|  Keys   |   Label   |      Description       |
| :-----: | :-------: | :--------------------: |
|   `a`   |    Add    |       Add Entry        |
|   `d`   |  Delete   |      Delete Entry      |
|   `k`   |   Kill    |       Kill Entry       |
|   `y`   |   Yank    |       Yank Entry       |
|  `C-e`  |   Copy    |   Copy to Kill Ring    |
|   `m`   |   Mark    |       Mark Entry       |
| `C-u m` |  UnMark   |      UnMark Entry      |
|   `e`   |   edit    |       Edit entry       |
|   `r`   |  Special  |      Mark Special      |
|   `s`   |  String   |     Insert @String     |
|   `v`   |   View    |    View Full Buffer    |
|   `m`   | Multiline | Insert Multiline Value |
|   `c`   |   Copy    |       Copy entry       |
|   `d`   |  Delete   |      Delete Entry      |
|   `h`   |  Hidden   |     Toggle Hidden      |
|   `w`   |   Write   |    Save DB to Name     |
|   `s`   |   Save    |        Save DB         |
|   `x`   |  Export   |       Export DB        |
|  `S-c`  | CrossRef  | Follow CrossReference  |
|   `i`   |  Insert   |    Insert Reference    |
|   `&`   |  Filter   |     Create Filter      |

