目录文件查找
glob("*"); 正则匹配,通过通配符来查找当前目录符合条件的文件,可通过../来逃逸
$变量=opendir(".")用变量接收当前目录的所有文件
whilereaddir()+closedir()
highlight_file("相对/绝对文件名路径");
readfile("相对/绝对文件名路径")
file_get_contents("相对/绝对文件名路径")