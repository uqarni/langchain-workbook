# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from functionz import color_teller

app = FastAPI()

class InputData(BaseModel):  # Create a Pydantic model for the input data
    thing: str

@app.post("/webhook")  # Change the decorator to @app.post
async def webhook_handler(data: InputData):  # Add the InputData model as a parameter
    # Process the "thing" input using your function or any other logic
    output = color_teller(data.thing)  # Access the "thing" value using data.thing

    # Return the output
    return {"output": output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main, host="127.0.0.1", port=8000)
