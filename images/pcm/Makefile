ifeq ($(CONFIG_MACH_PCM_SYS21X),y)
include $(S)2.1x/Makefile
endif

#####
#
# Video Card Font Image (MACH_VIDEO_FONT_BIN)
#
ifneq ($(MACH_VIDEO_FONT_BIN),)

$(eval $(call deploy_bin_as_rom,$(MACH_VIDEO_FONT_BIN)))

endif	# MACH_VIDEO_FONT_BIN

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
