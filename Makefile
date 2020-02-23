TOPDIR := ${shell pwd | sed -e 's/ /\\ /g'}
include $(TOPDIR)/tools/Config.mk

# This is the default goal of the final target (defined in Makefile.build)
.DEFAULT_GOAL := all

PHONY += clean mrproper distclean

clean: cleandocs
	$(foreach file,$(CLEAN),$(call cmd,del,$(file))$(newline))

mrproper: clean
	$(call cmd,del,$(CONFIG))

distclean: mrproper
	$(foreach fd,$(call fndfdwild,$(TOPDIR)/,*~)		\
		     $(call fndfdwild,$(TOPDIR)/,*.bak)		\
		     $(call fndfdwild,$(TOPDIR)/,*.old),	\
		$(call cmd,del,$(fd))$(newline))

# Configuration targets
#
# These targets depend on the kconfig-frontends packages.  To use these, you
# must first download and install the kconfig-frontends package from this
# location: https://gitlab.com/ymorin/kconfig-frontends.  See this repository
# for additional information, in:
# https://gitlab.com/ymorin/kconfig-frontends/-/blob/master/docs/kconfig.txt

PHONY += config oldconfig olddefconfig listnewconfig alldefconfig
PHONY += nconfig menuconfig qconfig gconfig

config:
	$(Q) kconfig-conf Kconfig

oldconfig:
	$(Q) kconfig-conf --oldconfig Kconfig

olddefconfig:
	$(Q) kconfig-conf --olddefconfig Kconfig

listnewconfig:
	$(Q) kconfig-conf --listnewconfig Kconfig

alldefconfig:
	$(Q) kconfig-conf --alldefconfig Kconfig

nconfig:
	$(Q) kconfig-nconf Kconfig

menuconfig:
	$(Q) kconfig-mconf Kconfig

qconfig:
	$(Q) kconfig-qconf Kconfig

gconfig:
	$(Q) kconfig-gconf Kconfig

%_defconfig:
	$(info $(space)$(space)LOAD:$(tab)$(tab)$(CONF_DIR)/$@)
	$(Q) kconfig-conf \
		--defconfig=$(CONF_DIR)/$@ \
		Kconfig

%_savedefconfig:
	$(info $(space)$(space)SAVE:$(tab)$(tab)$(CONF_DIR)/$*_defconfig)
	$(Q) kconfig-conf \
		--savedefconfig=$(CONF_DIR)/$*_defconfig \
		Kconfig

include $(TOPDIR)/tools/Makefile.build
