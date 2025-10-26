==========
 色图
==========

示例用法
=============

在数据上应用色图的简单示例::

    from trollimage.colormap import rdbu
    from trollimage.image import Image

    img = Image(data, mode="L")

    rdbu.set_range(-90 + 273.15, 30 + 273.15)
    img.colorize(rdbu)

    img.show()

.. image:: _static/hayan_simple.png

一个更复杂的示例，色图由一端的灰度和另一端的光谱色构建而成，如下所示：

.. image:: _static/my_cm.png

::

    from trollimage.colormap import spectral, greys
    from trollimage.image import Image

    img = Image(data, mode="L")

    greys.set_range(-40 + 273.15, 30 + 273.15)
    spectral.set_range(-90 + 273.15, -40.00001 + 273.15)
    my_cm = spectral + greys
    img.colorize(my_cm)

    img.show()

.. image:: _static/hayan.png


现在将调色板应用于数据，具有锐利的边缘::

    from trollimage.colormap import set3
    from trollimage.image import Image

    img = Image(data, mode="L")

    set3.set_range(-90 + 273.15, 30 + 273.15)
    img.palettize(set3)

    img.show()

.. image:: _static/phayan.png

API
===

请参阅 :class:`~trollimage.Colormap` API 文档。

默认色图
=================

颜色来自 www.ColorBrewer.org，由宾夕法尼亚州立大学地理系的 Cynthia A. Brewer 提供。

序列色图
~~~~~~~~~~~~~~~~~~~~

.. trollimage_colormap:: trollimage.colormap.sequential_colormaps

发散色图
~~~~~~~~~~~~~~~~~~~

.. trollimage_colormap:: trollimage.colormap.diverging_colormaps

定性色图
~~~~~~~~~~~~~~~~~~~~~


.. trollimage_colormap:: trollimage.colormap.qualitative_colormaps
   :category:

彩虹色图
~~~~~~~~~~~~~~~~

不要使用这个！请参阅 这里_ 和 那里_ 了解原因

.. _这里: https://www.nature.com/articles/s41467-020-19160-7
.. _那里: https://doi.org/10.1109/MCG.2007.323435

.. trollimage_colormap:: trollimage.colormap.rainbow
