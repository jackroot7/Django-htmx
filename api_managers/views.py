from ninja import NinjaAPI
from utils.API_schemas import *
api = NinjaAPI()


@api.post("/submit_fuel_usage", response = Response)
def submit_fuel_usage(request, input: UsageInputSchema):
    
    return Response.get_status_code(id=1)



@api.post("/change_config", response = Response)
def change_device_config(request, input: ConfigInputSchema):
    
    
    return Response.get_status_code(id=1)



@api.post("/change_config", response = Response)
def change_device_config(request, input: ConfigInputSchema):
    
    
    return Response.get_status_code(id=1)