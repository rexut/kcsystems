#####
#
# ROM Binary Dump (CONFIG_IMAGE_ROM)
#
ifeq ($(CONFIG_IMAGE_ROM),y)

#####
#
# Console Command Processor Image (OSYS_CPM22_CCP_BIN)
#
ifneq ($(OSYS_CPM22_CCP_BIN),)

#
# CCP part of ROM image (CONFIG_OSYS_CPM22_CCP_ROM_OFFS)
#
ifneq ($(CONFIG_OSYS_CPM22_CCP_ROM_OFFS),)

$(eval $(call add_bin_to_rom,					\
	$(OSYS_CPM22_CCP_BIN),					\
	$(CONFIG_OSYS_CPM22_CCP_ROM_OFFS)			\
))

else	# !CONFIG_OSYS_CPM22_CCP_ROM_OFFS

$(eval $(call deploy_bin_as_ram,				\
	$(OSYS_CPM22_CCP_BIN)					\
))

endif	# CONFIG_OSYS_CPM22_CCP_ROM_OFFS
endif	# OSYS_CPM22_CCP_BIN

#####
#
# Basic Disk Operating System Image (OSYS_CPM22_BDOS_BIN)
#
ifneq ($(OSYS_CPM22_BDOS_BIN),)

#
# BDOS part of ROM image (CONFIG_OSYS_CPM22_BDOS_ROM_OFFS)
#
ifneq ($(CONFIG_OSYS_CPM22_BDOS_ROM_OFFS),)

$(eval $(call add_bin_to_rom,					\
	$(OSYS_CPM22_BDOS_BIN),					\
	$(CONFIG_OSYS_CPM22_BDOS_ROM_OFFS)			\
))

else	# !CONFIG_OSYS_CPM22_BDOS_ROM_OFFS

$(eval $(call deploy_bin_as_ram,				\
	$(OSYS_CPM22_BDOS_BIN)					\
))

endif	# CONFIG_OSYS_CPM22_BDOS_ROM_OFFS
endif	# OSYS_CPM22_BDOS_BIN

#####
#
# Basic I/O System Image (OSYS_CPM22_BIOS_BIN)
#
ifneq ($(OSYS_CPM22_BIOS_BIN),)

#
# BIOS part of ROM image (CONFIG_PCM_SYS21X_BIOS_ROM_OFFS)
#
ifneq ($(CONFIG_PCM_SYS21X_BIOS_ROM_OFFS),)

$(eval $(call add_bin_to_rom,					\
	$(OSYS_CPM22_BIOS_BIN),					\
	$(CONFIG_PCM_SYS21X_BIOS_ROM_OFFS)			\
))

else	# !CONFIG_PCM_SYS21X_BIOS_ROM_OFFS

$(eval $(call deploy_bin_as_ram,				\
	$(OSYS_CPM22_BIOS_BIN)					\
))

endif	# CONFIG_PCM_SYS21X_BIOS_ROM_OFFS
endif	# OSYS_CPM22_BIOS_BIN

#####
#
# System Visual Debugger Image (PCM_SYS21X_SVDB_BIN)
#
ifneq ($(PCM_SYS21X_SVDB_BIN),)

#
# SVDB part of ROM image (CONFIG_PCM_SYS21X_SVDB_ROM_OFFS)
#
ifneq ($(CONFIG_PCM_SYS21X_SVDB_ROM_OFFS),)

$(eval $(call add_bin_to_rom,					\
	$(PCM_SYS21X_SVDB_BIN),					\
	$(CONFIG_PCM_SYS21X_SVDB_ROM_OFFS)			\
))

else	# !CONFIG_PCM_SYS21X_SVDB_ROM_OFFS

$(eval $(call deploy_bin_as_ram,				\
	$(PCM_SYS21X_SVDB_BIN)					\
))

endif	# CONFIG_PCM_SYS21X_SVDB_ROM_OFFS
endif	# PCM_SYS21X_SVDB_BIN

#####
#
# Voice Tape Monitor Image (PCM_SYS21X_VTAPE_BIN)
#
ifneq ($(PCM_SYS21X_VTAPE_BIN),)

#
# VTAPE part of ROM image (CONFIG_PCM_SYS21X_VTAPE_ROM_OFFS)
#
ifneq ($(CONFIG_PCM_SYS21X_VTAPE_ROM_OFFS),)

$(eval $(call add_bin_to_rom,					\
	$(PCM_SYS21X_VTAPE_BIN),				\
	$(CONFIG_PCM_SYS21X_VTAPE_ROM_OFFS)			\
))

else	# !CONFIG_PCM_SYS21X_VTAPE_ROM_OFFS

$(eval $(call deploy_bin_as_ram,				\
	$(PCM_SYS21X_VTAPE_BIN)					\
))

endif	# CONFIG_PCM_SYS21X_VTAPE_ROM_OFFS
endif	# PCM_SYS21X_VTAPE_BIN

endif	# CONFIG_IMAGE_ROM

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
