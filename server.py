from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class Server(BaseHTTPRequestHandler):
    """
    Класс, отвечающий за обработку входящих запросов от клиентов
    """

    def __get_html_content(self) -> str:
        """ Возвращает текст html файла index.html """
        with open("index.html") as html:
            return html.read()

    def do_GET(self) -> None:
        """ Обрабатывает входящие GET-запросы """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))
