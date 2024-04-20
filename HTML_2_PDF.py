import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from jinja2 import Template

def render_html(template, **kwargs):
    template = Template(template)
    return template.render(**kwargs)

def html_to_pdf(html_content, file_path, page_size=QPrinter.A4, orientation=QPrinter.Portrait):
    app = QApplication(sys.argv)

    # Create a QWebEngineView
    web_view = QWebEngineView()
    web_view.setHtml(html_content)

    def print_to_pdf():
        printer = QPrinter()
        printer.setPageSize(page_size)
        printer.setOrientation(orientation)

        dialog = QPrintDialog(printer)
        if dialog.exec_() == QPrintDialog.Accepted:
            web_view.page().print(printer, lambda success: print("PDF printing success:", success))
    
    # Connect the print action to the print_to_pdf function
    web_view.loadFinished.connect(print_to_pdf)

    sys.exit(app.exec_())

# Example Jinja template
template = """
<html>
<head><title>{{ title }}</title></head>
<body>
<h1>{{ heading }}</h1>
<p>{{ content }}</p>
</body>
</html>
"""

# Render HTML content using Jinja
html_content = render_html(template, title="Test HTML to PDF", heading="Hello, PDF!", content="This is a test HTML content.")

# Convert HTML to PDF with A4 page size and Portrait orientation
html_to_pdf(html_content, "output.pdf", QPrinter.A4, QPrinter.Portrait)
