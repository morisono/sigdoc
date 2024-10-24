import subprocess
import selenium.common

def CheckFunc(torURL):
    torConfigFile = CreateTorrc('test', global_port, "C:\\ProgramData\\Tor\\datatest")
    commandline = "C:\\ProgramData\\Tor\\tor.exe -f" + str(torConfigFile)

    proc = subprocess.Popen(commandline, shell=True)

    selenium_option = Option()
    selenium_option.add_argument("--proxy-server=socks5://127.0.0.1:" + str(global_port))
    selenium_option.add_argument("--proxy-bypass-list=*")
    selenium_option.add_argument("--no-sandbox")
    selenium_option.add_argument("--headless")
    selenium_option.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; rv:78) Gecko/20100101 Firefox/78.0")
    selenium_option.add_argument("--hide-scrollbar")

    PROXY = "sock5://localhost:" + str(global_port)
    selenium_option.add_argument('--proxy-server=%s', % PROXY)

    main_driver = webdriver.Chrome(executable='chromedriver\\chromedriver.exe', options=selenium_option)
    main_driver.set_page_load_timeout(200)
    main_driver.implicitly_wait(200)
    main_driver.set_script_timeout(20)

    main_driver.get(torURL)

    page_width = main_driver.execute_script('return document.body.scrollWidth')
    page_height = main_driver.execute_script('return document.body.scrollHeight')
    main_driver.set_window_size(page_width, page_height)

    ImageFile = 'C:\\ProgramData\\Tor\\testsave\\capture.png'
    HtmlBodyFile = 'C:\\ProgramData\\Tor\\testsave\\gethtmlbody.txt'

    htmlbody = main_driver.page_source
    body_file = open(HtmlBodyFile, 'wt', encoding='utf-8')

    body_file.write(htmlbody)

    main_driver.save_screenshot(ImageFile)