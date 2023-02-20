from typing import Union, List
from sqlalchemy.orm import class_mapper


def get_filters(model, filters, filters_non_equals):
    filter_by = {}

    for filter_ in filters: 
        if not filter_ in list(filters_non_equals.keys()):
            filter_by[filter_] = {'operator':'eq','column':filter_, 'value':filters[filter_]}
        elif filters_non_equals[filter_] == 'transacciones':
            filter_by[filter_] = {'operator':None,'column':'transacciones', 'value':{'operator':'eq','column':filter_,'value':filters[filter_]}}
        elif filters_non_equals[filter_] == 'between':
            filter_by[filter_] = {'operator':'between','column':filter_, 'value':filters[filter_]}
        elif filters_non_equals[filter_] == 'neq':
            filter_by[filter_] = {'operator':'neq','column':filter_, 'value':filters[filter_]}

    mapper = class_mapper(model)
    filters = []
    for k, v in filter_by.items():
        filters.append(get_filters_orm(model, v, mapper))

    return filters

def get_filters_orm(model, v, mapper):
    if 'transacciones' in v['column']:
        result = model.transacciones.has(**{v['value']['column']:v['value']['value']})
    elif 'eq' == v['operator']:
        result = mapper.columns[v['column']].__eq__(v['value'])
    elif 'neq' == v['operator']:
        result = mapper.columns[v['column']].__ne__(v['value'])
    elif 'between' == v['operator']:
        result = mapper.columns[v['column']].between(v['value'][0],v['value'][1])
    return result

def genera_respuesta(
        data: Union[dict, List] = None,
        # page: int = None,
        # limit: int = None,
        # total_rows: int = None,
        method: str = "GET",
):
    if data is None:
        data = {}
    elif isinstance(data, dict):
        data = data.__dict__

    response = {
        "data": data,
    }

    # if page is not None:
    #     response["page"] = page
    # if limit is not None:
    #     response["limit"] = limit
    # if total_rows is not None:
    #     response["total_rows"] = total_rows
    if method == "GET":
        response["appCode"] = "PRD-1"
        response["ztCode"] = 2001
        response["message"] = "Resource queried successfully"
    elif method == "POST":
        response["appCode"] = "PRD-1"
        response["ztCode"] = 2011
        response["message"] = "Resource created successfully"
    elif method == "PATCH" or method == "PUT":
        response["appCode"] = "PRD-1"
        response["ztCode"] = 2001
        response["message"] = "Resource updated successfully"
    elif method == "DELETE":
        response["appCode"] = "PRD-1"
        response["ztCode"] = 2001
        response["message"] = "Resource deleted successfully"
    elif method == "NOTFOUND":
        response["appCode"] = "PRD-1"
        response["ztCode"] = 4041
        response["message"] = "Resource Not Found"
        
    elif method == "SERVER":
        response["appCode"] = "PRD-1"
        response["ztCode"] = 5001
        response["message"] = "Unexpected error"


    return response
