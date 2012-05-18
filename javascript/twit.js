//ツイートカウント取得関数
var tweetCount = function(_id ,_url) {
	if(!_id)	return;
	var pageURL = (_url) ? _url : location.href;
	pageURL = encodeURI(pageURL);
	var callback_name = 'jsonp_' + _id;
	var url = 'http://urls.api.twitter.com/1/urls/count.json?url=' + pageURL + '&callback=' + callback_name + '&noncache=' + new Date();
	//JSONの読み込み
	var target = document.createElement('script');
	target.charset = 'utf-8';
	target.src = url;
	document.body.appendChild(target);
	window[callback_name] = function(data){
		//読み込み結果
		document.getElementById(_id).innerHTML = data.count;
	};
}
