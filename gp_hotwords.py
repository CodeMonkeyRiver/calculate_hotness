import gopup as gp

keyword="黄河"
wb_index = gp.weibo_index(word=keyword, time_type="1month")
print(wb_index)

cookie = 'BIDUPSID=82CC54A3E69E705B18765DB0A2EC197C; PSTM=1676728369; BAIDUID=82CC54A3E69E705BA95F1CA1EAE0716D:SL=0:NR=10:FG=1; BAIDUID_BFESS=82CC54A3E69E705BA95F1CA1EAE0716D:SL=0:NR=10:FG=1; ZFY=ZHKaEYizo8058wOvAAyAzprb7hupLq2xfaupdfNTErQ:C; newlogin=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BCLID=10819767448857529383; BCLID_BFESS=10819767448857529383; BDSFRCVID=GmIOJexroG3OZHOqbYIM2MLATSNbUdrTDYrEjGc3VtzSGYLVFsQ6EG0Pts1-dEub6j30ogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=GmIOJexroG3OZHOqbYIM2MLATSNbUdrTDYrEjGc3VtzSGYLVFsQ6EG0Pts1-dEub6j30ogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbC8VCDKJKD3qbjkq45HMt00qxby26nxam59aJ5y-J7nhp7LyMna-lFPXH5uWUonL2oa-Rb-QpbZql5FQP-53R0h0PJkWp5l-aCqKl0MLPb5hj6gQJoDj4TyDMnMBMPj5mOnanvn3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5vbDNbP; H_BDCLCKID_SF_BFESS=tbC8VCDKJKD3qbjkq45HMt00qxby26nxam59aJ5y-J7nhp7LyMna-lFPXH5uWUonL2oa-Rb-QpbZql5FQP-53R0h0PJkWp5l-aCqKl0MLPb5hj6gQJoDj4TyDMnMBMPj5mOnanvn3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5vbDNbP; BDUSS=5ZMndIQ1dYVGZMYW5aZEFyUkp3cjl1Ykh2OTBueTB1VDg3QkVUMnBOZE5oVjlsSUFBQUFBJCQAAAAAAAAAAAEAAABRLDQJ08DO3ta5vfi1xMrAvecAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE34N2VN-Ddla3; H_PS_PSSID=39636_39624_39671_39663_39684_39676; BA_HECTOR=a00la585a0a10g2004a4a42m1il63e91r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=3; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1700018328; bdindexid=kmkaimio7ucpum57htd29051e3; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04500307799bW0LQNHjvbbbcgpZogSg8XMBJGbapbZ2AerwzclJVQRhs1Eej%2F1E3ebVg9mgxlLRU2RSofCy3LPG9eoungXvFC1zrMPuqAg6%2FmsY8mKiYOYpHe%2FM1gKAiJ9aug3PPwJnPv0%2BGFgdhiaIqlRu%2B%2F9Rc1QUG8mPsC6aBDzT2OugfqvyFvHJt3foktjG4kMreZ2EFnn3iuKdJhP%2BpW26wtwDRIcw0wuXrxGTneHbzMi8WHRY2DoySxNa7ywHxygQzEiT7xLHuRgruCnkLvS%2FjUOUrcgC8L%2FjOkVn5lCUvSZpfOueBRxMQoGMg%2BqLrU2dkaV3W9nyovQHwlRDHDitpAud6QYBBLzTm%2F1A0df0AnzsvA0%3D39602485054371482624307508553931; __cas__rn__=450030779; __cas__st__212=b6360504b6787dd9f439863ebc4cac7c4261f2f32014a9059a898d1d8c6e01ba3f894ac5a21b1e46889f858d; __cas__id__212=51525872; CPTK_212=994874906; CPID_212=51525872; RT="z=1&dm=baidu.com&si=342256a1-fd39-45b4-a9b3-4c78b7579aec&ss=loz70oj0&sl=1&tt=1lj&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1700018351; ab_sr=1.0.1_YjBlODgzYzgwYzQwZWFjOTUxODBjZDdkYjAwNmZiYzg0Nzc1NWQ2ZWE2MGY4NTNkZjQzMDNjNTRiMGVlZWE4OGMyNjdjYmZkNmNkY2FhOTg0ZTUxMTkwMjIyZTZiNDRkN2I0ZDE3NjNlZTY4OTk5NmI1ZTkyNGRkMWJjNjY5NjUxNjZiYTRhMWRlZmQ0MTQ5MTc4ZWUwYjc4YTc5NWM2NQ==; BDUSS_BFESS=5ZMndIQ1dYVGZMYW5aZEFyUkp3cjl1Ykh2OTBueTB1VDg3QkVUMnBOZE5oVjlsSUFBQUFBJCQAAAAAAAAAAAEAAABRLDQJ08DO3ta5vfi1xMrAvecAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE34N2VN-Ddla3'

bd_df = gp.baidu_search_index(word=keyword, start_date='2023-11-01', end_date='2023-11-01', cookie=cookie)
print(bd_df)

# bd_hot = gp.baidu_hot_list()
# print('baidu hot list', bd_hot)
#
# weibo_hot = gp.weibo_hot_search_list()
# print(weibo_hot)
#
# wx_hot = gp.wx_hot_list()
# print(wx_hot)

zhihu_hot = gp.zhihu_hot_list()
#print(zhihu_hot)