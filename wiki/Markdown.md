```text
#  __  __            _       _
# |  \/  | __ _ _ __| | ____| | _____      ___ __
# | |\/| |/ _` | '__| |/ / _` |/ _ \ \ /\ / / '_ \
# | |  | | (_| | |  |   < (_| | (_) \ V  V /| | | |
# |_|  |_|\__,_|_|  |_|\_\__,_|\___/ \_/\_/ |_| |_|
#
```

Markdown
========

The only reason this page exists is due to several new tags recently added to Github Formatted Markdown,
and for the life of me, I am forgetting them every damn time.

[John Gruber](https://daringfireball.net/projects/markdown) created markdown in 2004, with assisstance from
Aaron Swartz. The original processor for markdown was `Markdown.pl` which, as you can tell, was written in
Perl.

In 2012, a group of blokes attempted to "standardize" markdown, but by 2014, Gruber officially voiced his
objection to the effort. Notably, Gruber was not a member of this group of blokes, and was not advised on how
it should be standardized. Principally due to Gruber's objection, the group changed the name of their
standardized version to "commonmark". So, commonmark and markdown are practically the same.

Variance
--------

You would think that something as dead simple as markdown would cause developers to conform to the same
"standard" set of markup tags, but you would be wrong. Truthfully, there is quite an absurd amount of variance
in what markdown tags to use, which makes use of a markdown linter rather absurd as well. As it
turns out, just about each of the bloody damn markdown processors has it's own "format" variance. Nonetheless,
the only one that really matters is the Github Markdown Format, as it is the most commonly used.

Github Formatted Markdown
-------------------------

The specification for Github formatted Markdown is a moving target, and with the rise of users adopting additional
tags from other markdown implementations, Github eventually adopts them as well.

The two new-ish tags which are difficult to remember are footnotes and callouts.

### Footnotes

To use footnotes in mardown, you create a footnote reference at the bottom of your page by adding a `- [^N]: $REFERENCE`, where
`N` is the reference number and `$REFERENCE` is the reference to use. The in your text add the flag for the
reference by adding `[^N]` at the end of the sentence you would like the reference to point to. (N being the
number of the reference.)

```text
This is some damn sentence that you would like to add a reference to. [^1] Equivocally as dull and boring, this is
another sentence that you would like to add a reference link to. [^2]

- [^1]: This would be a non-link footnote reference.
- [^2]: [This would be a linked reference](https://example.org)
```

### Callouts

Callouts are a recent addition to github, except Github does not refer to them as "callouts", Github refers to
them as "Alerts". The important thing to know is that Github only supports a limited set of "alerts", and
anything else will not work. They are:

- NOTE
- TIP
- IMPORTANT
- WARNING
- CAUTION

Anything else besides these five will not fly on the hub of git. The result of their use is a nice boxed
announcement. Alerts and the alert message body should always begin with a greater than sign `>`. The alert
type is defined inside of a pair of square brackets and preceded by an exclamation mark `>[!NOTE]`. The
message body of the alert begins on the next line and is preceded with a `>` sign.

```text
> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
```


