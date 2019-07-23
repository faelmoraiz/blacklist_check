import requests

apiUrl = 'https://api.hetrixtools.com/v2/<API>/blacklist-check/ipv4/'

def check(ip):
    result = requests.get(apiUrl+ip+'/').json()
    try:
        if result['blacklisted_count'] > 0:
            for y in result['blacklisted_on']:
                print(ip, y)
                f = open('lista.txt', 'a')
                f.write(ip+' '+str(y)+'\n')
                f.close()
        else:
            print(ip +' - CLEAN!!')
    except Exception as e:
        print(e)
        pass
        
def main():
    ip = '192.168.0.'
    
    for x in range(1,255):
        check(ip+str(x))
        print()

if __name__ == "__main__":
    main()
