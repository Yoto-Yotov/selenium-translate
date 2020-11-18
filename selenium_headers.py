import time

from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--disable-infobars')
options.add_argument("--lang=en")

SELENIUM_PREFS = {
    "translate": {"enabled": "true"},
    "translate_whitelists": {
        "af": "en",
    },
}

options.add_experimental_option("prefs", SELENIUM_PREFS)
chromedriver = "/home/yoto/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chromedriver, options=options)

driver.header_overrides = {
        'authority': 'seekingalpha.com',
        'sec-ch-ua': '"Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/'
                       '537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'),
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9,bg;q=0.8',
        'if-none-match': 'W/"ec172ce1e1d2e8467f3b847b1111ee56"',
        'referer': 'https://google.com',
        # 'cookie': 'machine_cookie=0287085854713; _pxvid=57e6bca2-f29c-11ea-b6fb-0242ac120004; _ga=GA1.2.910425039.1599656390; cto_bundle=JqV2kl9lcXAxV2slMkIlMkJkWlhRSk91ViUyRlNTSWN3QXpDN1A4MEYlMkZNOXlSWFFrcklEd2toZWoyciUyQkdMaHg1JTJGaDBMODlyanVOODcyaG9ReVhSUlA3dzNIV3k3dkY0bG56Z3MydW9HMUhaJTJGZWdJRWZkaVJJWXBsJTJCOSUyRldqMkd3TU5iSUh0TVc3VzRaOUFsSVdsVSUyRk5mc3YlMkZ5VnN4N1V3JTNEJTNE; _gcl_au=1.1.1439439214.1599656391; __tbc=%7Bjzx%7DlCp-P5kTOqotpgFeypItnDVbmfRjvTJ0LYhF5vK8ESRgdjf75qzwiQ4bVrh3bBteIQ_al9NV4VMTp58LjaCt6yvdKnBFny_Nk_rOp5zmuBdRgN0UtjJiejZ1sKesMqSwUVgFAp6l8Mpn6PJS7yCpyA; xbc=%7Bjzx%7Dx17VEt44TidLCE-27ltyonHRIQMK4EMSgtMkgZH72aVJJ7Q4rHRPQYwsiXcXSWdQvIPrEPo6eyXlPdhHqYax_62jqfBTrRfFiASPc1zn1utOQ2NVnaFT5OrRRvHc_sE-4GF5-LmnLxXLR1exnpxjsGviUC-coqywZPNv7zQyGx2HSs3jCjSOFm7Qos3brm7JITt72XNwjBzDn0zyE9AlpCW6OpxYHTogWNcHG9z4sh3GHYhtjPR7XQQyfwEaXyieRIVSZgIXf1UEMwzmzqzYut8lKHS_zS2xUG0akRxXiD95oYclnReZFta9eEYi9zsgj0uEx8mcW9kprtCkknH60tCjWaJX_n22V5Y8IgsZIwv6o7Kjqcv7XyOx8-4t59tvQfWBQm7SZ5f7S-fY6mwzwC8iALVMO_2aXHvCQtrN6-dHtcVGYMPCriJSBKOOtA7PEgXaXUGd10nWgyEWZTbe5Ds-wLv6AmDqgwNMySEPJWh9bggVP9EXNK4nSzg9nhsaXzsQdt5RuZ1HubKeuhO7dYyUNokmViS4L_8Kfn5_7xiltR_OjO8kHqbgNNZll-7L6GR8s6Z8VAEcK9X2EeYu4BAEWCuYHO-jFgihak8IZTIEm4VE2xHtMdjq8MKMLnwHRVFo3j9xMyMkyTGPo61KGKeBOqnZXEn-oRqhFhj0r18HDkqSY8nPbUCnk1koSwdz1HhoHj_pZS1fP_I_ydwN22oqIZ70XaZULI0Ow9hMqWlCSC5P537g6qyN8Q3fBEp5dDviyWkA1QrtIIfJgN4Sw4k2wU9e7vwzxAF-_Jng3py3g4Ohm3CwiVdakOGSe7_KOkO0ZX4U6USee0crGyhDc45YM8xzLQveve8pw2ok3WMUR9YP6ySCE7PE3AozA8PSbzomXtA7o8ptnlvEnyVsj1b8_1DxZNwFGiSk863WgmtqU21hiD-sQo-w6KqBlbLGbl_fyiUzVG8SGHM5ezjTbe3WlF0rD29mD2BGzs-ucp-Tql7xi8_leqqclU_vABAJVkO-MviByDz3-5-Y2hbb1l0JIpllVLPE4A2KDWuG0OMtsWbFx2OIcvKti--8D7MA; ga_clientid=910425039.1599656390; h_px=1; g_state={"i_p":1606479012100,"i_l":4}; __pnahc=0; session_id=6e38db76-5c75-4fce-b567-ca6bdcd6d46b; prism_25946650=93b0b9f5-5738-4041-bf1a-9fbaff139429; __pat=-18000000; mnet_session_depth=1%7C1599804419118; __aaxsc=2; _igt=cc4a6d97-bffe-455a-f3a3-93552b0e486e; aasd=1%7C1605005649102; _ig=f922e63c-88b1-438a-da8d-762835d8293e; __pvi=%7B%22id%22%3A%22v-2020-11-18-10-58-10-574-C3rNii5XIUGN1IlH-c7e065f02a1d0c6060ec2d61a554c479%22%2C%22domain%22%3A%22.seekingalpha.com%22%2C%22time%22%3A1605689890771%7D; _gid=GA1.2.1311518020.1605689891'
    }

driver.get('https://seekingalpha.com')
driver.implicitly_wait(5)
time.sleep(5)

print(f"Request Headers:  {driver.last_request.headers} \n")
try:
    print(f"Response Headers: {driver.last_request.response.headers} \n")
except Exception:
    pass
print(f"Request Cookie: {driver.last_request.headers.get('cookie')} \n")
print(driver.page_source)
