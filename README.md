[![Build Status](https://travis-ci.org/rexut/kcsystems.svg?branch=master)](https://travis-ci.org/rexut/kcsystems)

# KC-Systems Build Environment

The building environment was once created to reproduce the ROM and floppy disk
images of old and historical operating systems for various Zilog Z80-based
computer systems from the GDR, in German the so-called "Kleincomputer".

## Howto use the build environment

```bash
$: make help
$: make menuconfig
```

### System packages on Ubuntu (>= 16.04):

#### GNU core utilities

... for create/copy/move/delete files.

```bash
$: sudo apt-get install coreutils
```

#### GNU stream editor

... for filtering/transforming text.

```bash
$: sudo apt-get install sed
```

#### GNU Make utility

... for directing compilation/execution.

```bash
$: sudo apt-get install make
```

#### Linux Kconfig parser and frontend

... for parsing/edit/change configure files.

```bash
$: sudo apt-get install kconfig-frontends
```
