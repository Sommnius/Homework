import xml.etree.ElementTree as ET
import requests
import re
import logger
import json


class Rss:
    @logger.log
    def __init__(self, source: str, limit: int):
        self.link = source
        self.limit = limit
        self.root = ""
        self.feed_title = ""
        self.__str_fields = ["title", "pubDate", "link", "description", "category"]
        self.__media_fields = ["{*}content", "{*}thumbnail", "enclosure"]
        self.items = []
        self.get_items()
        self.feed = {"Feed": self.feed_title,
                     "Link": self.link,
                     }

    @logger.log
    def find_story(self, item: ET.Element) -> dict:
        story = {}
        url_list = []
        for field in self.__str_fields:
            data = item.findtext(field)
            if isinstance(data, str):
                pattern = re.compile("<.*?>")
                clean_str = re.sub(pattern, '', data)
                story.update({field.capitalize(): clean_str})
        for field in self.__media_fields:
            for url in item.findall(field):
                if url is not None:
                    url_list.append(url.get("url"))
        story.update({"Images": ", ".join(url_list)})
        return story

    @logger.log
    def get_items(self):
        xml = requests.get(self.link).text
        self.root = ET.fromstring(xml)
        self.feed_title = self.root.find("./channel/title").text
        for item in self.root.findall(".//item"):
            if self.limit == 0:
                break
            self.items.append(self.find_story(item))
            self.limit -= 1

    @logger.log
    def print_rss(self, print_in_json):
        if print_in_json:
            print(json.dumps([self.feed, self.items], indent=4, ensure_ascii=False))
        else:
            for key, value in self.feed.items():
                print(f"{key}:{value}")
            print()
            for item in self.items:
                for key, value in item.items():
                    print(f"{key}:{value}")
                print()
