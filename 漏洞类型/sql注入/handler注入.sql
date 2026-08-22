handler 库名.表名 open;(如果没有入库打开表格的时候前面加上库名就行)
handler 表名 read first;
将handler指针重置到第一行开始读取
handler 表名 read first limit 行数;
一次性读取几行,且总是从第一行开始读取;

handler 表名 read next;
handler指针指向下一行,且无法回到上一行,如果下一行为空就不会显示
handler 表名 read next limit 行数;
一次性读取几行,从上次读取行数的下一行开始;

handler 表名 close;
关闭handler指针