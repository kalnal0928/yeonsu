from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pyautogui
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트
input_value = input("강좌를 선택하세요 예 '1 or 2 or 3 or 4'=>")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 자동화 탐지 방지 설정
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 브라우저 생성
driver = webdriver.Chrome(options=chrome_options)

# 자동화 탐지 방지 JavaScript 실행
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        window.navigator.chrome = {
            runtime: {}
        };
        Object.defineProperty(navigator, 'languages', {
            get: () => ['en-US', 'en']
        });
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3]
        });
    """
})

def lec1():
    btn = driver.find_element(By.CSS_SELECTOR, '#crseList > li:nth-child(1) > div.txt_box > div.btn_box.mt0 > a.bnt_basic_line.small').click()

def lec2():
    btn = driver.find_element(By.CSS_SELECTOR, '#crseList > li:nth-child(2) > div.txt_box > div.btn_box.mt0 > a.bnt_basic_line.small').click()

def lec3():
    btn = driver.find_element(By.CSS_SELECTOR, '#crseList > li:nth-child(3) > div.txt_box > div.btn_box.mt0 > a.bnt_basic_line.small').click()

def lec4():
    btn = driver.find_element(By.CSS_SELECTOR, '#crseList > li:nth-child(4) > div.txt_box > div.btn_box.mt0 > a.bnt_basic_line.small').click()

url_k = "https://www.gbeti.or.kr/system/login/login.do"  # 경북교육연수원
url_j = "https://www.neti.go.kr/system/login/login.do"  # 중앙교육연수원
url_list = [url_k, url_j]
driver.get(url_list[0])
time.sleep(3)

# 윈도우 최대화
driver.maximize_window()

# 아이디 입력
# 방법 1: CSS_SELECTOR와 클래스 사용 (점으로 공백 대체)
try:
    id_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".text_login.id"))
    )
    id_field.click()
    my_id = "********"  # 아이디 입력
    pyperclip.copy(my_id)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
except Exception as e:
    print("CSS 선택자로 접근 실패:", e)

# # 방법 2: XPath와 placeholder 속성 사용
# try:
#     id_field = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='6~20자의 영문, 숫자만 가능']"))
#     )
#     id_field.click()
# except Exception as e:
#     print("XPath placeholder로 접근 실패:", e)

# # 방법 3: XPath와 title 속성 사용
# try:
#     id_field = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//input[@title='아이디를 입력하세요']"))
#     )
#     id_field.click()
# except Exception as e:
#     print("XPath title로 접근 실패:", e)

# # 방법 4: JavaScript 실행 (가장 강력한 방법)
# try:
#     # 클래스로 요소 찾기
#     script = """
#     document.querySelector('.text_login.id').click();
#     document.querySelector('.text_login.id').focus();
#     """
#     driver.execute_script(script)
# except Exception as e:
#     print("JavaScript 실행 실패:", e)

# # 방법 5: 속성 조합 사용
# try:
#     id_field = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "input.text_login.id[placeholder='6~20자의 영문, 숫자만 가능']"))
#     )
#     id_field.click()
# except Exception as e:
#     print("속성 조합 접근 실패:", e)

# # 방법 6: ActionChains 사용
# try:
#     id_field = driver.find_element(By.CSS_SELECTOR, ".text_login.id")
#     actions = ActionChains(driver)
#     actions.move_to_element(id_field).click().perform()
# except Exception as e:
#     print("ActionChains 실패:", e)
# # wait = WebDriverWait(driver, 10)
# id_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'text_login id')))
# driver.execute_script("arguments[0].click();", id_input)  # JavaScript로 클릭


try:
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".text_login.pw"))
    )
    password_field.click()
    my_pass = "*******" # 비밀번호 입력
    pyperclip.copy(f'{my_pass}')
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
except Exception as e:
    print("CSS 선택자로 비밀번호 필드 접근 실패:", e)
# try:
#     id_field = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".text_login pw"))
#     )
#     id_field.click()
#     my_pass = "an09283259@"
#     pyperclip.copy(f'{my_pass}')
#     pyautogui.hotkey("ctrl", "v")
#     time.sleep(1)
# except Exception as e:
#     print("CSS 선택자로 접근 실패:", e)
# # 비밀번호 입력
# search = driver.find_element(By.CLASS_NAME, '').click()

