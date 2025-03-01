```text
#                              _           _    _                  _
#  _ __  _   _ _ __  _ __ ___ (_) ___  ___| |_ | |_ ___  _ __ ___ | |
# | '_ \| | | | '_ \| '__/ _ \| |/ _ \/ __| __|| __/ _ \| '_ ` _ \| |
# | |_) | |_| | |_) | | | (_) | |  __/ (__| |_ | || (_) | | | | | | |
# | .__/ \__, | .__/|_|  \___// |\___|\___|\__(_)__\___/|_| |_| |_|_|
# |_|    |___/|_|           |__/
```

Pyproject.toml: One file to configure them all
===============================================

It might be benefitial to be authoratative on shit like this, but it would appear there is a push to use
`pyproject.toml` as a standardized configuration file for all Python projects, much like `package.json` is for
Node.Js. The project manager "Poetry" has been using it for years, and provides a smooth means to do most of
the heavy lifting of creating and formatting it for you. The package manager "Uv" does this autogeneration
as well, but not 100%. If uv is not used to generate `pyproject.toml`, then uv will not make any changes to
it. This was done to prevent pre-existing settings from being overwritten, but does this at the expense of
providing a seamless means to automate it's project integration. 

## Ipsum Filler Shit

Sunt, elit, consequat sint deserunt sunt enim.  Aliquip proident officia excepteur, deserunt mollit magna; laboris.  Lorem do anim sunt, irure ut cupidatat, tempor.  Cupidatat nulla velit irure nulla, sint, et.  Ipsum lorem incididunt ut, magna consequat non, commodo commodo do, quis.

Lorem dolor voluptate nostrud anim ea, velit sed voluptate adipiscing, est, laborum.  Nulla labore consectetur ex irure sed aliqua proident.  Sed laborum commodo quis commodo sed, sit sunt sit do pariatur.  Exercitation, minim amet dolore mollit non mollit excepteur tempor, nisi cupidatat.  Velit, enim, deserunt, amet nulla.  Et ullamco cupidatat ex, aliquip id laboris excepteur elit.  In sint velit aliquip excepteur lorem voluptate exercitation.  Ex, incididunt in deserunt, veniam, laboris.  Consectetur deserunt dolore cupidatat excepteur excepteur, pariatur sit, amet id.  Elit proident adipiscing enim, quis qui, non magna occaecat minim pariatur.  Exercitation cillum excepteur lorem nisi; consequat consequat ad; ut.  Aute amet reprehenderit, anim sunt cupidatat, nostrud.  Sint, ad culpa incididunt mollit proident, do sed do.  Minim anim; sint, lorem proident, fugiat qui officia id cillum; laborum laboris.  Aute ipsum amet ut irure ipsum sed, elit ullamco, excepteur aliquip.  Esse enim, ea adipiscing exercitation deserunt ad deserunt minim nostrud qui.  Culpa sunt, laboris cupidatat, nostrud sed.  Commodo, quis, consectetur est anim lorem est consequat, incididunt veniam do.  Reprehenderit, ullamco velit, esse dolor irure mollit.
