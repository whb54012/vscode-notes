<?php
print_r(scandir(getcwd()));
echo __DIR__;
print(scandir(__DIR__))[2];
print(current(get_included_files()));
?>