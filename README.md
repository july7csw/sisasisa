## 시사를 시사하다, SISASISA
SISASISA(시사시사)는 최근 뉴스에 자주 언급되는 시사용어를 분석해 제공하는 모바일웹입니다.     
PC에서도 구동 가능한 반응형 웹이나, 모바일에 최적화되어 있습니다. (PC에서 구동 시 크롬에서 실행을 권장합니다)     
뉴스 언급 빈도가 급상승한 시사용어 콘텐츠를 선별함으로써 시사용어 학습과 시사 상식 이해를 돕고자 합니다.     
<br/>
## 기획의도
시사용어를 익히려고 했다가 어디서부터 시작해야 할지 막막했던 기억이 있습니다.     
시사용어를 사전 형식으로 모아놓은 앱이나 사이트는 있지만 양이 방대했고, 무엇보다 시의성 있는 시사용어를 파악할 수가 없었습니다.      
이미 시의성을 잃은 용어보다는 지금 중요한 시사용어를 알고 싶다는 필요에서 '시사시사'는 시작했습니다.     
시의성 있는 시사용어를 선별하는 기준으로는 뉴스가 가장 적합하다고 판단했습니다.     
단순히 뉴스 내 고빈도 언급이 아닌 최근 1년 대비 언급량 상승 지수 등 상대적인 분석으로 정밀도를 높였으며,     
분야별 필터링, 연관어 워드클라우드, 스크랩 기능 등으로 사용자 친화적인 기능을 포함했습니다.     
<br/>
## 기술사항
+ Python, JavaScript, jQuery, HTML, CSS
+ Django, AWS(Nginx, uWSGI)
+ MySQL     
<br/>

## API & DATA     
+ API     
한국언론진흥재단 빅카인즈 OpenAPI (현재는 비공개)
+ DATA     
기획재정부 시사경제용어 (공공데이터)     
http://www.econedu.go.kr/mec/ots/brd/list.do?mnuBaseId=MNU0000124&tplSer=4     
<br/>

## 기능
+ 로그인
<div>
<img src="/sisasisa/ss_login.png"  width="300">
</div>
네이버와 구글 계정으로 로그인이 가능합니다.
<br/><br/>

+ 스크랩
<div>
<img src="/sisasisa/ss_scrap01.png"  width="300">
<img src="/sisasisa/ss_scrap02.png"  width="300">
</div>
로그인한 사용자는 시사용어를 스크랩할 수 있습니다.     
시사용어 상세 설명에서 별 모양 아이콘으로 스크랩/스크랩해제합니다.     
MY 메뉴에서 스크랩한 시사용어를 열람하고 관리합니다.
<br/><br/>

+ 검색
<div>
<img src="/sisasisa/ss_search.png"  width="300">
</div>
키워드를 통해 시사용어를 검색할 수 있습니다.     
검색 범위는 용어와 뜻까지 포함합니다.     
<br/><br/>

## 주요 콘텐츠     
+ STEADY
<div>
<img src="/sisasisa/ss_steady01.png"  width="300">
<img src="/sisasisa/ss_steady02.png"  width="300">
</div>
최근 1년간 뉴스에 꾸준히 높은 빈도로 언급된 시사용어를 랭킹 형식으로 제공합니다.     
사회/경제/IT/문화 카테고리별로 필터링하여 랭킹 확인 가능합니다.     
개별 시사용어를 선택하면 용어의 뜻과 최근 1년간 해당 용어가 언급된 기사의 키워드를 워드클라우드 형식으로 볼 수 있습니다.
<br/><br/>

+ HOT
<div>
<img src="/sisasisa/ss_hot01.png"  width="300">
<img src="/sisasisa/ss_hot02.png"  width="300">
</div>
최근 1년 대비 전월 뉴스 언급량이 급상승한 시사용어를 랭킹 형식으로 제공합니다.     
사회/경제/IT/문화 카테고리별로 필터링하여 랭킹 확인 가능합니다.     
개별 시사용어를 선택하면 용어의 뜻과 최근 1년간 해당 용어가 언급된 기사의 키워드를 워드클라우드 형식으로 볼 수 있습니다.
<br/><br/>

+ MY
<div>
<img src="/sisasisa/ss_my01.png"  width="300">
<img src="/sisasisa/ss_my02.png"  width="300">
</div>
사용자가 스크랩한 시사용어 목록을 제공합니다.     
스크랩 목록에서 시사용어를 삭제할 수 있습니다.     
<br/>

