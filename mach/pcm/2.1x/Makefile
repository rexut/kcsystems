#####
#
# Basic I/O System Definitions
#

MACH_SYSTEM_DEF := $(S)pcm$(M80_SFX_SRC)

$(eval $(call add_flt_tgt,					\
	$(S)pcm$(M80_SFX_SRC),					\
	$(S)pcm$(M80_SFX_SRC)$(FLT_SFX_SRC)			\
))

#####
#
# Basic I/O System (CONFIG_PCM_SYS21X_BIOS)
#
ifeq ($(CONFIG_PCM_SYS21X_BIOS),y)

ifneq ($(CONFIG_MACH_PCM_SYS210),y)

OSYS_CPM22_BIOS_BIN := $(S)bios$(IMG_SFX_BIN)

$(eval $(call add_m80_obj,					\
	$(S)bios$(LINKMT_SFX_OBJ),				\
	$(S)pcm$(M80_SFX_SRC) $(S)pcmbios$(M80_SFX_SRC)		\
))

$(eval $(call add_linkmt_bin,					\
	$(S)bios$(IMG_SFX_BIN),					\
	$(S)bios$(LINKMT_SFX_OBJ),				\
	$(CONFIG_PCM_SYS21X_BIOS_BASE)				\
))

else	# CONFIG_MACH_PCM_SYS210

OSYS_CPM22_BIOS_BIN := $(S)dumps/pcmbios$(IMG_SFX_BIN)

endif	# !CONFIG_MACH_PCM_SYS210

endif	# CONFIG_PCM_SYS21X_BIOS

#####
#
# System Visual Debugger (CONFIG_PCM_SYS21X_SVDB)
#
ifeq ($(CONFIG_PCM_SYS21X_SVDB),y)

ifneq ($(CONFIG_MACH_PCM_SYS210),y)

PCM_SYS21X_SVDB_BIN := $(S)svdb$(IMG_SFX_BIN)

$(eval $(call add_m80_obj,					\
	$(S)svdb$(LINKMT_SFX_OBJ),				\
	$(S)pcmsvdb$(M80_SFX_SRC)				\
))

$(eval $(call add_linkmt_bin,					\
	$(S)svdb$(IMG_SFX_BIN),					\
	$(S)svdb$(LINKMT_SFX_OBJ),				\
	$(CONFIG_PCM_SYS21X_SVDB_BASE)				\
))

else	# CONFIG_MACH_PCM_SYS210

PCM_SYS21X_SVDB_BIN := $(S)dumps/pcmsvdb$(IMG_SFX_BIN)

endif	# !CONFIG_MACH_PCM_SYS210

endif	# CONFIG_PCM_SYS21X_SVDB

#####
#
# Voice Tape Monitor (CONFIG_PCM_SYS21X_VTAPE)
#
ifeq ($(CONFIG_PCM_SYS21X_VTAPE),y)

ifneq ($(CONFIG_MACH_PCM_SYS210),y)

PCM_SYS21X_VTAPE_BIN := $(S)vtape$(IMG_SFX_BIN)

$(eval $(call add_m80_obj,					\
	$(S)vtape$(LINKMT_SFX_OBJ),				\
	$(S)pcmvtape$(M80_SFX_SRC)				\
))

$(eval $(call add_linkmt_bin,					\
	$(S)vtape$(IMG_SFX_BIN),				\
	$(S)vtape$(LINKMT_SFX_OBJ),				\
	$(CONFIG_PCM_SYS21X_VTAPE_BASE)				\
))

else	# CONFIG_MACH_PCM_SYS210

PCM_SYS21X_VTAPE_BIN := $(S)dumps/pcmvtape$(IMG_SFX_BIN)

endif	# !CONFIG_MACH_PCM_SYS210

endif	# CONFIG_PCM_SYS21X_VTAPE

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
