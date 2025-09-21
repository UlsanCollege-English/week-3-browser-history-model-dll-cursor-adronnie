class _N:
    __slots__ = ("url", "prev", "next")

    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def current(self):
        """Return the current URL, or None if empty."""
        return self.cur.url if self.cur else None

    def visit(self, url):
        """
        If not at the end, drop all forward entries,
        then append url and move cursor.
        """
        node = _N(url)

        if self.cur is None:  # first ever visit
            self.head = self.tail = self.cur = node
            return

        # If not at the tail, cut off forward history
        if self.cur.next:
            self.cur.next.prev = None
            self.cur.next = None
            self.tail = self.cur

        # Append new node
        self.cur.next = node
        node.prev = self.cur
        self.cur = node
        self.tail = node

    def back(self, steps=1):
        """Move left up to steps times."""
        while steps > 0 and self.cur and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.current()

    def forward(self, steps=1):
        """Move right up to steps times."""
        while steps > 0 and self.cur and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.current()
