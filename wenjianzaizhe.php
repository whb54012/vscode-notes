<?php
header("Content-Disposition: attachment; filename=flag_is_here.docx");
header("Content-Type: application/octet-stream");
readfile('flag_is_here.docx');
?>