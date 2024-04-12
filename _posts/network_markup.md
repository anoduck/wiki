Towards a better network diagramming solution
==============================================

Perhaps this is just the opinion of one person, but from what has been tested so far, all of the available
solutions to diagram a network layout are seriously lacking in depth of substance. Networks themselves are
more than just a series of connections, the interface the network communicates on possesses its own
characteristic, so does the protocol it communicates, the number of interfaces per network, etc, etc...

A complete network diagram solution should possesses the ability to display these differences in detail
graphically, rather than merely store the finer details as unviewable data. Furthermore, as network technology becomes
more virtualized and abstract a complete diagramming solution should be able to represent this in a manner
that is distinctly different that physical connections. Networking occurs as much on the internal level as it
does on the external, that is, the networking that occurs internally on a system can be just as complex or
even more complex than the network communication that occurs externally. 

To accomplish some symbolance of a more complete network diagramming solution, it is not required to create a
whole new markup language, but to simply take advantage of one already available. Examples of these are json,
yaml, or even toml. Then all is required is the code to interpret the selected markup into a logically
coherent graphical representation. As ascii art is superior in to other forms of artistic expression, the
generation of graphical representation should, by nature, be in ascii. 
