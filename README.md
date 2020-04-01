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

#### Add the CP/M for Linux (CPM4L) APT Repository

```bash
$: sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/rexut:/CPM4L/x$(lsb_release -si)_$(lsb_release -sr)/ /' > /etc/apt/sources.list.d/home:rexut:CPM4L.list"
$: wget -nv https://download.opensuse.org/repositories/home:rexut:CPM4L/x$(lsb_release -si)_$(lsb_release -sr)/Release.key -O Release.key
$: sudo apt-key add - < Release.key && rm -f Release.key
$: sudo apt-get update
```

#### GNU core utilities

... for create/copy/move/delete files and compute and check checksums.

```bash
$: sudo apt-get install coreutils
```

#### GNU stream editor

... for filtering/transforming text.

```bash
$: sudo apt-get install sed
```

#### Yet Another Z80 Emulator

... for emulate Z80 and CP/M on Unix systems.

```bash
$: sudo apt-get install yaze
```

#### SRecord EPROM file format utility

... for reads/manipulate/join/convert/write numerous EPROM file formats.

```bash
$: sudo apt-get install srecord
```

#### Library with disc image file utility

... for create/format/copy/convert/write numerous (floppy) disk image formats.

```bash
$: sudo apt-get install libdsk-utils
```

#### Tools to access CP/M file systems

... for create/copy/move/delete files to/from CP/M file systems.

```bash
$: sudo apt-get install cpmtools
```

#### Java KC-Emulator

... for emulate the generated system images of old "DDR Kleincomputer".

```bash
$: sudo apt-get install jkcemu
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

# KC-Systems Documentation

The documentation is written using Sphinx documentation system. To
install it in a Python virtual environment, please do:

**Some design rules for documentation:**

* We will never add images in binary formats like PNG or BMP. Valid image
  formats that are alowed are: SVG and the original design files such as
  DIA or XCF.

## Howto build the documentation

**Python 3.7 virtual environment:**

```bash
$: python3 -m venv --copies --promp="$(basename $(pwd))[$(python3 --version)]" .py38env
$: source .py38env/bin/activate
$: pip install --upgrade pip
$: pip install --upgrade setuptools
$: pip install --upgrade --requirement tools/requirements.txt
```

**Bootstrap fonts:**

```bash
$: ./docs/_static/fonts/.rebuild-dejavu
```

**Documentation tests:**

```bash
$: make testdocs V=1
$: make spelldocs V=1
```

**Documentation builds:**

```bash
$: make htmldocs
$: make pdfdocs
```

**Clean-up:**

```bash
$: make cleandocs
$: deactivate
$: rm -rf .py38env
```

### System packages on Ubuntu (>= 16.04):

```bash
$: sudo apt-get install build-essential python3.7-dev
$: sudo apt-get install curl tar bzip2 woff2 eot-utils
$: sudo apt-get install fontconfig fontforge-nox
$: sudo apt-get install libfreetype6-dev librsvg2-bin icoutils
$: sudo apt-get install poppler-utils imagemagick pdf2svg
$: sudo apt-get install latexmk xindy unifont fonts-dejavu
$: sudo apt-get install fonts-wqy-microhei fonts-font-awesome
$: sudo apt-get install texlive-xetex texlive-pictures
$: sudo apt-get install texlive-fonts-recommended texlive-fonts-extra
$: sudo apt-get install enchant aspell aspell-en aspell-de
$: sudo apt-get install wamerican-huge wngerman wgerman-medical
```
