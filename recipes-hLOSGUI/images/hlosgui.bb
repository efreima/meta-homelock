
SUMMARY = "hlOS USER INTERFACE"
DESCRIPTION = "User interace for homelock functions"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI += " file://Capture.png \
 						 file://config.txt \
						 file://homelockQT.pyproject \
						 file://homelockQT.pyproject.user \
						 file://page1.py \
						 file://page1.ui \
						 file://page2.py \
						 file://page2.ui \
						 file://page3.py \
						 file://page3.ui \
						 file://page4.py \
						 file://page4.ui \
						 file://widget.py \
						"

FILES_${PN} += " \
	/usr/* \
"

do_install() {
	install -d ${D}${datadir}/hLOSGUI
	
	install -m 0777 ${WORKDIR}/Capture.png ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/config.txt ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/homelockQT.pyproject ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/homelockQT.pyproject.user ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/page1.py ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/page1.ui ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/page2.py ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/page2.ui ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/page3.py ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/page3.ui ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/page4.py ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/page4.ui ${D}/${datadir}/hLOSGUI
	install -m 0777 ${WORKDIR}/widget.py ${D}/${datadir}/hLOSGUI
}
