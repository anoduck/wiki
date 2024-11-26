```text
#  _____                           __        ___ _    _
# | ____|_ __ ___   __ _  ___ ___  \ \      / (_) | _(_)___
# |  _| | '_ ` _ \ / _` |/ __/ __|  \ \ /\ / /| | |/ / / __|
# | |___| | | | | | (_| | (__\__ \   \ V  V / | |   <| \__ \
# |_____|_| |_| |_|\__,_|\___|___/    \_/\_/  |_|_|\_\_|___/
#
```

Wikis for Emacs
---------------

This wiki is entirely maintained from within the local configuration of NeoVIM. NeoVIM handles
nearly every task needed to maintain it. The ASCII graphic is generated with the NeoVIM package,
and the file structure and markdown files are all handled by the markflow.nvim package, which is excellent if
you have not tried it already. Both VIM and NeoVIM have traditionally been excellent at providing extensions
for users to maintain their own personal knowledge store. For VIM, this feature is provided by the legendary
VimWiki package, which can also be used with NeoVIM without any problems. IMHOP, both VIM and NeoVIM are light
enough and provide excellent markdown rendering and inline code redering to be excellently suited for the purpose.

But, what if you wanted to do this in EMACS? In theory, EMACS should excel at this rather simple task, but
what would one use to do accomplish this task? Sadly, there are not too many options available for EMACS,
well, not as many as can be found with other editors. There are many ways in which one can configure a
"wiki-ish" configuration, but this is not the same thing. A good wiki package should provide structure for the
wiki to exist in, this is primarily done with providing the ability for pages to internally link with one
another. Wiki's should also provide the ability to publish it's content to the web for viewing, after all, a
wiki is not very good if no one is able to look at it. Lastly, a good wiki package should be convenient to
use. This is the failing of many wiki applications, they are standalone or would require an additional program
for use. This would means an additional set of configuration files to manage, and the added time it takes to
open and close such an application.

With all of this being said. Let's take a look at three of the options available, and later on will dive into
how to use them. These options are Org-Mode, EmacsMuse, and Easy-Jekyll mode.

### [Org Wiki](https://github.com/abo-abo/plain-org-wiki)

There is not much to be said about org wiki, as it relies mostly on org-mode to provide all the features, and
merely ensures internal links to other pages are created with org-link and redirects to those pages. The wiki
is then published via the org-export-dispatch feature, when can render them as either markdown or as any other
wiki is published, that is in HTML. The benefit being, it all can be done from within org mode, which may not
be very impressive, but certainly is sufficient and very handy.

### [EmacsMuse](https://www.emacswiki.org/emacs/EmacsMuse)

The EmacsMuse is the successor to Emacs Wiki Mode, which was the primary means to provide a wiki functionality
to EMACS and was created way back in 2005. EmacsMuse was designed for use with the web wiki framework "OddMuse" in
mind, but does not require an installation of oddmuse to function. EmacsMuse can export the wiki to many
different formats as desired, and provides all the usual bells and whistles one would expect from a wiki
system. It even allows configuration of different source formats, so one can write the wiki in whatever markup
language one prefers. All of which means, EmacsMuse is a solid solution to provide this feature.

### [Easy-Jekyll](https://github.com/masasam/emacs-easy-jekyll)

Easy-Jekyll is a solution that would be missed by the consideration of many, but for our purposes at least, is
a solution that will provide all the needed features. As it turns out, this wiki, "The DasWiki", is actually a
site managed by the Jekyll webframework. There is surprisingly little that separates the structure of a blog
from that of a wiki, the primary difference is the taxonomy generated from it't type of content. So, as long
as one has a site format that supports a wiki, then there is no reason why a blog engine could not maintain it
as well. 

```elisp
(use-package easy-jekyll
  :init
  (setq easy-jekyll-basedir "~/wiki/"
		easy-jekyll-url "https://anoduck.github.io"
		easy-jekyll-root "~/Sandbox/wiki/")
  :bind ("C-c C-e" . easy-jekyll))
```
