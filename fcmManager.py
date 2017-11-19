# Send to single device.
from pyfcm import FCMNotification
from flask import request

class fcmManager:
    def __init__(self):
        self._request = request.args
        pass

    push_service = FCMNotification(api_key="AAAA92s0PRQ:APA91bHFZT1syIKAqrga2favcykb3zZ2XoGCJYRlImPHFrb45afs9PgsxRB0uuWLQIMncquaZ3TXlA_6rHqYwG-DLnJw1FQW6McvTK0NYVyP4U_ROVeMLs_eL_iTIAUYnTpug3O5tNUJ")

    # OR initialize with proxies

    # proxy_dict = {
    #           "http"  : "http://127.0.0.1",
    #           "https" : "http://127.0.0.1",
    #         }
    # push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

    def send(self):
        registration_id = self._request.get("id", "")
        message_title = self._request.get("t", "")
        message_body = self._request.get("b", "")
        message_from = self._request.get("f", "")
        result = fcmManager.push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                                   message_body=message_body, message_from=message_from)
        return result
