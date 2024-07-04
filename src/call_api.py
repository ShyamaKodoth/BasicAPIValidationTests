import requests


def api(method, url, payload=None):
    json_response = response = None
    headers = {"Content-Type": "application/json"}

    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            if type(payload) is list or type(payload) is tuple:
                response = requests.post(url, headers=headers, json=payload)
            else:
                response = requests.post(url, headers=headers, data=payload)
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=payload)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            print("Please check the Request Method Again!")

    except Exception as error:
        print(error)
        print("The call to URL: %s , Method: %s failed with Response: %s"
            % (url, method, str(response))
        )

    return response
