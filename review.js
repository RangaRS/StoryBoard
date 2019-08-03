

var NAME = "visitor_name";
var EMAIL = "visitor_email";
var COMMENTS = "visitor_comments";




function putInLocal(key, value){
    localStorage.setItem(key, value);
}

function putInSession(key, value){
    sessionStorage.setItem(key, value);
}

function get(key){
    if((value = sessionStorage.getItem(key)) == null){
        value = localStorage.getItem(key);
    }
    return value;
}


function addComments(comment){
    comments = get(COMMENTS);
    if(comments == null || comments === null || comments == "null"){
        comments = "{}";
    }
    comments = JSON.parse(comments);
    pageComments = comments[page];
    if(pageComments == null || pageComments === null || pageComments == "null"){
        pageComments = "[]";
        pageComments = JSON.parse(pageComments);
    }
    pageComments.push(comment);
    comments[page] = pageComments;
    putInSession(COMMENTS, JSON.stringify(comments));
}

function getAllComments(){
    comments = get(COMMENTS);
    if(comments == null || comments === null || comments == "null"){
        comments = "{}";
    }
    comments = JSON.parse(comments);
    return comments;
}

function getComments(forPage){
    comments = get(COMMENTS);
    if(comments == null || comments === null || comments == "null"){
        comments = "{}";
    }
    comments = JSON.parse(comments);
    pageComments = comments[page];
    if(pageComments == null || pageComments === null || pageComments == "null"){
        pageComments = "[]";
        pageComments = JSON.parse(pageComments);
    }
    return pageComments;
}


$( document ).ready(function() {
	url = $(location).attr("href");
	var pathArray = window.location.pathname.split('/');
	page = $("input#pageName").val();
	if(page == "null" || page === null || page == null || page == "undefined"){
		page = pathArray[pathArray.length-1];
	}
	topic = pathArray[pathArray.length-2];
	COMMENTS = COMMENTS+"_"+topic;

	doNotShow = $("input#DoNotShowComment").val();
	if(doNotShow){
		
	}
	else{
		
		var html = "<style> html, body {     min-height: 100%; } body {     position: relative;     font-family: arial; } input[type='submit'] {     width: 120px;     padding: 9px 0px;     font-weight: normal;     margin-top: 4px;     background: #3289c7;     color: #fff;     border: 0px;     font-size: 13px;     text-align: center; } #setup input[type='submit'] {     margin: auto;     display: block;     margin-left: 140px; } .form-heading {     font-family: lato;     background: #eee;     padding: 15px 101px 15px 94px;     margin: -30px -70px; } input[type='text'] {     border: 1px solid #ddd;     width: 260px;     height: 33px; } input[type='text']#name {     margin-top: 40px;     margin-left: 40px; } input[type='text']#email {     margin-top: 15px;     margin-left: 43px;     margin-bottom: 20px; } .editor-content {     padding: 10px;     outline: none;     min-height: 80px;     background: #fff;     border-radius: 5px 5px 5px 5px; } .comments {     margin: 10px auto; } .comment_box {     top: 0;     right: 0;     position: absolute;     width: 20%;     z-index: 5;     float: right;     background: #f9f9f9;     border: 1px solid #ddd;     padding: 16px;     bottom: 0px;     box-shadow: 5px -9px 25px #888888 } .insert-text .total-comment:before {     content: 'Total comment: ';     font-weight: normal; } .list-comments {     font-family: lato; } .editor {     border: 1px solid #ccc;     border-radius: 2px;     background: #fff; } .comment_button {  border-radius: 10px 10px 0px 0px;  top: 40%;     right: -66px;     position: absolute;     width: 150px;     z-index: 5;     background: #29bb78;     color: #fff;     float: right;     text-align: center;     padding: 13px 15px;     transform: rotate(-90deg); } #show {          position: absolute;     left: -38px;     background: #eee;     border: 1px solid #ddd;     padding: 8px 13px;     top: -1px;     color: #000; } #user {     padding-bottom: 10px; } .overlay {      /* some styles to position the modal at the center of the page */     position: absolute;     z-index: 50;     top: 25%;     left: 34%;     margin-top: 0px;     background-color: #fff;     outline: 9999px solid rgba(0,0,0,0.5);     width: 450px;     padding: 15px 0px 25px 70px; } .hide {     display: none; } textarea {     resize: none;     outline: none;     width: 394px;     font-family: tahoma;     background: #f9f9f9; } textarea:focus {     background: #fff; } .content {     width: 100%; } .sub-feed {     color: #888; } .insert-text {     position: relative; } .insert-text .loading {     position: absolute;     bottom: -25px;     display: none; } .insert-text .total-comment {     position: absolute;     bottom: 8px;     right: 0px;     font-size: 14px; } .list-comments > div {     padding: 10px;     border-bottom: 1px solid #eee; } .list-comments > div:last-child {    } .editor-header {     border-bottom: 1px solid #ccc;     display: none; } .editor-header a {     display: inline-block;     padding: 10px;     color: #666; } .editor-header a:hover {     color: #000; } } .editor-content:focus {     background: #fff; } b {     font-weight: bold; } i {     font-style: italic; } p {     line-height: 20px; } a {     text-decoration: none; } [data-role='bold'] {     font-weight: bold; } [data-role='italic'] {     font-style: italic; } [data-role='underline'] {     text-decoration: underline; } [class^='menu'] {     position: relative;     top: 6px;     display: block;     width: 27px;     height: 2px;     margin: 0 auto;     background: #999; } [class^='menu']:before {     content: '';     top: -5px;     width: 80%;     position: relative;     display: block;     height: 2px;     margin: 0 auto;     background: #999; } [class^='menu']:after {     content: '';     top: 3px;     width: 80%;     position: relative;     display: block;     height: 2px;     margin: 0 auto;     background: #999; } .menu-left {     margin-right: 5px; } .menu-left:before {     margin-right: 5px; } .menu-left:after {     margin-right: 5px; } .menu-right {     margin-left: 5px; } .menu-right:before {     margin-left: 5px; } .menu-right:after {     margin-left: 5px; } .sub-title {     font-size: 14px;     padding-bottom: 10px;     padding-top: 10px; } </style> <div id='setup' class='hide'> <b class='form-heading'>Fill the form before jumping into UI prototype</b><br />   <br />   Name  :   <input type='text' name='name' id='name'>   <br />   <br />   Email :   <input type='text' name='email' id='email'>   <br />   <br />   <input type='submit'  value='Start' onclick='saveLocally();'> </div> <div class='comment_button' id='hide' style='display: block;'>Add Comments</div> <div class='comment_box' style='display:none'><a href='#' id='show' >X</a>   <div id='content' style='display: block;' class='content'>     <div class='comments'>       <div id='user'>Welcome Guest </div>       <div class='sub-title'>Submit your feedback</div>       <div class='editor'>         <div class='editor-header'> <a href='#' data-role='bold'>B</a> <a href='#' data-role='italic'>I</a> <a href='#' data-role='underline'>U</a> <a href='#' data-role='justifyleft'><i class='menu-left'></i></a> <a href='#' data-role='justifycenter'><i class='menu-center'></i></a> <a href='#' data-role='justifyright'><i class='menu-right'></i></a> </div>         <div id='text' class='editor-content' contenteditable> </div>       </div>       <div class='insert-text'> <span class='loading'>Loading...</span> <span class='total-comment'></span>         <p>           <input type='submit' value='Add comment' />         </p>       </div>       <div class='list-comments'></div>     </div>   </div> </div> ";

		$('body').append(html);


		name = get(NAME);
		email = get(EMAIL);
		if(name == null || name == "undefined" || name == "null" || !name || name == ""){
			$('#setup').removeClass('hide').addClass('overlay');
		}
		else{
			$('#user').html("Welcome "+name);
		}
	}

});

