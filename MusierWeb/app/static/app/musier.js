// 文本编辑插件
{}(function($){
    /*
     * 文本域光标操作（选、添、删、取）
     */
    $.fn.extend({
        /*
         * 获取光标所在位置
         */
        iGetFieldPos:function(){
            var field=this.get(0);
            if(document.selection){
                //IE
                $(this).focus();
                var sel=document.selection;
                var range=sel.createRange();
                var dupRange=range.duplicate();
                dupRange.moveToElementText(field);
                dupRange.setEndPoint('EndToEnd',range);
                field.selectionStart=dupRange.text.length-range.text.length;
                field.selectionEnd=field.selectionStart+ range.text.length;
            }
            return field.selectionStart;
        },
        /*
         * 选中指定位置内字符 || 设置光标位置
         * --- 从start起选中(含第start个)，到第end结束（不含第end个）
         * --- 若不输入end值，即为设置光标的位置（第start字符后）
         */
        iSelectField:function(start,end){
            var field=this.get(0);
            //end未定义，则为设置光标位置
            if(arguments[1]==undefined){
                end=start;
            }
            if(document.selection){
                //IE
                var range = field.createTextRange();
                range.moveEnd('character',-$(this).val().length);
                range.moveEnd('character',end);
                range.moveStart('character',start);
                range.select();
            }else{
                //非IE
                field.setSelectionRange(start,end);
                $(this).focus();
            }
        },
        /*
         * 选中指定字符串
         */
        iSelectStr:function(str){
            var field=this.get(0);
            var i=$(this).val().indexOf(str);
            i != -1 ? $(this).iSelectField(i,i+str.length) : false;
        },
        /*
         * 在光标之后插入字符串
         */
        iAddField:function(str){
            var field=this.get(0);
            var v=$(this).val();
            var len=$(this).val().length;
            if(document.selection){
                //IE
                $(this).focus()
                document.selection.createRange().text=str;
            }else{
                //非IE
                var selPos=field.selectionStart;
                $(this).val($(this).val().slice(0,field.selectionStart)+str+$(this).val().slice(field.selectionStart,len));
                this.iSelectField(selPos+str.length);
            };
        },
        /*
         * 删除光标前面(-)或者后面(+)的n个字符
         */
        iDelField:function(n){
            var field=this.get(0);
            var pos=$(this).iGetFieldPos();
            var v=$(this).val();
            //大于0则删除后面，小于0则删除前面
            $(this).val(n>0 ? v.slice(0,pos-n)+v.slice(pos) : v.slice(0,pos)+v.slice(pos-n));
            $(this).iSelectField(pos-(n<0 ? 0 : n));
        }
    });
})(jQuery);
/*
文本框代理
*/
var LongNote = 0,
    pitch = 0,
    sharp = 0,
    total = 0,
    meter = parseInt($('#Meter').val())+2;
var lenUnLock = false,
    pitUnLock = false,
    sharpUnLock = false,
    n_bgn = false;
$("#inputArea").keyup(function(evt) {
  var content = $(this).val();
  content = content.replace(/[^\x00-\xff]/g,"");
  content = content.replace(/[A-Za-z\s ]/g,"");
  $(this).val(content);
});    
$("#inputArea").keydown(function(event){
  switch (event.keyCode) {
    case 46: // Delete
    case 8: // Backspace
      var pos=$(this).iGetFieldPos();
      var v=$(this).val();
      switch (v.charAt(pos-1)){
        case ",":
          if((pitch <= -1)&&pitUnLock){
            pitch += 1;
            $(this).iDelField(1);
          }else if(pitUnLock&&(pitch <= 1)){
            $(this).iAddField("'");
            pitch += 1;
          }
          break;
        case "'":
          if((pitch >= 1)&&pitUnLock){
            pitch -= 1;
            $(this).iDelField(1);
          }else if(pitUnLock&&(pitch >= -1)){
            $(this).iAddField(",");
            pitch -= 1;
          }
          break;
        case "+":
          if(LongNote >= 1){
            LongNote -= 1;
            $(this).iDelField(1);
          }
          if(LongNote == 0){
            pitUnLock = true;
          };
          if ((LongNote+(total%(2*meter)))===(2*meter)){
            console.log(LongNote);
            lenUnLock =false;
          }else{
            lenUnLock =true;
          }
          break;
        case "1":
        case "2":
        case "3":
        case "4":
        case "5":
        case "6":
        case "7":
          total -= 1;
          for(var i = v.length-2; i >=0;i-- ){
            var note = v.charAt(i);
            console.log(note,LongNote);
            switch (note){
              case ",":
                pitch -= 1;
                break;
              case "'":
                pitch += 1;
                break;
              case "+":
                LongNote += 1;
                break;
            }
            if (!isNaN(parseInt(note, 10))){
              break;
            }

          }
          total -= LongNote;
          if ((LongNote+(total%(2*meter)))===(2*meter)){
            console.log(LongNote);
            lenUnLock =false;
          }else{
            lenUnLock =true;
          }
          $(this).iDelField(1);
          break;
      }
      return false;
      break;
  };
});

