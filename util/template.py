import math

import simplejson as json
from flask import jsonify


class ReponseTemplate():
    response_template = {
        "success": "Success",
        "data": [],
        "meta": {
            "code": 200,
            "message": "OK",
            "errors": [],
            "pages": {}
        }
    }

    def jsonify_ok_row_response(self, rows, page_index=1, page_size=10, total=0):
        self.response_template['meta']['errors'] = []
        self.response_template['meta']['code'] = 200

        if rows is None:
            self.response_template['data'] = []
        else:
            json_result = [{key.lower(): value for (key, value) in row.items()} for row in rows]
            self.response_template['data'] = json_result

        pages = {"limit": 1, "page": 1, "total": 0, "count": 0}
        pages['limit'] = page_size
        pages['page'] = page_index
        pages['count'] = int(math.ceil(float(total) / page_size))
        pages['total'] = total if total > 0 else len(self.response_template['data'])
        self.response_template['meta']['pages'] = pages

        return jsonify(self.response_template)

    def jsonify_ok_list_response(self, data, page_index=1, page_size=10, total=0):
        self.response_template['meta']['errors'] = []
        self.response_template['meta']['code'] = 200

        if data is None:
            self.response_template['data'] = []
        else:
            json_result = [{key.lower(): value for (key, value) in d.items()} for d in data]
            self.response_template['data'] = json_result

        pages = {"limit": 1, "page": 1, "total": 0, "count": 0}
        pages['limit'] = page_size
        pages['page'] = page_index
        pages['count'] = int(math.ceil(float(total) / page_size))
        pages['total'] = total if total > 0 else len(self.response_template['data'])
        self.response_template['meta']['pages'] = pages

        return jsonify(self.response_template)

    def jsonify_ok_str_response(self, json_str, page_index=1, page_size=10, total=0):
        self.response_template['meta']['errors'] = []
        self.response_template['meta']['code'] = 200

        if json_str is None or json_str == '':
            self.response_template['data'] = []
        else:
            json_result = json.loads(json_str)
            self.response_template['data'] = json_result

        pages = {"limit": 1, "page": 1, "total": 0, "count": 0}
        pages['limit'] = page_size
        pages['page'] = page_index
        pages['count'] = int(math.ceil(float(total) / page_size))
        pages['total'] = total if total > 0 else len(self.response_template['data'])
        self.response_template['meta']['pages'] = pages

        return jsonify(self.response_template)

    def jsonify_ok_obj_response(self, obj, page_index=1, page_size=10, total=0):
        self.response_template['meta']['errors'] = []
        self.response_template['meta']['code'] = 200

        if obj is None:
            self.response_template['data'] = []
        else:
            self.response_template['data'] = obj

        pages = {"limit": 1, "page": 1, "total": 0, "count": 0}
        pages['limit'] = page_size
        pages['page'] = page_index
        pages['count'] = int(math.ceil(float(total) / page_size))
        pages['total'] = total if total > 0 else len(self.response_template['data'])
        self.response_template['meta']['pages'] = pages

        return jsonify(self.response_template)

    def jsonify_ok_df_response(self, df, page_index=1, page_size=10, total=0, orient='records'):
        self.response_template['meta']['errors'] = []
        self.response_template['meta']['code'] = 200

        if df is None:
            self.response_template['data'] = []
        else:
            json_str = df.to_json(orient=orient)
            json_result = json.loads(json_str)
            self.response_template['data'] = json_result

        pages = {"limit": 1, "page": 1, "total": 0, "count": 0}
        pages['limit'] = page_size
        pages['page'] = page_index
        pages['count'] = int(math.ceil(float(total) / page_size))
        pages['total'] = total if total > 0 else len(self.response_template['data'])
        self.response_template['meta']['pages'] = pages

        return jsonify(self.response_template)

    def jsonify_bad_response(self, errors, code):
        self.response_template['meta']['errors'] = errors
        self.response_template['meta']['code'] = code
        self.response_template['data'] = []
        self.response_template['meta']['pages'] = {}
        return jsonify(self.response_template)
