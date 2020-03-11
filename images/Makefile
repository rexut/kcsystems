#####
#
# Build Information
#
ifeq ($(CONFIG_IMAGE_ROM),y)
$(call bi,set,img,type,"ROM Binary Dump: $(IMAGE_ROM_NAME)")
endif

ifeq ($(CONFIG_IMAGE_SYS),y)
$(call bi,set,img,type,"System Track Dump: $(IMAGE_SYS_NAME)")
endif

ifeq ($(CONFIG_IMAGE_DSK),y)
$(call bi,set,img,type,"System Disk Image: $(IMAGE_IMG_NAME)")
endif

#####
#
# Computer specific image generator
#
ifneq ($(CONFIG_MACH),)
include $(S)$(CONFIG_MACH)/Makefile
endif	# !CONFIG_SYSV

#####
#
# Disk Image Transistions
#
ifeq ($(CONFIG_IMAGE_DSK_CPC),y)
$(eval $(call add_dsktrans_cpc))
endif

ifeq ($(CONFIG_IMAGE_DSK_CQM),y)
$(eval $(call add_dsktrans_cqm))
endif

ifeq ($(CONFIG_IMAGE_DSK_IMD),y)
$(eval $(call add_dsktrans_imd))
endif

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
