# automate finding error 500

$edit_file = '/var/www/html/wp-settings.php'

#replace phpp with php

exec { 'replacement_line':
  command => "sed -i 's/phpp/php/g' ${edit_file}",
  path    => shell,
}
