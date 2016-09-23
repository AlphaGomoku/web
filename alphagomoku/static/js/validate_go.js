( function () {

var validate = {}



//8방향
var vector = [
        {x:1,y:1,c:1},
        {x:1,y:0,c:4},
        {x:1,y:-1,c:3},
        {x:0,y:1,c:2},
        {x:0,y:-1,c:2},
        {x:-1 ,y:1 ,c:3},
        {x:-1 ,y:0 ,c:4},
        {x:-1 ,y:-1,c:1 }
]

var dX = [0,1,1, 1]
var dY = [1,1,0,-1]
Array.prototype.isUniqueList = function() {

    for (var i = 0; i < this.length - 1; i++)
    {   
        for (var j = 0; j <this.length; j++)
        {   
            if ( i != j)
            {   
                if (this[i] == this[j])
                {   
                return false
                }   
            }   
        }   

    }   

return true
}//end


validate.isThere = function (list_of_go,loc) {

    var isThere_index = 0

    if (list_of_go.length == 0)
        { 
            return 0;
        }

    list_of_go.some( function(val) {
                        if (val == (loc.x + 10000*loc.y))
                          { 
                              return true
                          }
                        else
                         {
                            isThere_index +=1
                             return false
                         }})

    if (isThere_index == list_of_go.length)
        {
            return 0
        }
    else
        {
            return 1
        }
} // end




validate.isWin = function(cIdx,x,y) {    
    for(var n=0;n<4;n++){
        var dx = dX[n],dy = dY[n];
        var cnt = 1;
        for(var m=0;m<2;m++){
            dx*=-1;
            dy*=-1;
            var tx = x,ty = y;
            var nx = tx+dx,ny = ty+dy;
            
            while(nx>=0 && nx<15 && ny>=0 && ny<15 && cIdx==Map[ny][nx]){
                cnt++;
                tx = nx; 
                ty = ny;
                nx = tx+dx;
                ny = ty+dy;
            }
        }       
        if(cnt>=5) return true;
    }
    return false;
} 

validate.isThreeThree = function(cIdx,x,y) {
    var fourNum=0;
    var threeNum=0;
        for(var n=0;n<4;n++){
        var dx = dX[n],dy = dY[n];
        var cnt = 1;
        var flag =1;
        for(var m=0;m<2;m++){
            dx*=-1;
            dy*=-1;
            var tx = x,ty = y;
            var nx = tx+dx,ny = ty+dy;
            while(nx>=0 && nx<15 && ny>=0 && ny<15 && (cIdx==Map[ny][nx] || flag==1)){
                if(cIdx!=Map[ny][nx]) flag=0;                
                else cnt++;
                tx = nx; 
                ty = ny;
                nx = tx+dx;
                ny = ty+dy;
            }
        }     
        if(cnt==3) threeNum++;  
        else if(cnt==4) fourNum++;
       console.log("Cnt : " +cnt);
    }
    if (threeNum>=2){alert('3X3 invalid'); return true;}
    else if(fourNum>=2) {alert('4X4 invalid'); return true;} 
    else return false;

} //end 
validate.isSix = function(cIdx,x,y) {
  for(var n=0;n<4;n++){
        var dx = dX[n],dy = dY[n];
        var cnt = 1;
        for(var m=0;m<2;m++){
            dx*=-1;
            dy*=-1;
            var tx = x,ty = y;
            var nx = tx+dx,ny = ty+dy;
            
            while(nx>=0 && nx<15 && ny>=0 && ny<15 && cIdx==Map[ny][nx]){
                cnt++;
                tx = nx; 
                ty = ny;
                nx = tx+dx;
                ny = ty+dy;
            }
        }       
        if(cnt>5) {alert('over 5 invalid'); return true;}
    }
    return false;
} //end 


this.validate = validate


})();
