```text
#  ____  ____  ____     ____               _
# / ___||  _ \|  _ \   / ___|_ __ __ _ ___| |__
# \___ \| | | | |_) | | |   | '__/ _` / __| '_ \
#  ___) | |_| |  _ <  | |___| | | (_| \__ \ | | |
# |____/|____/|_| \_\  \____|_|  \__,_|___/_| |_|
#
#   ____
#  / ___|___  _   _ _ __ ___  ___
# | |   / _ \| | | | '__/ __|/ _ \
# | |__| (_) | |_| | |  \__ \  __/
#  \____\___/ \__,_|_|  |___/\___|
#
```

## The SDR Crash Course

Everything you ever wanted to know about SDR, if only the bastard had finished the wiki page on it. ROFL...

Having no background in engineering, electronics, radio technology, and having learned everything I know about
computers on my own; entering the world of radio frequencies has been quite an uphill challenge.

>[!NOTE]
>It would be wise if time was taken to outline what is supposed to go in this section.

### Modulation

These definitions and explanations are written in layman's terms without the use of any jargon what-so-ever.
They are not precise, but are meant to be understood by someone who has no experience or knowledge in radio
technology. That, and it is late. I am tired, so deal with it. 

1. WaveForm - the shape of an electronic signal when graphed as a function of time.
2. Carrier Signal - Is a fancier word for the waveform of an electronic signal.
3. Modulation - is the process of variating the waveform.
4. Amplitude Modulation - variating the waveform by amplitude.
5. Frequency Modulation - variating the waveform by frequency (i.e. Pitch for musically minded)
6. Angle Modulation - is based on varying the frequency of a waveform. Angle Modulation is comprised of both
   FM and Phase Modulation.
7. Phase Modulation - is where a modulated waveform is modulated againy by overlayering a secondary modulation on top of
   it. So basically a doubly modulated waveform.

__Modulation occurs in two ways:__
1. Continuous Wave
2. Pulse Wave

### Performing a basic scan of the radio spectrum

Whenever you find your self in a new and unfamiliar place, at one point or another, you will have to find out
where things are located at. In realm of rf technology this is performed by scanning the available radio
spectrum to see what is out there. Performing a spectrum scan is an important beginning step in every radio
endeavor, not only because it allows you to discover what is out there, it provides important information of
signals in the area that could be the source of interference.

#### Requirements to perform a scan

Before performing your scan you will need a few things, many of these are quite obvious, regardless the list
is provided below.

- A software defined radio(sdr) - Any of the many commonly found SDR platforms will work, but it will effect
  the software used to perform the scan. RTL-SDR has the most variety of software available, and is probably
  the best choice for the initial scan.
- A wideband antenna to scan with. - This might seem obvious, but it is important to recognize antennas are
  designed by what frequency ranges they are intended to be used with. The frequency range of the antenna
  helps to determine the antenna shape and size. Discone antennas are also referred to as "scanning" antenna,
  this is because of the wide bandwidth they can recieve (but not transmit), so they are optimal for the job,
  but not required. A simple dipole antenna is sufficient enough to do the job, as long as it's length is
  compatible with the desired range. This can be calculated with a dipole antenna calculator, which can be
  found by searching google.
- Appropriate cabling, we have already delved into the world of coaxial cabling in another post, so it is just
  important to keep this in mind.
- Computer - Nothing special needed here, just any computer running Linux will do, as long as you have all the
  needed dependencies for the software installed.
- [rtl-power-fftw](https://github.com/AD-Vega/rtl-power-fftw) - this will be the software used to perform the scan,
- and it is available on github. Ensure you have dependencies including libfftw3-dev.

#### Performing your scan

The scan itself is performed within a matter of minutes, as the fftw3 library is very fast and purpose built
for running these algorithms. The only downside to the software we are going to use is it uses a lot of
command line options rather than a configuration file, so it might be confusing if your not familiar with the
command line flags. A bonus of using this particular piece of software is it generates output in a format that
was intentionally designed to be compatible with gnuplot, which means it can easily generate graphs directly
from the command line.

Below is the proverbial "hail mary" for rtl_power_fftw. It runs rtl_power_fftw to scan frequencies from 100Mhz
to 1000Mhz (or 1Ghz), averages the result of 100 scans through the spectrum, and generates a nice graph for
you.

```bash
rtl_power_fftw -b 512 -d 0 -f 100M:1G -n 100 |\
gnuplot -e "set terminal png size 1280, 960; set output 'new-spectrum.png'; set title 'Frequency Spectrum'; set autoscale; set xlabel 'Frequency (Hz)'; set ylabel 'Power (dB)'; plot '-' w l;"
# ----------------------------
# A Simpler approach would be
# ----------------------------
rtl_power_fftw -f 1420405752 -n 100 -b 512 |\
   gnuplot -e "set term png; unset key; plot '-' w l" >plot.png
```

Just remember on that last one, it is a "w" as in "willow" followed by an "l" as in "Lion". Also notice,
rather than setting the output with `set output 'my-graph.png'`, it simply redirects the output to a png file
as abreviated in trash code `gnuplot "..." >my-graph.png`.

If for some reason you decide not to forgo the use of gnuplot at this time, then you will need to redirect the
output to a `dat` file for use later.

```bash
rtl_power_fftw -b 512 -d 0 -f 100M:1G -n 100 >my-data.dat
# And when your ready to process it.
gnuplot -e "set terminal png size 1280, 960; set output 'new-spectrum.png'; set title 'Frequency Spectrum'; set autoscale; set xlabel 'Frequency (Hz)'; set ylabel 'Power (dB)'; plot 'my-data.dat' w l;"
```

There exists a third option, which is optimized for saving space, and that is to generate two files from the
scan a binary file for the data results of your scan, and a matrix file containing the info needed to extract 
the data from the binary file. This is done by using the `-m` flag, but it is important to keep in mind that the
binary output will not be compatible for use with gnuplot. Being brutally honest, we are still unsure quite
what to do with it.

```bash
rtl_power_fftw -b 512 -d 0 -f 100M:1G -n 100 -m my-data
```
