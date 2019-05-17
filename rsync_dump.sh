#!/bin/bash

# shop
rsync --progress --exclude=.example --delete-before -azv /var/www/shop/na_dump/dump mylab@mylab.babah24.ru::mylab/shop
rsync --progress --exclude=CACHE --exclude=syncapp_tmp --delete-before -azv /var/www/shop/media mylab@mylab.babah24.ru::mylab/shop

# crm
rsync --progress --exclude=.example --delete-before -azv /var/www/shop/na_dump/dump mylab@mylab.babah24.ru::mylab/shop