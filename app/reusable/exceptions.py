# Thirdy Imports
class OPException(Exception):
    def __init__(self, payload=None, data=None):
        Exception.__init__(self)
        if data is None:
            data = []
        self.zt_code = payload["zt_code"]
        self.app_code = payload["app_code"]
        self.message = payload["message"]
        self.status_code = payload["status_code"]
        self.data = data

    def to_dict(self):
        response = {"zt_code": self.zt_code, "app_code": self.app_code, "message": self.message, "data": self.data}
        return response


