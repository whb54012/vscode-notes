

文件查看
1.highlight_file("相对/绝对文件名路径"); 高亮打印文件内容
2.show_source("相对/绝对文件名路径"); 同上
3.readfile("相对/绝对文件名路径"); 输出文件原始内容
4.echo file_get_contents("相对/绝对文件名路径"); 打开文件,需手动echo打印
5.file("相对/绝对文件名路径"); 返回数组
6.$f=fopen("相对/绝对文件名路径","r");
echo fread($f,读取字节数); 打开文件去读取文件原始内容,需手动echo打印

打印函数
var_dump(); 显示类型 + 值,万能
print_r(); 打印数组类型
echo ; 打印普通数据类型