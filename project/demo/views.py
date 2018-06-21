from django.shortcuts import render
from django.http import HttpResponse

import cloudinary.uploader
import cloudinary.utils


def index(request):
    return HttpResponse(
        '<p>index view</p>'
        + str(cloudinary.utils.cloudinary_url(
            "lake.jpg",
            width=100,
            height=150,
            crop="fill"))
    )

def upload(request):
    return HttpResponse(
        '<p>upload view</p>'
        # + str(cloudinary.uploader.upload('demo/public/lake.jpg'))
        + str(cloudinary.uploader.upload(
            "https://1.bp.blogspot.com/-_0JXDpvIF1U/WaxcVIT7HxI/AAAAAAAAAnM/gSfCaKXo79ACEHN2LiERWPUV4nSGyYcsACLcBGAs/s1600/4_fraktal3608ab310dc594c738706a02f4962899f.jpg",
            public_id = 'sample_remote'))
        + str(cloudinary.utils.cloudinary_url('sample_remote'))
    )

def cleanup(request):
    # img = cloudinary.CloudinaryImage("demo/public/lake", format="jpg")
    #
    # return HttpResponse(
    #     '<p>cleanup view</p>'
    #     + img.build_url(width=100, height=100, crop="fill")   # http://res.cloudinary.com/cloud_name/image/upload/c_fill,h_100,w_100/sample.png
    #     + '<br>'
    #     + img.image(width=100, height=100, crop="fill")   # <img src="http://res.cloudinary.com/cloud_name/image/upload/c_fill,h_100,w_100/sample.png" width="100" height="100"/>
    # )
    context = dict(
    )
    return render(request, 'upload.html', context)

