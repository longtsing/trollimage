# 中文文档构建测试脚本

此脚本用于测试中文文档是否可以正确构建。

## 测试步骤

1. 确保已安装必要的依赖：
   ```bash
   pip install sphinx sphinx-rtd-theme sphinxcontrib-apidoc
   ```

2. 进入中文文档目录：
   ```bash
   cd doc_zh
   ```

3. 清理之前的构建（如果有）：
   ```bash
   # Linux/Mac
   make clean
   
   # Windows
   make.bat clean
   ```

4. 构建 HTML 文档：
   ```bash
   # Linux/Mac
   make html
   
   # Windows
   make.bat html
   ```

5. 检查构建结果：
   - 查看 `_build/html/` 目录是否存在
   - 打开 `_build/html/index.html` 查看文档
   - 检查所有页面是否正确显示中文内容
   - 检查色图图片是否正确生成在 `_static/colormaps/` 目录

## 预期结果

- ✅ 所有页面内容均为中文
- ✅ 导航菜单显示中文
- ✅ 色图图片正确生成
- ✅ API 文档正确生成
- ✅ 所有链接正常工作
- ✅ 搜索功能正常

## 常见问题

### 问题 1：找不到 trollimage 模块

**解决方案**：确保已安装 trollimage 包：
```bash
pip install -e ..
```

### 问题 2：找不到 sphinx 主题

**解决方案**：安装 sphinx_rtd_theme：
```bash
pip install sphinx-rtd-theme
```

### 问题 3：API 文档没有生成

**解决方案**：安装 sphinxcontrib-apidoc：
```bash
pip install sphinxcontrib-apidoc
```

### 问题 4：色图图片没有生成

**解决方案**：确保 trollimage 包已正确安装，并且可以导入 colormap 模块。
