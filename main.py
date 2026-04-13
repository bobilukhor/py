from fastapi import FastAPI

# Create the FastAPI app object.
app = FastAPI(
    title="My API app",
    description="This is my first endpoint API.",
)

@app.get("/newsupdate")
async def get_newsupdate():
    
    ## Endpoint used when a client sends a GET request to /newsupdate.
    return [
        {
        
        "title": "Heavy traffic in M50!",  # News headline.
        "likes": 22  # Number of likes from users.
        },
        {
        "title": "Rain expected this evening",  
        "likes": 30 
        }, 
        {
        "title": "Summer Sales start this weekend",
        "likes": 87
        }
        ]
