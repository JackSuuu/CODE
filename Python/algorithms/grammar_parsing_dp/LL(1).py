class LL1Parser:
    def __init__(self, grammar, start_symbol):
        self.grammar = grammar
        self.start_symbol = start_symbol
        self.first_sets = {}
        self.follow_sets = {}
        self.parse_table = {}
        self.build_first_sets()
        self.build_follow_sets()
        self.build_parse_table()

    def compute_first(self, symbol):
        if symbol in self.first_sets:
            return self.first_sets[symbol]

        first = set()
        if symbol not in self.grammar:  # Terminal
            first.add(symbol)
        else:  # Non-terminal
            for production in self.grammar[symbol]:
                for prod_symbol in production:
                    prod_first = self.compute_first(prod_symbol)
                    first.update(prod_first - {'ε'})
                    if 'ε' not in prod_first:
                        break
                else:
                    first.add('ε')
        self.first_sets[symbol] = first
        return first

    def build_first_sets(self):
        for non_terminal in self.grammar:
            self.compute_first(non_terminal)

    def compute_follow(self, symbol):
        if symbol in self.follow_sets:
            return self.follow_sets[symbol]

        follow = set()
        if symbol == self.start_symbol:
            follow.add('$')  # End of input marker

        for nt, productions in self.grammar.items():
            for production in productions:
                for i, prod_symbol in enumerate(production):
                    if prod_symbol == symbol:
                        rest = production[i + 1:]
                        if rest:
                            rest_first = set()
                            for r in rest:
                                rest_first.update(self.compute_first(r) - {'ε'})
                                if 'ε' not in self.compute_first(r):
                                    break
                            else:
                                rest_first.add('ε')
                            follow.update(rest_first - {'ε'})
                        if not rest or 'ε' in rest_first:
                            follow.update(self.compute_follow(nt))
        self.follow_sets[symbol] = follow
        return follow

    def build_follow_sets(self):
        for non_terminal in self.grammar:
            self.compute_follow(non_terminal)

    def build_parse_table(self):
        for non_terminal, productions in self.grammar.items():
            for production in productions:
                first = set()
                for symbol in production:
                    first.update(self.compute_first(symbol) - {'ε'})
                    if 'ε' not in self.compute_first(symbol):
                        break
                else:
                    first.add('ε')

                for terminal in first - {'ε'}:
                    self.parse_table[(non_terminal, terminal)] = production

                if 'ε' in first:
                    for terminal in self.compute_follow(non_terminal):
                        self.parse_table[(non_terminal, terminal)] = production

    def parse(self, tokens):
        stack = [self.start_symbol]  # Initialize stack with start symbol
        tokens.append('$')  # Append end-of-input marker
        pos = 0  # Initialize position

        while stack:
            x = stack[-1]  # Peek at the top of the stack
            current_token = tokens[pos]

            if x in self.grammar:  # Non-terminal
                if (x, current_token) in self.parse_table:
                    stack.pop()  # Pop the non-terminal
                    production = self.parse_table[(x, current_token)]
                    if production != ['ε']:
                        stack.extend(reversed(production))  # Push symbols of β onto stack (backwards)
                else:
                    raise SyntaxError(f"Error: No rule for ({x}, {current_token}) in parse table.")
            else:  # Terminal or end-of-input marker
                if x == current_token:
                    stack.pop()  # Match and pop
                    pos += 1  # Move to the next token
                else:
                    raise SyntaxError(f"Error: Unexpected token {current_token}, expected {x}.")

        if pos == len(tokens) - 1:  # Check if all input tokens are consumed
            print("Input is successfully parsed.")
        else:
            raise SyntaxError("Error: Input could not be parsed.")

# Example usage
if __name__ == "__main__":
    grammar = {
        'E': [['T', 'E\'']],
        'E\'': [['+', 'T', 'E\''], ['ε']],
        'T': [['F', 'T\'']],
        'T\'': [['*', 'F', 'T\''], ['ε']],
        'F': [['(', 'E', ')'], ['id']]
    }
    parser = LL1Parser(grammar, 'E')
    tokens = ['id', '+', 'id', '*', 'id']
    parser.parse(tokens)