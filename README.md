<h1 align="center"> PCGVS (Potential Collision Graph Video Synopsis)</h1>

# Introduction

Video synopsis is an intelligent condensation approach to solve fast video browsing and retrieval for surveillance cameras. However, collision caused by unsatisfied tube rearrangement in traditional methods brings uncomfortable visual effect to users and how to mitigate the collision still remains an attracting topic. Unlike conventional methods that deal with tube rearrangement by minimizing a global energy function, we propose a novel approach by formulating it as a graph coloring problem. 



<img width="1000" alt="Screen Shot 2022-09-23 at 00 14 12" src="https://user-images.githubusercontent.com/81319640/198190180-59b99859-63d8-495c-9273-919854f5c30d.png">



In this approach, all the tubes are firstly mapped into the spatial domain for analyzing their potential collision relationship. The input tube set is then represented by a graph structure, where each node stands for a tube and the edge between two nodes represents the potential collision relationship. To mitigate the collision artifacts,that method finds the mapping of tubes from original video to synopsis video by L(q)-coloring the graph, which separates tubes from their collision points. The parameter q is left tunable to make a compromise between collision artifacts and synopsis length, which can better meet users demand of freely adjusting the compactness of synopsis video. The shifted objects are finally composited with the background image to obtain the high-quality video synopsis.

------

- **[Install](#-Install)**
- **[Quickstart](#-Quickstart)**
- **[Eval](#-Eval)**
- **[CLI](#-CLI)**
- **[Bibliography](#Bibliography)**

------

# Install

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
# Quickstart

Step1: Object Tracking to generate the file txt information of object 
```bash
!python track.py --source /Test.mp4 --yolo-weights weights/yolov5m.pt --strong-sort-weights osnet_x0_25_msmt17.pt --save-txt 
```
Step2: Custom runing sysnopsis video:

In PCGVS_Main/run_all.py lease add the path for custom dataset:

Input video
```bash
input_vid="/pcgvs-main/notebooks/Metadata/Video_input/video.mp4"
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
Input background (if image background does not exist yet runing in notebook 2. Extract Patches and Background)
```bash
input_background="/pcgvs-main/notebooks/Metadata/synopsis/background.png"
```

Runing all for synopsis video:

```bash
python run_all.py
```

Runing step by step in /PCGVS_MAIN/notebooks/notebook_step
# Eval

Evaluated through the following metric: FR,CR,OR

Input original video:
```bash
vpath ="/pcgvs-main/notebooks/Metadata/Video_input/video.mp4"
```
Input synopsis video:
```bash
spath ="./synopsis/synopsis.avi"
```
Evalue 3 metric:
```bash
python eval.py
```
To visualization runing /notebook_step/ 5. Video Synopsis on synthetic data.ipynb

<img width="540" alt="Screen Shot 2022-10-27 at 11 22 02" src="https://user-images.githubusercontent.com/81319640/198190950-c5d23c4f-2c10-4e73-9c8b-7fb46fa9ab46.png">


# CLI

```bash
$ python .\cli.py --help
Usage: cli.py [OPTIONS]

Options:
  -i TEXT                 Source video path  [required]
  -o TEXT                 Path of the synopsis folder  [required]
  -q INTEGER              q parameter of L(q)-coloring problem.  [default: 3]
  -t INTEGER              Threads used in Strong Sort algorithm.  [default: 1]
  -c FLOAT                Confidence threshold for Yolov5.  [default: 0.15]
  --interp / --no-interp  Interpolates the missing bounding boxes
  --help                  Show this message and exit.
```
# Bibliography
```
@article{HeGSQH17,  
  title 	= {Graph coloring based surveillance video synopsis},  
  author 	= {Yi He and Changxin Gao and Nong Sang and Zhiguo Qu and Jun Han},  
  year 		= {2017},  
  doi 		= {10.1016/j.neucom.2016.11.011},  
  url 		= {http://dx.doi.org/10.1016/j.neucom.2016.11.011},  
  researchr 	= {https://researchr.org/publication/HeGSQH17},  
  cites 	= {0},  
  citedby 	= {0},  
  journal 	= {Neurocomputing},  
  volume 	= {225},  
  pages 	= {64-79}, 
}
```
