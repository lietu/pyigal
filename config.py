# -*- coding: utf-8 -*-

build_path = "site"
template_path = "templates"
image_path = "site/images"

title = "Page title"

thumbnails = [
    {
        'width': 400,
        'height': 300,
        'destination': "site/images/400x300",
        'template_name': "small"
    },
    {
        'width': 1280,
        'height': 800,
        'destination': "site/images/1280x800",
        'template_name': "large"
    }
]
