# 3번



## 1. super key

row를 특정하려면 알아야 하는 최소 컬럼은?

- 어떤 작물인가
- 어떤 작물이고, 어떤 품종인가
- 어떤 작물이고, 어떤 품종이면서, 어디서 생산되었는가
- 어떤 작물이고, 어떤 품종이면서, 어떤 등급이고, 어디서 생산되었는가

이 4가지 조건을 알아야 비로소 하나의 row를 특정할 수 있다.



여기서 어디서에 대한 조건이 Country / Region으로 나뉜다. Region을 알면 Country를 알 수 있지만 Country를 안다고 해서 Region을 알 수 있는건 아니기 때문에

- `'Product', 'Variety', 'Grades', 'Region'`
- `'Region', 'Country'`

2가지 조건으로 테이블을 나눈 뒤 중복을 제거했다. 물론 기준에 따라서 국가별로 조건을 거는 경우가 많다면 그대로 남겨두거나 Country를 foreigin key로 사용하도록 테이블 구성을 해도 될것 같다.

![image](https://user-images.githubusercontent.com/52685258/144448632-b0557747-e925-468e-b64c-4a4c301bc8a4.png)

![image](https://user-images.githubusercontent.com/52685258/144448675-8737676a-03d7-43a8-b3ac-e897d906f7c5.png)





## 2. date column

날짜 컬럼이 너무 많았다. 새로운 날짜가 생길 때마다 컬럼을 추가하는건 매우 비효율적이기 때문에 날짜를 나타내는 `Produce_Date` 컬럼을 만든 뒤 모든 날짜 관련 컬럼을 `Produce_Date` 컬럼의 value로 넣었고, 날짜 컬럼이 갖고 있던 value는 `Product_Quantity` 라는 새로운 컬럼을 만들어 그 값으로 넣어주었다.

table reshaping에는 pandas의 melt 메서드를 사용했다.

![image](https://user-images.githubusercontent.com/52685258/144449461-f41d3949-7cfd-4206-af8f-a788eaf19479.png)

Country 컬럼을 삭제한 건 선택사항이다. 이제 위에서 분리했던 4개 컬럼 `'Product', 'Variety', 'Grades', 'Region'` 을 기준으로 원하는 날짜만 안다면 생산량을 알 수 있다.



## 3. 중복 문제

NaN 등으로 컬럼의 unique함을 따질 수 없는 경우도 있었다.

![image](https://user-images.githubusercontent.com/52685258/144450416-4ac9e1bb-3ae6-480a-b922-475a070303ce.png)

Grade로 나눠지거나 Region이 좀 더 상세하게 나눠져야 유일한 row를 식별할 수 있을 것 같은데, 이 상태라면 `Product, Country, Variety, Grades, Region`  5개 컬럼으로도 유일한 값을 식별할 수 없다. 

추가적인 조건이 필요하거나, 나의 데이터와 정규화에 대한 이해도가 부족한 것이라 생각한다. 정규화할 수 없다고 판단했고, 2번 과정에서 `Product_Quantity` 컬럼이 NaN인 row는 전부 삭제했지만 중복은 여전히 남아있다.