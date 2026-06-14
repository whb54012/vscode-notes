<?php
// 1. 读取外部HTML模板
$tpl = file_get_contents('外部html模板');

$data = [
    '{page_title}'  => '新闻详情页',
    '{news_title}'  => 'PHP模板使用教程',
    '{time}'        => date('Y-m-d H:i:s'),
    '{news_content}' => '这是通过 str_replace 实现的文件模板替换，前后端代码分离。'
];

// 批量替换
$finalHtml = str_replace(array_keys($data), array_values($data), $tpl);

// 输出页面
echo $finalHtml;
?>