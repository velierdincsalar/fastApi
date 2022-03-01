def registerEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "userId":str(item["userId"]),
        "bookId":str(item["bookId"]),
        "employeeId":str(item["employeeId"]),
        "startDate":str(item["startDate"]),
        "endDate":str(item["endDate"])
    }
    
def registersEntity(entity)-> list:
    return [registerEntity(item) for item in entity]