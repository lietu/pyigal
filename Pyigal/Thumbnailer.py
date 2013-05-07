# -*- coding: utf-8 -*-

import os
import Image
import sys


class Thumbnailer(object):
    config = None
    image_list = None

    def set_config(self, config):
        self.config = config

    def set_image_list(self, image_list):
        self.image_list = image_list

    def create_thumbnails(self):

        # Make sure the destination directories exist
        for thumbnail_config in self.config["thumbnails"]:
            if not os.path.exists(thumbnail_config["destination"]):
                os.mkdir(thumbnail_config["destination"])

        image = None

        for source in self.image_list:
            source_path = os.path.join(self.config["image_path"], source)

            for thumbnail_config in self.config["thumbnails"]:

                destination_path = os.path.join(
                    thumbnail_config["destination"],
                    source
                )

                # Skip existing thumbnails
                if (os.path.exists(destination_path)):
                    sys.stdout.write("-")
                #    print "%(src)s -> %(dst)s ... skipped" % \
                #        {"src": source_path, "dst": destination_path}
                    continue

                sys.stdout.write(".")

                #print "%(src)s -> %(dst)s" % \
                #    {"src": source_path, "dst": destination_path}

                # Open the source file
                if image is None:
                    image = Image.open(source_path)

                # Resize according to config
                size = (
                    thumbnail_config["width"],
                    thumbnail_config["height"]
                )

                thumb = image.copy()
                thumb.thumbnail(size, Image.ANTIALIAS)

                # Save destination file
                thumb.save(destination_path)

            # Clear the image
            image = None

        print ""
