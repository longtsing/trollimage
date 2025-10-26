# TrollImage 中文文档 - 快速参考

## 文件清单

### 配置文件
- `conf.py` - Sphinx 配置文件（已设置中文语言）
- `trollimage_colormap.py` - 自定义 Sphinx 指令，用于生成色图图片

### 构建脚本
- `Makefile` - Linux/Mac 构建脚本
- `make.bat` - Windows 构建脚本

### 文档文件
- `index.rst` - 首页
- `installation.rst` - 安装指南
- `colormap.rst` - 色图文档

### 示例文件
- `examples/utilities-examples.py` - 工具函数示例代码
- `examples/hrv.rgb` - 示例数据文件
- `examples/setvak.rgb` - 示例数据文件

### 静态资源
- `_static/hayan.png` - 首页展示图片
- `_static/hayan_simple.png` - 简单示例图片
- `_static/my_cm.png` - 自定义色图示例
- `_static/phayan.png` - 调色板示例图片
- `_static/colormaps/` - 色图图片存放目录（构建时自动生成）

### 自动生成目录
- `api/` - API 文档自动生成目录
- `_build/` - 构建输出目录（构建时生成）

## 与原文档的对应关系

| 原文档 (doc/) | 中文文档 (doc_zh/) | 翻译状态 |
|--------------|-------------------|---------|
| index.rst | index.rst | ✅ 已翻译 |
| installation.rst | installation.rst | ✅ 已翻译 |
| colormap.rst | colormap.rst | ✅ 已翻译 |
| conf.py | conf.py | ✅ 已翻译并配置中文 |
| trollimage_colormap.py | trollimage_colormap.py | ✅ 注释已翻译 |
| Makefile | Makefile | ✅ 帮助信息已翻译 |
| - | make.bat | ✅ 新增 Windows 支持 |
| examples/utilities-examples.py | examples/utilities-examples.py | ✅ 注释已翻译 |
| examples/*.rgb | examples/*.rgb | ✅ 已复制 |
| _static/*.png | _static/*.png | ✅ 已复制 |

## 关键配置更改

### conf.py 中的语言设置
```python
# 设置文档语言为简体中文
language = 'zh_CN'
```

### 其他配置保持一致
- 项目名称：TrollImage
- 版本号：与主包版本一致
- 主题：sphinx_rtd_theme
- 扩展：autodoc, intersphinx, napoleon, apidoc, trollimage_colormap

## 构建命令快速参考

### HTML 文档
```bash
make html          # Linux/Mac
make.bat html      # Windows
```

### 清理构建
```bash
make clean         # Linux/Mac
make.bat clean     # Windows
```

### 其他格式
```bash
make latexpdf      # PDF 文档
make epub          # EPUB 电子书
make singlehtml    # 单页 HTML
make linkcheck     # 检查链接
```

## 文档更新工作流

1. 更新文档源文件（.rst 文件）
2. 运行 `make clean` 清理旧构建
3. 运行 `make html` 重新构建
4. 在浏览器中查看 `_build/html/index.html`
5. 确认更改无误后提交

## 注意事项

1. **自动生成内容**：
   - API 文档在每次构建时自动从源代码生成
   - 色图图片在首次构建时自动生成

2. **依赖要求**：
   - Python 3.x
   - Sphinx
   - sphinx-rtd-theme
   - sphinxcontrib-apidoc
   - trollimage（需要先安装项目本身）

3. **文件编码**：
   - 所有 .rst 文件使用 UTF-8 编码
   - 所有 .py 文件使用 UTF-8 编码

4. **兼容性**：
   - 完全兼容 Sphinx 标准构建流程
   - 可以使用所有 Sphinx 支持的输出格式
