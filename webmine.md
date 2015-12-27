

```
import requests
from bs4 import BeautifulSoup
import textblob
```


```
url_to_scrape = 'http://uptake.com/'
```


```
r = requests.get(url_to_scrape)
```


```
soup = BeautifulSoup(r.text, "lxml")
```


```
r = requests.get(url_to_scrape, headers={'User-Agent': 'Mozilla/5.0'})
```


```
soup = BeautifulSoup(r.content, "lxml")
```


```
print(soup.prettify)
```

    <bound method Tag.prettify of <!DOCTYPE html>
    <html class="no-js" lang="en-US">
    <head>
    <meta charset="utf-8"/>
    <meta content="ie=edge" http-equiv="x-ua-compatible"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/favicon.ico" rel="shortcut icon"/>
    <meta content="Home" property="og:title"/>
    <meta content="" property="og:description"/>
    <meta content="http://uptake.com/" property="og:url"/>
    <meta content="" property="og:image"/>
    <link href="//cloud.typography.com/6511954/725746/css/fonts.css" rel="stylesheet" type="text/css"/>
    <title>Home | Uptake</title>
    <meta content="Uptake" name="copyright" property="og:site_name"/>
    <meta content="Home, Uptake" property="og:title"/>
    <script type="text/javascript">
    			window._wpemojiSettings = {"baseUrl":"http:\/\/s.w.org\/images\/core\/emoji\/72x72\/","ext":".png","source":{"concatemoji":"http:\/\/uptake.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=4.3.1"}};
    			!function(a,b,c){function d(a){var c=b.createElement("canvas"),d=c.getContext&&c.getContext("2d");return d&&d.fillText?(d.textBaseline="top",d.font="600 32px Arial","flag"===a?(d.fillText(String.fromCharCode(55356,56812,55356,56807),0,0),c.toDataURL().length>3e3):(d.fillText(String.fromCharCode(55357,56835),0,0),0!==d.getImageData(16,16,1,1).data[0])):!1}function e(a){var c=b.createElement("script");c.src=a,c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var f,g;c.supports={simple:d("simple"),flag:d("flag")},c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.simple&&c.supports.flag||(g=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",g,!1),a.addEventListener("load",g,!1)):(a.attachEvent("onload",g),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),f=c.source||{},f.concatemoji?e(f.concatemoji):f.wpemoji&&f.twemoji&&(e(f.twemoji),e(f.wpemoji)))}(window,document,window._wpemojiSettings);
    		</script>
    <style type="text/css">
    img.wp-smiley,
    img.emoji {
    	display: inline !important;
    	border: none !important;
    	box-shadow: none !important;
    	height: 1em !important;
    	width: 1em !important;
    	margin: 0 .07em !important;
    	vertical-align: -0.1em !important;
    	background: none !important;
    	padding: 0 !important;
    }
    </style>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=4.3" id="contact-form-7-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/useanyfont/uaf.css?ver=1447877802" id="uaf_client_css-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/js_composer/js_composer_front_custom.css?ver=4.4.2" id="js_composer_front-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/plugins/Ultimate_VC_Addons/assets/min-css/ultimate.min.css?ver=3.9.4" id="ultimate-style-min-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/smile_fonts/Defaults/Defaults.css?ver=4.3.1" id="bsf-Defaults-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/dist/styles/main.css?ver=4.3.1" id="uptake-css" media="all" rel="stylesheet" type="text/css"/>
    <script src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-includes/js/jquery/jquery.js?ver=1.11.3" type="text/javascript"></script>
    <script src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.2.1" type="text/javascript"></script>
    <script src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/plugins/Ultimate_VC_Addons/assets/min-js/ultimate.min.js?ver=3.9.4" type="text/javascript"></script>
    <link href="http://uptake.com/wp-includes/wlwmanifest.xml" rel="wlwmanifest" type="application/wlwmanifest+xml"/>
    <link href="http://uptake.com/" rel="canonical"/>
    <link href="http://uptake.com/" rel="shortlink"/>
    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-60287201-1']);
    _gaq.push(['_trackPageview']);
    (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
    </script>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-57x57.png" rel="apple-touch-icon" sizes="57x57"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-60x60.png" rel="apple-touch-icon" sizes="60x60"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-72x72.png" rel="apple-touch-icon" sizes="72x72"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-76x76.png" rel="apple-touch-icon" sizes="76x76"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-114x114.png" rel="apple-touch-icon" sizes="114x114"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-120x120.png" rel="apple-touch-icon" sizes="120x120"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-144x144.png" rel="apple-touch-icon" sizes="144x144"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-152x152.png" rel="apple-touch-icon" sizes="152x152"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/apple-touch-icon-180x180.png" rel="apple-touch-icon" sizes="180x180"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/android-chrome-192x192.png" rel="icon" sizes="192x192" type="image/png"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/favicon-96x96.png" rel="icon" sizes="96x96" type="image/png"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/manifest.json" rel="manifest"/>
    <link href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/fbrfg/favicon.ico" rel="shortcut icon"/>
    <meta content="#da532c" name="msapplication-TileColor"/>
    <meta content="/wp-content/uploads/fbrfg/mstile-144x144.png" name="msapplication-TileImage"/>
    <meta content="/wp-content/uploads/fbrfg/browserconfig.xml" name="msapplication-config"/>
    <meta content="#ffffff" name="theme-color"/><meta content="Powered by Visual Composer - drag and drop page builder for WordPress." name="generator"/>
    <!--[if IE 8]><link rel="stylesheet" type="text/css" href="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/plugins/js_composer/assets/css/vc-ie8.css" media="screen"><![endif]--><script type="text/javascript">jQuery(document).ready(function(){
    					jQuery(".ult_modal-body iframe").each(function(index, element) {
    						var st = '<style type="text/css" id="modal-css">';
    							st += ".fluid-width-video-wrapper{padding: 0 !important;}";
    							st += "</style>";
    						jQuery("head").append(st);
    					});
    				});</script> <link href="//cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" rel="stylesheet" type="text/css"/>
    </head>
    <body class="home page page-id-3068 page-template page-template-template-front-home page-template-template-front-home-php wpb-js-composer js-comp-ver-4.4.2 vc_responsive">
    <div class="svg-sprite">
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><symbol id="CommuterBenefits" viewbox="0 0 100 100"><path d="M78.4 6.2c4 0 7.2 3.2 7.2 7.2v55.4c0 4-3.2 7.2-7.2 7.2H21.6c-4 0-7.2-3.2-7.2-7.2V13.4c0-4 3.2-7.2 7.2-7.2h56.8m0-3H21.6c-5.6 0-10.2 4.6-10.2 10.2v55.4C11.4 74.4 16 79 21.6 79h56.8c5.6 0 10.2-4.6 10.2-10.2V13.4c0-5.7-4.6-10.2-10.2-10.2z" fill="#333"></path><path d="M24.4 77.2l-8.8 14.2c-.7 1.2-.4 2.7.8 3.4.4.3.9.4 1.3.4.8 0 1.7-.4 2.1-1.2l9.8-15.8c.2-.3.3-.7.3-1h-5.5zM75.6 77.2H70c0 .3.2.7.3 1L80.2 94c.5.8 1.3 1.2 2.1 1.2.4 0 .9-.1 1.3-.4 1.2-.7 1.5-2.3.8-3.4l-8.8-14.2zM73.8 17c1.1 0 2 .9 2 2v26c0 1.1-.9 2-2 2H26.2c-1.1 0-2-.9-2-2V19c0-1.1.9-2 2-2h47.6m0-3H26.2c-2.8 0-5 2.2-5 5v26c0 2.8 2.2 5 5 5h47.5c2.8 0 5-2.2 5-5V19c.1-2.7-2.2-5-4.9-5z" fill="#333"></path><g clip-rule="evenodd" fill="#333" fill-rule="evenodd"><circle cx="28.8" cy="61.2" r="4.6"></circle><circle cx="71.2" cy="61.2" r="4.6"></circle></g></symbol><symbol id="ConditionBasedMonitoring" viewbox="0 0 350 350"><path d="M54.3 165.6c-3.9 0-7.1 3.2-7.1 7.1s3.2 7.1 7.1 7.1 7.1-3.2 7.1-7.1-3.2-7.1-7.1-7.1z" fill="#0091B3"></path><path d="M105.4 157.5L96 170.4H64.6c.2.7.2 1.5.2 2.2 0 .4 0 .8-.1 1.2h33l10.4-14.3c-1-.5-1.9-1.2-2.7-2z" fill="#222720"></path><path d="M113.1 143.2c-3.9 0-7.1 3.2-7.1 7.1s3.2 7.1 7.1 7.1 7.1-3.2 7.1-7.1-3.2-7.1-7.1-7.1z" fill="#99999A"></path><path d="M161.4 109.8l-25.8 82.6-14.2-35.6c-.8 1-1.7 1.8-2.7 2.4l17.4 43.5 28.7-91.9c-1.3-.1-2.4-.5-3.4-1z" fill="#222720"></path><path d="M166.2 93.4c-3.9 0-7.1 3.2-7.1 7.1s3.2 7.1 7.1 7.1 7.1-3.2 7.1-7.1-3.2-7.1-7.1-7.1z" fill="#0091B3"></path><path d="M194.3 221.5l-24.1-111.3c-1 .4-2.2.7-3.4.8L191 222.2c1-.4 2.2-.7 3.3-.7z" fill="#222720"></path><path d="M194.7 224.9c-3.9 0-7.1 3.2-7.1 7.1s3.2 7.1 7.1 7.1 7.1-3.2 7.1-7.1-3.2-7.1-7.1-7.1z" fill="#99999A"></path><path d="M295.7 165.6c-3.9 0-7.1 3.2-7.1 7.1s3.2 7.1 7.1 7.1 7.1-3.2 7.1-7.1-3.2-7.1-7.1-7.1z" fill="#0091B3"></path><path d="M285.2 172.6c0-.8.1-1.5.2-2.2h-36.3l-21.8-39.9-30.7 91.2c1.2.2 2.2.6 3.2 1.2l28.2-83.8 18.9 34.8h38.2c.1-.4.1-.8.1-1.3z" fill="#222720"></path></symbol><symbol id="FridayLunch" viewbox="0 0 100 100"><path d="M43.1 67.9h13.7c-1.7-1.9-4.1-3.1-6.9-3.1s-5.1 1.2-6.8 3.1z" fill="#333"></path><path d="M50 58.6c-6.3 0-11.8 3.8-14.2 9.3h3.5c2.1-3.7 6.1-6.2 10.7-6.2s8.5 2.5 10.7 6.2h3.5c-2.4-5.5-7.9-9.3-14.2-9.3z" fill="#333"></path><path d="M50 43.1c12.5 0 23.2 7.4 28.1 18.1l-2.8 1.4A27.6 27.6 0 0 0 50 46.2c-13.3 0-24.3 9.3-27.1 21.7H26c2.8-10.7 12.4-18.6 24-18.6 10.1 0 18.7 6 22.6 14.7l-2.8 1.4c-3.4-7.6-11-12.9-19.8-12.9-9.8 0-18.1 6.5-20.8 15.5h3.3c2.6-7.2 9.4-12.4 17.5-12.4 7.6 0 14.2 4.6 17.1 11.2L64.8 68h13.8l1.5-.8c.1.3.1.5.2.8h3.1c-.1-.7-.3-1.5-.5-2.2l14.9-7.4c1.5-.8 2.1-2.6 1.4-4.2-.8-1.5-2.6-2.1-4.2-1.4l-14.2 7.1C75.5 48.2 63.7 40 50 40c-16.7 0-30.5 12-33.5 27.9h3.1C22.5 53.8 35 43.1 50 43.1zM25.2 39.1c0 .1 0 .1 0 0 0 .1 0 .1 0 0 .3.6.8.9 1.4.9.9 0 1.6-.7 1.6-1.6 0-.1 0-.3-.1-.4v-.1c-1.2-2.7-.1-5.7 1.3-9 1.5-3.5 3-7.4 1.3-11.3-.2-.6-.8-1-1.4-1-.8 0-1.5.7-1.5 1.5 0 .2 0 .4.1.5 1.3 2.8 0 5.7-1.3 9-1.4 3.4-3 7.2-1.4 11.1-.1.4-.1.4 0 .4zM62.9 38.7c.3.6.8.9 1.4.9.9 0 1.6-.7 1.6-1.6 0-.1 0-.3-.1-.4v-.1c-1.2-2.7-.1-5.7 1.3-9 1.5-3.5 3-7.4 1.3-11.3-.2-.6-.8-1-1.4-1-.8 0-1.5.7-1.5 1.5 0 .2 0 .4.1.5 1.3 2.8 0 5.7-1.3 9-1.4 3.4-3 7.2-1.4 11.1-.1.3-.1.3 0 .4zM47 25.3s0 .1 0 0c0 .1 0 .1 0 0 .3.6.8.9 1.4.9.9 0 1.6-.7 1.6-1.6 0-.1 0-.3-.1-.4v-.1c-1.2-2.7-.1-5.7 1.3-9 1.5-3.5 3-7.4 1.3-11.3-.2-.6-.8-1-1.4-1-.8 0-1.5.7-1.5 1.5 0 .2 0 .4.1.5 1.3 2.8 0 5.7-1.3 9-1.4 3.4-3 7.2-1.4 11.1-.1.3-.1.4 0 .4z" fill="#333"></path><path d="M94.1 70L78 84v9.5H20.4l-.6-9.5L4.2 70h89.9m0-3h-90c-1.2 0-2.4.8-2.8 1.9-.4 1.2-.1 2.5.8 3.3l14.7 13.1.5 8.3c.1 1.6 1.4 2.8 3 2.8H78c1.7 0 3-1.3 3-3v-8.1l15.1-13c.9-.8 1.3-2.1.8-3.3-.4-1.2-1.5-2-2.8-2z" fill="#333"></path></symbol><symbol id="FuelEnergy" viewbox="0 0 350 350"><path d="M255.1 173.4c0 10-1.8 19.5-5.1 28.3-19.9.3-130.1.3-150 0-3.3-8.8-5.1-18.3-5.1-28.3 0-44.3 35.9-80.1 80.1-80.1s80.1 35.8 80.1 80.1zM173.3 174.9l44.4-18.2" fill="none" stroke="#222720" stroke-miterlimit="10" stroke-width="3.453"></path><circle cx="114.1" cy="174.9" fill="#99999A" r="3"></circle><circle cx="233.3" cy="174.9" fill="#0091B3" r="3"></circle><circle cx="132.3" cy="138.4" fill="#99999A" r="3"></circle><circle cx="221.3" cy="138.4" fill="#0091B3" r="3"></circle><circle cx="175" cy="114.6" fill="#0091B3" r="3"></circle></symbol><symbol id="HappyHours" viewbox="0 0 100 100"><path d="M66.3 15.2c-2 9.3-4.7 21.6-5.3 23.5l-.1.5v.5c0 1.7.7 3 1.4 4.3 1.1 1.9 2 3.6 1 6.3-1.1 3.2-15.5 42.3-15.7 42.7l-.3.7v.2c-.4.1-1.1.1-2.3-.2-2.1-.4-4.4-1-6.9-1.9-3.9-1.4-7.6-3.2-10.6-4.7l-.1-.1c-.5-.3-1-.5-.6-1.4l.1-.2.1-.4c.1-.4 13-38 14.9-42.8.9-2.4 4.1-3.4 6.2-4.1 1.5-.5 2.5-.9 3.3-1.8l.4-.5.2-.7c.7-2.1 6.2-13.2 10.3-21.3l4 1.4m4.1-2.3l-9.7-3.5S49.8 30.5 48.8 34c-.7.9-8 1.7-10 6.9-1.9 4.9-14.9 42.9-14.9 42.9S21.7 87.9 26 90c3 1.5 6.9 3.4 11.1 4.9 2.4.9 4.9 1.6 7.4 2.1 6.9 1.3 6.5-2.9 6.5-2.9s14.5-39.5 15.7-42.7c2.2-6.1-2.3-9.5-2.3-11.8.9-2.9 6-26.7 6-26.7zM70.4 11.9l-8.3-3c-.9-.3-1.4-1.3-1-2.2.3-.9 1.3-1.4 2.2-1l8.3 3c.9.3 1.4 1.3 1 2.2s-1.3 1.3-2.2 1z" fill="#333"></path><path d="M33.7 80.5l11.5 4.2" fill="none" stroke="#333" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" stroke-width="2"></path><path d="M58.9 67.8l-29.1 2.6 4.7-12.9 29.1-2.6z" fill="none" stroke="#333" stroke-miterlimit="10" stroke-width="2"></path></symbol><symbol id="HealthCoverage" viewbox="0 0 100 100"><path d="M64.4 9.1v26.5h26.5v28.8H64.4v26.5H35.6V64.4H9.1V35.6h26.5V9.1h28.8m0-3H35.6c-1.7 0-3 1.3-3 3v23.5H9.1c-1.7 0-3 1.3-3 3v28.8c0 1.7 1.3 3 3 3h23.5v23.5c0 1.7 1.3 3 3 3h28.8c1.7 0 3-1.3 3-3V67.4h23.5c1.7 0 3-1.3 3-3V35.6c0-1.7-1.3-3-3-3H67.4V9.1c0-1.7-1.3-3-3-3z" fill="#333"></path></symbol><symbol id="LunchStipend" viewbox="-93 5 100 100"><path d="M-51 95.6c.6-.6 1-1.2 1.1-1.8 1.4-4.3 3.6-8 7-11.4 4.4-4.5 10.2-7.8 16.2-11.3 6.3-3.6 12.8-7.4 18.1-12.7 4.5-4.5 7.5-9.5 9.3-15.2.5-1.6.1-3.4-1.1-4.6l-28.1-28.1c-.9-.9-2.1-1.4-3.3-1.4-.4 0-.7.1-1 .2-.9.2-1.6.6-2.2 1.2-.6.5-1 1.2-1 1.8-1.4 4.3-3.6 8-7 11.4-4.5 4.5-10.2 7.8-16.2 11.3-6.3 3.6-12.8 7.4-18.1 12.7-4.5 4.5-7.5 9.5-9.3 15.2-.5 1.6-.1 3.4 1.1 4.6l27.9 28c.9.9 2.1 1.4 3.3 1.4.4 0 .7 0 1.1-.1.9-.2 1.6-.6 2.2-1.2zm-2.8-1.4l-1.2-1.3-6.9-6.9L-83 64.9l-.4-.4.2-.6c4.1-13.2 15-19.6 25.6-25.8 10.8-6.3 20.9-12.2 24.8-24.7l.5-1.6 1.2 1.2 21.2 21.2 6.9 6.9.4.4-.2.6c-4.1 13.3-15.1 19.6-25.7 25.8-10.8 6.3-20.9 12.2-24.8 24.7l-.5 1.6z" fill="#333"></path><path d="M-46.6 70.4c-1.8 1.3-3.5 2.8-5.1 4.4-1.5 1.5-2.9 3.1-4.1 4.8l-1.9 2.6c-.4.5-.3 1.3.2 1.8s1.4.5 2 0c.1-.1.2-.2.2-.3l1.8-2.5c1.1-1.5 2.4-3 3.8-4.4 1.6-1.6 3-2.8 4.8-4.1l.1-.1c.6-.5.6-1.4 0-2-.4-.7-1.2-.7-1.8-.2zM-36.3 29.8c-1.5 1.5-3.1 2.8-4.7 4-.1.1-.2.1-.3.2-.6.6-.6 1.5 0 2 .5.5 1.4.6 2 0 1.8-1.3 3.5-2.8 5-4.4 1.5-1.5 2.9-3.1 4.1-4.8l1.9-2.6c.5-.6.5-1.4-.1-1.9-.6-.6-1.4-.6-2 0-.1.1-.2.2-.2.3l-1.9 2.6c-1.1 1.7-2.4 3.2-3.8 4.6zM-37.3 64.3l-1.7-2.2-1.5 1.2c-1.3 1-2.4 1.5-3.4 1.4-1.2-.2-2-.8-4.5-3.9l2.6-2c1.7 2.1 2.1 2.4 2.5 2.5s.6-.1 1.4-.6l1.2-.9-3.9-5.1-2 1.3c-1.3.8-2.2 1.2-3.1 1.1-1.2-.2-2-.9-3.7-3.1-1.7-2.2-2.3-3.4-2.1-4.8.1-.9.8-1.9 2.1-2.8l1.4-1-1.5-1.9 2.2-1.7 1.5 1.9 1.2-.9c1.3-1 2.3-1.5 3.3-1.4 1.2.2 2 .8 4.5 3.7l-2.6 2c-1.6-1.9-2-2.3-2.4-2.3-.3 0-.5 0-1.2.5l-1 .8 3.8 4.9 2.2-1.4c1.3-.8 2.1-1.2 3-1.1 1.2.1 2 .9 3.8 3.2s2.4 3.5 2.2 4.9c-.1.9-.7 1.7-2 2.8l-1.6 1.2 1.7 2.2-2.4 1.5zM-47.7 53l1.2-.7-3.6-4.7-1.2.9c-.7.5-.8.7-.8 1.1 0 .4.4 1.1 1.4 2.4.9 1.2 1.3 1.5 1.7 1.6.3-.1.6-.2 1.3-.6zm5.3.3l3.8 4.9 1.3-1c.7-.5.8-.7.9-1.1.1-.4-.4-1.1-1.5-2.5-1-1.2-1.3-1.6-1.8-1.6-.3 0-.6.1-1.3.5l-1.4.8z" fill="#333"></path></symbol><symbol id="PTO" viewbox="0 0 100 100"><g fill="#333"><path d="M54.9 28.8c.3.5.6 1.1.9 1.6.1.2.2.3.4.2.3-.4.7-.8.6-1.4-.1-.8-.2-1.5-.3-2.3 0-.3-.1-.6 0-.8.5-.9 1.1-1.7 1.6-2.5.1-.2.3-.3.5 0 .2.2.4.4.5.6l2.7 3c.8.9 1.7 1.9 2.5 2.8.2.2.4.2.6 0 .3-.4.5-.8.3-1.3-.1-.3-.2-.6-.3-.8-.4-1.2-.9-2.3-1.3-3.5l-1.2-3c-.3-.7-.5-1.4-.8-2-.2-.5-.3-.9 0-1.4.9-1.4 1.8-2.9 2.6-4.3.3-.5.4-1.1.5-1.6.1-.5-.1-1-.6-1.3-.5-.3-1-.2-1.4.1-.4.3-.8.7-1.1 1.1l-3 4.5c-.2.3-.4.4-.8.4l-4.2.3-5.7.3c-.6 0-1.1.2-1.4.8-.2.4-.1.6.3.7l2.1.6c2 .6 4 1.2 5.9 1.8.4.1.5.2.2.6l-1.2 2.1c-.2.3-.4.6-.8.8-.7.2-1.3.4-1.9.7-.5.2-1 .4-1.3.9-.2.5-.2.7.4.7.6 0 1.1.1 1.7.1L45.5 38h3.6l5.8-9.2z"></path><path d="M84.5 17L59.3 1.1c-1-.6-2.1-.9-3.2-.9-2 0-4 1-5.1 2.8L13.6 62.2c-1.8 2.8-.9 6.5 1.9 8.3l19.1 12.1V79l-8.2-5.2 8.2-12.9v-5.6l-10.7 17-6.8-4.3c-1.4-.9-1.8-2.8-.9-4.2L53.6 4.6c.6-.9 1.5-1.4 2.6-1.4.6 0 1.1.2 1.6.5L83 19.6c1.4.9 1.8 2.8.9 4.2l-9 14.3c1.1.1 2 .7 2.6 1.5l9-14.2c1.6-2.9.8-6.6-2-8.4z"></path></g><path d="M74.2 41c.5 0 1 .5 1 1v53.7c0 .5-.5 1-1 1H38.6c-.5 0-1-.5-1-1V42c0-.5.5-1 1-1h35.6m0-3H38.6c-2.2 0-4 1.8-4 4v53.7c0 2.2 1.8 4 4 4h35.6c2.2 0 4-1.8 4-4V42c0-2.2-1.8-4-4-4z" fill="#333"></path><path d="M56.4 45.3c-6.8 0-12.3 5.5-12.3 12.3 0 6.8 5.5 12.3 12.3 12.3 6.8 0 12.3-5.5 12.3-12.3 0-6.8-5.5-12.3-12.3-12.3zm9.1 10.8h-3.4c-.1-2.4-.6-4.7-1.3-6.6 2.5 1.3 4.3 3.7 4.7 6.6zm-9.1 10.7c-.7 0-2.4-2.7-2.7-7.7h5.4c-.3 5-1.9 7.7-2.7 7.7zm-2.7-10.7c.3-5 2-7.7 2.7-7.7s2.4 2.7 2.7 7.7h-5.4zM52 49.5c-.7 1.9-1.2 4.2-1.3 6.6h-3.4c.5-2.9 2.3-5.3 4.7-6.6zm-4.7 9.6h3.4c.1 2.4.6 4.7 1.3 6.6-2.4-1.3-4.2-3.8-4.7-6.6zm13.5 6.6c.7-1.9 1.2-4.2 1.3-6.6h3.4c-.4 2.8-2.2 5.2-4.7 6.6z" fill="#333"></path><path d="M67.2 87.9H45.7c-.8 0-1.5-.7-1.5-1.5s.7-1.5 1.5-1.5h21.5c.8 0 1.5.7 1.5 1.5s-.7 1.5-1.5 1.5z" fill="#231F20"></path></symbol><symbol id="ParentalLeave" viewbox="0 0 100 100"><g fill="#333"><path d="M36 75.3V47.8L30.3 50l-1-2.8 7.3-3h2.9v31.1H36zM48.5 71.5c0-4.5.5-6.1 1.9-7.5.9-.9 1.9-1.5 4.3-2.5l8.7-3.5c1.7-.7 2.3-1.2 2.7-1.8.5-.7.8-1.6.8-4.1 0-1.8-.4-3.3-1-3.9-.6-.6-1.4-.8-3.1-.8h-6.3c-1.6 0-2.3.3-2.9.8-.5.6-.9 1.7-.9 5.2h-3.5c0-4.8.6-6.4 1.9-7.7 1-1 2.5-1.4 5.1-1.4h7.6c2.5 0 3.9.4 4.9 1.4 1.5 1.5 1.9 3.8 1.9 6.4 0 3.5-.5 4.9-1.5 6.2-.8 1.1-2.1 1.8-4.5 2.7l-8.7 3.5c-1.3.5-2.2 1-2.7 1.6-.7.8-1.1 1.6-1.1 4.5v1.6h18.8v3.1H48.5v-3.8z"></path><path d="M74.8 14.4h-5v-3.8c0-.6-.5-1-1-1-.6 0-1 .5-1 1v3.8H32.2v-3.8c0-.6-.5-1-1-1-.6 0-1 .5-1 1v3.8h-5c-6.1 0-11 4.9-11 11V75c0 6.1 4.9 11 11 11h49.6c6.1 0 11-4.9 11-11V25.4c0-6.1-4.9-11-11-11zm-49.6 1.7h5v1.6c-1.3.4-2.2 1.6-2.2 3 0 1.8 1.4 3.2 3.2 3.2 1.8 0 3.2-1.4 3.2-3.2 0-1.4-.9-2.6-2.2-3v-1.6h35.6v1.6c-1.3.4-2.2 1.6-2.2 3 0 1.8 1.4 3.2 3.2 3.2 1.8 0 3.2-1.4 3.2-3.2 0-1.4-.9-2.6-2.2-3v-1.6h5c5.1 0 9.3 4.2 9.3 9.3V33H15.9v-7.6c0-5.1 4.2-9.3 9.3-9.3zm6 4.8c.6 0 1-.5 1-1v-.4c.3.3.5.7.5 1.1 0 .8-.7 1.5-1.5 1.5s-1.5-.7-1.5-1.5c0-.4.2-.8.5-1.1v.4c0 .6.4 1 1 1zm37.6 0c.6 0 1-.5 1-1v-.4c.3.3.5.7.5 1.1 0 .8-.7 1.5-1.5 1.5s-1.5-.7-1.5-1.5c0-.4.2-.8.5-1.1v.4c0 .6.5 1 1 1zm6 63.4H25.2c-5.1 0-9.3-4.2-9.3-9.3V35h68.2v40c0 5.1-4.2 9.3-9.3 9.3z" stroke="#333" stroke-miterlimit="10" stroke-width=".5"></path></g></symbol><symbol id="PerformanceOptimization" viewbox="0 0 350 350"><path d="M240.7 191.5c7.1-9.5 10.2-21.1 8.5-32.9-1.6-11.7-7.8-22.1-17.2-29.3-8.4-6.3-18.4-9.4-28.8-8.9-1.3.1-2.7.2-4 .4-11.7 1.6-22.1 7.8-29.3 17.2-.6.8-.5 2 .4 2.7.5.3.9.4 1.2.4.6 0 1.1-.3 1.5-.8 6.5-8.6 16-14.2 26.7-15.7 1.3-.2 2.6-.3 3.9-.4 9.5-.5 18.5 2.4 26.2 8.2 8.6 6.5 14.2 16 15.7 26.7s-1.3 21.4-7.8 30c-.6.8-.5 2.1.4 2.7.5.3.9.4 1.2.4.5.1 1.1-.2 1.4-.7zM250.7 109.6l10-13.2c.6-.8.5-2.1-.4-2.7-.5-.3-.9-.4-1.2-.4-.6 0-1.1.3-1.5.8l-10 13.2c-.6.8-.5 2.1.4 2.7.5.3.9.4 1.2.4.6-.1 1.1-.4 1.5-.8zM217 94.3l2-16.4c.1-1-.6-2-1.7-2.1h-.3c-.9 0-1.7.8-1.8 1.7l-2 16.4c-.1 1 .6 2 1.7 2.1h.3c.9-.1 1.7-.8 1.8-1.7zM180.1 97.9l-6.4-15.2c-.3-.7-1.1-1.2-1.9-1.2-.2 0-.5.1-.7.2-1 .4-1.4 1.5-1 2.5l6.5 15.2c.3.7 1.1 1.2 1.9 1.2.2 0 .5-.1.7-.2.9-.4 1.4-1.5.9-2.5zM150.4 122.1c.6-.8.5-2-.4-2.7l-13.2-10c-.4-.3-.9-.4-1.2-.4-.6 0-1.1.3-1.5.8-.6.8-.5 2 .4 2.7l13.2 10c.5.3.9.4 1.2.4.7-.1 1.2-.3 1.5-.8zM276.4 219.8c.6-.8.5-2.1-.4-2.7l-13.2-10c-.5-.3-.9-.4-1.2-.4-.6 0-1.1.3-1.4.8-.6.8-.5 2 .4 2.7l13.2 10c.5.3.9.4 1.3.4.5-.1 1-.4 1.3-.8zM294.4 176.9c.1-.5-.1-1-.4-1.4-.3-.4-.8-.7-1.3-.7l-16.4-2h-.3c-.9 0-1.6.8-1.7 1.7-.1.5.1 1 .4 1.4.3.4.8.7 1.3.7l16.4 2h.3c.8-.1 1.6-.8 1.7-1.7zM287.5 133.2c.5-.2.8-.6 1-1 .2-.5.2-1 0-1.5-.3-.7-1.1-1.2-1.9-1.2-.2 0-.4.1-.6.2l-15.3 6.5c-.5.2-.8.6-1 1-.2.5-.2 1 0 1.5.3.7 1.1 1.2 1.9 1.2.2 0 .4-.1.6-.1l15.3-6.6z" fill="#222720"></path><path d="M238.1 207c0-21-17.1-38.2-38.2-38.2-3 0-5.9.4-8.9 1.1l-2 .5-.7-2c-6-18-22.9-30.1-41.9-30.1-10.8 0-21.2 4-29.3 11.3-8.1 7.2-13.3 17-14.5 27.6l-.3 2.1-2.1-.1c-.8-.1-1.6-.1-2.3-.1-18.2 0-33 14.8-33 33 0 14.4 9.6 27.4 23.4 31.5 2.9.9 5.8 1.4 8.8 1.4h104.6c3.2 0 6.5-.6 9.5-1.7h.2c16-5 26.7-19.6 26.7-36.3zm-28 32.7c-2.7 1-5.6 1.5-8.4 1.5H97.1c-2.6 0-5.1-.4-7.6-1.3-12.2-3.7-20.7-15.2-20.7-27.9 0-16.1 13.1-29.1 29.2-29.1 2 0 4 .2 5.9.6l2.3.5v-2.3c.4-21.8 18.5-39.6 40.4-39.6 18.8 0 35 12.8 39.3 31.1l.5 2.1 2-.7c3.8-1.4 7.7-2.1 11.6-2.1 18.9 0 34.3 15.4 34.3 34.3 0 15.2-9.8 28.4-24.2 32.9z" fill="#0091B3"></path></symbol><symbol id="PhilosophyClass" viewbox="0 0 100 100"><path d="M60.8 2.3h-9.1c-1.3 0-2.4 1.1-2.4 2.4v48.4H42.6c-12.7 0-23-10.3-23-23 0-8.8 5.2-17 13.1-20.8 1.2-.6 1.7-2 1.1-3.2-.4-.8-1.3-1.4-2.2-1.4-.4 0-.7.1-1 .2C21 9.6 14.8 19.5 14.8 30.1 14.8 45.5 27.3 58 42.6 58H49.3V95.3c0 1.3 1.1 2.4 2.4 2.4 1.3 0 2.4-1.1 2.4-2.4V58H60.8c15.3 0 27.8-12.5 27.8-27.8 0-15.4-12.5-27.9-27.8-27.9zm0 50.9H54.1V7.1H60.8c12.7 0 23 10.3 23 23s-10.3 23.1-23 23.1z" fill="#333"></path></symbol><symbol id="PlaningForecasting" viewbox="0 0 350 350"><path d="M247.7 174.9c0 40.2-32.6 72.7-72.7 72.7s-72.7-28.5-72.7-72.7c0-40.2 32.6-72.7 72.7-72.7s72.7 32.5 72.7 72.7z" fill="none" stroke="#222720" stroke-miterlimit="10" stroke-width="3.453"></path><path d="M175 176.4v-56M174.3 178.1l-22.5 22.6" fill="none" stroke="#99999A" stroke-linecap="square" stroke-miterlimit="10" stroke-width="3.453"></path><circle cx="174.3" cy="111.6" fill="#0091B3" r="3"></circle><circle cx="174.3" cy="238" fill="#0091B3" r="3"></circle><circle cx="111.1" cy="174.8" fill="#0091B3" r="3"></circle><circle cx="237.5" cy="174.8" fill="#0091B3" r="3"></circle></symbol><symbol id="SpeakerSeries" viewbox="0 0 100 100"><path d="M64.4 97H35.6c-1.1 0-1.9-.9-1.9-1.9s.9-1.9 1.9-1.9h28.9c1.1 0 1.9.9 1.9 1.9s-.9 1.9-2 1.9z" fill="#333"></path><path d="M50 97c-1.1 0-1.9-.9-1.9-1.9V73.2c0-1.1.9-1.9 1.9-1.9s1.9.9 1.9 1.9v21.9c0 1-.8 1.9-1.9 1.9z" fill="#333"></path><path d="M50 75.1c-10.9 0-19.8-8.9-19.8-19.8v-8c0-1.1.9-1.9 1.9-1.9s1.9.9 1.9 1.9v8c0 8.8 7.1 15.9 15.9 15.9s15.9-7.1 15.9-15.9v-8c0-1.1.9-1.9 1.9-1.9s1.9.9 1.9 1.9v8c.2 10.9-8.7 19.8-19.6 19.8z" fill="#333"></path><path d="M50 6.8c5.9 0 10.6 4.8 10.6 10.6v37C60.6 60.3 55.9 65 50 65c-5.9 0-10.6-4.8-10.6-10.6v-37c0-5.8 4.7-10.6 10.6-10.6M50 3c-8 0-14.4 6.5-14.4 14.4v37c0 8 6.5 14.4 14.4 14.4 8 0 14.4-6.5 14.4-14.4v-37C64.4 9.5 58 3 50 3z" fill="#333"></path></symbol><symbol id="SupplyChainOptimization" viewbox="0 0 350 350"><path d="M34.4 111.5h32.3v32.3H34.4z" fill="none" stroke="#5D5D5D" stroke-miterlimit="10" stroke-width="3"></path><path d="M119.7 111.5H152v32.3h-32.3z" fill="none" stroke="#99999A" stroke-miterlimit="10" stroke-width="3"></path><path d="M207.9 194h32.3v32.3h-32.3z" fill="none" stroke="#5D5D5D" stroke-miterlimit="10" stroke-width="3"></path><path d="M225.8 143.8h-3.5c-7.9 0-14.4-6.4-14.4-14.4v-3.5c0-7.9 6.4-14.4 14.4-14.4h3.5c7.9 0 14.4 6.4 14.4 14.4v3.5c-.1 8-6.5 14.4-14.4 14.4zM308.5 226.3H305c-7.9 0-14.4-6.4-14.4-14.4v-3.5c0-7.9 6.4-14.4 14.4-14.4h3.5c7.9 0 14.4 6.4 14.4 14.4v3.5c0 7.9-6.4 14.4-14.4 14.4z" fill="none" stroke="#0091B3" stroke-miterlimit="10" stroke-width="3"></path><path d="M79.2 127.7h29.5" fill="none" stroke="#222720" stroke-miterlimit="10" stroke-width="3"></path><path d="M102.7 135l-1.2-1.3 6.5-6-6.5-6.1 1.2-1.3 7.9 7.4z" fill="#222720"></path><path d="M164.1 127.7h29.4" fill="none" stroke="#222720" stroke-miterlimit="10" stroke-width="3"></path><path d="M187.6 135l-1.2-1.3 6.5-6-6.5-6.1 1.2-1.3 7.9 7.4z" fill="#222720"></path><g><path d="M248.3 210.1h29.4" fill="none" stroke="#222720" stroke-miterlimit="10" stroke-width="3"></path><path d="M271.8 217.5l-1.3-1.4 6.5-6-6.5-6 1.3-1.4 7.9 7.4z" fill="#222720"></path></g><g><path d="M224 152.4v29.5" fill="none" stroke="#222720" stroke-miterlimit="10" stroke-width="3"></path><path d="M216.6 175.9l1.4-1.2 6 6.5 6-6.5 1.4 1.2-7.4 8z" fill="#222720"></path></g></symbol><symbol id="WinterParty" viewbox="0 0 100 100"><path d="M83.8 51.7l9 9c.4.4.9.6 1.4.6s1-.2 1.4-.6c.4-.4.6-.9.6-1.4 0-.5-.2-1-.6-1.4l-7.8-7.8-.7-.7.7-.7 7.7-7.7c.4-.4.6-.9.6-1.4s-.2-1-.6-1.4c-.4-.4-.9-.6-1.4-.6s-1 .2-1.4.6l-9 9-.3.3H66.6l-.1-.8c-.4-2.4-1.3-4.6-2.7-6.6l-.5-.7.6-.6L75 27.7l.3-.3H88.5c1.1 0 2-.9 2-2s-.9-2-2-2h-12V11.5c0-1.1-.9-2-2-2s-2 .9-2 2v13.1l-.3.3L61 36l-.6.6-.7-.5c-2-1.4-4.2-2.3-6.6-2.7l-.8-.1v-17l.3-.3 9-9c.4-.4.6-.9.6-1.4s-.2-1-.6-1.4c-.4-.4-.9-.6-1.4-.6s-1 .2-1.4.6L51 12l-.7.7-.7-.7-7.7-7.7c-.4-.4-.9-.6-1.4-.6-.5 0-1 .2-1.4.6-.4.4-.6.9-.6 1.4s.2 1 .6 1.4l9 9 .3.3v16.9l-.8.1c-2.4.4-4.6 1.4-6.5 2.7l-.7.5-.6-.6-11.2-11-.3-.3V11.5c0-1.1-.9-2-2-2s-2 .9-2 2v12H12.4c-1.1 0-2 .9-2 2s.9 2 2 2h13.1l.3.3L37 39l.6.6-.5.7c-1.3 1.9-2.2 4.1-2.7 6.5l-.1.8H17.2l-.3-.3-9-9c-.4-.4-.9-.6-1.4-.6s-1 .2-1.4.6c-.4.4-.6.9-.6 1.4s.2 1 .6 1.4l7.7 7.7.7.7-.7.7L5.1 58c-.4.4-.6.9-.6 1.4 0 .5.2 1 .6 1.4.4.4.9.6 1.4.6.5 0 1-.2 1.4-.6l9-9 .3-.3h17l.1.8c.4 2.4 1.3 4.6 2.7 6.6l.5.7-.5.5-11.2 11.2-.3.3H12.3c-1.1 0-2 .9-2 2s.9 2 2 2h12v11.9c0 1.1.9 2 2 2s2-.9 2-2V74.4l.3-.3 11.2-11.2.6-.6.7.5c2 1.4 4.1 2.3 6.5 2.7l.8.1v17l-.3.4-9 9c-.8.8-.8 2 0 2.8.4.4.9.6 1.4.6.5 0 1-.2 1.4-.6l7.8-7.8.7-.7.7.7 7.7 7.7c.4.4.9.6 1.4.6s1-.2 1.4-.6c.4-.4.6-.9.6-1.4s-.2-1-.6-1.4l-9-9-.3-.3v-17l.8-.1c2.4-.4 4.6-1.3 6.5-2.7l.7-.5.6.6L72.2 74l.3.3V87.5c0 1.1.9 2 2 2s2-.9 2-2v-12h11.9c1.1 0 2-.9 2-2s-.9-2-2-2H75.3l-.3-.3-11.2-11.1-.6-.6.5-.7c1.4-2 2.3-4.2 2.7-6.5l.1-.8h16.9l.4.2zm-45.3-5.5c1.1-4.1 4.4-7.4 8.5-8.6l1.3-.4V47.4H38.1l.4-1.2zm9.9 6.2V61.6l-1.3-.3c-4.2-1.1-7.5-4.4-8.6-8.6l-.3-1.3H48.4v1zm3.9-7.1v-8l1.3.3c4.2 1.1 7.6 4.4 8.7 8.7l.3 1.3H52.4v-1.7c0-.3 0-.4-.1-.6zm10 7.4c-1.1 4.2-4.4 7.5-8.6 8.6l-1.3.3V51.4H62.6l-.3 1.3z" fill="#333"></path></symbol><symbol id="arrow-down" viewbox="0 0 40.8 22.4"><defs><path d="M0 0h40.8v22.4H0z" id="pa"></path></defs><clippath id="pb"><use overflow="visible" xlink:href="#pa"></use></clippath><path clip-path="url(#pb)" d="M1.4 1.5l19 18.1L39.5 1.5" fill="none" stroke="#FF6B00" stroke-width="4.029"></path></symbol><symbol id="arrow-top" viewbox="0 0 26.4 20"><path d="M13.2 0L0 13.2V20L13.2 6.7 26.4 20v-6.9z" fill="currentColor"></path></symbol><symbol id="icon_email" viewbox="0 0 30 30"><style>.remail-icon{fill:currentColor}</style><path class="remail-icon" d="M26.5 7.8L15 16.4 3.5 7.8c0-.4.1-.8.4-1 .3-.3.7-.4 1-.4h20.2c.4 0 .8.1 1 .4.3.2.4.6.4 1zm-23 2.6L15 19.1l11.5-8.7v11.8c0 .4-.1.8-.4 1-.3.3-.7.4-1 .4H4.9c-.4 0-.8-.1-1-.4-.3-.3-.4-.7-.4-1V10.4z"></path></symbol><symbol id="icon_instagram" viewbox="0 0 30 30"><style>.sinstagram-icon{fill:currentColor}</style><path class="sinstagram-icon" d="M25.6 7.4V11h-6.5c-1.1-1.2-2.5-1.8-4.2-1.8s-3 .6-4.2 1.8H4.3V7.4c0-.8.3-1.6.9-2.2s1.3-.9 2.2-.9h15.1c.8 0 1.6.3 2.2.9.6.6.9 1.4.9 2.2zm-5.3 5.4h5.4v9.7c0 .8-.3 1.6-.9 2.2s-1.3.9-2.2.9H7.4c-.8 0-1.6-.3-2.2-.9s-.9-1.3-.9-2.2v-9.7h5.4c-.3.7-.4 1.4-.4 2.2 0 1.6.6 2.9 1.7 4.1 1.1 1.1 2.5 1.7 4.1 1.7s2.9-.6 4.1-1.7c1.1-1.1 1.7-2.5 1.7-4.1-.2-.8-.3-1.5-.6-2.2zM14.9 19c-1.1 0-2-.4-2.8-1.1-.8-.8-1.1-1.7-1.1-2.8s.4-2 1.2-2.8c.8-.8 1.7-1.2 2.8-1.2s2 .4 2.8 1.2S19 14 19 15.1s-.4 2-1.2 2.8c-.8.7-1.7 1.1-2.9 1.1z"></path></symbol><symbol id="icon_linkedin" viewbox="0 0 30 30"><style>.tlinkedin-icon{fill:currentColor}</style><path class="tlinkedin-icon" d="M6.4 8c-.8 0-1.5-.2-2-.8-.6-.4-.8-1.1-.8-1.8s.2-1.4.8-1.9c.5-.5 1.2-.7 2-.7s1.5.2 2.1.7.8 1.1.8 1.8-.3 1.5-.8 1.9c-.6.6-1.2.8-2.1.8zM4 10.4h4.8v14.8H4V10.4zm12.4 14.7v-8.6c0-.9.2-1.6.8-2.1.5-.5 1.1-.8 1.8-.8s1.4.3 1.8.9c.4.5.8 1.4.8 2.5v8.1h4.8v-8.7c0-2.1-.5-3.7-1.5-4.9-1.1-1.2-2.4-1.7-4.1-1.7-1.7 0-3.1.9-4.2 2.5l-.1-2.1h-4.7l.1 3.4V25h4.5z"></path></symbol><symbol id="icon_twitter" viewbox="0 0 30 30"><style>.utwitter-icon{fill:currentColor}</style><path class="utwitter-icon" d="M27 7.5c-.7 1-1.5 1.8-2.4 2.5v.7c0 1.4-.2 2.6-.6 4-.3 1.4-.9 2.6-1.7 3.8s-1.7 2.3-2.9 3.2c-1.1.9-2.4 1.7-3.9 2.2-1.6.7-3.2.9-5 .9-3 0-5.5-.7-7.6-2.1.3 0 .8.1 1.1.1 2.2 0 4.2-.8 6.2-2.3-1 0-2.1-.3-2.9-1-.7-.7-1.3-1.5-1.6-2.4.3 0 .6.1.9.1.5 0 .9 0 1.3-.1-1.1-.2-2.1-.8-2.9-1.7s-1.1-2-1.1-3.2c.7.3 1.5.6 2.2.6-1.5-1-2.2-2.4-2.2-4.1 0-.8.2-1.6.7-2.4C5.8 7.7 7.3 9 9 9.8c1.7.9 3.7 1.4 5.7 1.5-.1-.3-.1-.7-.1-1.1 0-1.4.5-2.5 1.5-3.4.9-.9 2.2-1.5 3.6-1.5s2.6.6 3.7 1.6c1.1-.2 2.2-.6 3.1-1.1-.3 1.1-1.1 2.1-2.2 2.8.9-.4 1.8-.7 2.7-1.1z"></path></symbol><symbol id="logo" viewbox="0 0 327.9 40.3"><style>.vlogo{fill:currentColor}</style><path class="vlogo" d="M97.4.5c-1-.2-2.6-.3-3.8-.3H58v40.1h10.8V29.1h24.9c1.7 0 3.3-.2 4.4-.4 7.1-1.2 10.9-6 10.9-14.1-.1-8.1-4.1-13.1-11.6-14.1zm1.1 14.6c0 3.2-1.6 4.8-4.5 4.8H68.8V9.7H94c2.9.1 4.5 1.6 4.5 4.8v.6zM327.9 40.3h-42.8V.2h42.8v9.3h-33v6.4h33v8.8h-33V31h33zM133.9 40.3h10.8V9.7h18.6V.2h-48.1v9.5h18.7zM15.3 40.3h18.5c9.9-.1 15.1-5.3 15.2-15.2V.2H38.6v24.9c0 3.6-2.1 5.5-5.7 5.7H16.1c-3.7-.2-5.6-2-5.7-5.7V.2H0v24.9C.2 35 5.3 40.2 15.3 40.3zM278.1 40.3h-13.6l-15.9-15.9-15.9 15.9h-6.6V0h9.7v23.7L259.2.2h13.7l-17.5 17.4zM215.7 26.1L190.2.5l-.3-.3-.3.3L164 26.1l-.1.1V40.3l.8-.8 25.2-25.2 25.2 25.2.8.8V26.2l-.2-.1z"></path></symbol><symbol id="playround" viewbox="0 0 42 42"><style>.wst0{fill:currentColor}.wst1{clip-path:url(#wSVGID_2_);fill:none;stroke:currentColor;stroke-width:2}</style><path class="wst0" d="M17 12.6v17.9l11.8-8.9z"></path><defs><path d="M0 0h42v42H0z" id="wSVGID_1_"></path></defs><clippath id="wSVGID_2_"><use overflow="visible" xlink:href="#wSVGID_1_"></use></clippath><circle class="wst1" cx="21" cy="21" r="20"></circle></symbol></svg> </div>
    <!--[if lt IE 9]>
          <div class="alert alert-warning">
            You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.      </div>
        <![endif]-->
    <header class="l-site-header" id="top" role="banner">
    <div class="l-wrap l-wrap--full">
    <a class="l-site-header__logo" href="/">
    <svg class="icon icon--logo">
    <use xlink:href="#logo"></use>
    </svg>
    </a>
    <div class="l-site-header__menu">
    <div class="primary-nav"><ul class="primary-nav__menu" id="menu-primary-nav"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4164" id="menu-item-4164"><a href="http://uptake.com/approach/">Approach</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4163" id="menu-item-4163"><a href="http://uptake.com/platform/">Platform</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4172" id="menu-item-4172"><a href="http://uptake.com/solutions/">Solutions</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4162" id="menu-item-4162"><a href="http://uptake.com/people/">People</a></li>
    <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4167" id="menu-item-4167"><a href="https://careers-uptake.icims.com/jobs/search?hashed=-435709820&amp;mobile=false&amp;width=949&amp;height=500&amp;bga=true&amp;needsRedirect=false&amp;jan1offset=-360&amp;jun1offset=-300">Join Us</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4166" id="menu-item-4166"><a href="http://uptake.com/ourblog/">Blog</a></li>
    </ul></div> </div>
    <div class="l-site-header__hamburger">
    <a class="hamburger js-hamburger" href="#">
    <span class="hamburger__top"></span>
    <span class="hamburger__middle"></span>
    <span class="hamburger__bottom"></span>
    </a>
    </div>
    </div>
    </header>
    <div class="l-site-header__mobile-menu">
    <div class="primary-nav primary-nav--mobile"><ul class="primary-nav__menu" id="menu-primary-nav-1"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4164"><a href="http://uptake.com/approach/">Approach</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4163"><a href="http://uptake.com/platform/">Platform</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4172"><a href="http://uptake.com/solutions/">Solutions</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4162"><a href="http://uptake.com/people/">People</a></li>
    <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-4167"><a href="https://careers-uptake.icims.com/jobs/search?hashed=-435709820&amp;mobile=false&amp;width=949&amp;height=500&amp;bga=true&amp;needsRedirect=false&amp;jan1offset=-360&amp;jun1offset=-300">Join Us</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4166"><a href="http://uptake.com/ourblog/">Blog</a></li>
    </ul></div></div>
    <div class="header__contact">
    <div class="header__contact__container">
    <a class="header__contact__close js___email_close" href="javascript:;">Close</a>
    <h2>Curious to learn how Uptake can impact your company? Contact us below.</h2>
    <div class="wpcf7" dir="ltr" id="wpcf7-f4168-o1" lang="en-US" role="form">
    <div class="screen-reader-response"></div>
    <form action="/#wpcf7-f4168-o1" class="wpcf7-form" method="post" novalidate="novalidate">
    <div style="display: none;">
    <input name="_wpcf7" type="hidden" value="4168"/>
    <input name="_wpcf7_version" type="hidden" value="4.3"/>
    <input name="_wpcf7_locale" type="hidden" value="en_US"/>
    <input name="_wpcf7_unit_tag" type="hidden" value="wpcf7-f4168-o1"/>
    <input name="_wpnonce" type="hidden" value="529156be07"/>
    </div>
    <p><span class="wpcf7-form-control-wrap name"><input aria-invalid="false" aria-required="true" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required" name="name" size="40" type="text" value=""/></span>Name</p>
    <p><span class="wpcf7-form-control-wrap company"><input aria-invalid="false" aria-required="true" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required" name="company" size="40" type="text" value=""/></span>Company</p>
    <p><span class="wpcf7-form-control-wrap email"><input aria-invalid="false" aria-required="true" class="wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email" name="email" size="40" type="email" value=""/></span>Email</p>
    <p><span class="wpcf7-form-control-wrap phone"><input aria-invalid="false" class="wpcf7-form-control wpcf7-text" name="phone" size="40" type="text" value=""/></span>Phone</p>
    <p><span class="wpcf7-form-control-wrap message"><textarea aria-invalid="false" class="wpcf7-form-control wpcf7-textarea" cols="40" name="message" rows="10"></textarea></span>Message</p>
    <p><input class="wpcf7-form-control wpcf7-submit" type="submit" value="Send"/></p>
    <div class="wpcf7-response-output wpcf7-display-none"></div></form></div> </div>
    </div>
    <div class="wrap container" role="document">
    <div class="content row">
    <main class="main" role="main">
    <div class="splash">
    <div class="splash__fade"></div>
    <div class="splash__video" data-mp4-src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/2015/10/uptake-particle-cloud-demo.mp4" data-ogv-src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/2015/10/uptake-particle-cloud-demo.mp4" data-webm-src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/2015/10/uptake-particle-cloud-demo.mp4" id="splashVideo" style="background-image: url(http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/uploads/2015/10/video-still.png);">
    </div>
    </div>
    <div class="l-section l-section--hero">
    <div class="l-section__content">
    <div class="l-wrap l-wrap--wide">
    <h1 class="hero-title hero-title--inline js-hero-title">Our platform <span class="js-typed"></span></h1>
    </div>
    </div>
    <a class="l-section__next is-active" href="#callout">
    <svg class="icon icon--next">
    <use xlink:href="#arrow-down"></use>
    </svg>
    </a>
    </div>
    <div class="callout callout--carat" id="callout">
    <div class="l-wrap">
    <div class="callout__carat">
    <svg class="icon icon--carat">
    <use xlink:href="#arrow-top"></use>
    </svg>
    </div>
    <div class="callout__copy">
    <p>We help companies understand and act on their data. Uptake is building the singular platform that defines data-driven insight in major global industries.  We unlock answers, and our answers create value.</p>
    </div>
    </div>
    </div>
    <section class="l-section l-section--home l-section--vcenter" id="data">
    <div class="l-section__content">
    <div class="l-wrap">
    <div class="l-feature">
    <div class="l-feature__sub">
    <div class="svg-animation">
    <div class="svg-animation__content">
    <div class="valuable-asset-animation js-valuable-asset-animation">
    <div class="valuable-asset-animation__node-set js-node-set">
    <span class="valuable-asset-animation__node is-squared js-node-1"></span>
    <span class="valuable-asset-animation__node js-node-2"></span>
    <span class="valuable-asset-animation__node js-node-3"></span>
    <span class="valuable-asset-animation__node is-squared js-node-4"></span>
    <span class="valuable-asset-animation__node js-node-5"></span>
    <span class="valuable-asset-animation__node js-node-6"></span>
    <span class="valuable-asset-animation__node is-squared js-node-7"></span>
    <span class="valuable-asset-animation__node js-node-8"></span>
    <span class="valuable-asset-animation__node js-node-9"></span>
    </div>
    <div class="valuable-asset-animation__end-node-set js-end-node-set">
    <span class="valuable-asset-animation__node is-squared"></span>
    <span class="valuable-asset-animation__node"></span>
    <span class="valuable-asset-animation__node"></span>
    <span class="valuable-asset-animation__node is-squared"></span>
    <span class="valuable-asset-animation__node"></span>
    <span class="valuable-asset-animation__node"></span>
    <span class="valuable-asset-animation__node is-squared"></span>
    <span class="valuable-asset-animation__node"></span>
    <span class="valuable-asset-animation__node"></span>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="l-feature__main">
    <h2 class="block-title">Data is a valuable asset.</h2>
    <p class="lead">More than 99% of operational data collected from modern equipment goes to waste. We harness, normalize and store real-time data from machines, operations and third party sources to build a comprehensive big picture.</p>
    <p><a class="text-btn" href="/approach">Learn more about our approach <span class="arrow">âº</span></a></p>
    </div>
    </div>
    </div>
    </div>
    </section>
    <section class="l-section l-section--home l-section--vcenter" id="answers">
    <div class="l-section__content">
    <div class="l-wrap">
    <div class="l-feature l-feature--flipped">
    <div class="l-feature__sub">
    <div class="svg-animation">
    <div class="svg-animation__content">
    <div class="insights js-insights-from-connections-animation">
    <div class="insights__node-set">
    <div class="insights__node-set-inner-top js-node-set-inner-top">
    <span class="insights__node js-node"></span>
    <span class="insights__node js-node"></span>
    <span class="insights__node js-node"></span>
    <span class="insights__node js-node"></span>
    <span class="insights__node js-node"></span>
    </div>
    <div class="insights__node-set-inner-center js-node-set-inner-center">
    <span class="insights__node js-node js-node-1 js-side-node"></span>
    <span class="insights__node js-node js-node-2"></span>
    <span class="insights__node js-node js-node-3"></span>
    <span class="insights__node js-node js-node-4"></span>
    <span class="insights__node js-node js-node-5 js-side-node"></span>
    <span class="insights__node js-node js-node-6"></span>
    <span class="insights__node js-node js-node-7"></span>
    <span class="insights__node js-node js-node-8"></span>
    <span class="insights__node js-node js-node-9"></span>
    </div>
    <div class="insights__node-set-inner-center-outro js-node-set-inner-center-outro">
    <span class="insights__node js-node js-node-1 js-side-node"></span>
    <span class="insights__node js-node js-node-2"></span>
    <span class="insights__node js-node js-node-3"></span>
    <span class="insights__node js-node js-node-4"></span>
    <span class="insights__node js-node js-node-5 js-side-node"></span>
    <span class="insights__node js-node js-node-6"></span>
    <span class="insights__node js-node js-node-7"></span>
    <span class="insights__node js-node js-node-8"></span>
    <span class="insights__node js-node js-node-9"></span>
    </div>
    <div class="insights__node-set-inner-bottom js-node-set-inner-bottom">
    <span class="insights__node js-node"></span>
    <span class="insights__node js-node"></span>
    <span class="insights__node js-node"></span>
    <span class="insights__node js-node"></span>
    <span class="insights__node js-node"></span>
    </div>
    </div>
    <img alt="" class="insights__alert js-alert" src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/dist/images/insights-from-connections-animation/alert.svg"/>
    <img alt="" class="insights__hex-spokes js-hex-spokes" src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/dist/images/insights-from-connections-animation/hex-spokes.svg"/>
    <img alt="" class="insights__hex-outline js-hex-outline" src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/dist/images/insights-from-connections-animation/hex-outline.svg"/>
    </div>
    </div>
    </div>
    </div>
    <div class="l-feature__main">
    <h2 class="block-title">We transform data into insights.</h2>
    <p class="lead">Having data doesnât equal capturing its value. Our platform goes beyond descriptive analytics and delivers predictive recommendations.</p>
    <p><a class="text-btn" href="/platform">Learn more about our platform <span class="arrow">âº</span></a></p>
    </div>
    </div>
    </div>
    </div>
    </section>
    <section class="l-section l-section--home l-section--vcenter" id="actions">
    <div class="l-section__content">
    <div class="l-wrap">
    <div class="l-feature">
    <div class="l-feature__sub">
    <div class="svg-animation">
    <div class="svg-animation__content">
    <div class="workflow-integration-animation js-workflow-integration-animation">
    <img alt="" class="workflow-integration-animation__alert js-alert" src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/dist/images/workflow-integration-animation/alert.svg"/>
    <img alt="" class="workflow-integration-animation__phone js-phone" src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/dist/images/workflow-integration-animation/phone.svg"/>
    <img alt="" class="workflow-integration-animation__check js-check" src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/dist/images/workflow-integration-animation/check.svg"/>
    <span class="workflow-integration-animation__button js-button"></span>
    </div>
    </div>
    </div>
    </div>
    <div class="l-feature__main">
    <h2 class="block-title">We enable companies to take action.</h2>
    <p class="lead">Our solutions integrate into existing workflows so the right person can take action at the right time. Through actionable insights, our platform helps companies avoid failures within operations, work more efficiently, and discover new value.  </p>
    <p><a class="text-btn" href="/solutions">Learn more about our solutions <span class="arrow">âº</span></a></p>
    </div>
    </div>
    </div>
    </div>
    </section>
    </main><!-- /.main -->
    </div><!-- /.content -->
    </div><!-- /.wrap -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.js"></script>
    <footer class="footer">
    <div class="l-wrap l-wrap--full">
    <div class="footer__top">
    <a class="footer__arrow" href="/">
    <svg class="icon icon--top">
    <use xlink:href="#arrow-top"></use>
    </svg>
    </a>
    <div class="footer__menu">
    <ul>
    <li><a href="/approach">Approach</a></li>
    <li><a href="/platform">Platform</a></li>
    <li><a href="/people">People</a></li>
    </ul>
    <ul>
    <li><a class="footer__menu--external" href="https://careers-uptake.icims.com/jobs/search?hashed=-435709820&amp;mobile=false&amp;width=949&amp;height=500&amp;bga=true&amp;needsRedirect=false&amp;jan1offset=-360&amp;jun1offset=-300" target="_blank">Open Positions</a></li>
    <li><a class="" href="/ourblog">Blog</a></li>
    </ul>
    </div>
    </div>
    <div class="footer__social">
    <ul class="social-links">
    <li>
    <a href="https://twitter.com/uptake" rel="nofollow" target="_blank">
    <svg class="icon icon--social">
    <use xlink:href="#icon_twitter"></use>
    </svg>
    </a>
    </li>
    <li>
    <a href="https://instagram.com/uptakechicago" target="_blank">
    <svg class="icon icon--social">
    <use xlink:href="#icon_instagram"></use>
    </svg>
    </a>
    </li>
    <li>
    <a href="https://www.linkedin.com/company/3845987" target="_blank">
    <svg class="icon icon--social">
    <use xlink:href="#icon_linkedin"></use>
    </svg>
    </a>
    </li>
    <li>
    <a class="js___email_open" href="mailto:info@uptake.com" target="_blank">
    <svg class="icon icon--social">
    <use xlink:href="#icon_email"></use>
    </svg>
    </a>
    </li>
    </ul>
    <div class="media-inquiry">
    <p>Media Inquiries: 
            <a href="mailto:natalie.bauer@uptake.com">Natalie Bauer Luce</a><br/>
            or 312.626.2701</p>
    </div>
    </div>
    <div class="footer__copyright">
          Â© Uptake. All Rights Reserved. 2015
        </div>
    </div>
    </footer>
    <script type="text/javascript">
    /* <![CDATA[ */
    var alm_localize = {"ajaxurl":"http:\/\/uptake.com\/wp-admin\/admin-ajax.php","alm_nonce":"ab522b93f3","pluginurl":"http:\/\/uptake.com\/wp-content\/plugins\/ajax-load-more","scrolltop":"false"};
    /* ]]> */
    </script>
    <script src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/plugins/ajax-load-more/core/js/ajax-load-more.min.js?ver=1.1" type="text/javascript"></script>
    <script src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/plugins/contact-form-7/includes/js/jquery.form.min.js?ver=3.51.0-2014.06.20" type="text/javascript"></script>
    <script type="text/javascript">
    /* <![CDATA[ */
    var _wpcf7 = {"loaderUrl":"http:\/\/uptake.com\/wp-content\/plugins\/contact-form-7\/images\/ajax-loader.gif","sending":"Sending ...","cached":"1"};
    /* ]]> */
    </script>
    <script src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/plugins/contact-form-7/includes/js/scripts.js?ver=4.3" type="text/javascript"></script>
    <script type="text/javascript">
    /* <![CDATA[ */
    var ajaxpagination = {"ajaxurl":"http:\/\/uptake.com\/wp-admin\/admin-ajax.php"};
    /* ]]> */
    </script>
    <script src="http://2mv7ax322je72lpvht2l5f0f.wpengine.netdna-cdn.com/wp-content/themes/uptake/dist/scripts/bundle.js" type="text/javascript"></script>
    </body>
    </html>
    >
    


```

```


```
links = soup.find_all("a")
hrefs = []
for link in links:
    if "http" in link.get('href'):
        print(link.get('href'))
        hrefs.append(link.get('href'))
```

    http://uptake.com/approach/
    http://uptake.com/platform/
    http://uptake.com/solutions/
    http://uptake.com/people/
    https://careers-uptake.icims.com/jobs/search?hashed=-435709820&mobile=false&width=949&height=500&bga=true&needsRedirect=false&jan1offset=-360&jun1offset=-300
    http://uptake.com/ourblog/
    http://uptake.com/approach/
    http://uptake.com/platform/
    http://uptake.com/solutions/
    http://uptake.com/people/
    https://careers-uptake.icims.com/jobs/search?hashed=-435709820&mobile=false&width=949&height=500&bga=true&needsRedirect=false&jan1offset=-360&jun1offset=-300
    http://uptake.com/ourblog/
    https://careers-uptake.icims.com/jobs/search?hashed=-435709820&mobile=false&width=949&height=500&bga=true&needsRedirect=false&jan1offset=-360&jun1offset=-300
    https://twitter.com/uptake
    https://instagram.com/uptakechicago
    https://www.linkedin.com/company/3845987
    


```
l1 = hrefs[0:3]
l2 = [hrefs[5]]
l = l1+l2
print(l)
```

    ['http://uptake.com/approach/', 'http://uptake.com/platform/', 'http://uptake.com/solutions/', 'http://uptake.com/ourblog/']
    


```

```


```
html1 = requests.get((l[0]), headers={'User-Agent': 'Mozilla/5.0'})
s1 = BeautifulSoup(html1.content,"lxml")
for sc1 in s1(["script", "style"]):
    sc1.extract()
text1 = s1.get_text()
list1 = text1.split(',')
#print(text1)
html2 = requests.get((l[1]), headers={'User-Agent': 'Mozilla/5.0'})
s2 = BeautifulSoup(html2.content,"lxml")
for sc2 in s2(["script", "style"]):
    sc2.extract()
text2 = s2.get_text()
list2 = text2.split(',')
#print(text2)
html3 = requests.get((l[2]), headers={'User-Agent': 'Mozilla/5.0'})
s3 = BeautifulSoup(html3.content,"lxml")
for sc3 in s3(["script", "style"]):
    sc3.extract()
text3 = s3.get_text()
list3 = text3.split(',')
#print(text3)
html4 = requests.get((l[3]), headers={'User-Agent': 'Mozilla/5.0'})
s4 = BeautifulSoup(html4.content,"lxml")
for sc4 in s4(["script", "style"]):
    sc4.extract()
text4 = s4.get_text()
#print(text4)
list4 = text4.split(',')
#print(list4)
```


```
lists = list1+list2+list3+list4
lists =' '.join(lists)
wordlist = re.sub("[^a-zA-Z]", " ", lists) #removing non-letters 
```


```
###########
## sentiment polarity check
###########
from textblob import TextBlob
# get text
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in wordlist.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
#print(text)
text = text.lower()
wiki = TextBlob(text)
r = wiki.sentiment
print(r)
#print(wiki)
#The polarity score is a float within the range [-1.0, 1.0]. 
#The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
#TextBlob uses a classifier to predict the polarity of a sentence. By default it uses the Movie-Review data set. 

#Sentiment(polarity=0.2294366777013836, subjectivity=0.4917028690263986) which shows the subjectivity is neutral infact, on 
#uptake webpage. Polarity is positive (which was expected.) 
```

    Sentiment(polarity=0.2294366777013836, subjectivity=0.4917028690263986)
    


```
#tokenization
wiki.words


```




    WordList(['approach', 'uptake', 'approach', 'platform', 'solutions', 'people', 'join', 'us', 'blog', 'approach', 'platform', 'solutions', 'people', 'join', 'us', 'blog', 'close', 'curious', 'to', 'learn', 'how', 'uptake', 'can', 'impact', 'your', 'company', 'contact', 'us', 'below', 'name', 'company', 'email', 'phone', 'message', 'how', 'we', 'build', 'our', 'products', 'is', 'just', 'as', 'important', 'as', 'what', 'we', 'build', 'five', 'key', 'differentiators', 'define', 'our', 'approach', 'partnerships', 'with', 'industry', 'leaders', 'we', 'work', 'with', 'iconic', 'companies', 'to', 'tackle', 'hard', 'problems', 'combining', 'our', 'proprietary', 'technology', 'with', 'their', 'industry', 'leading', 'knowledge', 'and', 'wealth', 'of', 'data', 'our', 'partners', 'give', 'us', 'direct', 'access', 'to', 'deep', 'rich', 'data', 'collected', 'from', 'sensored', 'equipment', 'and', 'machines', 'throughout', 'operations', 'on', 'the', 'ground', 'research', 'we', 'work', 'from', 'the', 'ground', 'up', 'starting', 'in', 'the', 'field', 'whether', 'that', 's', 'a', 'rail', 'yard', 'a', 'triage', 'unit', 'or', 'a', 'power', 'plant', 'to', 'understand', 'real', 'world', 'constraints', 'and', 'context', 'of', 'use', 'we', 'see', 'firsthand', 'the', 'problems', 'our', 'partners', 'are', 'trying', 'to', 'solve', 'and', 'ones', 'they', 've', 'yet', 'to', 'identify', 'a', 'platform', 'approach', 'unbound', 'by', 'the', 'structure', 'of', 'one', 'specific', 'industry', 'we', 'look', 'at', 'data', 'across', 'seemingly', 'disparate', 'businesses', 'through', 'one', 'scope', 'for', 'a', 'truly', 'massive', 'big', 'picture', 'our', 'platform', 'creates', 'ever', 'more', 'accurate', 'predictions', 'as', 'we', 'integrate', 'findings', 'discovered', 'from', 'patterns', 'in', 'data', 'across', 'a', 'wide', 'array', 'of', 'industries', 'integration', 'into', 'workflow', 'we', 'don', 't', 'stop', 'at', 'the', 'analytics', 'we', 'deliver', 'answers', 'into', 'workflow', 'to', 'exactly', 'the', 'right', 'person', 'at', 'the', 'right', 'time', 'our', 'integrated', 'solutions', 'provide', 'real', 'time', 'insights', 'and', 'allow', 'for', 'seamless', 'action', 'to', 'be', 'taken', 'on', 'a', 'recommendation', 'producing', 'immediate', 'results', 'a', 'multidisciplinary', 'team', 'of', 'entrepreneurs', 'we', 've', 'instituted', 'a', 'new', 'way', 'of', 'building', 'software', 'we', 're', 'driving', 'transformational', 'change', 'not', 'incremental', 'using', 'speed', 'and', 'agility', 'we', 're', 'knocking', 'down', 'silos', 'to', 'build', 'on', 'knowledge', 'and', 'data', 'to', 'make', 'everyone', 'better', 'we', 'take', 'a', 'different', 'approach', 'to', 'data', 'the', 'world', 's', 'most', 'valuable', 'asset', 'data', 'has', 'always', 'been', 'there', 'unseen', 'and', 'uncollected', 'first', 'we', 'were', 'able', 'to', 'capture', 'it', 'collect', 'it', 'store', 'it', 'now', 'we', 'can', 'harness', 'its', 'power', 'to', 'change', 'the', 'world', 'around', 'us', 'big', 'data', 'is', 'only', 'getting', 'bigger', 'data', 'volume', 'is', 'set', 'to', 'grow', 'x', 'year', 'over', 'year', 'between', 'now', 'and', 'with', 'mission', 'critical', 'data', 'from', 'machines', 'and', 'equipment', 'expanding', 'as', 'more', 'assets', 'are', 'connected', 'across', 'operations', 'companies', 'can', 'no', 'longer', 'afford', 'to', 'be', 'anything', 'but', 'data', 'driven', 'data', 'used', 'to', 'be', 'something', 'to', 'maintain', 'and', 'manage', 'now', 'it', 's', 'a', 'valuable', 'asset', 'and', 'competitive', 'edge', 'businesses', 'can', 't', 'build', 'the', 'solution', 'themselves', 'speed', 'and', 'technology', 'talent', 'limit', 'the', 'ability', 'for', 'most', 'companies', 'to', 'build', 'the', 'software', 'required', 'that', 's', 'where', 'we', 'come', 'in', 'the', 'problems', 'that', 'we', 're', 'solving', 'address', 'some', 'of', 'the', 'highest', 'value', 'creation', 'opportunities', 'that', 'i', 'believe', 'exist', 'in', 'the', 'industrial', 'world', 'brad', 'keywell', 'co', 'founder', 'ceo', 'learn', 'more', 'about', 'uptake', 'see', 'what', 'we', 're', 'building', 'our', 'platform', 'approach', 'platform', 'people', 'open', 'positions', 'blog', 'media', 'inquiries', 'natalie', 'bauer', 'luce', 'or', 'uptake', 'all', 'rights', 'reserved', 'platform', 'uptake', 'approach', 'platform', 'solutions', 'people', 'join', 'us', 'blog', 'approach', 'platform', 'solutions', 'people', 'join', 'us', 'blog', 'close', 'curious', 'to', 'learn', 'how', 'uptake', 'can', 'impact', 'your', 'company', 'contact', 'us', 'below', 'name', 'company', 'email', 'phone', 'message', 'we', 'built', 'a', 'platform', 'that', 'will', 'transform', 'the', 'world', 'of', 'industry', 'minimize', 'downtime', 'optimize', 'performance', 'enhance', 'safety', 'our', 'platform', 'can', 'identify', 'problems', 'before', 'they', 'happen', 'to', 'help', 'the', 'world', 's', 'trains', 'run', 'on', 'time', 'make', 'power', 'grids', 'smarter', 'produce', 'more', 'food', 'for', 'the', 'world', 's', 'population', 'through', 'precision', 'agriculture', 'and', 'manage', 'water', 'supplies', 'more', 'efficiently', 'here', 's', 'how', 'it', 'works', 'intro', 'generation', 'normalization', 'storage', 'analysis', 'tools', 'services', 'solutions', 'machines', 'are', 'generating', 'huge', 'amounts', 'of', 'data', 'all', 'over', 'the', 'world', 'at', 'unfathomable', 'rates', 'data', 'generation', 'we', 'collect', 'this', 'valuable', 'data', 'from', 'sensored', 'equipment', 'operations', 'and', 'external', 'sources', 'like', 'weather', 'and', 'traffic', 'data', 'normalization', 'we', 'clean', 'and', 'normalize', 'data', 'from', 'real', 'time', 'disparate', 'sources', 'data', 'storage', 'our', 'polyglot', 'data', 'store', 'ensures', 'that', 'information', 'is', 'available', 'at', 'the', 'right', 'place', 'and', 'time', 'to', 'effectively', 'move', 'through', 'models', 'data', 'analysis', 'our', 'models', 'use', 'a', 'proprietary', 'rules', 'engine', 'and', 'machine', 'learning', 'technology', 'to', 'enable', 'real', 'time', 'recommendations', 'tools', 'services', 'our', 'tools', 'and', 'services', 'work', 'together', 'across', 'industries', 'creating', 'solutions', 'that', 'power', 'intelligent', 'work', 'solutions', 'these', 'prescriptive', 'solutions', 'integrate', 'into', 'any', 'workflow', 'at', 'any', 'time', 'delivering', 'intuitive', 'and', 'actionable', 'recommendations', 'play', 'our', 'proprietary', 'platform', 'meets', 'the', 'demands', 'of', 'the', 'modern', 'enterprise', 'dynamic', 'flexible', 'frameworks', 'are', 'designed', 'to', 'scale', 'and', 'leverage', 'evergreen', 'technologies', 'contextual', 'integration', 'with', 'workflow', 'makes', 'insights', 'actionable', 'and', 'provides', 'timely', 'answers', 'intelligent', 'a', 'world', 'class', 'machine', 'learning', 'engine', 'grows', 'smarter', 'in', 'one', 'industry', 'because', 'of', 'learnings', 'in', 'another', 'secure', 'robust', 'security', 'and', 'infrastructure', 'support', 'mission', 'critical', 'needs', 'explore', 'our', 'industry', 'offerings', 'our', 'solutions', 'approach', 'platform', 'people', 'open', 'positions', 'blog', 'media', 'inquiries', 'natalie', 'bauer', 'luce', 'or', 'uptake', 'all', 'rights', 'reserved', 'solutions', 'uptake', 'approach', 'platform', 'solutions', 'people', 'join', 'us', 'blog', 'approach', 'platform', 'solutions', 'people', 'join', 'us', 'blog', 'close', 'curious', 'to', 'learn', 'how', 'uptake', 'can', 'impact', 'your', 'company', 'contact', 'us', 'below', 'name', 'company', 'email', 'phone', 'message', 'our', 'industry', 'solutions', 'improve', 'uptime', 'minimize', 'failures', 'reduce', 'fuel', 'costs', 'and', 'streamline', 'operations', 'at', 'uptake', 'we', 'help', 'customers', 'realize', 'the', 'value', 'of', 'their', 'data', 'sensors', 'and', 'gauges', 'on', 'industrial', 'assets', 'collect', 'billions', 'of', 'data', 'points', 'every', 'day', 'we', 'give', 'customers', 'the', 'tools', 'and', 'visuals', 'to', 'transform', 'that', 'data', 'into', 'real', 'and', 'measurable', 'value', 'our', 'broad', 'range', 'of', 'industrial', 'solutions', 'include', 'condition', 'based', 'monitoring', 'track', 'real', 'time', 'measurements', 'from', 'thousands', 'of', 'high', 'value', 'assets', 'across', 'your', 'industrial', 'ecosystem', 'understand', 'each', 'asset', 's', 'health', 'status', 'and', 'location', 'in', 'every', 'corner', 'of', 'the', 'globe', 'and', 'make', 'informed', 'decisions', 'about', 'how', 'and', 'when', 'they', 'are', 'maintained', 'using', 'the', 'world', 's', 'most', 'intuitive', 'industrial', 'analytics', 'and', 'visualization', 'platform', 'planning', 'and', 'forecasting', 'create', 'optimal', 'operation', 'plans', 'based', 'on', 'performance', 'data', 'and', 'schedule', 'recovering', 'strategies', 'to', 'minimize', 'operational', 'disruptions', 'due', 'to', 'unforeseen', 'events', 'improve', 'forecasting', 'to', 'ensure', 'that', 'parts', 'and', 'equipment', 'are', 'available', 'when', 'needed', 'minimizing', 'unscheduled', 'downtime', 'fuel', 'and', 'energy', 'manage', 'and', 'optimize', 'the', 'yield', 'of', 'fuel', 'and', 'energy', 'improve', 'fuel', 'efficiency', 'with', 'the', 'ability', 'to', 'adapt', 'to', 'network', 'conditions', 'and', 'plan', 'routes', 'based', 'on', 'speed', 'terrain', 'and', 'other', 'constraints', 'monitor', 'asset', 'performance', 'and', 'benchmark', 'assets', 'in', 'a', 'fleet', 'to', 'identify', 'poorly', 'performing', 'assets', 'and', 'equipment', 'in', 'need', 'of', 'repair', 'or', 'maintenance', 'supply', 'chain', 'optimization', 'increase', 'the', 'speed', 'of', 'operations', 'by', 'connecting', 'data', 'points', 'across', 'your', 'enterprise', 'calibrate', 'interdependent', 'processes', 'so', 'that', 'activity', 'in', 'one', 'section', 'of', 'the', 'supply', 'chain', 'triggers', 'automated', 'best', 'responses', 'throughout', 'your', 'connected', 'operation', 'performance', 'optimization', 'improve', 'speed', 'efficiency', 'and', 'effectiveness', 'across', 'operations', 'using', 'asset', 'tracking', 'to', 'adjust', 'operating', 'plans', 'incorporating', 'asset', 'specific', 'context', 'like', 'weather', 'terrain', 'and', 'geography', 'analyze', 'operator', 'actions', 'to', 'identify', 'trends', 'and', 'efficiencies', 'gather', 'network', 'insights', 'to', 'improve', 'solutions', 'within', 'business', 'constraints', 'learn', 'more', 'about', 'who', 'we', 'are', 'our', 'people', 'approach', 'platform', 'people', 'open', 'positions', 'blog', 'media', 'inquiries', 'natalie', 'bauer', 'luce', 'or', 'uptake', 'all', 'rights', 'reserved', 'blog', 'uptake', 'insights', 'data', 'design', 'technology', 'and', 'culture', 'at', 'uptake', 'culture', 'data', 'design', 'news', 'technology', 'all', 'topics', 'posted', 'by', 'adam', 'mcelhinney', 'on', 'november', 'in', 'data', 'steps', 'to', 'better', 'analytics', 'teams', 'i', 'recently', 'stumbled', 'across', 'an', 'old', 'blog', 'post', 'the', 'joel', 'test', 'steps', 'to', 'better', 'code', 'outlining', 'a', 'quick', 'yes', 'read', 'more', 'posted', 'on', 'october', 'in', 'news', 'a', 'note', 'from', 'brad', 'uptake', 'has', 'grown', 'incredibly', 'fast', 'into', 'a', 'team', 'driving', 'by', 'passion', 'and', 'curiosity', 'with', 'some', 'recent', 'news', 'now', 'we', 're', 'able', 'to', 'move', 'even', 'faster', 'read', 'more', 'posted', 'on', 'august', 'in', 'technology', 'the', 'what', 'and', 'why', 'of', 'the', 'internet', 'of', 'things', 'what', 'the', 'internet', 'of', 'things', 'really', 'is', 'why', 'it', 's', 'happening', 'now', 'and', 'what', 'it', 'means', 'for', 'everyone', 'read', 'more', 'posted', 'on', 'july', 'in', 'culture', 'building', 'with', 'creativity', 'and', 'logic', 'how', 'art', 'and', 'science', 'inform', 'uptake', 's', 'predictive', 'analytics', 'software', 'read', 'more', 'posted', 'on', 'july', 'in', 'design', 'user', 'centered', 'answers', 'the', 'relationship', 'between', 'social', 'science', 'and', 'design', 'thinking', 'and', 'what', 'makes', 'uptake', 's', 'approach', 'to', 'building', 'software', 'unique', 'read', 'more'])




```
trigram=wiki.ngrams(n=3)

```


```
bigram = wiki.ngrams(n=2)
```


```

```


```

```


```

```


```

```


```

```
