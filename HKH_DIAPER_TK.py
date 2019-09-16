################################### 메리즈는 BR_J는 추가하지 않음. ###################################
def seperate_diaper_brand(x):
    ############# 하기스 #############
    if '하기스' in x:
        return '하기스'
    ############# 군 #############
    elif '군' in x:
        return '군'
    ############# 메리즈 #############
    elif '메리즈' in x:
        return '메리즈'
    ############# 팸퍼스 #############
    elif '팸퍼스' in x:
        return '펨퍼스'
    ############# 마미포코 #############
    elif '마미포코' in x:
        return '마미포코'
    ############# 보솜이 #############
    elif '보솜이' in x:
        return '보솜이'
    ############# 네이처러브메레 #############
    elif '러브메' in x:
        return '네이처러브메레'
    ############# 슈퍼대디 #############
    elif '슈퍼대디' in x:
        return '슈퍼대디'
    ############# 페넬로페 #############
    elif '페넬로페' in x:
        return '페넬로페'
    ############# 킨도 #############
    elif '킨도' in x:
        return '킨도'
    ############# 나비잠 #############
    elif '나비잠' in x:
        return '나비잠'
    else:
        pass  
########################## 하기스 브랜드 분류 ##########################
def haggies_j(x):
    if '보송' in x:
        return '보송보송'
    elif '매직' in x:
        return '매직핏'
    elif '네이처메이드' in x:
        return '네이처메이드'
    elif '에어솔솔' in x:
        return '에어솔솔'
    elif '맥스드라이' in x:
        return '맥스드라이'
    elif '크린베베' in x:
        return '크린베베'
    elif '오버나이트' in x:
        return '오버나이트'
    else:
        return '하기스_기타'
########################## 군 브랜드 분류 ##########################
def goon_j(x):
    if '오리지널' in x:
        return '오리지널'
    elif '마시멜로' in x:
        return '마시멜로'
    elif '슬림' in x:
        return '슬림'
    elif '소프트' in x:
        return '소프르'
    elif '슈퍼빅' in x:
        return '슈퍼빅'
    elif '원터' in x:
        return '윈터'
    elif '프렌드' in x:
        return '프렌드'
    elif '향기' in x:
        return '향기'
    else:
        return '군_기타'
########################## 펨퍼스 브랜드 분류 ##########################
def pampers_j(x):
    if '베이비' in x:
        return '베이비 드라이'
    elif '쿠루저' in x:
        return '크루저/액티브핏'
    elif '액티브' in x:
          return '크루저/액티브핏'
    elif '스와들러' in x:
        return '스와들러'
    else:
        return '펨퍼스_기타'
########################## 마미포크 브랜드 분류 ##########################
def mammypoko_j(x):
    if '보송허그' in x:
        return '보송허그'
    elif '360' in x:
        return '360핏 팬티'
    elif '쿨썸머' in x:
        return '쿨썸머'
    elif '골드퍼피' in x:
        return '골드퍼피'
    elif '굿밤' in x:
        return '굿밤'
    elif '로켓' in x:
        return '로켓흡수팬티'
    elif '리프가닉' in x:
        return '리프가닉'
    elif '슬림핏' in x:
        return '슬림핏'
    else:
        return '마미포크_기타'
########################## 보솜이 브랜드 분류 ##########################
def bosomi_j(x):
    if '리얼코튼' in x:
        return '리얼코튼'
    elif '리얼코튼썸머' in x:
        return '리얼코튼썸머'
    elif '액션핏' in x:
        return '액션핏'
    elif '디오가닉' in x:
        return '디오가닉'
    elif '마이핏' in x:
        return '마이핏'
    elif '베이비케어' in x:
        return '베이비케어'
    else:
        return '보솜이_기타'
########################## 네이처브메레 브랜드 분류 ##########################
def naturel_j(x):
    if '오리지널' in x:
        return '오리지널'
    elif '슬림' in x:
        return '슬림'
    elif '에코' in x:
        return '에코'
    else:
        return '네이처러브메레_기타'
########################## 슈퍼대디 브랜드 분류 ##########################
def superdady_j(x):
    if '매직' in x:
        return '매직슬림'
    elif '소프트' in x:
        return '리얼소프트'
    elif '리얼' in x:
        return '리얼슬림'
    else:
        return '슈퍼대디_기타'
######################### 페넬로페 브랜드 분류 ##########################
def penelope_j(x):
    if '뭉침' in x:
        return '뭉침없는'
    elif '실키' in x:
        return '실키슬림'
    elif '씬' in x:
        return '씬씬씬'
    elif '미라클' in x:
        return '미라클'
    else:
        return '페넬로페_기타'
########################## 킨도 브랜드 분류 #########################
def kindoh_j(x):
    if '프리미엄' in x:
        return '프리미엄'
    elif '에어' in x:
        return '에어드라이'
    elif '업앤' in x:
        return '업앤플레이'
    else:
        return '킨도_기타'
######################### 나비잠 브랜드 분류 ##########################
def nabijam_j(x):
    if '울트라' in x:
        return '울트라씬'
    elif '매직' in x:
        return '매직소프트'
    elif '슈퍼' in x:
        return '슈퍼드라이'
    elif '코지' in x:
        return '코지'
    else:
        return '나비잠_기타'