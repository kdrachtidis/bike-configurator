from datetime import datetime

msg_init = "Bike Configurator API:"  # API logs identifier

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_print(*args, **kwargs):
    timestamp = get_timestamp()
    if (args) == ("read",):
        print(f"[{timestamp}] {msg_init} Reading {kwargs.get('obj_type', '')} with id = {kwargs.get('obj_id', '')}.")
    elif (args) == ("read_by_group",):
        print(f"[{timestamp}] {msg_init} Reading {kwargs.get('obj_type', '')}s under group with id = {kwargs.get('group_id', '')}.")
    elif (args) == ("read_all",):
        print(f"[{timestamp}] {msg_init} Reading all {kwargs.get('obj_type', '')}s.")
    elif (args) == ("create",):
        print(f"[{timestamp}] {msg_init} Creating {kwargs.get('obj_type', '')}.")
    elif (args) == ("update",):
        print(f"[{timestamp}] {msg_init} Updating {kwargs.get('obj_type', '')} with id = {kwargs.get('obj_id', '')}.")
    elif (args) == ("delete",):
        print(f"[{timestamp}] {msg_init} Deleting {kwargs.get('obj_type', '')} with id = {kwargs.get('obj_id', '')}.")
    else:
        print(f"[{timestamp}]", *args, "is not recognized as argument.")

# HTTPException details messages

def log_exception(*args, **kwargs):
    if (args) == ("type",):
        return f"No bike type with id = {kwargs.get('obj_id', '')}." 
    elif (args) == ("group",):
        return f"No assembly group with id = {kwargs.get('obj_id', '')}."
    elif (args) == ("module",):
        return f"No assembly group module with id = {kwargs.get('obj_id', '')}." 
    elif (args) == ("component",):
        return f"No bike component with id = {kwargs.get('obj_id', '')}."
    else:
        return "Unknown object type for exception message."
    