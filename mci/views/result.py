from flask import Blueprint, render_template

bp = Blueprint('result', __name__, url_prefix='/')

@bp.route('/result')
def result():
    # 1. 맞으면 10점 틀리면 0점
    # 2. 개당 1점 
    # 3. 0.1 -> 1점...?? 이건 이야기 해봐야 할듯
    #4. 1개당 3점 , 다 맟히면 10점
    #5. 점수 갖고오기
    #6. 맞으면 10점 틀리면 0점
    #np.array['sim_point','stroop_point','write_point','wrong_point','remember_point','stt_point']

    #1 sim_point
    if sql[0][3] =='오답':
        sim_point = 0
    else : sim_point = 10
    # 2 stroop_point
    ##방법1. for 사용해서 점수 더하기
    stroop_point = 0
    index = range(2,10) # 아직 문제를 8개 할지 10개 할지 안 정해서 인덱스로 갖고옴. 나중에 10로 확정되면  for i in range(2,12) 로 바꾸면 될듯
    for i in index:
        if sql[1][index]=='정답':
            stroop_point += 1
        elif sql[1][index]=='오답':
            stroop_point +=0
    if stroop_point == 8: # 2점 더 주기(문제가 8개라서.. 만약 10개로 늘어나면 삭제하기)
        stroop_point = 10

    ## 방법2. 모든 컬럼을 하나의 list 에 담기 - stroop_point = len(list()) 
    index = range(2,10)
    stroop_list =[]
    for i in index :
        stroop_list.append(sql[1][index])
    stroop_point = stroop_list.count('정답')

    if stroop_point == 8: # 2점 더 주기(문제가 8개라서.. 만약 10개로 늘어나면 삭제하기)
        stroop_point = 10

    #3 write_point
    write_point =str(sql[2][2])[2]# 점수를 str 으로 바꿔서 슬라이싱 해서 갖고 오기
    write_point = int(write_point)
    if write_point == '0':
        if str(sql[2][2])[0] == '0':
            write_point = 0
        elif str(sql[2][2])[0] == '1':
            write_point = 10

    # 4 wrong_point
    # 방법 1 for 사용해서 점수 더하기
    wrong_point = 0
    if sql[3][1]== '정답': wrong_point +=3
    else : wrong_point +=0
    if sql[3][2]== '정답': wrong_point +=3
    else : wrong_point +=0
    if sql[3][3]== '정답': wrong_point +=3
    else : wrong_point +=0
    #이렇게 3개를 하게되면 마지막 1점을 어떻게 더 해줄지 고민해야함 if wrong_point == 9 : worng_point = 10 같을걸 생각해보기
    if wrong_point == 9:
        wrong_point = 10    

    # 방법 2 정답을 하나의 리스트에 담아서 정답의 갯수로 점수주기
    index = range(1,4)
    wrong_list =[]
    for i in index :
        wrong_list.append(sql[3][index])
        
    wrong_point = wrong_list.count('정답')
    if wrong_point == 9: # 2점 더 주기(문제가 8개라서.. 만약 10개로 늘어나면 삭제하기)
        wrong_point = 10
        
    #5 remember_point
    remember_point = sql[4][3]
    
    
    #6 stt_point
    if sql[5][4]==1 : stt_point = 10 
    else:stt_point = 0
    
    return render_template('dashboardd.html')