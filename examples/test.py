from pyairos import AirOSApi
import asyncio

host = "https://localhost"
username = "CHANGEME"
password = "CHANGEME"
verify = False

async def main():

    airos = AirOSApi(host, verify=verify)
    is_logged_in = await airos.login(username, password)

    if not is_logged_in:
        print("Failed to login")
        return
    
    ping = await airos.ping()

    if not ping:
        print("Ping failed")
        return
    print("Ping successful")
    
    status = await airos.get_local_status()
    print(status)

if __name__ == "__main__":
    asyncio.run(main())