import os
import cv2
import glob
import json
import shutil
import datetime
import argparse
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt


def make_unit_image(wavefile, imagefile, config):

    # parse config
    is_showlabel        = config['is_showlabel']
    label_size          = config['label_size']
    label_color         = config['label_color']
    label_alpha         = config['label_alpha']
    helical_edge_color  = config['helical_edge_color']
    vartical_edge_color = config['vartical_edge_color']
    background_color    = config['background_color']
    line_color          = config['line_color']
    yrange              = config['yrange']
    dpi                 = config['dpi']
    xsize_per_second    = config['xsize_per_second']
    ysize               = config['ysize']

    signaldata, samplerate = sf.read(wavefile)
    num_channel = len(signaldata.shape)
    if num_channel != 1:
        signaldata = signaldata.mean(axis=1)
    num_signals = len(signaldata)
    times = np.arange(num_signals) / samplerate

    x0, x1 = 0, times[-1]
    y0, y1 = yrange
    xs, ys = times, signaldata
    fig = plt.figure(figsize=(times[-1]*xsize_per_second, ysize))
    ax = fig.add_axes((0,0,1,1))
    ax.axis('off')
    ax.tick_params(bottom=False,left=False,right=False,top=False)
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)

    # show background color
    ax.fill_between([x0,x1],[y0,y0],[y1,y1],
                    facecolor=background_color)

    # show helical,vartical linep
    ax.plot([x0,x0], [y0, y1], color=vartical_edge_color)
    ax.plot([x1,x1], [y0, y1], color=vartical_edge_color)
    ax.plot([x0,x1], [y0, y0], color=helical_edge_color)
    ax.plot([x0,x1], [y1, y1], color=helical_edge_color)

    # show label
    if is_showlabel:
        label_text = wavefile.split('/')[-1]
        label_xpos = 0.1
        label_ypos = yrange[0]*0.9 + yrange[1]*0.1
        ax.text(label_xpos,
                 label_ypos,
                 label_text,
                 fontsize=label_size,
                 color=label_color)

    # show signal line
    ax.plot(xs, ys, color=line_color)

    plt.savefig(imagefile, dpi=dpi)
    plt.close()

def marge_images(imagefiles, outfile, config):
    # parse config
    aspect = config['aspect']
    imagefile = os.path.abspath(outfile)
    ims = []
    for f in imagefiles:
        # print(f)
        ims.append(cv2.imread(f))
        im = cv2.hconcat(ims)

    num_ydots, num_xdots, _ = im.shape
    # print('num x dots : '+str(num_xdots))
    # print('num y dots : '+str(num_ydots))
    num_row = int(np.sqrt(num_ydots*num_xdots*aspect)/num_ydots)
    np_x_add = num_row - num_xdots % num_row
    im = np.concatenate([im,
         np.zeros(num_ydots*3*np_x_add).reshape(num_ydots, np_x_add, 3)], axis=1)
    num_ydots, num_xdots, _ = im.shape
    # print(np_x_add)
    # print(im.shape)
    im_stacked = np.concatenate(
        np.array([im.reshape(num_ydots,num_row, num_xdots//num_row,3)[:,i,:,:]
                  for i in range(num_row)]))
    # print(im_stacked.shape)
    cv2.imwrite(imagefile,im_stacked)

