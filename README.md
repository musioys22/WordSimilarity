•	URL
o	https://XXX.run.app/word_similar
•	Method:
o	POST
•	URL Params
o	word = [string]
需尋找的字詞
•	Success Response:
o	Code: 200
Content: {'similar_words': […]}
•	Error Response:
o	Issue: 該字詞不在模型內
Code: 400 錯誤請求
Content: 'word "XXX" not in vocabulary'
OR
o	Issue: 沒有相似字詞
Code: 400 錯誤請求
Content: 'Can not found similar word'

