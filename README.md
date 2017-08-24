# Pre-process images for Deep Learning


Sometimes, we have not enough images for training in Deep Learning if we using ourself datasets.

I create this small program to process images for getting more training datasets.

After processing, you could get 8x images for training.


# Demo

## Origin Image:

<img src="./images/1.jpg" width="30%">

## Generate Images:

<img src="./images/1_180.jpg" width="30%"> <img src="./images/1_180_fip.jpg" width="100"> <img src="./images/1_180_mirror.jpg" width="100">  

<img src="./images/1_270.jpg" width="100"> <img src="./images/1_90.jpg" width="100"> <img src="./images/1_90_fip.jpg" width="100"> <img src="./images/1_90_mirror.jpg" width="100">


## Usage
`python main.py -d=images_dir`


## Processing

1. rotate 90, 180, 270
2. flip
3. mirror

