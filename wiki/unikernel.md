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
developmental progression, as it provides the foundation for which truly self contained environments can
be built upon.

### Unikernel variations

Unikernels come in different forms; language specific unikernels, Linux compatible unikernels, and Posix
compliant unikernels. The latter two are generic unikernels. A handful of language specific unikernels are available for programming languages. Rust,
Ocaml, Go, ErLang, Pascal, Java, C++, NodeJS and Haskell have unikernels specifically designed to support those languages.

### Unikernels

A table representation of available unikernel technologies as of Summer 2024. 

| Name      | Supported Langs       | Runtime Envs                  | Features                 | Active | Supported Systems    |
| --------- | --------------------- | ----------------------------- | ------------------------ | ------ | -------------------- |
| Kontain   | Any / All             | Docker                        | Uses Docker Build system | Yes    | Not Kali :(          |
| UniKraft  | Most                  | KVM Xen Linux                 | Kraft orchestration      | Yes    | Linux                |
| Nanos/Ops | Any / All             | Qemu Xen, Amzn, ggle, hyper V | Ops Orchestration        | Yes    | A whole buttload     |
| MirageOS  | OCaml only            | KVM or Xen                    | N/A                      | Yes    | Does it even matter? |
| OSv       | Most                  | Vbox ESXi Amzn ggle           | Cloud and IoT            | Yes    | Linux                |
| IncludeOS | Mostly for C++        | KVM Vbox VMware ggle          | Mothership orchestration | Yes    | Linux                |
|           |                       |                               |                          |        |                      |


Below are unikernels that may or may not be included in the above table.

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

### References

- [seeker89/unikernels](https://github.com/seeker89/unikernels)
- [cetic/unikernels](https://github.com/cetic/unikernels)
- [unikernel.org](https://unikernel.org)
