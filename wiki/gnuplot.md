```text
#   ____             ____  _       _
#  / ___|_ __  _   _|  _ \| | ___ | |_
# | |  _| '_ \| | | | |_) | |/ _ \| __|
# | |_| | | | | |_| |  __/| | (_) | |_
#  \____|_| |_|\__,_|_|   |_|\___/ \__|
#
```

GnuPlot: The not as boring as you think graphing utility
========================================================

It is funny how at first impression, you might mistakenly disregard something as being boring or something you
believe you will never have to touch in your lifetime. For many of us, this is the case, but if you are
visiting this page, it is because you learned your first impression was wrong. GnuPlot can be terribly boring, 
unless you need to sue it, then it gets pretty swanky.

Crashing your way through gnuplot
---------------------------------

"Crashing" is used in the subtitle of this page for a reason. It is not meant as a substitution for reading
gnuplot's documentation, which is not the most explanative docs in the computational world. GnuPlot's docs are
more akin to a reference guide, than an actual manual to learn by. In these situations, do not forget, the
search engine can be your best friend. For this particular page, the "Search It" approach was used, and the
page created to store the lessons learned from the study that followed.

### Running Gnuplot

There are three ways to run gnuplot. 1) the shell, 2) via a gnuplot script file, or 3) from the builtin
gnuplot shell. Whichever way you prefer, the instructions for plotting are the same. For scripts, comments are
denoted with a `#`, just as with sh-langs. Commands are seperated by a new line, or a `;`. Lastly, just typing
`exit` will allow you to exit the gnuplot shell.

#### Running Gnuplot from the shell

If you are going to run gnuplot from the shell, simply use `gnuplot -e` followed by your plotting instructions
encapsulated int a pair of double or single parenthesis. If you are piping a command to gnuplot, then use
`"-"` or `'-'` relative to the opposite of how your instructions are encapsulated. Remember that in sh-lang
`""` will translate env variables, where in `''` it will not. If you want the output written to a file, as
would be the case when using gnuplot to generate a png file, simply use one of those directional pipe symbols,
i.e. greater than symbol.

#### Using Gnuplot's built-in shell

The only downfall to using the built-in shell to generate your plot is errors might be encountered if you
attempt to pipe the output of another command to the shell, as everything piped to the shell will be
interpreted as plotting instructions and not data. Also if you are going to run the same series of
instructions over and over again, having to re-inter your commands for every run will be quite tedious. Also,
keep in mind the shell is quite limited, and does not come fully loaded with all the conveniences built into
your bash or zsh shell.

##### Accessing data in the gnuplot shell

When using gnuplot's built in shell, the name of the file containing the data you desire to plot is placed in
double quotes after you enter the plot directive. For example, `plot "MY-DATAFILE.dat" w l`. This is how you
access datafile from within the gnuplot shell.

#### Writing Gnuplot script files

As mentioned before, if you are going to run the same series of instructions more than once, using the shell
is not optimal. For this situation it is best to write all your instructions into a gnuplot script file, and
then pipe the output of any command to gnuplot using the gnuplot script file. The `-c` flag allows you to do
this. For example, `some_command > gnuplot -c script_file.p`. Whether there is an officially project
recognized file extension for gnuplot files is unclear, for now, it doesn't appear this is the case.

### Gnuplot Instruction Syntax

Since instructions for gnuplot is for all reasonable purposes a structured markup language, your best chance
at finding out about it is to use [GnuPlot's Reference Documentation](http://gnuplot.info/docs_5.5/Overview.html).
Keeping this in mind, there are a few tidbits to go over. 

#### Format

So far, in this tutorial the terms "Instructions" and "Commands" have been used interchangeably. This is
mentioned, because the author is too lazy to go back and change this. When in reality, Commands given to
gnuplot to generate output come in two forms. 1) One being the graph settings to determine the parameters
that control how the graph looks, what output format will be generated, labeling, and dimensions. 2) The
second being the actual instructions for plotting graphs. 

From our incredibly limited experience, to define a setting one would use the `set` keyword, and as one
would expect to undefine or clear a setting, the `unset` keyword is used. Other setting keywords are `clear`
which clears out any previous plots, and `reset` returns any previous settings to the defaults. Things that
may be defined in the settings are term(output), output(not term), autoscale, title, enabling the key, the
xlabel and the ylabel.

Instructions for plotting graphs begin with the `plot` keyword followed by the source of the data, the type of
data, the format the data is in, and finally, instructions on how the data is to be processed.

### Input and Output

