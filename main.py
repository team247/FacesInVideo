#-* coding:UTF-8 -*
#!/usr/bin/env python
import os
import click
from moviepy.editor import *
from PIL import Image
import cv2
import numpy
import face_recognition


def create_if_not_exists(dir_name):
    dir_name = os.path.abspath(dir_name)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


@click.command()
@click.option('--path', default='', help='path to video file')
@click.option('--fps', default=0, help='fps for file')
@click.option('--rotate', default=0, help='rotate before processing')
def process(path, fps, rotate):
    create_if_not_exists('frams')
    create_if_not_exists('faces')
    clip = VideoFileClip(path).rotate(rotate)
    if fps:
        clip = clip.set_fps(fps)
    clip.write_images_sequence("frams/%04d.jpeg")
    frame_count = 0
    for frame in clip.iter_frames():
        print 'process frame', frame_count
        frame_count += 1
        face_locations = face_recognition.face_locations(frame)
        if face_locations:
            print 'found face', face_locations
            frame_copy = numpy.copy(frame)
            for face in face_locations:
                top, right, bottom, left = face
                print top, right, bottom, left
                cv2.rectangle(frame_copy, (left, top),
                              (right, bottom), (0, 0, 255), 2)
            image = Image.fromarray(frame_copy)
            image_path = os.path.join('faces', '%d.png' % frame_count)
            image.save(image_path)


if __name__ == "__main__":
    process()
