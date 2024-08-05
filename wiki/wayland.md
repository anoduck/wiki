```text
# __        __          _                 _
# \ \      / /_ _ _   _| | __ _ _ __   __| |
#  \ \ /\ / / _` | | | | |/ _` | '_ \ / _` |
#   \ V  V / (_| | |_| | | (_| | | | | (_| |
#    \_/\_/ \__,_|\__, |_|\__,_|_| |_|\__,_|
#                 |___/
#
```

## Wayland: I still have not quite figured this thing out... that wayland...

For some reason or another, I always associate Wayland with some slick haired country music singer that smells
of wiskey, cigarettes, and cologne. Not dissing it, just saying...

### WTF, is it?

Well, that is a good question. Supposedly it is the long awaited successor to the X windows system. So, it
replaces X, not compliments it. In the X windows system, X acts as a server that controls the display functions
of the system, and serves those capabilities to the client, which in most cases is the desktop environment. On
wayland, the server-client model is eliminated, and desktops environments directly control all display
capabilities. You would naturally assume, wayland to have a smaller footprint and possess a lighter load on
the system running it, but you would be wrong. Due to it's mature codebase and refinements over the years, X
possesses the lighter footprint and significantly lighter load.

#### How do I implement it?

Another good question. From what we have read so far the answer is not a fun one. Certain programs that you
would use under X are going to be replaced with a Wayland equivolant. This means your login manager, and your
vnc server will need to be replaced.

### How do you get rid of it?

Obviously, you perform the same steps you used to implement it in reverse, but if you had forgotten how you
implemented it, then you would be in the same boat we find ourselves in. 

### References

Most of the references used for our local implementation of wayland and sway came from the archlinux wiki. 

- [Sway](https://wiki.archlinux.org/title/Sway)
- [Wayland](https://wiki.archlinux.org/title/Wayland)