Data to be plotted can either be generated by a function, read from a file, read from a defined datablock
(which we did not cover), or extracted from a previously defined array. If data is be read from a file, then
instructions are provided in the format `plot "<filename>" <data_type> <dataformat>`. There are many data types
and way gnuplot can be told to interpret those datatypes. We are primarily concerned with the binary file
type, which is plotting data that has been compiled into a binary file. As one would expect the organization
of this binary data can come in several formats, but the most commonly encountered format it the `binary_matrix`.

Output for script files is either defined using the `terminal` (`term` for short) keyword, the `output`
keyword or both. If both are provided, the `terminal` or `term` definition needs to precede the `output` keyword.
Failing to place `terminal` before `output` could cause gnuplot to fail to generate the desired plot, as
certain terminal values have additional options that will be overwritten if they follow `output`.
In gnuplot a `terminal` can be any form of output. This would include an actual terminal, or even a png image
file. If one wants to dump the output into the terminal they are using, the keyword `dumb` is used to
designate the user wants to dump the graph into the termina. If one wants to generate an image, either using
"png" or "gif", please be sure to set the size of the image desired. This will help to prevent generation of
wee-little tiny images for plots with lots of data.

### Creating a working example

Here is a script file written to serve a particular task. I do not reccommend using it, but more than likely
many of the keywords are often repeated. 

```gnuplot
# First, change the terminal setting
set term dumb size 120, 30
# Clear up any previously existing plots
clear
reset session
# Now configure plot settings
set autoscale
unset key
# Configure some "niceties"
set title "Frequency Spectrum"
set xlabel "Frequency (Hz)"
set ylabel "Power (dB)"
# Set up the plot
plot "$DATA_FILE" w l
```

### Ploting more than one figure per frame

Gnuplot can plot more than one figure in a frame ( like subplot in matlab ) i.e., try:

``` gnuplot
      set multiplot;                          # get into multiplot mode
      set size 1,0.5;  
      set origin 0.0,0.5;   plot sin(x); 
      set origin 0.0,0.0;   plot cos(x)
      unset multiplot                         # exit multiplot mode
```

### Script Template File

Here is a little template file you can use as a starting point for writing gnuplot scripts. This file is
courtesy of Henri P. Gavin of Duke University. 

``` gnuplot
# File name: save.plt - save a Gnuplot plot as a PostScript file
# to save the current plot as a postscript file issue the commands:
#  gnuplot>   load 'saveplot'
#  gnuplot>   !mv my-plot.ps another-file.ps
set size 1.0, 0.6
set terminal postscript portrait enhanced mono dashed lw 1 "Helvetica" 14 

# Change below to match desired output. AKA: my-plot.gif for gif, and my-plot.png for png
set output "my-plot.ps"

replot
set terminal x11
set size 1,1

#      set terminal postscript {<mode>} {enhanced | noenhanced}
#                              {color | colour | monochrome}
#                              {blacktext | colortext | colourtext}
#                              {solid | dashed} {dashlength | dl <DL>}
#                              {linewidth | lw <LW>}
#                              {<duplexing>}
#                              {"<fontname>"} {<fontsize>}


#     set terminal gif {transparent} {interlace}
#                       {tiny | small | medium | large | giant}
#                       {size <x>,<y>}
#                       {<color0> <color1> <color2> ...}

#     set terminal png
#             {{no}transparent} {{no}interlace}
#             {tiny | small | medium | large | giant}
#             {font <face> {<pointsize>}}
#             {size <x>,<y>} {{no}crop}
#             {{no}enhanced}
#             {<color0> <color1> <color2> ...}
```

### Another Functional example

For plotting data captured from a software defined radio, it can be quite easy to create a plot if the data is
formatted directly. 

``` gnuplot
reset session
unset key
set autoscale
set title "Frequency Spectrum"
set xlabel "Frequency (Hz)"
set ylabel "Power (dB)"
set term png size 1280, 960; set output "spectrum.png"
plot "$DATA_FILE" w l
```

### Misc Odds and Ends

Here are a few means to customize the plotting:

``` gnuplot
      Create a title:                  > set title "Force-Deflection Data" 
      Put a label on the x-axis:       > set xlabel "Deflection (meters)"
      Put a label on the y-axis:       > set ylabel "Force (kN)"
      Change the x-axis range:         > set xrange [0.001:0.005]
      Change the y-axis range:         > set yrange [20:500]
      Have Gnuplot determine ranges:   > set autoscale
      Move the key:                    > set key 0.01,100
      Delete the key:                  > unset key
      Put a label on the plot:         > set label "yield point" at 0.003, 260 
      Remove all labels:               > unset label
      Plot using log-axes:             > set logscale
      Plot using log-axes on y-axis:   > unset logscale; set logscale y 
      Change the tic-marks:            > set xtics (0.002,0.004,0.006,0.008)
      Return to the default tics:      > unset xtics; set xtics auto
      set the comment character        > set datafile commentschar "#%"
```


