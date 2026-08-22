handler 库名.表名 open;(如果没有入库打开表格的时候前面加上库名就行)
handler 表名 read first;
将handler指针重置到第一行开始读取

handler 表名 read next;
handler指针指向下一行,如果下一行没有数据就返回空

handler 表名 close;