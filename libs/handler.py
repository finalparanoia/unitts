from libs.text import process_string
from requests import post
from json import dumps, loads
from libs.utils import download_audio
from shutil import move


endpoint = "http://127.0.0.1"


def bert_vits2(text: str, text_lang, characher):
    try:
        resp = post(f"{endpoint}:7860/run/predict", dumps(
            {
                "data": [text, characher, 0.5, 0.6, 0.9, 1, text_lang.upper(), None, "Happy", "Text prompt", "", 0.7],
                "event_data": None, "fn_index": 0, "session_hash": "9xnxbtz0ei"
            }))
        gen_tmp_path = loads(resp.text)["data"][1]["name"]
        dst_tmp_path = f"./tmp/{process_string(text)}.wav"
        move(gen_tmp_path, dst_tmp_path)
        return dst_tmp_path
    except Exception as e:
        print(e)


def gpt_sovits(text: str, text_lang):
    try:
        uri = f"{endpoint}:9880/?prompt_language=zh&text={process_string(text)}&text_language={text_lang}"
        save_path = f"./{process_string(text)}.wav"
        download_audio(uri, save_path)
        return save_path
    except Exception as e:
        print(e)
