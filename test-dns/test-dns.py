import socket
def status_dns()
    try: 
        add1=socket.gethostbyname('control-plane-1")
        print("success")
    except Exception as err:
        print(err)

def main()
    status_dns()
                                  
if __name__ == '__main__':
    (main())