# pw_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'text_login pw')))
# driver.execute_script("arguments[0].click();", pw_input)  # JavaScript로 클릭
# my_pass = "an09283259@"
# pyperclip.copy(my_pass)
# pyautogui.hotkey("ctrl", "v")
# time.sleep(1)

# 로그인 버튼 클릭
# 로그인
search = driver.find_element(By.CSS_SELECTOR, 'body > section > form > div > div > button').click()
time.sleep(3)

# 팝업창 제거
try:
    driver.switch_to.window(driver.window_handles[-1])
    search = driver.find_element(By.CSS_SELECTOR, '#wrap > div.popup_btn > div > button.closeBtn').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
except:
    pass

# 나의 학습방으로 들어가기
time.sleep(2)
btn = driver.find_element(By.CSS_SELECTOR, '#header_lnb > ul > li:nth-child(6) > a').click()
time.sleep(3)

# 수강과정 선택
btn = driver.find_element(By.CSS_SELECTOR, '#header_lnb > ul > li:nth-child(6) > ol > li:nth-child(4)').click()
time.sleep(3)

# 학습하기 또는 이어보기 클릭
try:
    if input_value == "1":
        lec1()
    elif input_value == "2":
        lec2()
    elif input_value == "3":
        lec3()
    elif input_value == "4":
        lec4()
except:
    pass

# 새창 제어
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)

# 강의 보기 버튼 있을 때
try:
    btn = driver.find_element(By.CSS_SELECTOR, '#lectBtnControl > p').click()
except:
    pass

time.sleep(3)

# 플레이 버튼 클릭
try:
    btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'vjs-big-play-button')))
    btn.click()  # 비디오 버튼
except:
    pass

time.sleep(1)

# 무한 루프: 자동화 탐지 방지 및 강의 진행
while True:
    current_time = time.time()

    # 
        # 쿠키 갱신 (30분 ~ 2시간 사이 랜덤)
    if 'next_cookie_refresh' not in locals():
        next_cookie_refresh = current_time + random.uniform(30 * 60, 2 * 60 * 60)

    if current_time >= next_cookie_refresh:
        cookies = driver.get_cookies()
        for cookie in cookies:
            driver.add_cookie(cookie)
            time.sleep(random.uniform(0.5, 1.2))
        next_cookie_refresh = current_time + random.uniform(30 * 60, 2 * 60 * 60)

    # 비디오 버튼 클릭
    try:
        time.sleep(random.uniform(7, 20))
        btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'vjs-big-play-button')))
        btn.click()
        time.sleep(random.uniform(7, 20))
    except:
        pass

    # 추가된 경고창 처리
    try:
        time.sleep(random.uniform(7, 20))
        wait = WebDriverWait(driver, 10)
        btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#alertInfoMobile > div.popup_wrap > div > div > a.btn_white.btn_basic.cancel')))
        btn.click()
        
    except (TimeoutException, NoSuchElementException):
        pass

    # 다음 버튼 클릭
    try:
        time.sleep(random.uniform(7, 20))
        btn = driver.find_element(By.CSS_SELECTOR, '#next-btn').click()
        time.sleep(random.uniform(7, 20))
    except:
        pass

    # 문제 확인 버튼 클릭
    try:
        time.sleep(random.uniform(7, 21))
        btn = driver.find_element(By.CSS_SELECTOR, '#lxPlayerIframe > div.quizShowBtn').click()
        time.sleep(random.uniform(7, 20))
    except:
        pass

    # 다음 강의로 이동
    try:
        time.sleep(random.uniform(7, 20))
        next_class = driver.find_element(By.CLASS_NAME, 'next-btn.vjs-control')
        actions = ActionChains(driver)
        actions.move_to_element(next_class).click().perform()
        time.sleep(random.uniform(7, 20))

        da = Alert(driver)
        da.dismiss()
        time.sleep(random.uniform(7, 20))
    except:
        continue