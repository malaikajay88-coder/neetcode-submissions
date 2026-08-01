class StockSpanner:

    def __init__(self):
        # Stack stores (price, span)
        self.stack = []

    def next(self, price: int) -> int:

        # Today's span is at least 1 (today itself)
        span = 1

        # Remove all previous prices that are
        # less than or equal to today's price
        while self.stack and self.stack[-1][0] <= price:

            # Remove the top element
            prev_price, prev_span = self.stack.pop()

            # Add its span because those days are
            # also part of today's span
            span += prev_span

        # Store today's price and its computed span
        self.stack.append((price, span))

        # Return today's span
        return span