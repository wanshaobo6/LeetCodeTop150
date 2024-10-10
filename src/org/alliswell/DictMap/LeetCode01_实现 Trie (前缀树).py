# 208. 实现 Trie (前缀树)
# 中等
#
# 相关标签
# 相关企业
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。
#
# 请你实现 Trie 类：
#
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
#
#
# 示例：
#
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
#
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#
#
# 提示：
#
# 1 <= word.length, prefix.length <= 2000
# word 和 prefix 仅由小写英文字母组成
# insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次

class TrieNode:
    def __init__(self, is_leaf: bool, next: dict):
        self.is_leaf = is_leaf
        self.next = next

class Trie:

    def __init__(self):
        self.trie_map = {}

    def insert(self, word: str) -> None:
        if not word:
            return
        tmp_map = self.trie_map
        word_len = len(word)
        for i in range(word_len):
            c = word[i]
            if c in tmp_map:
                trie_node = tmp_map.get(c)
            else:
                trie_node = TrieNode(is_leaf=False, next={})
                tmp_map[c] = trie_node
            if i == word_len-1:
                trie_node.is_leaf = True
            tmp_map = trie_node.next
        return

    def search(self, word: str) -> bool:
        if not word:
            return False
        tmp_map = self.trie_map
        word_len = len(word)
        for i in range(word_len):
            c = word[i]
            if c not in tmp_map:
                return False
            trie_node = tmp_map.get(c)
            if i == word_len-1:
                return trie_node.is_leaf
            tmp_map = trie_node.next
        return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        tmp_map = self.trie_map
        word_len = len(prefix)
        for i in range(word_len):
            c = prefix[i]
            if c not in tmp_map:
                return False
            trie_node = tmp_map.get(c)
            tmp_map = trie_node.next
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':
    trie = Trie();
    trie.insert("apple");
    trie.insert("abc");
    print(trie.search("apple"))   # 返回 True
    print(trie.search("app"))     # 返回 False
    print(trie.startsWith("app")) # 返回 True
    trie.insert("app")
    print(trie.search("app"))     # 返回 True
