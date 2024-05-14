```text
#  __  __                           _     _
# |  \/  | ___ _ __ _ __ ___   __ _(_) __| |
# | |\/| |/ _ \ '__| '_ ` _ \ / _` | |/ _` |
# | |  | |  __/ |  | | | | | | (_| | | (_| |
# |_|  |_|\___|_|  |_| |_| |_|\__,_|_|\__,_|
#
```

Mermaid
=======

The diagram engine that lives inside the browser, and on the web.
-----------------------------------------------------------------

It would be convenient if one could say a lot of nice things about mermaid, it is pretty swanky, and
becoming very popular. It's popularity is derived from mermaid's relatively easy means to interface with the web in
a reasonably dynamic way. Traditionally, diagram generation markup languages have their own "translator" that
takes the formatted text and converts it to the graphical representation, otherwise referred to as the
diagram. This graphical representation has to then be added to the web content in a compatible way, this often
involves the generation of a image file. With mermaid, the syntax is included along with the other web
content, and then is translated into a graphical representation inside the user's browser as they view the
webpage. Thus, mermaid circumvents many of the steps normally required to share written diagrams on the web.

The reason one might feel indifferent to mermaid is that except for how the diagram is rendedered, very little
distinguishes it from other diagram generating engines. In fact, when it comes to certain types of diagrams,
mermaid is far behind the rest of the pack, trailing in both complexity and features. The syntax itself is
cumbersome, and does not feel natural or intuitive at all. Several diagram types appear rather bland when
compared to their non-web counterparts.

From currently accumulated experience, the diagram type that stands out the most as being different than what
other diagramming engines provide is the ER diagram. ER stands for "Entity Relationship", and mermaid is the
only diagramming language that appears to support it. 

Then Entity relationship diagram
-----------------------

ER diagrams are denoted with the use of the `ERDiagram` header. The remaining portions of the diagram must be
indented behind this header afterwards. 

### Relationships

(damn "c" key is sticking)

The ER diagram is a series of statements that comprises three subcomponents.

1. Cardinality of A - How many elements of B can be related to A.
2. Identity - Does A confer an identity on B?
3. Cardinality of B - How many elements of A can be related to B.

Cardinality is expressed in two characters, the outer represents the maximum value, and the inner represents
the minimum value. Have a gander at the Cardinality table below:

| Symbol  | Value   |
| ------- | ------- |
| '\'     | One     |
| '0'     | zero    |
| '}'     | Many    |

Now if take this table and apply it as you would to an ER diagram:

| Value (left) | Value (Right) | Meaning |
|--------------|---------------|---------|
| '|o'         | 'o|'          | zero or one |
| '||'         |  '||'        | Exatly one |
| '}o'         | 'o{'        | Zero or more |
| '}|'         | '|{'        | One or more |

Identity is considered to be confered if one entity is reliant on the other entity to exist or occur. In ER
diagrams this is expressed with either a solid or a dotted line. A table to represent this would look like:

| Identity | Non Identity |
| ---------| -------------|
|  `--`    | `..`         |

### Attributes, aliases, and comments

Further complexity can be added to an ER diagram with the use of attributes, aliases, and comments. Where
attributes and comments add definition and characteristics to entities, aliases make writing diagrams much
easier. 

Attributes are expressed inside a pair of curly brackets and follow the `label value` notation.

```mermaid
example {
    string value
}
```

Comments expand upon the attribute framework and add addition definition and clarity.

```mermaid
example {
    string value "comment"
}
```

Aliases are designated outside of a pair of square brackets with the name of the entity placed inside and
encapsulated in a pair of double quotations marks. 

```mermaid
ex["example"] {
    string value "comment"
}
```

And that is how to create a diagram in mermaid.
