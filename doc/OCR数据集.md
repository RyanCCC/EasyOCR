# OCR数据集

本文档介绍OCR数据集，主要分为文字检测和文字识别的数据集

## 文字检测

### VOC格式的数据集

在本仓库实现的CTPN代码中，训练集文件架构如下图所示，是标准的VOC格式的数据。

![](./src/detection_dataset_voc_structure.png)


训练集的标注文件以`xml`格式保存，如下图所示：

![](./src/detection_dataset_voc.png)
 

`xml`文件中的信息是已经经过分割box的标记：

![](./src/detection_dataset_voc_annotation.png)

可视化的结果如下：

![](./src/demo_split.png)

### mlt数据集

mlt数据集其实跟VOC数据集相似，都是保存分割后的box的坐标。该数据集下包含两个文件夹：`image`和`label`。`image`保存的是图像数据，`label`保存的是标签数据。其中`label`数据如下图所示：

![](./src/detection_dataset_mlt.png)


![](./src/detection_dataset_mlt_label.png)


### paddleOCR 文字检测

PaddleOCR 中的文本检测算法支持的标注文件格式如下，中间用"\t"分隔：

```
" 图像文件名                    json.dumps编码的图像标注信息"
ch4_test_images/img_61.jpg    [{"transcription": "MASA", "points": [[310, 104], [416, 141], [418, 216], [312, 179]]}, {...}]
```

![](./src/detection_dataset_ctw1500.png)

![](./src/detection_dataset_ctw1500_label.png)

### 其他数据集

1. [ICDAR 2015](https://rrc.cvc.uab.es/?ch=4&com=downloads)
2. [total text](https://paddleocr.bj.bcebos.com/dataset/total_text.tar)


## 参考

1. [mlt数据集](https://github.com/eragonruan/text-detection-ctpn)

2. [VOC数据集](https://github.com/YCG09/chinese_ocr/tree/master/ctpn、https://github.com/xiaofengShi/CHINESE-OCR/tree/master/ctpn/ctpn)

3. [OCR数据介绍](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_ch/dataset/ocr_datasets.md)