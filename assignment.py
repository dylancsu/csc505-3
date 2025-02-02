
class Page:
    def __init__(self, name, to, frm):
        self.name=name
        self.to=to
        self.frm=frm

main_ = Page("main", "list", "any")
list_ = Page("list", "main, print", "main")
print_ = Page("sync", "main", "list")

pages = [main_, list_, print_]

for i, page in enumerate(pages, start=1):
    print(f"Page {i}: {page.name}. Reachable from {page.to}, reaches {page.frm}")
