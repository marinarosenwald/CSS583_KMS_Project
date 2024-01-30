from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
import os

from models import Definition, DefinitionUpdate

router = APIRouter()

@router.post("/", response_description="Define a word", status_code=status.HTTP_201_CREATED, response_model=Definition)
def create_word(request: Request, word: Definition = Body(...)):
    word = jsonable_encoder(word)
    new_word = request.app.database[os.getenv("DB_DEFINITION_TAG")].insert_one(word)
    created_word = request.app.database[os.getenv("DB_DEFINITION_TAG")].find_one(
        {"_id": new_word.inserted_id}
    )

    return created_word


@router.get("/", response_description="List all words", response_model=List[Definition])
def list_words(request: Request):
    words = list(request.app.database[os.getenv("DB_DEFINITION_TAG")].find())
    return words


@router.get("/{id}", response_description="Get a single word by id", response_model=Definition)
def find_word(id: str, request: Request):
    if (word := request.app.database[os.getenv("DB_DEFINITION_TAG")].find_one({"_id": id})) is not None:
        return word

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word with ID {id} not found")


@router.put("/{id}", response_description="Update a Definition", response_model=Definition)
def update_word(id: str, request: Request, word: DefinitionUpdate = Body(...)):
    word = {k: v for k, v in word.model_dump().items() if v is not None}

    if len(word) >= 1:
        update_result = request.app.database[os.getenv("DB_DEFINITION_TAG")].update_one(
            {"_id": id}, {"$set": word}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word with ID {id} not found")

    if (
        existing_word := request.app.database[os.getenv("DB_DEFINITION_TAG")].find_one({"_id": id})
    ) is not None:
        return existing_word

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word with ID {id} not found")


@router.delete("/{id}", response_description="Delete a word")
def delete_word(id: str, request: Request, response: Response):
    delete_result = request.app.database[os.getenv("DB_DEFINITION_TAG")].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word with ID {id} not found")