from undetected_chromedriver import Chrome

chrome = Chrome()

chrome.get('https://www.realtor.com/realestateagents/43224')

listings = chrome.find_elements('xpath', '//div[@id="agent_list_wrapper"]/div[1]/ul[1]/div')

print("Length is: ", len(listings))

for i in range(1, len(listings)+1):
    name = chrome.find_element('xpath', f'(//span[@class="jsx-3873707352 text-bold"])[{i}]').text
    company = chrome.find_element('xpath', f'(//div[@class="jsx-3873707352 agent-group text-semibold "]/div[@class="base__StyledType-rui__sc-108xfm0-0 gUsEmW"])[{i}]').text
    print(f"Name: {name}, Company: {company}")