from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

posts :list[dict] = [
    {
        "id":1,
        "title":"Harsha",
        "content":"I am really happy to be here",
        "date_posted":"2024-06-10"
    },

    {
        "id":2,
        "title":"John",
        "content":"This is the second post",
        "date_posted":"2024-06-11"
    }
]

@app.get("/" , response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts" , response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['content']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts


