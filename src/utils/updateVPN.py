class updaterVPN:

    def updateFILE(self,url,port,status,path_vpn):
        successful = ""
        msg = ""
        if status: 
            try:
                PATH = path_vpn
                with open(PATH,'r',encoding='utf-8') as f:
                    data = f.readlines()
                    print("[+] Actual URL: " + data[3])
            except Exception:
                successful = False
                pass

            f_url = data[3].split(" ")[1]
            f_port = data[3].split(" ")[2]
            successful = True
            
            if f_url == url and f_port == port:
                msg = "[+] Nothing to Do"
                
                print(msg)
            else:
                data[3] = "remote {} {} \n".format(url,port)
                with open(PATH, 'w', encoding='utf-8') as file:
                    file.writelines(data)
                msg = "[+] File Updated: " + data[3]
                print(msg)
        return {
            'msg' : msg,
            'status' : successful
        }