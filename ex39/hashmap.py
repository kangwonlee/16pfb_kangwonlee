# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex39.html
# http://eclass.kpu.ac.kr/ilos/pf/course/lecture_material_view_form.acl?ARTL_NUM=373489&SCH_KEY=&SCH_VALUE=&display=10&start=1


def new(num_buckets=256):
    """
    Initializes a Map with the given number of buckets.
    :param num_buckets:
    :return:
    """
    aMap = []
    for i in range(0, num_buckets, ):
        aMap.append([])
    return aMap


# 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit

#  오류노트 에 각자 오류노트 작성
