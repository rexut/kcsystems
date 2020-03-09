#####
#
# Build Information
#
$(call bi,set,mach,vers,$(CONFIG_SYSV))

ifeq ($(CONFIG_MACH_PCM_SYS21X),y)
$(call bi,set,mach,name,"PC/M RAM-Floppy-System")
MACH_PCM_SYS_MKF := $(S)2.1x/Makefile
MACH_PCM_HW_MKF := $(S)hw/Makefile
endif

ifneq ($(MACH_PCM_SYS_MKF)$(MACH_PCM_HW_MKF),)
include $(MACH_PCM_SYS_MKF)
include $(MACH_PCM_HW_MKF)
endif

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
