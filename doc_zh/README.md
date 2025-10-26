# TrollImage 中文文档

这是 TrollImage 项目的中文文档目录，包含了所有必要的文件来构建完整的中文版文档。

## 目录结构

```
doc_zh/
├── api/                      # API 文档自动生成目录
├── examples/                 # 示例文件
│   ├── hrv.rgb
│   ├── setvak.rgb
│   └── utilities-examples.py
├── _static/                  # 静态资源
│   ├── colormaps/           # 色图图片（自动生成）
│   ├── hayan.png
│   ├── hayan_simple.png
│   ├── my_cm.png
│   └── phayan.png
├── colormap.rst             # 色图文档
├── conf.py                  # Sphinx 配置文件
├── index.rst                # 文档首页
├── installation.rst         # 安装说明
├── Makefile                 # Linux/Mac 构建文件
├── make.bat                 # Windows 构建文件
└── trollimage_colormap.py   # 自定义 Sphinx 指令
```

## 构建文档

### 在 Linux/Mac 上

```bash
cd doc_zh
make html
```

### 在 Windows 上

```cmd
cd doc_zh
make.bat html
```

### 查看文档

构建完成后，在浏览器中打开 `_build/html/index.html` 文件查看文档。

## 与原 doc 目录的区别

1. **语言设置**：`conf.py` 中设置了 `language = 'zh_CN'`
2. **内容翻译**：所有 `.rst` 文档文件都已翻译成中文
3. **注释翻译**：Python 文件中的注释也已翻译成中文
4. **帮助信息**：Makefile 和 make.bat 中的帮助信息都已翻译成中文

## 完全替代性

此中文文档目录 `doc_zh` 可以完全替代原 `doc` 目录来构建中文版本的文档：

- ✅ 包含所有必要的配置文件
- ✅ 包含所有文档源文件
- ✅ 包含所有示例文件
- ✅ 包含所有静态资源
- ✅ 支持所有构建目标（html、latex、epub 等）
- ✅ 使用相同的 Sphinx 扩展和主题

## 维护说明

当原英文文档更新时，需要同步更新此中文文档以保持内容一致性。
