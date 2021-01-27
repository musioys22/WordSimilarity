# URL
1. https://XXX.run.app/word_similar
# Method:
1. POST
# URL Params
1. requests: {'word':['XX']}
2. word : [string]
3. ['XX'] : 需尋找的字詞
# Success Response:
1. Code: 200
2. Content: {'similar_words': […]}
# Error Response:
1. Issue: 該字詞不在模型內
2. Code: 400 錯誤請求
3. Content: 'word "XXX" not in vocabulary'
- OR
1. Issue: 沒有相似字詞
2. Code: 400 錯誤請求
3. Content: 'Can not found similar word'

