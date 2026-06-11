from pydantic import BaseModel, validate_call, ValidationError

# class Item(BaseModel):
#   name: str
#   description: str | None = None  # description independent
#   price: float


# create an independent function for validation
@validate_call
def validate_name(name: str):
  return name

try:
  name = validate_name(name='Ali')
  print("Name is valid")
except ValidationError as error:
  print(f"name is invalid {error}")