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
    
    status = await airos.get_local_status()
    print(status)

if __name__ == "__main__":
    asyncio.run(main())