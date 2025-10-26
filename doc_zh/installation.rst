============
安装
============

Trollimage 可以通过 conda-forge（通过 conda）、PyPI（通过 pip）或从源代码（通过 pip+git）获得。
以下说明显示如何安装 trollimage 的稳定版本或从源代码安装。

基于 Conda 的安装
========================

可以通过从 conda-forge 频道安装包来将 Trollimage 安装到 conda 环境中。如果您还没有
访问 conda 安装的权限，我们建议安装
`miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ 以获得最小和最简单的安装。

以下命令将使用 ``-c conda-forge`` 来确保从 conda-forge 频道下载包。
或者，您可以通过运行以下命令告诉 conda 始终使用 conda-forge：

.. code-block:: bash

    $ conda config --add channels conda-forge

在新的 conda 环境中
--------------------------

我们建议为您使用 trollimage 的工作创建一个单独的环境。要创建一个新环境
并一次性安装 trollimage，您可以运行：

.. code-block:: bash

    $ conda create -c conda-forge -n my_trollimage_env python trollimage

然后，您必须激活该环境，以便任何将来的 python 或 conda 命令将使用此环境。

.. code-block::

    $ conda activate my_trollimage_env

这种创建安装了 trollimage（以及可选的其他包）的环境的方法通常可以比先创建
环境然后再安装 trollimage 和其他包（请参阅下面的部分）更快地创建。

在现有环境中
--------------------------

.. note::

    建议在首次探索 trollimage 时，创建一个专门用于此目的的新环境，
    而不是修改用于其他工作的环境。

如果您已经有一个 conda 环境，它已激活，并且您想将 trollimage 安装到其中，
请运行以下命令：

.. code-block:: bash

    $ conda install -c conda-forge trollimage

基于 Pip 的安装
======================

Trollimage 可从 Python 包索引（PyPI）获得。可以使用
`Virtualenv <http://pypi.python.org/pypi/virtualenv>`_ 为 ``trollimage`` 创建沙箱环境。

要安装 `trollimage` 包和最少的 python 依赖项：

.. code-block:: bash

    $ pip install trollimage

从源代码安装
===================

要直接从 github 安装到现有环境（基于 pip 或 conda）：

.. code-block:: bash

    $ pip install git+https://github.com/pytroll/trollimage.git

如果您已安装 ``git`` 命令，这将自动下载源代码并将其安装到当前环境中。
如果您想修改 trollimage 的本地副本并立即在您的环境中看到效果，请改用以下命令。
此命令应从 git 仓库克隆版本的根目录（``setup.py`` 所在的位置）运行：

.. code-block::

    $ pip install -e .
