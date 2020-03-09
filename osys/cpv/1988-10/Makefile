#####
#
# Build Information
#
$(call bi,set,osys,vers,"1988-10")

#####
#
# Console Command Processor (CONFIG_OSYS_CPM22_CCP)
#
ifeq ($(CONFIG_OSYS_CPM22_CCP),y)

OSYS_CPM22_CCP_BIN := $(S)$(call unquote,$(CONFIG_OSYS_CPM22_CCP_IMAGE))

endif	# CONFIG_OSYS_CPM22_CCP

#####
#
# Basic Disk Operating System (CONFIG_OSYS_CPM22_BDOS)
#
ifeq ($(CONFIG_OSYS_CPM22_BDOS),y)

OSYS_CPM22_BDOS_BIN := $(S)$(call unquote,$(CONFIG_OSYS_CPM22_BDOS_IMAGE))

endif	# CONFIG_OSYS_CPM22_BDOS

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
