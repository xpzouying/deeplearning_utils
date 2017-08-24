# Pre-process images for Deep Learning


Sometimes, we have not enough images for training in Deep Learning if we using ourself datasets.

I create this small program to process images for getting more training datasets.

After processing, you could get 8x images for training.


# Demo

Origin Image:

![origin](images/1.jpg)

Generate Images:

- <img src="./images/1_180.jpg", width="100">
- <img src="./images/1_180_fip.jpg", width="100">
- <img src="./images/1_180_mirror.jpg", width="100">
- <img src="./images/1_270.jpg", width="100">
- <img src="./images/1_90.jpg", width="100">
- <img src="./images/1_90_fip.jpg", width="100">
- <img src="./images/1_90_mirror.jpg", width="100">


- ![1_180](images/1_180.jpg)
- ![1_180_fip](images/1_180_fip.jpg)
- ![1_180_mirror](images/1_180_mirror.jpg)
- ![1_270](images/1_270.jpg)
- ![1_90](images/1_90.jpg)
- ![1_90_fip](images/1_90_fip.jpg)
- ![1_90_mirror](images/1_90_mirror.jpg)


## Usage
`python main.py -d=images_dir`


## Processing

1. rotate 90, 180, 270
2. flip
3. mirror

