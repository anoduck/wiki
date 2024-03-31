```text
#  ____  _             _   _   _ __  __ _
# |  _ \| | __ _ _ __ | |_| | | |  \/  | |
# | |_) | |/ _` | '_ \| __| | | | |\/| | |
# |  __/| | (_| | | | | |_| |_| | |  | | |___
# |_|   |_|\__,_|_| |_|\__|\___/|_|  |_|_____|
#
```

## Plantuml

Plantuml is first and foremost a markup language that enables the quick creation of diagrams through
processing textual files. It is extremely easy to learn, and very powerful... well as powerful as a diagram
processing language can be. After all, it isn't curing cancer.

The best place to find out more knowledge, or anything about [plantuml is the website.](https://plantuml.com)

The main purpose for creating this page was to provide some quick references for commonly used features of
plantuml. If you must, you can call it a cheatsheet of sorts.

### Diagram Types

If you have ever created a diagram before, you generally need to know what type of diagram you are trying to
create before going about and created one. Plantuml offers several types, and if you do not see what you are
looking for, understand that the type of diagram maybe titled something different from what you are looking
for.

**The different types for diagrams in Plantuml are:**

- Sequence
- Use Case
- Class
- Activity
- Component
- State
- Object
- Deployment
- Timing
- Regex
- Network
- Wireframe
- Archimate
- Gantt
- Chronoloy
- MindMap
- WBS
- Json
- Yaml

#### Activity Diagram

The Activity diagram is one of diagram types offered by Plantuml, another name for it could be "Process",
which is oddly always what I mistakenly think it is. As usual, plantuml requires a `@startuml`, and a
`@enduml` to denote where the markup language begins and ends. Generally, there two are paired with `start`
and `stop` or `end`, although these two are not required, and sometimes need to be left out. Element labels are denoted
with a `:` at the beginning, and a `;` at the end.

##### Keywords

| Keyword           | type        | Description | Intermediary Statement | Closing Statement | Example |
| ----------------- | ----------- | ----------- | ---------------------- | ----------------- | ------- |
| switch            | Conditional |             | case                   | end switch        |         |
| if ... then       | Conditional |             | else                   | endif             |         |
| fork              |             |             |                        | end fork          |         |
| while             | Loop        |             |                        | endwhile          |         |
| kill, stop, break |             |             |                        |                   |         |

#### Network Diagrams

Network Diagrams in Plantuml take on a form very similar to Json. As with all plantuml diagram files, the
block of code containing the diagram is nested between a `@startuml` and a `@enduml`. Within a network diagram
the entire diagram is nested within a `nwdiag` label followed by two curly brackets `{` and `}`. Networks are
declared by the `network` keyword, followed by the name of the network, and everything pertaining to that
network nested within a pair of curly brackets. Addresses are designated with the `address` keyword, and
so forth. Just as with Json, lines of code can be commented out with `/` and `/` respectively. 

##### Keywords

| Keyword | Description                | requires brackets   | example |
| ------- | -------------------------- | -----------------   | ------- |
| nwdiag  | encases the entire diagram | yes, content nested |         |
| network | defines a network block    | Yes, content nested |         |
| address | defines ip address         | No, quotes          |         |
| group   | defines group              |                     |         |

#### Deployment Diagrams

Deployment diagrams are whole other beast than both network and activity diagrams, as they can display very
complex relationships in an extremely easy manner. Except for the standard `@startuml` and `@enduml`, they
primarily consist of keyword / value pairs. The kicker is the cornicopea of keywords available for use. These
keywords represent a variating degree of objects, items, and stuff. A line is then used to demonstrate the
relationship. 

For more info go to the [plantuml website](https://plantuml.com/deployment-diagram) for a better demonstrations.

#### Class Diagrams

Plantuml's class diagram schema is intended to be intuitive and multilingual, and incorporates features any
programmer would be comfortable with. Yet, from the perspective of someone who did not go the traditional
route and learn Java or C++ in a formal setting, many of these features are not familiar at all, and possess
either obscure or ambiguious meaning. So for this reason, some jargon needs to be sorted.

##### Class Types

When reading the Plantuml documentation on class diagrams, the first thing one might scratch their head at is
the need to distinguish different class types. From personal experience this was encountered first learning
Zig, but let's not digress.

| Keyword        | Description                                                |
| -------        | -----------                                                |
| abstract class | A class that is purely virtual in existence?               |
| static class   | A fuzzy class that does not render clearly on the monitor? |

``` plantuml
@startuml example diagram
class Example Class {
    +{static} int something
    -{abstract} void method()
    ~void packagePrivateMethod()
    #{abstract} char protectedMethod(int param)
    }
@enduml
```

### Themes

Plantuml provides several "themes" that bring color, style, and overall pazazz to the diagram. To find the
theme that best suits you, head over to the [theme gallery](https://the-lum.github.io/puml-themes-gallery/).

### Style

Plantuml also allows customizing the style of the diagram to one's taste or as needed. Similar to css in an
html file, plantuml uses the flags `<style>` and `</style>` to define the beginning and end of style
configurations. The target characteristic is followed by a pair of squigly brackets, and contained within is
the designation of style parameters. Styling differs according to diagram type and preselected theme. So,
please checkout the plantuml site on how to do this properly.


