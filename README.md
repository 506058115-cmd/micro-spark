# micro-spark

把每行一个数字变成一行终端微型图表，适合快速扫一眼小型时间序列。

## 使用

需要 Python 3.8+，不安装依赖。

```sh
python micro_spark.py values.txt
```

也可以用管道输入：

```sh
printf '2\n4\n3\n9\n' | python micro_spark.py
```

输入是一行一个有限数字；空行会跳过。没有指定文件时从标准输入读取。
如果当前输出编码无法表示 Unicode 图块，会自动改用 ASCII 字符。

## 许可

MIT，见 [LICENSE](LICENSE)。
## Linux x86_64 下载

- [单文件版](https://github.com/506058115-cmd/micro-spark/releases/download/v1.0.0/micro-spark-linux-x86_64-onefile.tar.gz)
- [目录版](https://github.com/506058115-cmd/micro-spark/releases/download/v1.0.0/micro-spark-linux-x86_64-onedir.tar.gz)
- [v1.0.0 Release 页面](https://github.com/506058115-cmd/micro-spark/releases/tag/v1.0.0)

压缩包附带构建信息和依赖许可证；Release 另附 SHA-256 校验文件。产物在 WSL Ubuntu 24.04（Python 3.12.3、PyInstaller 6.22.2）中构建，目标为 GNU/Linux x86_64。较旧的发行版可能需要兼容的 glibc。
