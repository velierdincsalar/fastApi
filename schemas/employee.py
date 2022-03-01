def employeeEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "surname":item["surname"],
        "email":item["email"],
        "password":item["password"]
    }
    
def employeesEntity(entity)-> list:
    return [employeeEntity(item) for item in entity]
    