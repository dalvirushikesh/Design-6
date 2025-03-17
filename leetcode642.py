#Time Complexity = 
# Traversing the Trie to find the current node: O(M).
# DFS to collect all sentences with the current prefix: O(S * L).
# Sorting the sentences: O(S log S).
#Space Complexity = O(N * L)
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)  # Stores child nodes
        self.sentences = defaultdict(int)     # Stores sentences and their frequencies

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()  # Root of the Trie
        self.prefix = ""        # Current input prefix
        self.current_node = self.root  # Current node in the Trie

        # Initialize the Trie with historical data
        for sentence, time in zip(sentences, times):
            self._insert(sentence, time)

    def _insert(self, sentence: str, time: int):
        node = self.root
        for char in sentence:
            node = node.children[char]
        node.sentences[sentence] += time

    def input(self, c: str) -> List[str]:
        if c == "#":
            # Save the current sentence and reset
            self._insert(self.prefix, 1)
            self.prefix = ""
            self.current_node = self.root
            return []

        self.prefix += c
        if not self.current_node:
            return []

        if c not in self.current_node.children:
            self.current_node = None
            return []

        self.current_node = self.current_node.children[c]

        # Retrieve all sentences with the current prefix
        sentences = []
        self._dfs(self.current_node, self.prefix, sentences)

        # Sort by frequency (descending) and ASCII order (ascending)
        sorted_sentences = sorted(sentences, key=lambda x: (-x[1], x[0]))

        #  top 3 sentences
        return [sentence for sentence, _ in sorted_sentences[:3]]

    def _dfs(self, node: TrieNode, prefix: str, sentences: List[tuple]):
        for sentence, freq in node.sentences.items():
            sentences.append((sentence, freq))
        for char, child in node.children.items():
            self._dfs(child, prefix + char, sentences)

