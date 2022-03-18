from fastapi import FastAPI
from nepali_to_roman import nep_to_rom
app = FastAPI()


@app.get("/nep-roman/{text}")
async def root(text: str):
    return {"data":nep_to_rom(text)}
