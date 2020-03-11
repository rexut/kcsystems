#####
#
# PC/M System Version 2.1x
#
ifeq ($(CONFIG_MACH_PCM_SYS21X),y)
$(call bi,set,mach,video,"64/16 original")
MACH_VIDEO_FONT_BIN := $(S)dumps/orig6416$(IMG_SFX_BIN)
endif

#####
#
# PC/M System Version 3.3x
#
ifeq ($(CONFIG_MACH_PCM_SYS33X),y)

ifeq ($(CONFIG_PCM_VIDEO_ORIG_6416),y)
$(call bi,set,mach,video,"64/16 original")
MACH_VIDEO_FONT_BIN := $(S)dumps/orig6416$(IMG_SFX_BIN)
endif

ifeq ($(CONFIG_PCM_VIDEO_VID2K_8024),y)
$(call bi,set,mach,video,"80/24 (VID2K)")
MACH_VIDEO_FONT_BIN := $(S)dumps/v2k8024$(IMG_SFX_BIN)
endif

endif

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
