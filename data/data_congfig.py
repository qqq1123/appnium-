class global_var:
    #case_id
    ID = '0'
    url = '2'
    run = '3'
    request_way = '4'
    head = '5'
    case_depend = '6'
    data_depend = '7'
    data = '8'
    expect = '9'
    result = '10'
    field_data_depend = '11'



#获取caseid
def get_id():
    return global_var.ID

def get_url():
    return global_var.url

def get_run():
    return global_var.run

def get_request_way():
    return global_var.request_way

def get_head():
    return global_var.head

def get_case_depend():
    return global_var.case_depend

def get_data_depend():
    return global_var.data_depend

def get_data():
    return global_var.data

def get_expect():
    return global_var.expect

def get_request():
    return global_var.result
def get_header_value():
    header = {
        "header":"123456",
        "cookie":"Lirundong"
    }
def get_field_data_depend():
    return global_var.field_data_depend


