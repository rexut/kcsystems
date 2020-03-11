#####
#
# System Image (MACH_SYSTEM_BIN)
#
ifneq ($(MACH_SYSTEM_BIN),)

#####
#
# System Image (OSYS_CPM22_CCP_OBJS && OSYS_CPM22_BDOS_OBJS)
#
ifneq ($(OSYS_CPM22_CCP_OBJS)$(OSYS_CPM22_BDOS_OBJS),)

$(eval $(call add_linkmt_bin,					\
	$(MACH_SYSTEM_BIN),					\
	$(OSYS_CPM22_PREAMBLE_OBJS)				\
	$(OSYS_CPM22_CCP_OBJS)					\
	$(OSYS_CPM22_BDOS_OBJS)					\
	$(OSYS_CPM22_BIOS_OBJS),				\
	$(OSYS_CPM22_LINK_BASE)					\
))

#####
#
# System Track Dump (CONFIG_IMAGE_SYS)
#
ifeq ($(CONFIG_IMAGE_SYS),y)

$(eval $(call deploy_bin_as_sys,$(MACH_SYSTEM_BIN)))

endif	# CONFIG_IMAGE_SYS

#####
#
# System Disk Image (CONFIG_IMAGE_DSK)
#
ifeq ($(CONFIG_IMAGE_DSK),y)

$(eval $(call add_sys_to_dsk,$(MACH_SYSTEM_BIN)))

endif	# CONFIG_IMAGE_DSK

#####
#
# ROM Image !(OSYS_CPM22_CCP_OBJS || OSYS_CPM22_BDOS_OBJS)
#
else	# !(OSYS_CPM22_CCP_OBJS || OSYS_CPM22_BDOS_OBJS)

$(eval $(call add_linkmt_bin,					\
	$(MACH_SYSTEM_BIN),					\
	$(OSYS_CPM22_BIOS_OBJS),				\
	$(OSYS_CPM22_LINK_BASE)					\
))

#####
#
# ROM Binary Dump (CONFIG_IMAGE_ROM)
#
ifeq ($(CONFIG_IMAGE_ROM),y)

$(eval $(call deploy_bin_as_rom,$(MACH_SYSTEM_BIN)))

endif	# CONFIG_IMAGE_ROM

endif	# OSYS_CPM22_CCP_OBJS || OSYS_CPM22_BDOS_OBJS

endif	# MACH_SYSTEM_BIN

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
