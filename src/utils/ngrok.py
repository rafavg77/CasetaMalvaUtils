import requests

class NgrokTunnel:

    def getNgrokTunnel(self,API_TOKEN):
        public_url = ''
        url = ''
        port = ''

        try:
            url = "https://api.ngrok.com/endpoints"
            headers = {"Ngrok-Version":"2","Authorization":"Bearer %s" % (API_TOKEN)}
            response = requests.get(url,headers=headers)
            endpoints = response.json()["endpoints"]
            
            if len(endpoints) > 0:
                endpoint = endpoints[0]

                public_url = endpoint["public_url"]
                public_url = public_url.replace("tcp://","")
                public_url = public_url.split(":")

                url = public_url[0]
                port = public_url[1]
                successful = True
            else:
                successful = False

        except requests.exceptions.Timeout as errc:
            print("Timeout Erro: ",errc)

        return {
            'url' : url,
            'port' : port,
            'status' : successful 
        }