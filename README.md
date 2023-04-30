# langchain-workbook

# run this to start local server
uvicorn main:app --host 127.0.0.1 --port 8000 --reload

# what is working now:
/webhook : takes an input and returns its color demonstrating "few shot" examples

# run this to query to query 
curl -X POST -H "Content-Type: application/json" -d '{"thing": "your_input_here"}' http://127.0.0.1:8000/webhook
