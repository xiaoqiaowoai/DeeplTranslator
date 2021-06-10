#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author:kouguozhao  作者
# FileName:deepl_translator  文件名称
# DateTime:2021/6/10 13:08  当前时间
# SoftWare: PyCharm  创建文件的IDE名称


import requests
import json
import time


class DeeplTranslator:

    request_data = {
        "id": int(time.time()),
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "commonJobParams": {"formality": None},
            "jobs": [{
                "kind": "default",
                "raw_en_sentence": "",
                "raw_en_context_before": [],
                "raw_en_context_after": [],
                "preferred_num_beams": 4,
                "quality": "fast"
            }],
            "lang": {
                "user_preferred_langs": [],
                "source_lang_user_selected": "auto",
                "target_lang": ""
            },
            "priority": -1,
            "timestamp": int(time.time())
        }
    }

    headers = {
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "content-type": "application/json",

    }

    request_url = "https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs"

    def __init__(self, target_lang, source_context):
        self.request_data["params"]["jobs"][0]["raw_en_sentence"] = source_context
        self.request_data["params"]["lang"]["target_lang"] = target_lang

    def translate(self):
        resp = requests.post(url=self.request_url, data=json.dumps(self.request_data,ensure_ascii=False), headers=self.headers)
        print(resp)
        print(resp.text)
        response_text_dict = json.loads(resp.text)
        result = response_text_dict["result"]["translations"][0]["beams"][0]["postprocessed_sentence"]
        return result


if __name__ == '__main__':
    deepl_translator = DeeplTranslator(source_context="hello world", target_lang="ZH")
    result = deepl_translator.translate()
    print(result)
