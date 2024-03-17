from fastapi import FastAPI

app = FastAPI()

# GET request
@app.get("/")
async def get_endpoint():
    return {"message": "This is a GET request"}

# POST request
@app.post("/post_endpoint")
async def post_endpoint():
    return {"message": "This is a POST request"}

# PUT request
@app.put("/put_endpoint")
async def put_endpoint():
    return {"message": "This is a PUT request"}

# DELETE request
@app.delete("/delete_endpoint")
async def delete_endpoint():
    return {"message": "This is a DELETE request"}

# PATCH request
@app.patch("/patch_endpoint")
async def patch_endpoint():
    return {"message": "This is a PATCH request"}

# OPTIONS request
@app.options("/options_endpoint")
async def options_endpoint():
    return {"message": "This is an OPTIONS request"}

# HEAD request
@app.head("/head_endpoint")
async def head_endpoint():
    return {"message": "This is a HEAD request"}
