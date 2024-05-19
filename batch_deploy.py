import os.path

import requests

server_list = ["localhost:6800"]
start_url = "http://{server}/schedule.json"
scrapy_project_folder = "C:\\Users\\ASUS\\PycharmProjects\\scrapy_example"
scrapy_cfg_template_path = os.path.join(scrapy_project_folder, "scrapy_template.cfg")
os.chdir(scrapy_project_folder)
project = "scrapy_test"
spider = "blog_crawler"

with open(scrapy_cfg_template_path, encoding='utf-8') as f:
    scrapy_cfg_template = f.read()


def deploy(server):
    scrapy_cfg = scrapy_cfg_template.replace("$server$", server)
    with open("scrapy.cfg", "w", encoding='utf-8') as f:
        f.write(scrapy_cfg)
    os.system("scrapyd-deploy")


def launch(server):
    url = start_url.format(server=server)
    result = requests.post(url, data={"project": project, "spider": spider}).text
    print('服务器：', server, '返回结果：', result)


if __name__ == '__main__':
    for server in server_list:
        deploy(server)
        launch(server)
