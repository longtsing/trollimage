# Sphinx 文档的 Makefile
#

# 您可以从命令行设置这些变量。
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# 内部变量。
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest

help:
	@echo "请使用 \`make <target>'，其中 <target> 是以下之一"
	@echo "  html       生成独立的 HTML 文件"
	@echo "  dirhtml    在目录中生成名为 index.html 的 HTML 文件"
	@echo "  singlehtml 生成单个大型 HTML 文件"
	@echo "  pickle     生成 pickle 文件"
	@echo "  json       生成 JSON 文件"
	@echo "  htmlhelp   生成 HTML 文件和 HTML 帮助项目"
	@echo "  qthelp     生成 HTML 文件和 qthelp 项目"
	@echo "  devhelp    生成 HTML 文件和 Devhelp 项目"
	@echo "  epub       生成 epub"
	@echo "  latex      生成 LaTeX 文件，您可以设置 PAPER=a4 或 PAPER=letter"
	@echo "  latexpdf   生成 LaTeX 文件并通过 pdflatex 运行它们"
	@echo "  text       生成文本文件"
	@echo "  man        生成手册页"
	@echo "  changes    概述所有已更改/添加/弃用的项目"
	@echo "  linkcheck  检查所有外部链接的完整性"
	@echo "  doctest    运行嵌入在文档中的所有 doctest（如果启用）"

clean:
	-rm -rf $(BUILDDIR)/*
	-rm -rf api/*.rst
	-rm -rf _static/colormaps/*.png

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "构建完成。HTML 页面在 $(BUILDDIR)/html 中。"

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "构建完成。HTML 页面在 $(BUILDDIR)/dirhtml 中。"

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "构建完成。HTML 页面在 $(BUILDDIR)/singlehtml 中。"

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "构建完成；现在您可以处理 pickle 文件。"

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "构建完成；现在您可以处理 JSON 文件。"

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "构建完成；现在您可以在 $(BUILDDIR)/htmlhelp 中运行 HTML Help Workshop" \
	      "与 .hhp 项目文件。"

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "构建完成；现在您可以在 $(BUILDDIR)/qthelp 中运行 "qcollectiongenerator"" \
	      "与 .qhcp 项目文件，如下所示："
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/TrollImage.qhcp"
	@echo "要查看帮助文件："
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/TrollImage.qhc"

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "构建完成。"
	@echo "要查看帮助文件："
	@echo "# mkdir -p $$HOME/.local/share/devhelp/TrollImage"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/TrollImage"
	@echo "# devhelp"

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "构建完成。epub 文件在 $(BUILDDIR)/epub 中。"

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "构建完成；LaTeX 文件在 $(BUILDDIR)/latex 中。"
	@echo "在该目录中运行 \`make' 以通过 (pdf)latex 运行这些文件" \
	      "（在此处使用 \`make latexpdf' 自动执行此操作）。"

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "通过 pdflatex 运行 LaTeX 文件..."
	make -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex 完成；PDF 文件在 $(BUILDDIR)/latex 中。"

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "构建完成。文本文件在 $(BUILDDIR)/text 中。"

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "构建完成。手册页在 $(BUILDDIR)/man 中。"

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "概述文件在 $(BUILDDIR)/changes 中。"

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "链接检查完成；在上面的输出中查找任何错误" \
	      "或在 $(BUILDDIR)/linkcheck/output.txt 中。"

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "源代码中 doctest 的测试完成，请查看" \
	      "$(BUILDDIR)/doctest/output.txt 中的结果。"
