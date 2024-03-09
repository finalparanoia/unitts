from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from libs.handler import gpt_sovits, bert_vits2


app = FastAPI()


app.mount("/files", StaticFiles(directory="./tmp"), name="tmp")


def gen_voice(text: str, text_lang: str, model: str, characher: str):
    if model == "gpt_sovits":
        return gpt_sovits(text, text_lang)
    elif model == "bert_vits2":
        return bert_vits2(text, text_lang, characher)
    else:
        return "invalid model"


@app.get("/gen/{model}/")
async def generate_helper(text: str, model: str , characher: str="lanjiu", text_lang: str="zh"):
    if text:
        return gen_voice(text, text_lang, model, characher)
    return "view docs in /docs"


if __name__ == "__main__":
    from uvicorn import run
    run(app="main:app", host="0.0.0.0", port=8000)
