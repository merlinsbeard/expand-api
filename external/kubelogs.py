import subprocess
import logging
import requests
import json
import arrow
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class KubeLog(object):
    """
    Wrapper for kubernetes
    """


    def __init__(self, service, namespace, token):
        self.service = service
        self.namespace = namespace
        self.token = token

    def get_replicas(self):
        """Get the repilca names from namespace.

        Return a List containing the replicas names
        """
        logger.warning("get_replicas")
        cmd = (f'kubectl get pods -n {self.namespace} '
               f'| grep {self.service} '
                '| cut -d " " -f1')
        names = subprocess.check_output(cmd, shell=True)
        logger.warning(cmd)
        return names.decode().split()

    def get_replicas_logs(self, replica):
        """Return Logs of a specific replica"""
        cmd = f'kubectl logs -n {self.namespace} {replica}'
        logs = subprocess.check_output(cmd, shell=True)
        logger.warning("Done with logs")
        return logs.decode()

    def post_in_gist(self, logs, replica):
        now = arrow.now()
        now = now.timestamp
        title = f'{self.namespace}-{replica}-{now}.log'
        url = "https://api.github.com/gists"
        headers = {'authorization': f'Basic {self.token}'}
        payload = {
                "description": "the description for this gist",
                "public": False,
                "files": {
                    title: {
                        "content": logs
                                }
                         }
                }
        logger.warning("Posting in gist")
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        return r.json()

