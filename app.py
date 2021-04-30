from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

sensordb = []

class SensorIn(BaseModel):
    address: str
    name: str

class Sensor(BaseModel):
    id: int
    address: str
    name: str

@app.post("/sensors")
def add_sensor(sensor_in: SensorIn) -> Sensor:
    sensordb.append(sensor_in)
    sensor_out_dict = sensordb[-1].dict()
    sensor_out_dict.update({"id": len(sensordb)-1})
    return Sensor(**sensor_out_dict)

@app.get("/sensors")
def get_sensors():
    return sensordb


@app.get("/sensors/{sensor_id}")
def get_sensor(sensor_id: int):
    sensor = sensor_id 
    return sensordb[sensor]

@app.post("/sensors/{sensor_id}")
def update_sensor(sensor_id: int, sensor: Sensor):
    sensordb[sensor_id] = sensor
    return {"message": "Sensor has been updated succesfully"}

@app.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: int):
    sensordb.pop(sensor_id-1)
    return {"message": "Sensor has been deleted succesfully"}

