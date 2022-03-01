def bookEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "category":item["category"],
        "author":item["author"],
        "pages":item["pages"]
    }
    
def booksEntity(entity)-> list:
    return [bookEntity(item) for item in entity]
    