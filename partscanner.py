#@osmanmuratgul

import socket

def port_scan(target_host, target_ports):
    for port in target_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)  #zamanı kendinize göre ayarlayabilirsiniz :)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port} açık")
            sock.close()
        except KeyboardInterrupt:
            print("Tarama işlemi kullanıcı tarafından iptal edildi.......")
            break
        except socket.gaierror:
            print("Geçersiz bir site adresi......")
            break
        except socket.error:
            print("Bağlantı hatası......")
            break

# Örnek kullanım
target_host = input("Taranacak siteyi giriniz...: ") 
target_ports = [80, 443, 8080, 8888]  # Kontrol etmek istediğiniz portları buraya ekleyebilirsiniz :)

port_scan(target_host, target_ports)
