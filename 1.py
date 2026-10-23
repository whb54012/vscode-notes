import sys
print("isatty =", sys.stdout.isatty(), "| line_buffering =", sys.stdout.line_buffering)

for i in range(2):
    print(f"【答案{i}】这行应该出现在提示符【之前】", flush=True)
    x = input("请输入问题")
    if x == "exit":
        break
print("结束")