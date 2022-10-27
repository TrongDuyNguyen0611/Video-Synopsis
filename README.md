<h1 align="center">pcgvs (Potential Collision Graph Video Synopsis)</h1>

![simulation](media/synopsis.gif)

------

- **[Install](#-Install)**
- **[Runing](#-Runing)**

------


## ⚡ Install

Create another conda environment (3.9.12 or 3.9.13): 

```bash
conda create --name pcgvs python=3.9
```

Install the package locally:

```bash
pip install -e .
```
```bash
pip install -r requirements.txt
```
Install detectron2 for segmentation:

```bash
conda install -c conda-forge detectron2
```
Install if you want to run yolov5 deepsort for Object Tracking:
/PCGVS-Main/YoloV5_DeepSort_Pytorch
```bash
pip install -r requirements_DS.txt







Run Notebook step by step in /PCGVS_MAIN/notebooks/notebook_step





