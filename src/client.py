from utils import ngrok
from utils import updateVPN
from utils import vpnActioner
from utils import cameraUtil
from configparser import ConfigParser
import os

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, "config/config.ini")
config = ConfigParser()
config.read(initfile)

NGROK_API = config.get("default","ngrok_api")
path_vpn = config.get("default","path_vpn")
path_openvpn = config.get("default","path_openvpn")

def connectVPN():
    msg = ""
    status = ""
    
    tunnel = ngrok.NgrokTunnel()
    url = tunnel.getNgrokTunnel(NGROK_API)

    if url["status"]:
        adress = url["url"]
        port = url["port"]

        update = updateVPN.updaterVPN()
        updateStatus = update.updateFILE(adress,port,True,path_vpn)

        if updateStatus["status"]:
            vpn = vpnActioner.VPN()
            vpn.upVPN(path_vpn,path_openvpn)
        else:
            print("[!] No es posible conectarse la VPN Magenta")

    else:
        print("[!] Conexión no exitosa el Tunnel Magenta")
    
    return {
            "msg" : msg,
            "status" : status
        }

def takePhoto():
    camera = cameraUtil.ColliCameras()
    cam = camera.takePhoto2()
    print("[+] Se tomo una fotografía del porton")
    print(cam)
    
    return cam

def openDoor():
    pass

def tomarFoto():

    connect = connectVPN()
    if connect["status"]:
        photo = takePhoto()
        if photo["status"]:
            print("[+] Fotografia tomada con exito")

tomarFoto()