```text
#  _   ___     _____ __  __
# | \ | \ \   / /_ _|  \/  |
# |  \| |\ \ / / | || |\/| |
# | |\  | \ V /  | || |  | |
# |_| \_|  \_/  |___|_|  |_|
#
```

## NeoVIM

Wow! I find it hard to believe I have allowed this page to remain incomplete for such a long time. If anything, it is a
testament to how little this page was needed for reference. 

### Background History of VI. 

Strap in kids, because this is pretty neat in a nerdy sort of way. 

"vi" was actually originally just a "mode" written for a much earlier editor `ex` by Bill Joy in 1976. Therefore the "v"
in "vi" stood for "visual mode", and the "i" stood for "insert". Joy changed the program so it would begin in "visual
mode", which is how it earned it’s name. Therefore, "ex" and "vi" are synonymous, and are in fact the same program, just
in a different mode. It took till the early 1980’s before finally "vi" became referrenced over "ex" in official
documentation and pathway calls. The first operating system to do this was FreeBSD.

Another child of the eighties, "vim" which stands for "vi improved", is a variant of vi derived from the Stevie text
editor for the Amiga Operating System. Vim continues to be one of the most popular text editors today.

"Nvim" or "NeoVIM" is a continuation to improve upon the improved. It is a complete refactoring of the already
refactored, further extension of feature-fulness by the additional support of LUA scripting, native support of the Tree
Sitter syntax highlighting system, and the Language Server Protocol. All of which makes NeoVIM one of the most
definitive, if not the definitive, modern text editor for the twenty-first century.

### Status of TreeSitter and NeoVIM July 2026

A long experienced bug in nvim led to the discovery of shocking news that nvim’s support for treesitter had waned,
grinded to a halt, and by many considered currently unsupported. This is quite an unexpected surprise since NeoVIM has
supported treesitter natively as a foundational feature for a very long time. The word on the street is the developer in
charge of maintaining treesitter abruptly ceased work on the project, and abandoned the repository. The official NeoVIM
project is currently scrambling to find someone else to take over providing support.

#### Impact on Wiki Maintenance

This wiki was created in NeoVIM, was maintained in NeoVIM, and uses Jake Vincent’s brilliant
[mkdnflow](https://www.github.com/jakewvincent/mkdnflow.nvim) package to aid in link navigation and maintaining a
compatible directory structure with the github wiki. 

The current [standing bug](https://github.com/neovim/neovim/issues/39032) in how tree-sitter parses markdown files has
made upkeep of this wiki a going concern. It does not break functionality, but ejects several iritating error messages
in the editor when markdown files are first opened, causes tree-sitter to completely crash, and subsequently strips the
buffer of all syntax highlighting. 

As of the summer of 2026, the current version of NeoVIM is 12, and the reccommended fix is unfortunately to revert
NeoVIM back to version 11, which still maintains full compatibility with tree-sitter. It is uncertain when this is going
to change.

### Insert a Section symbol

To insert a section symbol in either vim or neovim: `Ctrl+k⇧ Shift+S⇧ Shift+E (a Vim digraph)`

### Links

*I reccommended everything and anything written by Von Heikemen*

* [nvim-starter](https://github.com/VonHeikemen/nvim-starter)
* [init.lua](https://gist.github.com/VonHeikemen/8fc2aa6da030757a5612393d0ae060bd)
* [Build your own](https://vonheikemen.github.io/devlog/tools/build-your-first-lua-config-for-neovim/)
* [Which Key for nvim](https://github.com/folke/which-key.nvim)
