# &#9889; OpenCv Image Manipulator
### v 1.0

*Apply OpenCv filters on your image with command line.*

## Operations
At the moment, the filter avaibles are:

- **Average**
- **Median**
- **Gaussian**
- **Bilateral**

## How to use it?
```python main.py [image_name] [filter_name] [kernel_size] [optional_arguments...]```

### Here some examples:
 ```
    python main.py lena.jpg average 5
    python main.py lena.jpg median 3
    python main.py lena.jpg gaussian 5 -sx 10 -sy 5
    python main.py lena.jpg bilateral 3 -d 9 -sc 75 -ss 75
```

## Disclaimer

I wrote this program just for fun. It has not been tested.

## Enjoy it! &#128540;
