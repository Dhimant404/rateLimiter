from fastapi import APIRouter

from app.core.wait import delayed_reply

router = APIRouter()

@router.get("/fetchData")
async def read_data():
    # Function that waits 10 seconds before sending back a reply 
    delayed_reply(5)
    return {"message": "The data was sucsfully fetched !"}

# @router.post("/example")
# async def create_example(item: dict):
#     return {"message": "Example item created.", "item": item}

# @router.put("/example/{item_id}")
# async def update_example(item_id: int, item: dict):
#     return {"message": "Example item updated.", "item_id": item_id, "item": item}

# @router.delete("/example/{item_id}")
# async def delete_example(item_id: int):
#     return {"message": "Example item deleted.", "item_id": item_id}