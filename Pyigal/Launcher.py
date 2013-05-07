# -*- coding: utf-8 -*-

import os
import glob
from datetime import datetime
from Thumbnailer import Thumbnailer
from HtmlGenerator import HtmlGenerator


class Launcher(object):
    config = None

    def set_config(self, config):
        self.config = config

    def start(self):
        start_time = datetime.now()

        image_list = self.find_images()

        print "Found %(num)d images, checking thumbnails..." % \
            {'num': len(image_list)}

        print "(- skipped, . generating)"

        thumbnailer = Thumbnailer()
        thumbnailer.set_config(self.config)
        thumbnailer.set_image_list(image_list)
        thumbnailer.create_thumbnails()

        print "Images OK."

        image_data = self.get_image_data(image_list)

        template_params = {
            'image_data': image_data,
            'title': self.config["title"],
            'now': datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")
        }

        generator = HtmlGenerator()

        print "Generating HTML..."

        generator.generate(
            os.path.join(self.config["template_path"], 'index.html'),
            template_params
        )

        print "Saving HTML..."

        generator.save(
            os.path.join(self.config["build_path"], 'index.html')
        )

        end_time = datetime.now()

        elapsed = (end_time - start_time).total_seconds()

        print "All done! Time taken: %(time).3f seconds" % {'time': elapsed}

    def find_images(self):
        image_list = []

        for file in glob.glob(os.path.join(self.config["image_path"], '*')):
            if os.path.isfile(file):
                image_list.append(os.path.basename(file))

        return image_list

    def get_image_data(self, image_list):
        image_data = []
        for image in image_list:
            original = os.path.relpath(
                os.path.join(self.config["image_path"], image),
                self.config["build_path"]
            )

            original = original.replace('\\', '/')

            thumbnails = {}

            for thumbnail_config in self.config["thumbnails"]:
                path = os.path.relpath(
                    os.path.join(thumbnail_config["destination"], image),
                    self.config["build_path"]
                )

                path = path.replace('\\', '/')

                thumbnails[thumbnail_config["template_name"]] = path

            image_data.append({
                'original': original,
                'thumbnails': thumbnails
            })

        return sorted(image_data, cmp=self.image_sort)

    def image_sort(self, first, second):
        return cmp(first["original"], second["original"])