$("#inputArea").keypress(function(event){

  var k = event.which; 
  
  k = String.fromCharCode(k);
  switch(k){
      case "w": 
        console.log(pitUnLock);
        if((pitch <= -1)&&pitUnLock){
          pitch += 1;
          $(this).iDelField(1);
        }else if(pitUnLock&&(pitch <= 1)){
          $(this).iAddField("'");
          pitch += 1;
        }
        break;
      case "s": 
        if((pitch >= 1)&&pitUnLock){
          pitch -= 1;
          $(this).iDelField(1);
        }else if(pitUnLock&&(pitch >= -1)){
          $(this).iAddField(",");
          pitch -= 1;
        }
        break;
      case "d": 
        if(lenUnLock){
          $(this).iAddField("+");
          LongNote += 1;
          pitUnLock = false;
        }
        console.log("LongNote",LongNote);
        if ((LongNote+(total%(2*meter)))===(2*meter)){
          
          lenUnLock =false;
        }
        break;
      case "a": 
        console.log(LongNote);
        if(LongNote >= 1){
          LongNote -= 1;
          $(this).iDelField(1);
        }
        if(LongNote == 0){
          pitUnLock = true;
        };
        if (n_bgn){
          lenUnLock = true;
        }
        break;
      case "1": 
        $(this).iAddField("1");
        if ((LongNote+1+total%(2*meter))===(2*meter)){
          lenUnLock =false;
        }else{
          lenUnLock = true;
        }
        total = total+LongNote+1;
        LongNote = 0;
        pitch = 0;
        pitUnLock = true;
        n_bgn = true;
        break;
      case "2": 
        $(this).iAddField("2");
        if ((LongNote+1+total%(2*meter))===(2*meter)){
          lenUnLock =false;
        }else{
          lenUnLock = true;
        }
        total = total+LongNote+1;
        LongNote = 0;
        pitch = 0;
        pitUnLock = true;
        n_bgn = true;
        break;
      case "3": 
        $(this).iAddField("3");
        if ((LongNote+1+total%(2*meter))===(2*meter)){
          lenUnLock =false;
        }else{
          lenUnLock = true;
        }
        total = total+LongNote+1;
        LongNote = 0;
        pitch = 0;
        pitUnLock = true;
        n_bgn = true;
        break;
      case "4": 
        $(this).iAddField("4");
        if ((LongNote+1+total%(2*meter))===(2*meter)){
          lenUnLock =false;
        }else{
          lenUnLock = true;
        }
        total = total+LongNote+1;
        LongNote = 0;
        pitch = 0;
        pitUnLock = true;
        n_bgn = true;
        break;
      case "5": 
        $(this).iAddField("5");
        if ((LongNote+1+total%(2*meter))===(2*meter)){
          lenUnLock =false;
        }else{
          lenUnLock = true;
        }
        total = total+LongNote+1;
        LongNote = 0;
        pitch = 0;
        pitUnLock = true;
        n_bgn = true;
        break;
      case "6": 
        $(this).iAddField("6");
        if ((LongNote+1+total%(2*meter))===(2*meter)){
          lenUnLock =false;
        }else{
          lenUnLock = true;
        }
        total = total+LongNote+1;
        LongNote = 0;
        pitch = 0;
        pitUnLock = true;
        n_bgn = true;
        break;
      case "7": 
        $(this).iAddField("7");
        if ((LongNote+1+total%(2*meter))===(2*meter)){
          lenUnLock =false;
        }else{
          lenUnLock = true;
        }
        total = total+LongNote+1;
        LongNote = 0;
        pitch = 0;
        pitUnLock = true;
        n_bgn = true;
        break;
  }
  if ($(this).val().length === 0){
    n_bgn = false;
  }
  return false;
});
/*
Title 响应
*/
$('#Title').change(function(){
    $('#editor-textarea').focus();
    var Title = $('#Title').val(),
        content = $('#editor-textarea').val();
    var pos_T = content.indexOf("T"),
        pos_end = content.indexOf("M")-1;
    $('#editor-textarea').iSelectField(pos_T+2);
    $('#editor-textarea').iDelField(-(pos_end-pos_T-2));
    $('#editor-textarea').iAddField(Title);
    $('#editor-textarea').change();
    $('#Title').focus();
});

$('#Meter').change(function(){
  meter = parseInt($(this).val())+2;
  console.log(meter);

});
$('#clear').click(function(){
    LongNote = 0;
    pitch = 0;
    sharp = 0;
    total = 0;
    meter = parseInt($('#Meter').val())+2;
    lenUnLock = false;
    pitUnLock = false;
    sharpUnLock = false;
    n_bgn = false;
    $('#inputArea').val("");
    $("#Major").removeAttr("readonly");
    $("#Meter").removeAttr("readonly");
});

