# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class ScrapymangaPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
import mimetypes
import os
import hashlib
from scrapy.utils.python import to_bytes


class CustomImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
            media_guid = (f'{request.url.split("/")[-3]}_{request.url.split("/")[-2]}')
            print(media_guid)
            media_ext = f'page_{request.url.split("/")[-1]}'
            print(media_ext)
            # Handles empty and wild extensions by trying to guess the
            # mime type then extension or default to empty string otherwise
            # if media_ext not in mimetypes.types_map:
            #     media_ext = ''
            #     media_type = mimetypes.guess_type(request.url)[0]
            #     if media_type:
            #         media_ext = mimetypes.guess_extension(media_type)
            return f'full/{media_guid}/{media_ext}' 