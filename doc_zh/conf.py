# -*- coding: utf-8 -*-
#
# TrollImage 文档构建配置文件，由
# sphinx-quickstart 于 2013年12月2日 09:40:29 创建。
#
# 此文件在其包含目录设置为当前目录的情况下被 execfile() 执行。
#
# 请注意，并非所有可能的配置值都出现在此
# 自动生成的文件中。
#
# 所有配置值都有默认值；被注释掉的值
# 用于显示默认值。

import os
import sys
from trollimage import __version__

# 如果要使用 autodoc 记录的扩展（或模块）位于另一个目录中，
# 请在此处将这些目录添加到 sys.path。如果目录相对于
# 文档根目录，请使用 os.path.abspath 使其绝对，如下所示。
# sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# -- 一般配置 -----------------------------------------------------

# 如果您的文档需要最低的 Sphinx 版本，请在此处声明。
# needs_sphinx = '1.0'

# 在此处添加任何 Sphinx 扩展模块名称，作为字符串。它们可以是
# Sphinx 附带的扩展（名为 'sphinx.ext.*'）或您自定义的扩展。
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx',
              'sphinx.ext.napoleon', 'sphinxcontrib.apidoc', "trollimage_colormap"]
# API 文档
apidoc_module_dir = "../trollimage"
apidoc_output_dir = "api"
apidoc_excluded_paths = []

# 在此处添加包含模板的任何路径，相对于此目录。
templates_path = ['_templates']

# 源文件名的后缀。
source_suffix = '.rst'

# 源文件的编码。
# source_encoding = 'utf-8-sig'

# 主 toctree 文档。
master_doc = 'index'

# 关于项目的一般信息。
project = u'TrollImage'
copyright = u'2018, The Pytroll Team'

# 您正在记录的项目的版本信息，用作
# |version| 和 |release| 的替换，也在
# 构建文档的各个其他地方使用。
#

# 简短的 X.Y 版本。
short_version = ".".join(__version__.split(".")[:2])
# 完整版本，包括 alpha/beta/rc 标签。
release = short_version

# Sphinx 自动生成内容的语言。有关
# 支持的语言列表，请参阅文档。
language = 'zh_CN'

# 有两个选项可以替换 |today|：要么，将 today 设置为某个
# 非 false 值，然后使用它：
# today = ''
# 否则，today_fmt 用作 strftime 调用的格式。
# today_fmt = '%B %d, %Y'

# 相对于源目录的模式列表，用于匹配在查找源文件时要忽略的文件和目录。
exclude_patterns = ['_build']

# 用于所有文档的 reST 默认角色（用于此标记：`text`）。
# default_role = None

# 如果为 true，'()' 将附加到 :func: 等交叉引用文本。
# add_function_parentheses = True

# 如果为 true，当前模块名称将添加到所有描述
# 单元标题的前面（例如 .. function::）。
# add_module_names = True

# 如果为 true，sectionauthor 和 moduleauthor 指令将显示在
# 输出中。默认情况下它们被忽略。
# show_authors = False

# 要使用的 Pygments（语法高亮）样式的名称。
pygments_style = 'sphinx'

# 用于模块索引排序的忽略前缀列表。
# modindex_common_prefix = []


# -- HTML 输出选项 ---------------------------------------------------

# 用于 HTML 和 HTML Help 页面的主题。有关内置主题的列表，请参阅文档。
html_theme = 'sphinx_rtd_theme'

# 主题选项是特定于主题的，并进一步自定义主题的外观和感觉。
# 有关每个主题可用选项的列表，请参阅文档。
# html_theme_options = {}

# 在此处添加包含自定义主题的任何路径，相对于此目录。
# html_theme_path = []

# 此 Sphinx 文档集的名称。如果为 None，则默认为
# "<project> v<release> documentation"。
# html_title = None

# 导航栏的较短标题。默认与 html_title 相同。
# html_short_title = None

# 要放置在侧边栏顶部的图像文件（相对于此目录）的名称。
# html_logo = None

# 要用作文档 favicon 的图像文件（在静态路径内）的名称。
# 此文件应为 Windows 图标文件（.ico），大小为 16x16 或 32x32 像素。
# html_favicon = None

# 在此处添加包含自定义静态文件（如样式表）的任何路径，
# 相对于此目录。它们在内置静态文件之后复制，
# 因此名为 "default.css" 的文件将覆盖内置的 "default.css"。
html_static_path = ['_static']

# 如果不为 ''，则使用给定的 strftime 格式在每个页面底部插入 'Last updated on:' 时间戳。
# html_last_updated_fmt = '%b %d, %Y'

# 如果为 true，将使用 SmartyPants 将引号和破折号转换为
# 印刷正确的实体。
# html_use_smartypants = True

# 自定义侧边栏模板，将文档名称映射到模板名称。
# html_sidebars = {}

# 应呈现到页面的其他模板，将页面名称映射到模板名称。
# html_additional_pages = {}

# 如果为 false，则不生成模块索引。
# html_domain_indices = True

# 如果为 false，则不生成索引。
# html_use_index = True

# 如果为 true，则将索引拆分为每个字母的单独页面。
# html_split_index = False

# 如果为 true，则将指向 reST 源的链接添加到页面。
# html_show_sourcelink = True

# 如果为 true，则在 HTML 页脚中显示 "Created using Sphinx"。默认为 True。
# html_show_sphinx = True

# 如果为 true，则在 HTML 页脚中显示 "(C) Copyright ..."。默认为 True。
# html_show_copyright = True

# 如果为 true，将输出 OpenSearch 描述文件，并且所有页面都将
# 包含引用它的 <link> 标记。此选项的值必须是
# 从中提供完成的 HTML 的基本 URL。
# html_use_opensearch = ''

# 这是 HTML 文件的文件名后缀（例如 ".xhtml"）。
# html_file_suffix = None

# HTML 帮助构建器的输出文件基本名称。
htmlhelp_basename = 'TrollImagedoc'


# -- LaTeX 输出选项 --------------------------------------------------

# 纸张大小（'letter' 或 'a4'）。
latex_paper_size = 'a4'

# 字体大小（'10pt'、'11pt' 或 '12pt'）。
# latex_font_size = '10pt'

# 将文档树分组为 LaTeX 文件。元组列表
# (源起始文件, 目标名称, 标题, 作者, 文档类 [howto/manual])。
latex_documents = [
  ('index', 'TrollImage.tex', u'TrollImage 文档',
   u'The Pytroll Team', 'manual'),
]

# 要放置在标题页顶部的图像文件（相对于此目录）的名称。
# latex_logo = None

# 对于 "manual" 文档，如果这为 true，则顶级标题是部分，
# 而不是章节。
# latex_use_parts = False

# 如果为 true，则在内部链接后显示页面引用。
# latex_show_pagerefs = False

# 如果为 true，则在外部链接后显示 URL 地址。
# latex_show_urls = False

# LaTeX 前导码的附加内容。
# latex_preamble = ''

# 要作为附录附加到所有手册的文档。
# latex_appendices = []

# 如果为 false，则不生成模块索引。
# latex_domain_indices = True


# -- 手册页输出选项 --------------------------------------------

# 每个手册页一个条目。元组列表
# (源起始文件, 名称, 描述, 作者, 手册部分)。
man_pages = [
    ('index', 'trollimage', u'TrollImage 文档',
     [u'The Pytroll Team'], 1)
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'xarray': ('https://docs.xarray.dev/en/stable', None),
    'dask': ('https://dask.pydata.org/en/latest', None),
    'rasterio': ('https://rasterio.readthedocs.io/en/latest', None),
}
