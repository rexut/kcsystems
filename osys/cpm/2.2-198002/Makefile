#####
#
# Build Information
#
$(call bi,set,osys,vers,"2.2 (February, 1980)")

#####
#
# Basic Disk Operating System (CONFIG_OSYS_CPM22_BDOS)
#
ifeq ($(CONFIG_OSYS_CPM22_BDOS),y)

OSYS_CPM22_BDOS_OBJS := $(S)bdos$(LINKMT_SFX_OBJ)

$(eval $(call add_m80_obj,					\
	$(S)bdos$(LINKMT_SFX_OBJ),				\
	$(S)bdos$(M80_SFX_SRC)					\
))

ifeq ($(CONFIG_OSYS_SUPPORTS_BDOS_IMAGE),y)

OSYS_CPM22_BDOS_BIN := $(S)$(call unquote,$(CONFIG_OSYS_CPM22_BDOS_IMAGE))

$(eval $(call add_linkmt_bin,					\
	$(S)$(call unquote,$(CONFIG_OSYS_CPM22_BDOS_IMAGE)),	\
	$(S)bdos$(LINKMT_SFX_OBJ),				\
	$(CONFIG_OSYS_CPM22_BDOS_BASE)				\
))

endif	# CONFIG_OSYS_SUPPORTS_BDOS_IMAGE

endif	# CONFIG_OSYS_CPM22_BDOS

#####
#
# Console Command Processor (CONFIG_OSYS_CPM22_CCP)
#
ifeq ($(CONFIG_OSYS_CPM22_CCP),y)

OSYS_CPM22_CCP_OBJS := $(S)ccp$(LINKMT_SFX_OBJ)

$(eval $(call add_m80_obj,					\
	$(S)ccp$(LINKMT_SFX_OBJ),				\
	$(S)ccp$(M80_SFX_SRC)					\
))

ifeq ($(CONFIG_OSYS_SUPPORTS_CCP_IMAGE),y)

OSYS_CPM22_CCP_BIN := $(S)$(call unquote,$(CONFIG_OSYS_CPM22_CCP_IMAGE))

$(eval $(call add_linkmt_bin,					\
	$(S)$(call unquote,$(CONFIG_OSYS_CPM22_CCP_IMAGE)),	\
	$(S)ccp$(LINKMT_SFX_OBJ),				\
	$(CONFIG_OSYS_CPM22_CCP_BASE)				\
))

endif	# CONFIG_OSYS_SUPPORTS_CCP_IMAGE

endif	# CONFIG_OSYS_CPM22_CCP

# Local variables:
# coding: utf-8
# mode: text
# mode: make
# End:
# vim: fileencoding=utf-8 filetype=make :
