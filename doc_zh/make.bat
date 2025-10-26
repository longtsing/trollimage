@ECHO OFF

REM Sphinx 文档的命令文件

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set BUILDDIR=_build
set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% .
if NOT "%PAPER%" == "" (
	set ALLSPHINXOPTS=-D latex_paper_size=%PAPER% %ALLSPHINXOPTS%
)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.请使用 `make ^<target^>` 其中 ^<target^> 是以下之一
	echo.  html       生成独立的 HTML 文件
	echo.  dirhtml    在目录中生成名为 index.html 的 HTML 文件
	echo.  singlehtml 生成单个大型 HTML 文件
	echo.  pickle     生成 pickle 文件
	echo.  json       生成 JSON 文件
	echo.  htmlhelp   生成 HTML 文件和 HTML 帮助项目
	echo.  qthelp     生成 HTML 文件和 qthelp 项目
	echo.  devhelp    生成 HTML 文件和 Devhelp 项目
	echo.  epub       生成 epub
	echo.  latex      生成 LaTeX 文件，您可以设置 PAPER=a4 或 PAPER=letter
	echo.  text       生成文本文件
	echo.  man        生成手册页
	echo.  changes    概述所有已更改/添加/弃用的项目
	echo.  linkcheck  检查所有外部链接的完整性
	echo.  doctest    运行嵌入在文档中的所有 doctest（如果启用）
	goto end
)

if "%1" == "clean" (
	for /d %%i in (%BUILDDIR%\*) do rmdir /q /s %%i
	del /q /s %BUILDDIR%\*
	del /q /s api\*.rst
	del /q /s _static\colormaps\*.png
	goto end
)

if "%1" == "html" (
	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%/html
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成。HTML 页面在 %BUILDDIR%/html 中。
	goto end
)

if "%1" == "dirhtml" (
	%SPHINXBUILD% -b dirhtml %ALLSPHINXOPTS% %BUILDDIR%/dirhtml
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成。HTML 页面在 %BUILDDIR%/dirhtml 中。
	goto end
)

if "%1" == "singlehtml" (
	%SPHINXBUILD% -b singlehtml %ALLSPHINXOPTS% %BUILDDIR%/singlehtml
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成。HTML 页面在 %BUILDDIR%/singlehtml 中。
	goto end
)

if "%1" == "pickle" (
	%SPHINXBUILD% -b pickle %ALLSPHINXOPTS% %BUILDDIR%/pickle
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成；现在您可以处理 pickle 文件。
	goto end
)

if "%1" == "json" (
	%SPHINXBUILD% -b json %ALLSPHINXOPTS% %BUILDDIR%/json
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成；现在您可以处理 JSON 文件。
	goto end
)

if "%1" == "htmlhelp" (
	%SPHINXBUILD% -b htmlhelp %ALLSPHINXOPTS% %BUILDDIR%/htmlhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成；现在您可以在 %BUILDDIR%/htmlhelp 中运行 HTML Help Workshop
	echo.与 .hhp 项目文件。
	goto end
)

if "%1" == "qthelp" (
	%SPHINXBUILD% -b qthelp %ALLSPHINXOPTS% %BUILDDIR%/qthelp
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成；现在您可以在 %BUILDDIR%/qthelp 中运行 "qcollectiongenerator"
	echo.与 .qhcp 项目文件。
	goto end
)

if "%1" == "devhelp" (
	%SPHINXBUILD% -b devhelp %ALLSPHINXOPTS% %BUILDDIR%/devhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成。
	goto end
)

if "%1" == "epub" (
	%SPHINXBUILD% -b epub %ALLSPHINXOPTS% %BUILDDIR%/epub
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成。epub 文件在 %BUILDDIR%/epub 中。
	goto end
)

if "%1" == "latex" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成；LaTeX 文件在 %BUILDDIR%/latex 中。
	goto end
)

if "%1" == "text" (
	%SPHINXBUILD% -b text %ALLSPHINXOPTS% %BUILDDIR%/text
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成。文本文件在 %BUILDDIR%/text 中。
	goto end
)

if "%1" == "man" (
	%SPHINXBUILD% -b man %ALLSPHINXOPTS% %BUILDDIR%/man
	if errorlevel 1 exit /b 1
	echo.
	echo.构建完成。手册页在 %BUILDDIR%/man 中。
	goto end
)

if "%1" == "changes" (
	%SPHINXBUILD% -b changes %ALLSPHINXOPTS% %BUILDDIR%/changes
	if errorlevel 1 exit /b 1
	echo.
	echo.概述文件在 %BUILDDIR%/changes 中。
	goto end
)

if "%1" == "linkcheck" (
	%SPHINXBUILD% -b linkcheck %ALLSPHINXOPTS% %BUILDDIR%/linkcheck
	if errorlevel 1 exit /b 1
	echo.
	echo.链接检查完成；在上面的输出中查找任何错误
	echo.或在 %BUILDDIR%/linkcheck/output.txt 中。
	goto end
)

if "%1" == "doctest" (
	%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest
	if errorlevel 1 exit /b 1
	echo.
	echo.源代码中 doctest 的测试完成，请查看
	echo.%BUILDDIR%/doctest/output.txt 中的结果。
	goto end
)

:end
