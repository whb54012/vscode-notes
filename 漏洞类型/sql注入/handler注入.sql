handler 库名.表名 open;(如果没有入库打开表格的时候前面加上库名就行)
handler 表名 first;
handler 表名 next;
handler 表名 close;
读取表里的数据,读几行就用几行next