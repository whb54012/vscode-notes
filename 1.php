<?php
print_r(scandir(getcwd()));
echo __DIR__;
print_r(scandir(__DIR__));
print(current(get_included_files()));
?>