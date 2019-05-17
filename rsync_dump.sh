#!/bin/bash

# shop
#rsync --progress --delete-before -azv /var/www/shop/na_dump/dump mylab@mylab.babah24.ru::mylab/shop
#rsync --progress --exclude=CACHE --exclude=syncapp_tmp --delete-before -azv /var/www/shop/media mylab@mylab.babah24.ru::mylab/shop

# crm
rsync --progress --delete-before -azv /var/www/crmdata/dump mylab@mylab.babah24.ru::mylab/crm
rsync --progress --exclude=CACHE --exclude=additionalphoto --exclude=buyer_anketa --exclude=cashreportfile --exclude=corpmailfile --exclude=docflowfile --exclude=goodscert_pdf --exclude=librarybook --exclude=materialvalue --delete-before -azv /var/www/crm/media mylab@mylab.babah24.ru::mylab/crm