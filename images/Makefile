#####
#
# Build Information
#
ifeq ($(CONFIG_IMAGE_ROM),y)
$(call bi,set,img,type,"ROM Binary Dump: $(IMAGE_ROM_NAME)")
endif

#####
#
# Computer specific image generator
#
ifneq ($(CONFIG_MACH),)
include $(S)$(CONFIG_MACH)/Makefile
endif	# !CONFIG_SYSV

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
