# FacesInVideo
extract frams from video and face recognition


# install
install opencv and dlib
then 
```
 pip install -r requirements.txt

```

# usage
```
Usage: main.py [OPTIONS]

Options:
  --path TEXT       path to video file
  --fps INTEGER     fps for file
  --rotate INTEGER  rotate before processing
  --help            Show this message and exit.
```


eg :python main.py --path securepos-bonesio1.20180103.114256.mp4 --rotate 180 --fps 2


and then you can check frams and faces in the current folder
