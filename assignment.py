
class Page:
    def __init__(self, name, to, frm):
        self.name=name
        self.to=to
        self.frm=frm

main = Page("main", "list", "any")
list = Page("list", "main, print", "main")
print = Page("sync", "main", "list")

pages = [main, list, print]

for page, i in pages:
    print(f"Page {i}: {page.name}. Reachable from {page.to}, reaches {page.frm}")
