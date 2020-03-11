#####
#
# Basic I/O System Definitions
#

MACH_SYSTEM_DEF := $(S)pcmdef$(M80_SFX_SRC)

ifeq ($(CONFIG_MACH_PCM_SYS330),y)

$(eval $(call add_flt_tgt,					\
	$(S)pcmdef$(M80_SFX_SRC),				\
	$(S)pcmdef$(M80_SFX_SRC)$(FLT_SFX_SRC),			\
	BUILD_DATE="15.04.1990"					\
	BUILD_TIME="12:00"					\
))

else    # !CONFIG_MACH_PCM_SYS330

$(eval $(call add_flt_tgt,					\
	$(S)pcmdef$(M80_SFX_SRC),				\
	$(S)pcmdef$(M80_SFX_SRC)$(FLT_SFX_SRC),			\
	BUILD_DATE="$(shell date +'%d.%m.%Y')"			\
	BUILD_TIME="$(shell date +'%H:%M')"			\
))

endif   # CONFIG_MACH_PCM_SYS330

#####
#
# Bootstrap loader (CONFIG_PCM_SYS33X_BAS)
# BAS -> BIOS Anfangs-Segment (German)
#
ifeq ($(CONFIG_PCM_SYS33X_BAS),y)

OSYS_CPM22_PREAMBLE_OBJS := $(S)bas$(LINKMT_SFX_OBJ)

$(eval $(call add_m80_obj,					\
	$(S)bas$(LINKMT_SFX_OBJ),				\
	$(S)pcmbas$(M80_SFX_SRC) $(S)pcmdef$(M80_SFX_SRC)	\
))

endif	# CONFIG_PCM_SYS33X_BAS

#####
#
# Basic I/O System (CONFIG_PCM_SYS33X_BIOS)
#
ifeq ($(CONFIG_PCM_SYS33X_BIOS),y)

MACH_SYSTEM_BIN := $(S)$(IMAGE_BASE_NAME)$(IMG_SFX_BIN)

OSYS_CPM22_BIOS_OBJS := $(S)bios$(LINKMT_SFX_OBJ)
OSYS_CPM22_LINK_BASE := $(CONFIG_PCM_SYS33X_BIOS_BASE)

$(eval $(call add_m80_obj,					\
	$(S)bios$(LINKMT_SFX_OBJ),				\
	$(S)pcmbios$(M80_SFX_SRC) $(S)pcmdef$(M80_SFX_SRC)	\
	$(S)pcmboot$(M80_SFX_SRC) $(S)pcmvar$(M80_SFX_SRC)	\
	$(S)pcmio$(M80_SFX_SRC) $(S)pcmdisk$(M80_SFX_SRC)	\
	$(S)pcmvtape$(M80_SFX_SRC) $(S)pcmsvdb$(M80_SFX_SRC)	\
	$(S)pcmurlad$(M80_SFX_SRC) $(S)pcmcom$(M80_SFX_SRC)	\
))

endif	# CONFIG_PCM_SYS33X_BIOS

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
