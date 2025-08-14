from fastapi import FastAPI #import kelas FastAPI dari library fastapi

app = FastAPI() #membuat instance aplikasi FastAPI
#app ini yang nanti dipanggil oleh ASGI Server (cth: Uvicorn)
#untuk running API

#return dalam format JSON

@app.get("/")   #dekorator yang bilang ke FastAPI
#kalau ada request GET ke path /, jalankan read_root()
def read_root():
    return{"message": "Kalkulator Resistor API is running"}

@app.get("/resistor")
def calculate_resistor(band1: str, band2: str,
                       multiplier: str, tolerance: str = None):
    #sementara hanya return input
    return{
        "band1" : band1,
        "band2" : band2,
        "multiplier": multiplier,
        "tolerance" : tolerance
    }