$(document).ready(function(){
    $(".editor-header a").click(function(e){
      e.preventDefault();
  
      var _val = $(this).data("role"),
          _sizeValIn = parseInt($(this).data("size-val") + 1),
          _sizeValRe = parseInt($(this).data("size-val") - 1),
          _size = $(this).data("size");
      if(_size == "in-size"){
        document.execCommand(_val, false, _sizeValIn + "px");
      } else{
        document.execCommand(_val, false, _sizeValRe + "px");
      }
    });
  });
  
  $(document).ready(function(){
    var $text = $("#text"),
        $submit = $("input[type='submit']"),
        $listComment = $(".list-comments"),
        $loading = $(".loading"),
        _data,
        $totalCom = $(".total-comment");
    
    arr = getComments(page);
    for(i=0; i<arr.length; i++){
        $listComment.append(arr[i]);
    }

    $totalCom.text($(".list-comments > div").length);
  
    $($submit).click(function(){
      if($text.html() == ""){
        alert("Plesea write a comment!");
        $text.focus();
      } else{
        _data = $text.html();
        $loading.show().fadeOut(300);
        comment = "<div>"+_data+"</div>";
        $listComment.append(comment);
        $text.html("");
        $totalCom.text($(".list-comments > div").length);
        addComments(comment);
        return false;
      }
    });
  });

  $(document).ready(function(){    
    var show = $('.comment_box');
        $('#hide').click(function(){
            var hidden = $('.comment_button');
            hidden.hide('slide', {direction: 'right'}, 100, function(){show.show('slide', {direction: 'right'}, 50);});
        });
        
        $('#show').click(function(){
            var hidden = $('.comment_button');
            show.hide( function(){hidden.show('slide', {direction: 'right'}, 100);});
        });
    });

    $(document).ready(function(){    
        $("#end input[id='name']").val(get(NAME));
        $("#end input[id='email']").val(get(EMAIL));
        obj = getAllComments();
        comment_html = "";
        jQuery.each(obj, function(i, val) {
            comment_html += "<div id='page_wise'>";
            comment_html += i;
            comment_html += "<div style='padding-left:5em' id='comments'>";
            for(i=0; i<val.length;i++){
                comment_html += val[i] + "<br>";
            }
            comment_html += "</div>";
        });
        $("#end div[id='comments_box']").html(comment_html);
    });


    function saveLocally(){
        putInLocal(EMAIL, document.getElementById("email").value);
        putInLocal(NAME, document.getElementById("name").value);
        $('#setup').removeClass('overlay').addClass('hide');
    }