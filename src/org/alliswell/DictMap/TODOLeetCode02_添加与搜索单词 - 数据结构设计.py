# 211. 添加与搜索单词 - 数据结构设计
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#
# 实现词典类 WordDictionary ：
#
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
#
#
# 示例：
#
# 输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
#
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // 返回 False
# wordDictionary.search("bad"); // 返回 True
# wordDictionary.search(".ad"); // 返回 True
# wordDictionary.search("b.."); // 返回 True
#
#
# 提示：
#
# 1 <= word.length <= 25
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最多调用 10^4 次 addWord 和 search

class TrieNode:
    def __init__(self, is_leaf: bool):
        self.is_leaf = is_leaf
        self.next = [None] * 26

from typing import List
class WordDictionary:

    def __init__(self):
        self.dict_map = [None] * 26

    def addWord(self, word: str) -> None:
        if not word:
            return
        tmp_map = self.dict_map
        word_len = len(word)
        for i in range(word_len):
            index = ord(word[i]) - ord('a')
            assert 0 <= index < 26
            if tmp_map[index]:
                trie_node = tmp_map[index]
            else:
                trie_node = TrieNode(is_leaf=False)
                tmp_map[index] = trie_node
            if i == word_len-1:
                trie_node.is_leaf = True
            tmp_map = trie_node.next
        return

    def search(self, word: str) -> bool:
        if not word:
            return False
        return self.search_core(word, 0, self.dict_map)

    def search_core(self, word: str, word_idx:int, dict_map: List[TrieNode]) -> bool:
        c = word[word_idx]
        if c == '.':
            left, right = 0, 26
        else:
            index = ord(c) - ord('a')
            left, right = index, index+1
        for i in range(left, right):
            trie_node = dict_map[i]
            if not trie_node:
                continue
            if word_idx == len(word)-1:
                return trie_node.is_leaf
            if self.search_core(word, word_idx+1, trie_node.next):
                return True
        return False



if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))
    print(wordDictionary.search("bad"))
    print(wordDictionary.search(".ad"))
    print(wordDictionary.search("b.."))