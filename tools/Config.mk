include $(TOPDIR)/tools/gmsl/gmsl

# Control build verbosity

ifeq ($(V),1)
  qsout =
  quiet =
  Q :=
else
  qsout = >/dev/null
  quiet = quiet_
  Q := @
endif

# Init all relevant variables used in make files so
# 1) they have correct type
# 2) they do not inherit any value from the environment

CONFIG :=
CONFIG_MACH :=
CONFIG_OSYS :=
PREREQ :=

# Preset all configuration variables to used in the build system.
# Define functions to access to the configuration set.

CONFIG := $(S).config
-include $(CONFIG)

# Read in the configuration set w/o blank lines and comments.
cfgset = $(call frdstrip,$(1))

# Get a set of all configuration variable names.
cfgsvn = $(call map,vname,$(call cfgset,$(1)))

# Get a set of values of all configuration variables.
cfgsvv = $(call map,vvalue,$(call cfgset,$(1)))

# These are configuration variables that are quoted by configuration tool
# but which must be unquoated when used in the build system.

CONFIG_MACH := $(patsubst "%",%,$(strip $(CONFIG_MACH)))
CONFIG_SYSV := $(patsubst "%",%,$(strip $(CONFIG_SYSV)))
CONFIG_OSYS := $(patsubst "%",%,$(strip $(CONFIG_OSYS)))

# Preset some default search paths. Maybe abel to change by configuration
# anytime in the future.

CPMBIN_DIR := $(S)tools/cpmbin
DEPLOY_DIR := $(S)images

# Try to determine where files are located.  If the caller did
# include /foo/Makefile then extract the /foo/ so that getsdir()
# will return transparently with the correct value.

_sdir = $(if $(MAKEFILE_LIST),\
	$(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST)))

# If there are any spaces in the path in S then give up

S = $(call getsdir)
getsdir = $(if $(call eq,1,$(call length,$(call _sdir))),\
	  $(patsubst %Makefile,%,$(call _sdir)))
#	  $(patsubst $(TOPDIR)/%Makefile,%,$(call _sdir)))

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
