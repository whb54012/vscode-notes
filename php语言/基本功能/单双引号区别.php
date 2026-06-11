单引号:'内容',会将里面的内容转换成字符串,不具备php解析功能
双引号:"内容",会将里面内容当成字符串,但却具有php解析功能
echo "$_COOKIE";打印cookie变量的值
echo '$_COOKIE';打印字符串"$_COOKIE"
谁在外面就按照谁的规定执行
    echo "hello '$_COOKIE'";会将$_COOKIE解析成变量,并且输出hello和cookie的值
    echo 'hello "$_COOKIE"';会将$_COOKIE当成字符串,输出hello和"$_COOKIE"