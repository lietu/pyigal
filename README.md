# Pyigal - Pythonized Image Gallery

Pyigal is a tool to generate simple and nice looking HTML image galleries from your image collections.


## How does it work?

You put your images in the image folder (site/images by default) and run the tool. Pyigal will scan the folder for images and then proceeds to generate thumbnails out of them and a HTML file with links to all the images.

The thumbnail sizes and the HTML template are easy to configure via the config.py -file. By default the site will show 400x400 thumbnails of your images and opens 1280x1280 versions in a gallery dialog when clicking them. The dialog will have a download link to the original version.

The default system uses Fancybox and jinja2 templates with Python Image Library to generate the HTML galleries.


## What do I need to do?

1. Install Python (likely you'll want 32bit) [http://www.python.org/download/](http://www.python.org/download/)
1. Install Python Image Library [http://www.pythonware.com/products/pil/](http://www.pythonware.com/products/pil/)
1. Download Pyigal
1. Edit config.py and/or templates/index.html to taste (Optional)
1. Create the folder site/images (or whatever you configured) and put your images in it
1. Run "python pyigal.py" or double-click on pyigal.py
1. Publish all files and folders under sites/ to the web

If you add/remove pictures, it is enough to just rerun Pyigal to generate any missing thumbnails and update the HTML. If you update pictures, you will have to manually delete the thumbnail(s) for it to be regenerated.


## How about licensing?

Short answer: new BSD, and MIT. Long answer: Read the LICENSE -file