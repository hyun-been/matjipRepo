import mysql.connector

def create_table(db_name):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='asdf', database=db_name)
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE address (name VARCHAR(255), address VARCHAR(255), number TEXT)')

    sql = 'INSERT INTO address (name, address, number) VALUES (%s, %s, %s)'
    val = [('가문의우동', '서대문구 연세로9길 13' , '02-325-8325'), ('가미분식', '서대문구 이화여대8길 2 무궁화상가아파트', '02-364-3948'), ('가배당', '서대문구 이화여대길 52', 'NULL'), ('가야가야', '서대문구 이화여대5길 7-3', '02-363-7877'), ('가츠벤또', '마포구 백범로 13 신촌 르 메이에르타운 2차 105호', '02-711-0606'), ('간판없는집', '서대문구 연세로5다길 41', '02-6404-8469'), ('개미집', '서대문구 연세로11길 15 1층', '02-332-3237'), ('고냉지', '서대문구 연세로2마길 30', '02-313-0845'), ('고삼이', '서대문구 연세로7안길 38', '02-324-1403'), ('고스트요거트', '서대문구 이화여대길 52-15 1층', '02-313-8468'), ('고쌈냉면', '서대문구 신촌역로 31', '02-313-9392'), ('곰미커피', '서대문구 신촌역로 11 연출하우스 1층', '070-4306-9621'), ('곱창먹방', '서대문구 이화여대길 64', '02-313-5252'), ('공룡통닭', '마포구 신촌로 170 이대역 푸르지오시티', '02-711-4100'), ('공복', '서대문구 연세로12길 23 1층', '02-312-6692'), ('공차', '서대문구 이화여대길 48', '070-4208-0933'), ('구구족', '서대문구 이화여대8길 2', '02-313-9414'), ('굽네', '서대문구 연세로 42-32', '02-312-9494'), ('그릭데이', '서대문구 이화여대길 88-21 2층', '02-363-9222'), ('긴자료코', '서대문구 이화여대5길 28', '02-309-5861'), ('김밥천국', '서대문구 신촌역로 19-2', '02-312-2104'), ('까미네닭강정', '서대문구 신촌역로 22-5 신촌박스퀘어 1층 19', '010-9162-1487'), ('까이식당', '서대문구 이화여대2가길 24 1층', '070-7570-0871'), ('꼬끼오분식', '서대문구 이화여대길 72-3 2층', '070-4897-7111'), ('나이스샤워', '서대문구 연세로 35', '02-6348-1020'), ('날마다', '서대문구 이화여대1길 33 UCU 1층', '070-4639-3651'), ('낭만식탁', '서대문구 이화여대5길 6', '02-312-1238'), ('내가찜한닭', '서대문구 이화여대7길 7', '02-312-0101'), ('내사랑', '서대문구 이화여대2길 37', '070-8248-3752'), ('너스레', '서대문구 이화여대7길 22', '02-364-2221'), ('노란집', '서대문구 신촌역로 22 박스퀘어 2층 50호', '010-4832-3509'), ('다나제과', '서대문구 이화여대길 52-33 지하 1층', '010-4329-1006'), ('다다', '서대문구 이화여대3길 10', '02-393-1444'), ('다이몬키친', '서대문구 명물길 72 1층', '02-6369-6889'), ('닭꼬치야', '서대문구 신촌로11길 12 1층 우측', '02-332-5520'), ('담다베이글', '마포구 신촌로 190', '02-3275-1534'), ('대관령집밥', '서대문구 이화여대1안길 16', '02-393-5095'),  ('대성이네', '서대문구 연세로5나길 33 1층', '02-325-9658'), ('대작', '서대문구 명물길 27-13', '02-312-9201'), ('대현매운족발', '서대문구 연세로2길 95', '02-312-2215'), ('더파니니', '서대문구 이화여대길 50-10', '02-362-3567'), ('더벤티', '서대문구 이화여대길 52', '02-363-7292'), ('더빅바나나', '마포구 신촌로4길 14 지하1층', '010-3284-5002'), ('더착한커피', '서대문구 이화여대1안길 3', '02-393-2849'), ('도나파스텔', '서대문구 신촌역로 16 1층', '02-365-7074'), ('도토리칼국수', '서대문구 명물길 27-19', '02-704-2588'), ('돈노코돈먹기', '서대문구 신촌역로 43 2층', '02-392-9993'), ('돈우마미', '서대문구 연세로5길 38', '010-3829-1482'), ('돈천동식당', '서대문구 이화여대길 52-39', '010-7734-8321'), ('돼지김밥', '마포구 숭문길 201', '02-702-0945'), ('디델리', '서대문구 이화여대7길 16 2층', '02-362-7042'), ('딸기골', '서대문구 연대동문길 29', '02-363-5563'), ('떡장군', '서대문구 연세로4길 67', '02-6081-0019'), ('떰브커피', '서대문구 이화여대7길 29 1층', '02-363-9807'), ('또르띠', '서대문구 이화여대7길 31 1층', '02-313-3888'), ('뜸들이다', '마포구 백범로 20', '02-6449-7252'), ('라구식당', '서대문구 연세로 42-24 1층', '02-364-2224'), ('라멘81번옥', '서대문구 신촌역로 16 신촌가이아', '02-313-2232'), ('라밥', '마포구 신촌로 170', '02-715-1005'), ('락희돈', '서대문구 신촌로 141 은하빌딩 1층', '02-393-9905'), ('롯데리아', '서대문구 이화여대길 59 1층', '02-312-3468'), ('료테이스시', '서대문구 명물길 36-4', '02-393-8902'), ('리또리또', '서대문구 이화여대길 52-33', '02-392-2525'), ('마기오', '서대문구 신촌로 171 1층', '02-6013-0520'), ('마더린러', '서대문구 이화여대5길 5', '070-7758-3030'), ('마이헬싱키', '서대문구 신촌로 203 핀란드타워 1층', '070-7012-2948'), ('마포텐', '서대문구 이화여대7길 29 마포텐', '070-4642-9882'), ('막퍼주는집', '서대문구 신촌역로 22-5 1층 10호', '02-3719-6921'), ('만나빈', '서대문구 성산로 551', 'NULL'), ('만동제과', '서대문구 연희로 32', '02-6489-2334'), ('맘맘테이블', '서대문구 연세로4길 33 1층', '02-313-0813'), ('맘스터치', '서대문구 신촌로 169-1', '02-365-1799'), ('매머드커피', '서대문구 이화여대8길 2', '010-6558-6342'), ('매운향솥', '서대문구 연세로11길 24', '02-336-7188'), ('메가커피', '서대문구 이화여대길 24 1층', '02-313-0910'), ('명성회관', '마포구 대흥로30길 17', '02-715-5599'), ('모닭모닭', '마포구 와우산로27길 24', '070-8286-9930'), ('모모커피', '서대문구 이화여대길 22', '070-8880-7747'), ('모미지식당', '서대문구 이화여대5길 15 2층', '070-4154-2000'), ('무릉도원', '서대문구 이화여대2가길 24', '02-365-4777'), ('문카페', '서대문구 이화여대8길 62 상가동 105호', '010-9968-1736'), ('미겔스타일', '서대문구 이화여대5길 36 1층 가호', '010-5008-6170'), ('미스터카츠', '서대문구 이화여대7길 20-6 2층', '02-363-0900'), ('민들레', '서대문구 이화여대1길 42-1', 'NULL'), ('밀랑스', '마포구 대흥로28길 5', '010-2553-3419'), ('밀키웨이', '서대문구 이화여대길 52-33 지하1층', '02-365-7939'), ('바나프레소', '서대문구 이화여대길 33', '070-8998-8950'), ('바른생각피자', '서대문구 이화여대길 88-13', '02-313-8244'), ('바비구기', '서대문구 이화여대8길 11', '02-363-3050'), ('박가네', '서대문구 이화여대5길 7-1', '02-393-8853'), ('반서울', '서대문구 이화여대길 87 2층', '070-8882-0110'), ('밥이꿀바비꿀', '서대문구 신촌역로 16 1층 101-1호', '070-4065-9417'), ('방배유부김밥', '서대문구 이화여대3길 6', '02-392-2555'), ('배떡', '서대문구 명물길 76-5', '02-6015-9312'), ('배바위양곱창', '서대문구 연세로7안길 42', '02-337-9993'), ('버거앤치즈', '서대문구 이화여대5길 8', '02-3291-5050'), ('버거킹', '서대문구 연세로 25', '02-322-3669'), ('버텍스', '서대문구 이화여대길 52-39', '02-363-9297'), ('베러댄와플', '서대문구 이화여대7길 35', '070-4032-0176'), ('베브릿지', '서대문구 이화여대길 37 1층', '070-7543-1913'), ('베지베어', '서대문구 신촌역로 22-5 박스퀘어 2층 49호', '070-7938-7373'), ('벨라프라하', '서대문구 이화여대길 77', '02-363-3559'), ('벨르커피', '서대문구 신촌로 149 신촌자이엘라 101동 208호', '02-313-5937'), ('별난아지매', '서대문구 이화여대길 50-8 1층', '02-565-3383'), ('볶음쌈밥', '서대문구 이화여대길 63', '02-362-8698'), ('봄봄', '서대문구 이화여대길 7 1층', '070-8881-1224'), ('불굴의떡볶이', '마포구 백범로1길 8-9 1층 우측', '02-6010-5001'), ('불밥', '서대문구 이화여대8길 11', '02-362-9833'), ('비밀', '서대문구 이화여대7길 48', '02-313-0877'), ('빈스빈스', '서대문구 이화여대길 43', '02-364-0924'), ('빠빠빠', '서대문구 연세로11길 19', '02-338-7888'), ('빵낀과', '서대문구 이화여대길 57', '02-364-8002'), ('사장님돈까스', '서대문구 이화여대7길 7 지하', '02-313-2280'), ('산동전병', '서대문구 이화여대길 88-15 1층 1호', '02-393-8777'), ('산청자매훠궈', '서대문구 이화여대1안길 16 1층', '02-6404-7788'), ('산타비', '서대문구 이화여대7길 10', '02-303-0039'), ('서브웨이', '서대문구 이화여대7길 30', '02-364-8870'), ('서왕만두', '서대문구 신촌역로 16', '02-312-8869'), ('세아마라탕', '서대문구 이화여대길 16 2층', '02-363-8860'), ('셔틀즈', '서대문구 이화여대길 56-3', '010-6502-7580'), ('소녀방앗간', '서대문구 이화여대길 52-39 1층', '02-363-0603'), ('소도적', '서대문구 명물길 27-13 1층', '02-362-0508'), ('소바야린', '서대문구 이화여대3길 10 1층', '02-312-0703'), ('소오밥집', '서대문구 이화여대길 50-10', '02-6397-8917'), ('솔리드웍스', '서대문구 이화여대길 88-3 1층', '070-4795-8437'), ('수복곱창', '서대문구 연세로9길 31', '02-337-2640'), ('쉬바펍', '서대문구 연세로 42-24', '02-365-6809'), ('스시가마시', '서대문구 신촌역로 17', '02-363-8691'), ('스시히바리', '서대문구 신촌로 189', '02-393-8289'), ('스타벅스', '서대문구 이화여대길 52', '1522-3232'), ('스탠바이키친', '서대문구 연대동문길 49', '02-365-6353'), ('스텔라커피', '마포구 신촌로 160 상가102호', '02-719-0472'), ('스튜디오웝', '서대문구 성산로 539', '010-6491-5520'), ('신룽푸마라탕', '서대문구 연세로4길 1', '02-392-3808'), ('신연경', '서대문구 연세로11길 25 (창천동) 비동', '02-392-8987'), ('심플리키친', '서대문구 이화여대5길 35 상가 1층 107호', '070-4132-7000'), ('싸움의고수', '서대문구 명물길 20', '02-365-7237'), ('쏘이54', '서대문구 이화여대3길 12', '010-5749-8710'), ('쏙만두', '서대문구 이화여대7길 29', '02-313-0171'), ('아늑', '서대문구 이화여대7길 27-4', '010-5393-7456'), ('아리랑컵밥', '서대문구 이화여대길 33', '02-313-3717'), ('아마스빈', '서대문구 이화여대7길 11', '02-393-1598'), ('아비꼬', '서대문구 이화여대2가길 17', '02-312-0252'), ('아콘스톨', '서대문구 신촌역로 17 1층 110호', '02-364-1301'), ('아토규카츠', '서대문구 명물길 38', '02-363-4588'), ('아티제', '서대문구 신촌로 99', '02-393-2155'), ('앨리스카페', '서대문구 이화여대길 52-31 2층', '02-392-8225'), ('야담', '서대문구 신촌역로 22-5 2층 51호', '070-7797-4008'), ('언니네양식당', '서대문구 신촌역로 22-5 신촌박스퀘어 2층 35호', '010-8248-7224'), ('엄마손김밥', '서대문구 이화여대5길 16 1층', '02-392-8939'), ('에그드랍', '서대문구 이화여대길 86', '02-363-1119'), ('엠아이스위트', '서대문구 명물길 66 1층', '070-8844-1106'), ('여래여거', '서대문구 이화여대길 56-3 1층 여래여거', '010-6472-5282'), ('여우골', '서대문구 연세로5다길 10', '02-6337-4988'), ('연래춘', '마포구 신촌로22길 9', '02-717-3623'), ('연어초밥', '서대문구 연세로2길 94 1층 3호', '02-313-2611'), ('염인돈라멘', '서대문구 연세로2길 89-5', '010-2143-9840'), ('영미김밥', '서대문구 신촌역로 21 1층', '02-6081-3314'), ('영주김밥', '서대문구 연세로2길 90 1층', '02-3147-2209'), ('예원닭강정', '서대문구 연세로4길 67 1층', '02-6408-0019'), ('오봉도시락', '서대문구 이화여대길 52', '02-363-7292'), ('와플덴', '서대문구 이화여대길 58', '010-3749-1349'), ('운이좋은아이', '서대문구 이화여대길 88-19 1층 3호', '010-4794-8773'), ('울리에', '서대문구 신촌역로 22-5 신촌박스퀘어 2층 47호', '010-7622-1607'), ('위샐러듀', '서대문구 이화여대길 52-31', '02-363-0113'), ('유라꾸', '서대문구 이화여대3길 12-4', '02-324-7779'), ('유야케도쿄', '서대문구 이화여대3길 28 101호', '02-6401-7991'), ('육수당', '마포구 신촌로 182', '02-712-6462'), ('육회본가', '서대문구 연세로9길 23', '02-335-1006'), ('윤끼', '서대문구 이화여대길 65-3 1층', '070-4145-7869'), ('은희네', '서대문구 신촌역로 22-5 신촌박스퀘어 1층 9호', '010-9129-0878'), ('의원상', '서대문구 이화여대길 72-5', 'NULL'), ('이삭토스트', '서대문구 이화여대7길 15', '02-312-2444'), ('이츠동', '서대문구 신촌로31길 14 1층', '010-2956-3438'), ('이층쌀방', '서대문구 신촌역로 22-5 신촌 박스퀘어 2층', '010-6207-6122'), ('이코노스시', '서대문구 신촌역로 14', '02-364-8997'), ('이화성', '서대문구 이화여대길 50-8', '0507-0493-5846'), ('장군닭갈비', '서대문구 이화여대길 45 1층', '02-323-3220'), ('전티마이', '서대문구 이화여대길 59 메르체쇼핑몰 3층', '070-8250-1235'), ('젊음의행진', '서대문구 연세로9길 29', '02-3141-0355'), ('정육면체', '서대문구 연세로5다길 22-8 1층', '070-4179-3819'), ('존재의이유', '서대문구 성산로 553', '02-312-2992'), ('종금양꼬치', '마포구 대흥로30길 21', '02-701-9908'), ('주주', '서대문구 신촌역로 22-5', 'NULL'), ('중식당유', '서대문구 이화여대길 65-3 1층', '02-313-3201'), ('쥬씨', '서대문구 이화여대길 37', '070-7797-0741'), ('지구촌떡볶이', '서대문구 신촌역로 19-2 2층', '02-363-0877'), ('지니네컵밥', '서대문구 신촌역로 22-5', '010-9073-8440'), ('지지고', '서대문구 이화여대길 64', '02-363-7977'), ('진국수', '서대문구 이화여대길 78', '02-312-5369'), ('진솔한식', '서대문구 연세로2길 83', '02-363-3660'), ('진커피', '서대문구 북아현로 100 지하', 'NULL'), ('착한순우리', '마포구 숭문길 216', '02-716-0852'), ('참참참', '서대문구 이화여대길 52-31 지하1층', '02-363-1005'), ('천진분식', '서대문구 이화여대5길 7', '02-364-0410'), ('청년국수', '서대문구 연세로12길 23 청년국수', '02-313-1125'), ('청년다방', '서대문구 신촌로 139', '02-312-8955'), ('청년치킨', '서대문구 북아현로 8-2 1층', '02-365-8808'), ('청화원', '서대문구 명물길 10 1층', '010-1564-5555'), ('체셔캣', '서대문구 신촌로 169-7 103호 체셔캣', '010-8967-7635'), ('초식곳간', '서대문구 이화여대5길 2 1층', '02-365-5679'), ('총각떡볶이', '서대문구 이화여대5길 7-1 1층', '02-393-9777'), ('치즈문', '서대문구 이화여대길 88-13 1층', '010-3494-1316'), ('치킨더홈', '서대문구 이화여대길 29', '02-392-1207'), ('카시타', '서대문구 연세로9길 34-1 지하1층', '010-7559-7515'), ('카우떡볶이', '서대문구 이화여대길 88-21', '02-313-9999'), ('카우키', '서대문구 연세로9길 37 1층 103호', '02-336-1426'), ('카페아늑', '서대문구 이화여대7길 27-4', '010-5393-7456'), ('카페조에', '서대문구 이화여대길 50-6 1층', '070-4116-0040'), ('카페코지', '서대문구 이화여대길 88-19', '070-4307-4192'), ('카페티아라', '서대문구 성산로 553 동문빌딩', '02-313-4268'), ('카페페라', '서대문구 이화여대8길 2', '02-313-6085'), ('카페27도씨', '마포구 신촌로 160 지하1층 B09호', '02-703-7727'), ('칸타트', '서대문구 이화여대길 48', '010-2806-5362'), ('커리야', '서대문구 이화여대길 52-35 2층', '02-364-9991'), ('커피온리', '서대문구 신촌로 73 1층 커피온리', '010-6665-8815'), ('커피쥬세요', '서대문구 이화여대길 60 1층', '070-7755-5588'), ('커피콩즙', '서대문구 신촌역로 22-5 1층', 'NULL'), ('코지라운지', '서대문구 연세로7안길 10-5 2층', '010-5145-1780'), ('코쿤캅', '서대문구 신촌역로 22-5', '010-2298-2834'), ('코피발리', '서대문구 봉원사길 8', '010-3929-7979'), ('콩불', '서대문구 연세로 35', '02-322-8922'), ('클로버', '서대문구 신촌역로 22-5', 'NULL'), ('탐라', '서대문구 이화여대길 88-3 2층', '02-364-6575'), ('통큰갈비', '서대문구 연세로5다길 40 1층', '02-3141-1397'), ('투고샐러드', '서대문구 연세로12길 30', '02-393-2290'), ('투썸', '서대문구 이화여대길 7 월성빌딩 2층', '02-312-8014'), ('파란상자', '서대문구 이화여대길 72-4', 'NULL'), ('파리바게트', '서대문구 이화여대길 6', '02-365-4355'), ('파스타리코', '서대문구 신촌역로 23 1층', '02-313-6282'), ('파스타브라바', '서대문구 이화여대길 79 3층', '02-363-7787'), ('파스텔드나따', '서대문구 이화여대8길 2', '02-312-6439'), ('파파노다이닝', '서대문구 이화여대길 88-14', '02-364-0604'), ('팔색콩불', '서대문구 신촌로 149 신촌자이엘라', '02-365-1183'), ('팔팔쌈닭', '서대문구 신촌역로 22-5', 'NULL'), ('포케포케', '서대문구 이화여대5길 15', '02-6952-7685'), ('포포나무', '서대문구 이화여대2가길 24', '02-363-4552'), ('포히엔', '서대문구 이화여대3길 2', '02-365-1985'), ('품어떡', '서대문구 연세로2길 85 1층', '070-7543-0109'), ('피자쵸이', '서대문구 북아현로 78', '02-363-4224'), ('한끼마끼', '서대문구 이화여대1길 15 1층', '010-2521-7954'), ('할리우드', '서대문구 성산로 551 MEINLIEBESALPS', '02-393-1230'), ('해신포차', '서대문구 연세로9길 28', '02-322-6957'), ('호미반', '서대문구 이화여대길 88-19', '010-2602-5373'), ('호밀밭', '서대문구 신촌역로 43', '02-392-5345'), ('홍호아', '서대문구 신촌역로 22-6 1층', '02-333-8666'), ('화덕닭갈비', '서대문구 이화여대8길 3 연화프라자 2층', '02-392-9888'), ('화상손만두', '서대문구 이화여대7길 30 2층', '02-312-5888'), ('후쿠스시', '서대문구 이화여대3길 8', '02-363-0535'), ('훈카츠', '서대문구 이화여대1길 42-14', '02-312-3006'), ('히비야', '서대문구 이화여대2가길 24', '070-7764-6193'), ('히우카우', '서대문구 연세로4길 61 ,1층', '02-308-5111')]

    mycursor.executemany(sql, val)
    mydb.commit()
    mydb.close()
