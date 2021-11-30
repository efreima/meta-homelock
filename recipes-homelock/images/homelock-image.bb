require /space/schoolspace/ROOT_HLOS/poky/meta/recipes-core/images/core-image-minimal.bb

SUMMARY = "hlOS USER INTERFACE"
DESCRIPTION = "User interace for homelock functions"
LICENSE = "OPEN"
GUI_FILES = "../../hLOSGUI/include/*"

#inherit core-image


#FILES_${PN} += " \
#	/usr/* \
#"
#
#do_install() {
#install -d ${D}${datadir}/hLOSGUI
#
#}
