import wikipedia #importは最初にまとめておくとはっきりする

def get_artist_events(keyward):
    wiki = wikipedia.Wikipedia('ja')  
    keyward = "ここにアーティスト名"
    result = wikipedia.search(keyward)
    page = wiki.page(keyward)
    print("検索結果",result) #絶対コードの並び違う
    
    if not page.exists(keyward):
        return print(f"アーティスト「{keyward}」の情報は見つかりませんでした。")
    
    content = page.text[:1000]  

    if '公演' in content or 'イベント' in content or 'コンサート' in content:
        return print(f"アーティスト「{keyward}」が開催したイベント情報を調査しました。\n{content}")
    else:
        return print(f"アーティスト「{keyward}」に関連するイベント情報は見つかりませんでした。")





