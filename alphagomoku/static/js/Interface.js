

function SetGo(x,y){  //x,y 에 돌 넣기.
    setGo(x,y);
}

function MapState(){ //Map 변수 반환받기
    return Map;
} 

function PrintMap(){ //Map 변수 확인
    for(var n=0;n<15;n++){
        console.log(Map[n]);
    }
}

function RemoveAll(){ //모두제거
     model.init_list('circ_data')
     model.init_list('list_go')
     model.init_obj('verify_data')
     dol_color='black';
     MapIni()
     view.refresh()
}

function RemoveOne(){ //마지막만 제거
        model.pop('circ_data') 
       var get_last_id = model.call_data('list_go')
       get_last_id = get_last_id[get_last_id.length-1] 
       model.pop('list_go')
       model.pop_obj('verify_data',get_last_id)
       dol_color = dol_color == 'black' ? 'white' : 'black' 
       view.refresh()
}