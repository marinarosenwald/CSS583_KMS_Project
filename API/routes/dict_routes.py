from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
import os

from models import Definition, DefinitionUpdate

dict_router = APIRouter()

@dict_router.post("/", response_description="Define a word", status_code=status.HTTP_201_CREATED, response_model=Definition)
def create_word(request: Request, word: Definition = Body(...)):
    search_word = word.word
    """if (found_word := request.app.database[os.getenv("DEFINITION_TAG")].find_one({"word": search_word})) is not None:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Word: {search_word} already exists")
    """
    word = jsonable_encoder(word)
    
    """new_word = request.app.database[os.getenv("DEFINITION_TAG")].insert_one(word)
    created_word = request.app.database[os.getenv("DEFINITION_TAG")].find_one(
        {"_id": new_word.inserted_id}
    )"""

    created_word = { 
        "_id": "1",
        "word": "a",
        "definition": "b",
        "keywords": [],
    }   

    return created_word


@dict_router.get("/", response_description="List all words", response_model=List[Definition])
def list_words(request: Request):
    # words = list(request.app.database[os.getenv("DEFINITION_TAG")].find())
    words = [{ 
        "_id": "1",
        "word": "a",
        "definition": "b",
        "keywords": [],
    }, { 
        "_id": "2",
        "word": "c",
        "definition": "d",
        "keywords": [],
    }] 
    return words


@dict_router.get("/{id}", response_description="Get a single word by id", response_model=Definition)
def find_word_by_id(id: str, request: Request):
    """if (found_word := request.app.database[os.getenv("DEFINITION_TAG")].find_one({"_id": id})) is not None:
        return found_word
    """
    found_word = { 
        "_id": "1",
        "word": "a",
        "definition": "b",
        "keywords": [],
    }   

    return found_word

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word with ID {id} not found")

@dict_router.get("/word/{word}", response_description="Get a single word by word", response_model=Definition)
def find_word_by_word(word: str, request: Request):
    """if (found_word := request.app.database[os.getenv("DEFINITION_TAG")].find_one({"word": word})) is not None:
        return found_word
    """
    found_word = { 
        "_id": "1",
        "word": "a",
        "definition": "b",
        "keywords": [],
    }   
    return found_word
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word: {word} not found")


@dict_router.put("/{id}", response_description="Update a Definition", response_model=Definition)
def update_word(id: str, request: Request, word: DefinitionUpdate = Body(...)):
    word = {k: v for k, v in word.model_dump().items() if v is not None}

    if len(word) >= 1:
        """
        update_result = request.app.database[os.getenv("DEFINITION_TAG")].update_one(
            {"_id": id}, {"$set": word}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word with ID {id} not found")
        """
        found_word = { 
            "_id": "1",
            "word": "a",
            "definition": "b",
            "keywords": [],
        }   
        return found_word
    """
    if (
        existing_word := request.app.database[os.getenv("DEFINITION_TAG")].find_one({"_id": id})
    ) is not None:
        return existing_word
    """
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word with ID {id} not found")


@dict_router.delete("/{id}", response_description="Delete a word")
def delete_word(id: str, request: Request, response: Response):
    """delete_result = request.app.database[os.getenv("DEFINITION_TAG")].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    """
    response.status_code = status.HTTP_204_NO_CONTENT
    return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Word with ID {id} not found")

