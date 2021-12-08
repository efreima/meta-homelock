require /space/schoolspace/ROOT_HLOS/poky/meta/recipes-graphics/images/core-image-x11.bb

SUMMARY = "hlOS USER INTERFACE"
DESCRIPTION = "User interace for homelock functions"
LICENSE = "MIT"

IMAGE_INSTALL += "libstdc++ mtd-utils"
IMAGE_INSTALL += "openssh openssl openssh-sftp-server"
IMAGE_INSTALL += "python3 python3-tkinter"
IMAGE_INSTALL += "python3-pyqt5"

#IMAGE_INSTALL += " \
#    rsync \
#    php \
#    php-cli \
#    php-modphp \
#    phpmyadmin \
#    sqlite3 \   
#    apache2 \
#    "
