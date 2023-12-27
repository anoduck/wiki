```text
#  __  __ _____ _   _____
# |  \/  | ____| | |_   _|
# | |\/| |  _| | |   | |
# | |  | | |___| |___| |
# |_|  |_|_____|_____|_|
#
```

## Melt

Melt is a command line video editing framework. In other words, it basically is the command line interface to
the python MLT framework. Verbatim, MLT is "an open source multimedia framework, designed and developed for television broadcasting."
Which is a fancy way of saying it does a lot of shit, so by solely using the command line, it is a garuantee you
won't have a clue in the world to what your actually doing. In fact, right below the introduction it states,
"The easiest way to try out and learn MLT is by using shotcut." Sadly, for those of us broke hackers with a
cheap vidcard on their server, this isn't quite an option. So, please forgive me as I try to make sense of
this gawd forsaken framework.

### Concepts

No lie, I almost always skip over any section that attempts to explain abstract concepts, but this time it is
really import. So, make sure you read these definitions, or you will probably get lost.

#### Producers

Interestingly, Linux Magazine decided to not dive into explaining the concept of "producers" in the melt 
framework, and after reading the melt framework, I nearly concure. Producers are things that produce
audio/video output. In almost all cases this would be a video file, but if desired can also be a input device,
a audio file, a text file, a image, or even a melt specific script.

Where things get rather confusing is the melt documentation also uses the term 'clip', for the sake of our
desired outcome we are going to assume that 'clip' and 'producer' are synonymous. As a 'clip' is a type of
producer, it just appears to be limited by spectrum as far as variety inclusivity is concerned.

#### Properties

Properties are additional statements in commands that define a characteristic of whatever precedes them. All
services have properties, except consumers. AND groups apparently can have properties too. This is not
clarified in the documentation, and is assumed to be the case from observation of the example employed. Both
`in=` and `out=` seem to be the two most commonly used properties.

#### Groups

The concept of "groups" is not emphasized at all in the melt documentation, but it is a pretty damn important
one. Groups allow you to "group" multiple producers together and apply actions to the entire "group" of files.
Just as important, groups allow you to exclude or "shed" properties of other files or actions from being applied
to a specific file or sets of files. Ever "producer" following a `-group` tag will be considered a part of that 
group, until the next `-group` flag is encountered.

#### Services

Services do shit, and is where all the fancy shit happens. All services generate output in one form or
another, except consumers. Consumers do not produce any output, because... obviously... they consume whatever the 
input is. The following is a list, I shamelessly ripped off of the Linux Magazine tutorial of melt. It shows
the the different types of services provided by melt and provides a short description.

```text
    * "consumers": The application or utility that plays clips, such as XML or JACK. If no consumer is specified, the default is SDL.
    * "filters": Frame modifiers that change how audio or visual are displayed. No filter affects the files – only how they are displayed. Examples include saturation, volume, and watermark.
    * "producers": Software playback libraries or components, or else wrappers for hardware drivers.
    * "transitions": How playback moves from one clip to another – for instance, luma, a change in brightness achieved by specifying a grayscale bitmap, or matte, a brief overlay of the two clips. When adding a transition to a command, use -mix LENGTH to set its duration, followed by -mixer TRANSITION.
    * "profiles": How a clip is processed, such as the frame resolution and scan rate. If not specified, the characteristics of the clips themselves are used. Beginners can generally ignore these services.
    * "presets": Playback options and formats. Again, beginners might want to ignore these services.
    * "formats": Audio, video, and audiovisual formats supported by Melt. Formats can be specified to force Melt to use a clip when it is having trouble identifying its format. Many listed formats are likely to be known only by experts.
    * "audio_codecs": Audio formats supported by Melt. Use this setting with -query rather than formats to reduce the size of the list displayed.
    * "video_codecs": Video formats supported by Melt. Use this setting with -query rather than formats to reduce the size of the list displayed.
```

To get a list of all the services available by type, use `melt -query $TYPE`, replacing `$TYPE` with the the
type you wish to inquire about. To get more information about a specific service use `melt -query $TYPE =
$SERVICE`, replacing `$TYPE` with the type the service is listed under, and replace `$SERVICE` with the
service you want to know more about.

As stated in the list above, there are several several types of services that scrappy hackers like myself need
not bother themselves with. These are formats, presets and profiles. 

#### Commands

So now we arrive at the business part. Since we have already discussed using `group` and `query`, there is no
need to review those again, but we do need to cover the other basic commands and syntax to provide a basic
understanding of Melt. 

First, to play a file using melt no option is needed. Just use `melt file.mp4`.

- `in=` and `out=`: These two statements are properties, and they determine, which frames the command applies to. Naturally `in`
  meaning begin or start, and `out` meaning end or finish. So, `melt in=0 out=25 video.mp4` will only play the
  first 25 frames of a file.
