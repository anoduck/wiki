```text
#  _       _ _         _
# (_)_ __ (_) |_   ___| |
# | | '_ \| | __| / _ \ |
# | | | | | | |_ |  __/ |
# |_|_| |_|_|\__(_)___|_|
#
```

## Welcome to the rest of your life.

One does not simply install Emacs. Creating an Emacs configuration file is a process that will take the rest
of your remaining life, and you still will have not completed it. Instead of set and done, think of it as a
process of continual maintenance.

Busey ipsum dolor sit amet. Go with the feeling of the nature. Take it easy. Know why you're here. And remember to balance your internal energy with the environment.You ever roasted doughnuts?Have you urinated? Have you drained your bladder? Are you free? Because if you haven't it will only come out later. I'm giving you some information that your bodily fluids may penetrate your clothing fibre's without warning.

You ever roasted doughnuts?It's good to yell at people and tell people that you're from Tennesee, so that way you'll be safe.I wrestled a bear once. A 750lbs black bear.Have you urinated? Have you drained your bladder? Are you free? Because if you haven't it will only come out later. I'm giving you some information that your bodily fluids may penetrate your clothing fibre's without warning.

The best way to communicate is compatible. Compatible communication is listening with open ears and an open mind, and not being fearful or judgemental about what you're hearing.Listen to the silence. And when the silence is deafening, you're in the center of your own universe.

### Use-Package

Use-package is a package for emacs, that allows you to easily load and configure other packages for your Emacs session. For
lack of a better explanation, it is sort of like "nix config" for emacs, except not at all.

The documentation for it is fairly extensive, and best if left to the author to maintain. So, here is a direct
link to the readme. [Use-Package Readme](https://github.com/jwiegley/use-package/blob/master/README.md)

#### Most Commonly used Keywords.

| Keyword     | Definition                                                 | example |
| ---         | ---                                                        | ---     |
| `:requires` | Declares dependencies both required and optional.          |         |
| `:defer`    | Defers loading of package for a few seconds.               |         |
| `:init`     | Declares code that needs execution before loading package. |         |
| `:config`   | Defines package configuration options.                     |         |
| `:bind`     | Declares key binds for package.                            |         |
| `:hook`     | Defines hooks for loading of package                       |         |
| `:ensure`   | Ensures that package is loaded.                            |         |
| `:if`       | Conditional loading keyword.                               |         |

#### syntactical format

In the following example, `$package` will be used to represent a desired package.

```elisp
(use-package $package
   :requires $another-package
	 :defer t
	 )
```

### Giving Emacs a boost

After reading an article on [emacswiki](https://emacswiki.com) I learned it was recommended to bump your
single file memory limit to 1GB. So I added.

```elisp
(setq most-positive-fixnum 1073741824)
```
