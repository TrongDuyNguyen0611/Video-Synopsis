<h1 align="center">pcgvs (Potential Collision Graph Video Synopsis)</h1>

![simulation](media/synopsis.gif)

------

- **[Install](#-Install)**
- **[Runing](#-Runing)**
- **[Eval](#-Eval)**

------


## Install

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
```
## Runing

Step1: Object Tracking to generate the file txt information of object 
```bash
!python track.py --source /Test.mp4 --yolo-weights weights/yolov5m.pt --strong-sort-weights osnet_x0_25_msmt17.pt --save-txt 
```
Step2: Custom runing sysnopsis video:

In PCGVS_Main/run_all.py lease add the path for custom dataset:

Input video
```bash
# input_vid="/pcgvs-main/notebooks/Metadata/Video_input/video.mp4"
```
Input image patches crop from detection
```bash
path="/pcgvs-main/notebooks/Metadata/synopsis/patches"
```
Object txt input from deepsort
```bash
input_txt="/pcgvs-main/notebooks/Metadata/data_input_txt_object/test.txt"
```
Output video synopsis path
```bash
output_vid="/pcgvs-main/notebooks/Metadata/synopsis"
```
Input background(if image background does not exist yet runing in notebook 2. Extract Patches and Background)
```bash
input_background="/pcgvs-main/notebooks/Metadata/synopsis/background.png"
```

Runing all for synopsis video:

```bash
python run_all.py
```

Runing step by step in /PCGVS_MAIN/notebooks/notebook_step


