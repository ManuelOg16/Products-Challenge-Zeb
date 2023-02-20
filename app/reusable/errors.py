"""
Errores Products DataBase
"""

PR_01 = {
    "app_code": "PR-01",
    "message": "transaction not found",
    "zt_code": 4041,
    "status_code": 404,
}

PR_406 = {
    "app_code": "PR-01",
    "message": "Not Acceptable Delete Super Admin",
    "zt_code": 4041,
    "status_code": 406,
}

PR_404 = {
    "app_code": "PRD-01",
    "zt_code": 4041,
    "status_code": 404,
    "message": "Not Found",
    "data": {},
}
PR_409 = {
    "app_code": "PRD-01",
    "zt_code": 4042,
    "status_code": 409,
    "message": "Resource Already Exists",
    "data": {},
}
PR_422 = {
    "app_code": "PRD-01",
    "zt_code": 4022,
    "status_code": 422,
    "message": "Error, Select a Valid Catalog_id For This Product ",
    "data": {},
}

PR_500 = {
    "app_code": "PRD-500",
    "zt_code": 5001,
    "status_code": 500,
    "message": "Unexpected error",
    "data": {},
}

