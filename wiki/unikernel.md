```text
#  _   _       _ _                        _
# | | | |_ __ (_) | _____ _ __ _ __   ___| |
# | | | | '_ \| | |/ / _ \ '__| '_ \ / _ \ |
# | |_| | | | | |   <  __/ |  | | | |  __/ |
#  \___/|_| |_|_|_|\_\___|_|  |_| |_|\___|_|
#
```

## Unikernels: Single Process Kernels

Up until the rise of virtualization to popularity, the concept of running a kernel for a solitary process was
counterproductive and highly problematic, but now things have changed. As technology moves closer to isolating
all processes in self contained virtualized environments, the unikernel is an essentially part of this
developmental progression, because it provides the foundation for which truly self contained environments can
be built upon.

### Unikernel variations

Unikernels come in different forms; language specific unikernels, Linux compatible unikernels, and Posix
compliant unikernels. The latter two are generic unikernels. A handful of language specific unikernels are available for programming languages. Rust,
Ocaml, Go, ErLang, Pascal, Java, C++, NodeJS and Haskell have unikernels specifically designed to support those languages. Java's jvm is thought of as
a unikernel.

### Unikernels

- [UniKraft](https://github.com/unikraft/unikraft) -- UniKraft has the appearance of being a popular generic
  unikernel, although is not as documented as one would expect.
- [Solo5](https://github.com/Solo5/solo5) -- A unikernel management and development framework for MirageOS
  (Ocaml) and IncludeOS (C++), but allows for development generic unikernels. The importantance of this unikernel 
  is its support of OpenBSD and flexibility.
- [Nanos](https://github.com/nanovms/nanos) -- Is by far the best documented, and most production ready unikernel
  on the market, which has an established marketplace for unikernel machines, [ops.city](https://ops.city).
  More information is in the [GitHub repository](https://github.com/nanovms/ops).
- [Eggos](https://github.com/icexin/eggos) -- A unikernel for the Go programming language that claims it can
  convert any go project into a unikernel. Although, if you are unifamiliar with go project creation and
  management this may not be the case.
- [ClickOS](https://github.com/sysml/clickos) -- Is a unikernel specifically developed for [Click](https://github.com/kohler/click),
  which is a modular packet processing and analysis router. In layman's terms, it's a unikernel specifically
  designed to route network packages. Configuration and usage is done in its own configuration language. 

### Links

- [Awesome MicroVMS](https://github.com/infracloudio/awesome-microvm)
- [Awesome unikernels](https://github.com/uniqernel/awesome-unikernels)
