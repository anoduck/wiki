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

Unikernels come in several forms; language specific unikernels, Linux compatible unikernels, and Posix
compliant unikernels. The later can be seen as generic unikernels. Only a handful of language specific unikernels are available for a few languages. Rust,
Ocaml, Go, ErLang, Pascal, Java, C++, NodeJS and Haskell have unikernels specifically designed to support those languages. Java can be
seen as the first example of a unikernel, due to it's JVM.

### Links

- [Awesome MicroVMS](https://github.com/infracloudio/awesome-microvm)
- [Awesome unikernels](https://github.com/uniqernel/awesome-unikernels)
- [unikraft](https://github.com/unikraft/unikraft)
- [nanos](https://github.com/nanovms/nanos)
- [Solo5](https://github.com/Solo5/solo5)