- `-serialise`: Perhaps the most important flag in melt. When added to the end of a melt command, `serialise filename.melt`
  will save the command to a file that later can be used to reperform the command in its entirety. To
  reperform the saved action use the file as if it is a producer. To add another clip to the process of
  reperforming a previous command, use the `-track` flag. (See `melt -query producer=melt_file` for more
  information.)
- `-filter`: Applies a filter service to the preceding group or producer. For example, `melt vidoe.mp4 -filter
  grayscale` will apply the grayscale filter to the preceding video file. If you are wanting the same result
  from a group of files, it is important to "shed" the filter from properties that might be included as part
  of the producers included in the group. So your command would look like, `melt -group video1.mp4 video2.mp4
  -group -filter grayscale`.
- `-attach`: is not explained at length in either the Linux Magazine tutorial or the melt documentation, but
  it is assumed `-attach` allows you to perform a filter service to solely a specific file. This is done by
  defining a name property for the group that includes the desired producer. 
  For example, `melt -group video1.mp4 video2.mp4 -group name=myvideo video3.mp4 -attach filter:grayscale
  name=myvideo`. This will only apply the filter to the third video, and leave the other video untouched.
- `-progress`: Will display a progress bar of the file playing. 
- `-hide-*`: Allows you to hide things, such as audio, video or tracks.
- `-mixer`: Allow you to create swanky transitions.
- `-blank` and `-track`: Are completely out of the scale of this wiki page. So, see the [melt docs](https://www.mltframework.org/docs/melt/) for more information.
- `-consumer`: is the damn flag you use to fucking finally write everything to file. The example provided is
  more of a pain in the ass than I would want to use, `-consumer avformat:output.avi acodec=libmp3lame vcodec=libx264`, so we are just going to assume `-consumer myfile.mp4` works just as well.

### Melt Help Output

To make life easier, lets just add the output to `melt --help`.

```bash
Usage: melt [options] [producer [name=value]* ]+
Options:
  -attach filter[:arg] [name=value]*       Attach a filter to the output
  -attach-cut filter[:arg] [name=value]*   Attach a filter to a cut
  -attach-track filter[:arg] [name=value]* Attach a filter to a track
  -attach-clip filter[:arg] [name=value]*  Attach a filter to a producer
  -audio-track | -hide-video               Add an audio-only track
  -blank frames                            Add blank silence to a track
  -chain id[:arg] [name=value]*            Add a producer as a chain
  -consumer id[:arg] [name=value]*         Set the consumer (sink)
  -debug                                   Set the logging level to debug
  -filter filter[:arg] [name=value]*       Add a filter to the current track
  -getc                                    Get keyboard input using getc
  -group [name=value]*                     Apply properties repeatedly
  -help                                    Show this message
  -jack                                    Enable JACK transport synchronization
  -join clips                              Join multiple clips into one cut
  -link id[:arg] [name=value]*             Add a link to a chain
  -mix length                              Add a mix between the last two cuts
  -mixer transition                        Add a transition to the mix
  -null-track | -hide-track                Add a hidden track
  -profile name                            Set the processing settings
  -progress                                Display progress along with position
  -query                                   List all of the registered services
  -query "consumers" | "consumer"=id       List consumers or show info about one
  -query "filters" | "filter"=id           List filters or show info about one
  -query "links" | "link"=id               List links or show info about one
  -query "producers" | "producer"=id       List producers or show info about one
  -query "transitions" | "transition"=id   List transitions, show info about one
  -query "profiles" | "profile"=id         List profiles, show info about one
  -query "presets" | "preset"=id           List presets, show info about one
  -query "formats"                         List audio/video formats
  -query "audio_codecs"                    List audio codecs
  -query "video_codecs"                    List video codecs
  -quiet                                   Set the logging level to quiet
  -remove                                  Remove the most recent cut
  -repeat times                            Repeat the last cut
  -repository path                         Set the directory of MLT modules
  -serialise [filename]                    Write the commands to a text file
  -setlocale                               Make numeric strings locale-sensitive
  -silent                                  Do not display position/transport
  -split relative-frame                    Split the last cut into two cuts
  -swap                                    Rearrange the last two cuts
  -track                                   Add a track
  -transition id[:arg] [name=value]*       Add a transition
  -verbose                                 Set the logging level to verbose
  -timings                                 Set the logging level to timings
  -version                                 Show the version and copyright
  -video-track | -hide-audio               Add a video-only track
For more help: <https://www.mltframework.org/>
```

### References

- [Linux Magazine Melt Tutorial](https://www.linux-magazine.com/Issues/2018/206/Command-Line-Melt)
- [Melt Manual](https://www.mltframework.org/docs/melt/)
