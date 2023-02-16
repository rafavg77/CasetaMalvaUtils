import subprocess

class VPN():
    def downVPN(self):
        result = subprocess.run(['sudo', 'killall','openvpn'], stdout=subprocess.PIPE)
        #print(result.stdout.decode('utf-8'))

    def upVPN(self,path_vpn,path_openvpn):
        msg = ""
        status = False

        print("[+] Mantando proceso de VPN")
        self.downVPN()
    
        print("[+] Copiando archivo de VPN")
        p = subprocess.Popen("sudo cp %s %s" % (path_vpn,path_openvpn), stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()

        print("[+] Levantando VPN")
        p = subprocess.Popen("sudo systemctl start openvpn-client@325", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()

        msg = "[+] Conectado a VPN Magenta"
        status = True
        print(msg)

        return {
            "msg" : msg,
            "status" : status
        }