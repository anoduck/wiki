```text
#  _          _
# | |    __ _| |_ _____  __
# | |   / _` | __/ _ \ \/ /
# | |__| (_| | ||  __/>  <
# |_____\__,_|\__\___/_/\_\
#
```

Latex
======

This is not an introductionary page to latex, because we haven't quite figured it out for ourselves,
and to be honest it is much more robust than most modern markup languages out there. In short, Latex
is specifically designed for document creation and processing. Latex is also old as dirt, and has been around
since the time of dinosaurs (well...close enough). The basic workflow is you creating a document in latex, and
then execute latex to process the document into some other document format. Where it get's tricky is Latex has
an abundance of packages, these packages introduce features, and in order to implement these features the
packages have to implement new sytax. Sometimes this syntax conflicts with other packages, so things can get
quite unpleasant real quick.

Layout of a latex document
---------------------------

No time to wax philosophical here, the layout of latex documents is pretty basic.

``` latex
% This is a comment in latex.
% Below is the "preamble", it's where you setup the rest of your document.
% First real line declare's the file is a document, followed by the font size, and document class.
\documentclass[12pt]{article}
% Next you setup your packages for use.
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\geometry{letterpaper, margin=1in}
\usepackage{fancyhdr}
% The last package you load is your font. This prevents it from being written over.
\usepackage{noto}
% The you begin your document here.
\begin{document}

You can write some shit down here if you want.


% This is where you end the file, like so:
\end{document}
```

Latex Syntax
-------------

As things move along, I will add information here to remember.

### Always output today's date inf format `MONTH D, YEAR`

Very simply, all this requires is `\today`.

### Only output the name of today.

So if you do not want the full date string, and simply want to output what day today is, then it get's a
little trickier. You will need to add a package as well.

``` latex
\usepackage{datenumber}

Today is \datedayname.
```

### Output the date thirty days from now

Similarly, you will need to add a different package and the appropriate syntax.

Don't worry about packages slowing down latex, the majority are built in.

```latex
\usepackage{advdate}

Vacation is continued until \AdvanceDate[30]\today.
```

### Combining files into one document

There is a package called "combine" that can do this, but for this example we will just use the keywork
"subfile".

```latex
% main.tex

\documentclass{report}
\usepackage{subfiles}

\begin{document}
\tableofcontents
\subfile{chapter1.tex}
\end{document}

% chapter1.tex

\documentclass[main.tex]{subfiles}
\begin{document}
Here comes some text
\end{document}
```


